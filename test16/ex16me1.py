
# -*- coding: utf-8 -*-
#coding = utf-8

from sys import argv

script, filename = argv #将命令行参数发给命令

print "We're going to erase %r" %filename #格式化字符串为，文件名
print "If you don't want that, hit CTRL-C(^C)"
print "if you do want that ,hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename,'w') #定义变量target，打开文件，并且可以读写

print "Truncating the file. Goodbye!"
target.truncate()#truncate() 方法用于截断文件，如果指定了可选参数 size，则表示截断文件为 size 个字符。 如果没有指定 size，则从当前位置起截断；截断之后 size 后面的所有字符被删除。

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "I'm going to write these to the file."

target.write(line1 + "\n" + line2 + "\n"+ line3 +"\n",)#×.write,表示写入内容
1

print "And finally, we close it."
target.close() #关闭文档
