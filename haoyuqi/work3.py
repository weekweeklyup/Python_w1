#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description="remove even number .")
parser.add_argument("-o", "--outputfile", help="output files.")
args = parser.parse_args()
output = args.outputfile

def remove_even(num):
    """去出字符串中偶数"""
    for i in range(2,num):
        if (num % 2) == 0:
            return False
        else:
            return True

ls = [51,33,54, 68,56,34,67,88,431]
remove_even_ls = []
with open(output,'w',encoding="utf-8") as fo:
    for j in ls:
        if remove_even(j) == True:
            remove_even_ls.append(j)
    length = len(remove_even_ls)
    res = "列表%s 去除偶数后为%s, 长度为%s." %(ls,remove_even_ls,length)
    fo.write(res)
fo.close()
