# -*- coding: utf-8 -*-
#coding = utf-8
from sys import argv #引入命令行参数sys.argv


script,filename = argv #命令行里输入的内容将被带入到命令行参数中

txt = open (filename)#定义一个元素txt

print "Here's your file %r:" % filename#显示"here's your file %r"%(格式化字符串)

print txt.read()#读取打开的文件filename
 	
print "Type the filename again:"
file_again =  raw_input(">") #定义file_again，在>后输入文件名

txt_again = open(file_again)#定义txt_again为打开上方输入的文件名

print txt_again.read()#打印读取打开的文件内容