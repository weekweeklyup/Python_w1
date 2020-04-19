#!/usr/bin/env python3
import argparse


parser = argparse.ArgumentParser(description="calculate letter times .")
parser.add_argument("-i", "--inputfile", help="input files.")
parser.add_argument("-o", "--outputfile", help="output files.")
args = parser.parse_args()
input = args.inputfile
output = args.outputfile
def count_char(test_str):
    """统计字符串个数"""
    return {k: test_str.count(k) for k in set(test_str) if k not in " "}

content = open(input, 'r')
data = content.read()
count_dict = {}
count_dict = count_char(data)

#输出结果
with open(output,'w') as fo:
    for k in count_dict.keys():
        value = count_dict[k]
        value = str(value)
        res = k + "\t" + value + '\n'
        fo.write(res)
fo.close()
content.close()

