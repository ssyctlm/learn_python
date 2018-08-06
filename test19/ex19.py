# -*- coding: utf-8 -*-
#coding : utf-8
def cheese_and_crackers(cheeese_count,boxex_of_crackers):
	#定义函数cheese_and_cracker
	print "You have %d cheeses!"%cheeese_count
	print "You have %d boxes of crackers!"%boxex_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)
#调用函数cheese_and_crackers,并传递20，30为参数

print "OR,we can use variables from our script:"
amount_of_cheese = 10
#定义amount_of_cheese = 10
amount_of_crackers = 50
#定义amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)
#调用函数cheese_and_crackers,并传递两个参数

print "We can even do math inside too:"
cheese_and_crackers(10+20,5+6)
#调用函数cheese_and_crackers，并且传递数字及数字表达式

print "And we can combine the two, variables and math"
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers)
#调用函数cheese，并且传递一个参数表达式如上