'''
2.输入A-Z任意字母，输出对应大写字母在字母表中的位置。如输入A，则输出1.
示例：Python letter.py –i task2.txt –o result2.txt
输入：task2.txt文件
A Z F G H K B A D F X Y
输出：result2.txt文件
1 26 6 7 8 11 2 1 4 6 24 25
'''
#!/usr/bin/env python3
import argparse
parser = argparse.ArgumentParser(description="calculate letter site .")
parser.add_argument("-i", "--inputfile", help="input files.")
parser.add_argument("-o", "--outputfile", help="output files.")
args = parser.parse_args()
input = args.inputfile
output = args.outputfile

content = open("task2.txt", 'r')

data = content.read()

data_tmp = data.replace(" ","")
with open("work2.txt",'w') as fo:
    for i in data_tmp:
        k = ord(i)
        #unicode 码转换
        j = k - 64
        res = str(j) + "\t"
        fo.write(res)
fo.close()
content.close()
