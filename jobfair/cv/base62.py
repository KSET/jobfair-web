import string
import random  
import hashlib

BASE_LIST = string.digits + string.letters
BASE_DICT = dict((c, i) for i, c in enumerate(BASE_LIST))

def decode(string, reverse_base=BASE_DICT):
    length = len(reverse_base)
    ret = 0
    for i, c in enumerate(string[::-1]):
        ret += (length ** i) * reverse_base[c]

    return ret

def encode(integer, base=BASE_LIST):
    length = len(base)
    ret = ''
    while integer != 0:
        ret = base[integer % length] + ret
        integer /= length

    return pad(ret)

def pad(string, min_length=10):
    if len(string) < min_length:
        return string + hashlib.sha1(str((random.random()))).hexdigest()[:min_length-len(string)]
    return string

