#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        sweet = (length, None)
        return sweet
    sweet = (length, sentence[0])
    return sweet
