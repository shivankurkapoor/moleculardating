'''
Author : Shivankur Kapoor
Contact : kapoors@usc.edu
Description: Contains methods to normalize, generate random strings, clean input sequences
'''
import random
import string


def normalize(x, mean, std):
    '''
    Normalization using standard formula
    :param x: input number
    :param mean: mean of distribution
    :param std: std var of distribution
    :return: normalized value
    '''
    return float(x - mean) / float(std)


def random_string(N=3):
    '''
    Generates random alphanumeric string of length N
    :param N: length of the string
    :return: random string
    '''
    randstring = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
    return randstring


def clean_seqeunce(sequence):
    '''
    Clean the input sequence
    :param sequence: input sequence
    :return: clean sequence
    '''
    sequence = sequence.replace('-', '_')
    sequence = sequence.replace('~', '_')
    sequence = sequence.replace('a', 'A')
    sequence = sequence.replace('c', 'C')
    sequence = sequence.replace('g', 'G')
    sequence = sequence.replace('t', 'T')
    sequence = sequence.replace('R', '_')
    sequence = sequence.replace('Y', '_')
    sequence = sequence.replace('W', '_')
    sequence = sequence.replace('M', '_')
    sequence = sequence.replace('K', '_')
    sequence = sequence.replace('N', '_')
    return sequence
