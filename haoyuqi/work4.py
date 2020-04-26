#!/usr/bin/env python3
import argparse
import pandas as pd


parser = argparse.ArgumentParser(description="calculate GC content.")
parser.add_argument("-i", "--inputfile", help="input file.")
parser.add_argument("-o", "--outputfile", help="output file.")
args = parser.parse_args()
input = args.inputfile
output = args.outputfile

def read_fasta_file(inputfile):
    seq_dic = {}
    total_sequence_list = ''
    with open(inputfile) as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                ids = line.strip('>')
                seq = ''
            else:
                seq = seq + line
                seq_dic[ids] = seq
            if line[0:1] != '>':
                total_sequence_list += line

    return total_sequence_list

def get_gc_content(sequence):
    """
    计算序列的 GC 含量
    """
    sequence = sequence.upper()
    count_g = sequence.count('G')
    count_c = sequence.count('C')
    count_a = sequence.count('A')
    count_t = sequence.count('T')
    count_t = sequence.count('N')

    gc_content = (count_g + count_c) / (count_a + count_t + count_c + count_g + count_n)

    return gc_content

seq = read_fasta_file(input)
sequence_gc_content = get_gc_content(seq)
with open(output,'w') as fo:
    res = 'genome gc content :{:.2%}'.format(sequence_gc_content)
    fo.write(res)
fo.close()
