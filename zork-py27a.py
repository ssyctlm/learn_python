#!/usr/bin/python
# -*- coding: utf-8 -*-
import string
loop = 3
while loop == 3:
	print ("----------------------------------")
	print ("欢迎来到魔域！")
	print ("你正站在一个白色屋子的西侧，这屋子的前门被木板挡住了")
	print ("（一个神秘的小路延伸到了西南侧的森林里。）")
	print ("还有一个小邮箱")

	#第一屏并且输入
	first = raw_input("你想做什么？")
	if first.lower() == ("打开邮箱"):
		print ("----------------------------------")
		print ("你开玩笑吧。")
		loop = 4
	if first.lower() == ("打开邮箱"):
		print ("----------------------------------")
		print ("打开了小邮箱你看见了一个传单。")
		loop = 4
	if first.lower() == ("去东边"):
		print ("----------------------------------")
		print ("门被木板挡住了，你试了试，无法移动木板")
		loop = 4
	if first.lower() == ("去开门"):
		print ("----------------------------------")
		print ("这门打不开")
		loop = 4
	if first.lower() == ("拿走木板"):
		print ("----------------------------------")
		print ("这木板被钉得非常牢固")
		loop = 4
	if first.lower() == ("仔细看看房子"):
		print ("----------------------------------")
		print ("这所房子是一个美丽的殖民地房子，漆成白色。 很明显，业主必须非常富有")
		loop = 4
	if first.lower() == ("阅读传单"):
		print ("----------------------------------")
		print ("欢迎来到魔域python版，你的任务是找到玉雕像")
		loop = 4
	if first.lower() == ("去西南边"):
		loop = 8
	else:
		print ("----------------------------------")
		loop = 4

	#第一个输入循环
	while loop == 4:
		if loop == 4:
			print ("----------------------------------")
			print ("你正站在一个白色屋子的西侧，这屋子的前门被木板挡住了")
			print ("（一个神秘的小路延伸到了西南侧的森林里。）")
			print ("还有一个小邮箱")
			second = raw_input ("你想做什么？")
		if second.lower() == ("拿起邮箱"):
			print ("----------------------------------")
			print ("它被安全地锚在了地上")
			hello = 2
		if second.lower() == ("打开邮箱"):
			print ("----------------------------------")
			print ("打开了小邮箱你看见了一个传单。")
			hello = 2
		if second.lower() == ("去东边"):
			print ("----------------------------------")
			print ("门被木板挡住了，你试了试，无法移动木板")
			hello = 2
		if second.lower() == ("打开门"):
			print ("----------------------------------")
			print ("门打不开")
			hello = 2
		if second.lower() == ("拿走木板"):
			print ("----------------------------------")
			print ("这木板被钉得非常牢固")
			hello = 2
		if second.lower() == ("仔细看看房子"):
			print ("----------------------------------")
			print ("这所房子是一个美丽的殖民地房子，漆成白色。 很明显，业主必须非常富有")
			hello = 2
		if second.lower() == ("去东南边"):
			loop = 8
		if second.lower() == ("阅读传单"):
			print ("----------------------------------")
			print ("欢迎来到魔域python版，你的任务是找到玉雕像。")
			loop = 4
		if second.lower() == ("去西南边"):
			loop = 8
		else:
			print ("----------------------------------")
			loop = 4
		
# 西南循环
	while  loop == 8:
		if loop == 8:
			print ("----------------------------------")
			print ("这里是森林，各个方向都有树。东边的方向，看起来像日光")
			forest_inp = raw_input("你想做什么？")
		if forest_inp.lower() == ("去西面"):
			print ("----------------------------------")
			print ("你应该需要一个弯刀去更远的西方")
			loop = 8
		if forest_inp == ("去北面"):
			print ("----------------------------------")
			print ("森林太深邃，难以穿越到北方")
			loop = 8
		if forest_inp.lower() == ("去南面"):
			print ("----------------------------------")
			print ("暴风雨的树木挡住了你的路。")
			loop = 8
		if forest_inp.lower() == ("去东边"):
			loop = 9
		else:
			print ("----------------------------------")
			loop = 8

# 东边循环和栅栏输入
	while loop == 9:
		if loop == 9:
			print ("----------------------------------")
			print ("你现在在一条清洁的道路，周围的森林围绕着你。一条路通向了南边。")
			print ("这里有一个敞开的栅栏，通向无尽的黑暗")
			grating_inp = raw_input ("你想做什么？")
		if grating_inp.lower() == ("去南边"):
			print ("----------------------------------")
			print ("你看到一个大怪物在转悠")
			loop = 9
		if grating_inp.lower() == ("跳下栅栏"):
			loop = 10
		else:
			print ("----------------------------------")
			loop = 9


#栅栏循环以及进入洞穴
	while loop == 10:
		if loop == 10:
			print ("----------------------------------")
			print ("你进入了一个狭窄黑暗的洞穴，阴森的台阶通向下边")
			print ("在角落有一个男性的骷髅骨架")
			cave_inp = raw_input ("你想做什么？")
		if cave_inp.lower() == ("拿起骷髅"):
			print ("----------------------------------")
			print ("你为什么这么做？你是个疯子？")
			loop = 10
		if cave_inp.lower() == ("砸碎骷髅"):
			print ("----------------------------------")
			print ("神经病。注意尊重死者！")
			loop = 10
		if cave_inp.lower() == ("点亮房间"):
			print ("----------------------------------")
			print ("你需要一个火炬或者油灯")
			loop = 10
		if cave_inp.lower() == ("打断骷髅"):
			print ("----------------------------------")
			print ("我有2个问题：为什么？用什么？")
			loop = 10
		if cave_inp.lower() == ("走下台阶"):
			loop = 11
		if cave_inp.lower() == ("测量台阶"):
			loop = 11
		else:
			print ("----------------------------------")
			loop = 10

#游戏结束
	while loop == 11:
		if loop == 11:
			print ("----------------------------------")
			print ("你进入了一个泥石流房间")
			print ("泥巴里半埋着一个宝箱，里面装满了珠宝")
			last_inp = raw_input ("你想做什么？")
		if last_inp.lower() == ("打开宝箱"):
			print ("----------------------------------")
			print ("你找到了玉雕像并且完成了你的任务！")
		else:
			print ("----------------------------------")
			loop = 11

		# 退出循环，进入游戏尾声
		exit_inp = raw_input("你还想继续吗？Y/N")
		if exit_inp.lower() == ("N"):
			import os
			quit (1)

		if exit_inp.lower() == ("Y"):
			loop = 3
