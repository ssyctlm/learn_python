#coding:utf-8
from sys import argv
script, user_name = argv
prompt = ">"
print "hi %s, I'm the %s script." %(user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s" % user_name
likes = raw_input(prompt)

print "Where do you live %s" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "What do you want to say to me?"
said = raw_input(prompt)

print  """
Alright,so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
You said %r to me in addtion.
"""  % (likes, lives, computer, said)

#在敲代码的过程中，第四行我漏掉了一个%，其实起初我注意到这个问题了，但是我没有在意

