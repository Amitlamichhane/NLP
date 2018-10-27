
from __future__ import division
import traceback

from torch.nn.utils.rnn import pack_padded_sequence

import torch.nn.functional as F
import torch
from config import config



_config = config()


def find_tokens(token):
    if token == "B-TAR":
        return "I-TAR"
    else:
        return "I-HYP"

def extract_tokens(a):
    #use set instead of list to get the intersection

    token_position = set( )
    #token =""
    #to_find= ""
    start =0

    while start < len(a):
        #if it finds the starting position
        if a[start].startswith('B'):
            token = a[start]

            #now we need to find the end of the tokens
            end = start +1
            to_find = find_tokens(token)
            #print(to_find)
            while end < len(a):
                #check until it is 'O'
                #update check until it is to_find
                #since it might have I-HYP instead of I-TAR
                #when looking at B-TAR
                if a[end] != to_find:
                    #we get out of the loop
                    break
                end = end + 1
            #update set
            token_position.add((token,start,end))
            start = end -1
            #update l
        start = start + 1
    return token_position
#we iterate through each file trying to find the same token we check the first group with other
#

def evaluate(golden_list, predict_list):

    false_positive= false_negative = true_positive= 0
    for i in range(len(golden_list)):

        golden_tokens = extract_tokens(golden_list[i])
        #print("golden tokens is")
        #print(golden_tokens


        predict_tokens = extract_tokens(predict_list[i])

        inersection = len(predict_tokens.intersection(golden_tokens))

        true_positive  = true_positive + inersection
        false_positive += len(predict_tokens)- inersection
        false_negative += len(golden_tokens)-inersection



    if false_negative == 0 and false_positive == 0:
        return 1.00
    elif true_positive == 0 and (false_positive > 0 or false_negative >0):
        return 0.00
    else:
        #calculate recal and precision
        try:
            # print("True positive is ---->" + " " + str(true_positive))
            # print("False positive is ---->" + " " + str(false_positive))
            # print("False negative is ---->" + " " + str(false_negative))
            precision = float(true_positive / (true_positive + false_positive))
            #print("precision is ===>" + " " + str(precision))
            recall = true_positive / (true_positive + false_negative)
            # print("recall is ===>" + " " + str(recall))
            f1_score = (2 * precision * recall) / (precision + recall)
        except Exception:
            traceback.print_exc()

    #dont round
    print("f1 Score: ", round(f1_score,3))
    return round(f1_score,3)




#todo read lstm execution
#todo finish the lecture videos

def new_LSTMCell(input, hidden, w_ih, w_hh, b_ih=None, b_hh=None):

    #if input.is_cuda:
    #    igates = F.linear(input, w_ih)
    #    hgates = F.linear(hidden[0], w_hh)
    #    state = fusedBackend.LSTMFused()
    #    return state(igates, hgates, hidden[1]) if b_ih is None else state(igates, hgates, hidden[1], b_ih, b_hh)

    hx, cx = hidden
    gates = F.linear(input, w_ih, b_ih) + F.linear(hx, w_hh, b_hh)
    ingate, forgetgate, cellgate, outgate = gates.chunk(4, 1)

    #we need to change this line to change the import stuff
    #changin ingate to 1 - forgetgate

    forgetgate = F.sigmoid(forgetgate)
    ingate = 1- forgetgate
    cellgate = F.tanh(cellgate)
    outgate = F.sigmoid(outgate)

    cy = (forgetgate * cx) + (ingate * cellgate)
    hy = outgate * F.tanh(cy)

    return hy, cy






def get_char_sequence(model, batch_char_index_matrices, batch_word_len_lists):
    # resize batch_char_index_matrices
    sizes_batch = batch_char_index_matrices.size()
    mini_batch = batch_char_index_matrices.view(sizes_batch[0] * sizes_batch[1], -1)

    # get char_embeddings [14,14,50]
    input_char_embeds = model.char_embeds(mini_batch)

    # sort mini-batch
    sizes_len = batch_word_len_lists.size()
    mini_len = batch_word_len_lists.view(sizes_len[0] * sizes_len[1])
    perm_idx, sorted_mini_len = model.sort_input(mini_len)
    sorted_input_char_embeds = input_char_embeds[perm_idx]
    _, desorted_indices = torch.sort(perm_idx, descending=False)
    output_sequence = pack_padded_sequence(sorted_input_char_embeds, lengths=sorted_mini_len.data.tolist(),
                                           batch_first=True)

    # feed pack_padded sequence to char_lstm layer
    output_sequence, state = model.char_lstm(output_sequence)

    # (num_layers*num_directions), batch_size, hidden_size
    # currently ordered DECREASINGLY
    # re-order hidden_states to correspond with original order. ([2,14,50])
    hidden_recover = state[0]
    for i in range(hidden_recover.size()[0]):
        hidden_recover[i] = hidden_recover[i][desorted_indices]

    batch_size = sizes_batch[0] * sizes_batch[1]
    _, rev_indicies = torch.sort(torch.tensor([i for i in range(batch_size)]), descending=True)
    hidden_recover[1] = hidden_recover[1][rev_indicies]

    # we have
    # FBFBFBFBFB
    # we want
    # FFFFFFBBBBBB
    clone = hidden_recover.clone()
    # [2,14,50]

    fr = 0
    bc = batch_size - 1
    tg = 0
    for i in range(2):
        for j in range(batch_size):
            if tg == 0:
                clone[i][j] = hidden_recover[0][fr]
                fr += 1
            else:
                clone[i][j] = hidden_recover[1][bc]
                bc -= 1
            tg = (tg + 1) % 2

    return clone.view(sizes_batch[0], sizes_batch[1], -1)


