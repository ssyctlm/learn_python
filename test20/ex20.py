# -*- coding: utf-8 -*-
#coding : utf-8
from sys import argv

script,input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)#seek() 方法用于移动文件读取指针到指定位置。
	"""offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
	   whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。"""

def print_a_line(line_count, f):
	print line_count, f.readline()
	"""在这里折腾了很久，一直纳闷，没有传递参数给f，它怎么会打印的结果不同？
	几个小时后，最终发现，确实没有传递参数。而且file.readline()命令执行一次
	它就会向下迭代一行（即使是在赋值阶段），因此在查阅资料的时候，readline总不能
	良好的打印出我预期的结果。最终，配合seek（）的命令，它可以正确展现了。
	每打印一次，它自动迭代，读取打印下一行"""

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all (current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line, current_file)
