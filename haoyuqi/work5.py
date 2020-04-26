#!/usr/bin/env python3
import argparse
import pandas as pd

parser = argparse.ArgumentParser(description="calculate length of dataframe unequel zero.")
parser.add_argument("-i", "--inputfile", help="input file.")
parser.add_argument("-o", "--outputfile", help="output file.")
args = parser.parse_args()
input = args.inputfile
output = args.outputfile

df = pd.read_csv(input, sep="\t",header= 0,dtype="str",low_memory=False)
length = df.apply(lambda x : x.value_counts().get(0,0),axis=1)
df['length'] = length
result = df.to_csv(output, sep="\t",index=False)
