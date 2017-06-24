#!/usr/bin/python
#coding=utf-8
import fileinput  
import jieba
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

for line in fileinput.input(r"/home/gxy/DOC/wiki.zh.text.jian", inplace=1):  
    list=jieba.cut(line)
    print " ".join(list)
fileinput.close();
    
