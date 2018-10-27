
from __future__ import division
import traceback

from config import config
import torch.nn.functional as F


_config = config()


def find_tokens(token):
    if token == "B-TAR":
        return "I-TAR"
    else:
        return "I-HYP"

def extract_tokens(a):
    #use set instead of list to get the intersection

    token_position = set()
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
            print("True positive is ---->" + " " + str(true_positive))
            print("False positive is ---->" + " " + str(false_positive))
            print("False negative is ---->" + " " + str(false_negative))
            precision = float(true_positive / (true_positive + false_positive))
            #print("precision is ===>" + " " + str(precision))
            recall = true_positive / (true_positive + false_negative)
            # print("recall is ===>" + " " + str(recall))
            f1_score = (2 * precision * recall) / (precision + recall)
        except Exception:
            traceback.print_exc()

    #dont round
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






def get_char_sequence(model, bclearatch_char_index_matrices, batch_word_len_lists):
    pass;

