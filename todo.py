
from __future__ import division
import traceback

from config import config
import torch.nn.functional as F


_config = config()


def evaluate( golden_list, predict_list):
    false_positive = false_negative =true_positive =0
    precision = recall =0
    border_flag_hyp =0
    border_flag_tar =0
    f1_score = 0
    predict_flag_hyp = 0
    predict_flag_tar =0

    for i in range(len(golden_list)):
        for j in range(len(golden_list[i])):
            #needs to check exhaustively
            #patter matching
            golden = golden_list[i][j]
            pattern = predict_list[i][j]
            if border_flag_hyp:
                if predict_flag_hyp:
                    # doesnt matter if both match
                    if golden == pattern:
                        true_positive = true_positive +1
                    else:
                        false_positive = false_positive + 1
                        false_negative = false_negative +1
                    predict_flag_hyp = 0
                else:
                    if pattern == 'B-HYP':
                        predict_flag_hyp = 1
                    elif pattern == "B-TAR":
                        predict_flag_tar =1
                    false_negative = false_negative + 1

                border_flag_hyp= 0

            elif border_flag_tar:
                #if both we bb-TAR
                if predict_flag_tar:
                    # doesnt matter if both match
                    if golden == pattern:
                        true_positive = true_positive +1
                    else:
                        false_positive = false_positive + 1
                        false_negative = false_negative +1
                    predict_flag_tar = 0
                else:
                    if pattern == 'B-HYP':
                        predict_flag_hyp = 1
                    elif pattern == "B-TAR":
                        predict_flag_tar =1
                    false_negative = false_negative + 1

                border_flag_tar = 0
            elif predict_flag_hyp:
                if golden == "B-TAR":
                    border_flag_tar = 1

                elif golden == "B-HYP":

                    border_flag_hyp = 1
                    if golden == pattern:
                        true_positive = true_positive + true_positive
                    else:
                        if j == len(golden_list[i]) - 1:
                            false_negative = false_negative + 1
                 #other cases doesn't matter
                false_positive = false_positive + 1

                predict_flag_hyp= 0

            elif predict_flag_tar:
                #need to check if the next one is ITAR

                if golden == "B-TAR":
                    border_flag_tar = 1

                elif golden == "B-HYP":
                    border_flag_hyp = 1
                 #other cases doesn't matter
                false_positive = false_positive + 1
                predict_flag_tar= 0

            else:
                if(golden_list[i][j]=="B-TAR"):
                    border_flag_tar = 1

                    if (pattern == 'O'):
                        false_negative = false_negative +1
                    elif(pattern =="B-TAR"):
                        #still can't be true until we check the next pattern
                        predict_flag_tar = 1
                    elif(pattern == "B-HYP"):
                        #since marked wrong
                        #since marked as positive
                        false_negative = false_negative +1
                        false_positive = false_positive +1
                        predict_flag_hyp = 1


                elif(golden_list[i][j]=="B-HYP"):
                    #print("hello")
                    if (pattern == 'O'):
                        false_negative = false_negative +1
                    elif(pattern =="B-TAR"):
                        #still can't be true until we check the next pattern
                        false_negative = false_negative + 1
                        false_positive = false_positive + 1
                        predict_flag_tar = 1
                    elif(pattern == "B-HYP"):
                        #since marked wrong
                        #since marked as positive
                        #final check if it end of the sentence
                        if j == len(golden_list[i])-1:
                            true_positive = true_positive + 1
                        else:
                            predict_flag_hyp = 1
                    elif (pattern == "I-HYP"):
                        # since marked wrongel
                        # since marked as positive
                        # final check if it end of the sentence
                        if j == len(golden_list[i]) - 1:
                            false_negative = false_negative+ 1


                else:
                    if(predict_list[i][j]!='O'):

                        if (predict_list[i][j]=="B-HYP"):
                            if j == len(golden_list[i]) - 1:
                                false_positive = false_positive + 1
                            else:
                                predict_flag_hyp = 1

                        elif(predict_list[i][j]=="B-TAR"):
                            predict_flag_tar = 1

    #end of the thing resolves around what tag we still have
    #if the tags are flagged and both tags are same then we say positive
    #other wise negative depending on the tag
    try:
       #print("true_positive=>" +  "  "+  str(true_positive))
       #print("false_negative=>"+  " " + str(false_negative))
       #print("false positive=>" +  " " +str(false_positive))

       #if fp = 0 and fn = 0, then f1 = 1

       #elif tp = 0, then f1 = 0
        if false_negative ==0 and false_positive ==0:
            return 1.0
        elif true_positive ==0:
            return 0.0
        precision = float (true_positive/(true_positive+false_positive))
       #print("precision is ===>" + " " + str(precision))
        recall = true_positive/(true_positive+false_negative)
       #print("recall is ===>" + " " + str(recall))
        f1_score = (2* precision *recall)/(precision+recall)
    except Exception:
        traceback.print_exc()


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

