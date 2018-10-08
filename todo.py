import traceback

import torch
from config import config

_config = config()


def evaluate( golden_list, predict_list):
    false_positive = false_negative =true_positive =0
    precision = recall =0
    border_flag =0
    f1_score = 0

    for i in range(len(golden_list)):
        for j in range(len(golden_list[i])):
            #three condition to check if golden_list is 'O'
            if(golden_list[i][j]=='O'):



    try:
        precision = true_positive/(true_positive+false_positive)
        recall = true_positive/(true_positive+false_negative)
        f1_score = (2* precision *recall)/(precision+recall)
    except Exception:
        traceback.print_exc()
    return f1_score





def new_LSTMCell(input, hidden, w_ih, w_hh, b_ih=None, b_hh=None):
    pass;


def get_char_sequence(model, bclearatch_char_index_matrices, batch_word_len_lists):
    pass;

