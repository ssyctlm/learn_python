#coding:utf-8
import random
from sys import exit

print "欢迎来到寻宝世界"
def wood():
	print "你来到一个森林，森林里雾气笼罩，你只能隐隐看见两条路，一条深入迷雾，另外一条看过去隐约可以看见幽暗的灯光"
	print "你打算怎么办？"
	print "1.朝迷雾里走\n2.向着亮光走\n3.原路返回吧"
	choice = raw_input("::")
	if choice == "1" :
		print "你顺着脚下的路慢慢走进迷雾深处"
		lake ()
		
	elif choice == "2":
		print "向着幽暗的灯光前进"
		house()
		
	elif choice == "3":
		print"你转身退了回去"
		start()
		
	else:
		dead( "你犹豫不决，但慢慢感觉到头晕目眩，一下子栽倒在地，晕死了过去，原来雾里有毒孢子，你再也醒不过来了!\n game over")
		
def origin():
	print '你独自一人在一个海滩边醒来，背后是一艘被海浪打翻的船'
	print "你仔细回想……记起来你一周前在博物馆里遇见了一条会说话的蟒蛇，它给了你一张藏宝图，你便独自一人按照藏宝图来寻宝了"
	print "你翻身起来，掸掸身上的泥沙，发展藏宝图已经不见了，你环顾四周……"
	start ()
	
def start():
	print"----------------"
	print "你在沙滩上，面朝一片茂密的森林，背对一望无际的大海，左边是一片山，右边是沙滩一直延伸到远处"
	print "接下来你想先探索哪里？\n1.探索森林\n2.探索山\n3.探索沙滩"
	print"----------------"
	choice_start = raw_input("我的选择是:::")
	print"----------------"
	if choice_start == "1":
		wood()
	elif choice_start == "2":
		hill()
	elif choice_start == "3":
		beach()
	else:
		print "认真点选择，下边的路上如果乱选可能会丧命！！！"
		start()

def hill():
	print"----------------"
	print "走了10分钟终于到了山脚下，但是什么也没有，山非常高……"
	print "看来你走到了死胡同，还是回去吧"
	print "你回去吗？ yes？ no？"
	print"----------------"
	choice_hill = raw_input("我的选择是:::")
	if choice_hill == "yes":
		start()
	else:
		print "那就在这里呆一会看看吧……"
		dead("轰隆隆，突然地动山摇，原来这座山是一个沉睡的巨兽，它翻了个身，刚好把你压在了身下…… GAME OVER！")

def beach():
	print"----------------"
	print "来时坐的船已经粉碎了……"
	print "怎么才能从这里离开回家呢？唉……"
	print "不想这么多了，既来之则安之，还是先去寻找宝藏吧"
	print"----------------"
	choice_beach = raw_input("输入任意字符，继续寻宝")
	start()



def house():
	print "随着灯光越来越清晰，一间供猎人休息的木质房子展现在你眼前。看起来已经很久没人住过了，但是为什么会有灯光呢？\n 你要进屋去看看吗？"
	print "1.进去\n2.退回去\n3.再观察观察 "
	choice_house = raw_input(":::")
	if choice_house == "1":
		print "你上前几步，推开了虚掩的门，\"嘎吱\"一声"
		house_in()
	elif choice_house == "2":
		print "也许你确实不应该冒这个险，原路退了回去"
		dead("来时路上的雾更浓了，你才走了不远，便觉得昏昏入睡起来，原来雾里有毒孢子，最终你昏死了过去，再也起不来了。 \n GAME OVER")
	elif choice_house == "3":
		print "房子前写着一排小字"
		print "不入虎穴，焉得虎子"
		print "你四周环望，似乎没有别的异样了"
		house()
	else:
		print "没有别的选择了"
		house()


def lake():
	print "走了一会，豁然开朗，一片湖展现在你面前。湖面非常的平静，一点生物都没有。皎洁的月光倒影在湖面上，一动也不动，你不禁打了一个寒颤。\n这是一片四周被森林包围的湖泊。\n你打算怎么做？"
	print "1.有点渴了，喝口水吧\n2.绕着湖走一圈\n3.看来这里没什么东西，还是原路返回吧\n4.天色太晚了，不知道做什么，睡一觉吧"
	print"----------------"
	choice_lake = raw_input("我的选择是:::")
	print"----------------"
	if choice_lake == "1":
		print "你趴在湖边刚要用手捧水，突然从水下深出一个触角，缠住你的脖子，把你拖下了水。"
		dead("一个大湖怪从水中显现出来，你被它吞进了肚子里…… GAME OVER")
	elif choice_lake == "2":
		print "你绕胡走了一圈，发现这个湖其实是一个凹地，没有办法到达别的地方，你又回到了原点"
		lake()
	elif choice_lake == "3":
		wood()
	elif choice_lake == "4":
		print "很快你便睡着了，但是湖水悄悄涨高了，把你淹没了进去，你还没来得及喊叫，便被一个黏糊糊的触手拖入了湖中深处……"
		dead("一个大湖怪从水中显现出来，你被它吞进了肚子里…… GAME OVER")
	else:
		print "没有别的选择了"
		lake()


	
def house_in():
	print"----------------"
	print "这房子已经年久失修了，木质地板走上去嘎吱嘎吱作响"
	print "一只被拴在房屋中间柱子上的瞎狗听见有人来，便竖起了耳朵，呲牙低吼着"
	print "瞎狗身后有一扇门，看样子想通过就必须想办法绕过去"
	print"----------------"
	print "地上有一串鞭炮，有一个肉骨头，还有一把生锈的铁剑"
	print "你要怎么做呢？\n1.点燃鞭炮吸引狗，偷偷溜进门去\n2.拿肉骨头引诱它，偷偷溜进门去\n3.拿起铁剑和狗拼了"
	print"----------------"
	choice_housein = raw_input("我的选择是:::")
	print"----------------"
	if choice_housein == "1":
		print "狗真的扑向了鞭炮，你趁机溜进门去"
		guesspsw()
	if choice_housein == "2":
		print "狗扑向了骨头，大口啃起骨头来"
		dead("你悄悄从它身后溜过，但是地板嘎吱声太大，狗立刻反扑过来，一口咬断了你的脖子…… GAME OVER！")
	if choice_housein == "3":
		print "你鼓起勇气，挥舞着大剑向狗砍去，但是剑太顿了，没有砍伤狗"
		dead("狗扑了过来，咬断了你的脖子……GAME OVER！")
	else:
		print "你这么做什么意义也没有"
		dead("限制着狗的铁链子经不起狗一直地扑腾，很快就断开了，狗冲过来，一口咬断了你的脖子……GAME OVER!")

def guesspsw():
	print "'干的不错，伙计'。不知从哪里传了一一个低沉的声音"
	print "'你已经快要拿到宝藏了，但是你还需要再和我玩一个猜数字的游戏。'\n'我心里想着一个111-999之间的数，现在你需要在10次机会之内猜出这个数，'\n'猜对了你就可以拿到我为你准备的宝藏，猜错了……嘿嘿'"
	print"----------------"
	print"游戏开始了！"
	print"----------------"
	num = random.randint(111,999)
	tries = 0
	guess = 0
	while guess!=num and tries < 10 :
		print "你还有%s次机会"%(10-tries)
		guess = int(raw_input("你猜多少？"))
		if 999<guess or guess<111:
			print "嘿！我想的数是111-999之间的！你浪费了一次机会！"
		elif guess > num and 200=>guess-num>100:
			print"你猜的数忒大了"
		elif guess > num and guess-num>200:
			print "你猜的数大的离谱！"
		elif guess > num and guess - num <100:
			print "你猜的数接近了，但是有点大"
		elif guess < num and num-guess >200:
			print"你猜的数小的离谱！"
		elif guess < num and num-guess < 100:
			print "你猜的数很接近了，但是小了一点"
		elif guess < num and 200 => num-guess >100:
			print "你猜的数字忒小了，再试试"
		
		
		tries+=1
		
	if guess == num:
		print"恭喜，聪明鬼，你猜对了！我想的数就是%s!现在，你可以拿着这个数去打开密室的门了！"%num
		print "随后你面前凭空出现一扇门并且打开了"
		get_psw =True
		print"一个装饰精美的宝箱展现在你面前，宝箱盖上有一把密码锁，大概是需要你输入密码吧……"	
		psw = int(raw_input())
		
		if psw == num:
			print "咔嚓，宝箱开了，里边装有各式各样的珠宝和金币"
			print "恭喜你，获得了宝藏，而且宝箱里还有一个魔法飞毯，看来你可以回家了！"
		while psw!=num:
			print "你好像记错了密码，再想想吧"
			
	else:
		print "你的机会用完了！我想的数是%s,再见吧！"%num
		print "你想再试一次吗？\n1.yes\n2.no"
		again = raw_input()
		if again == "1":
			guesspsw()
		else :
			dead("你脚下的地板突然消失了，你顺势跌了下去，被下边锋利的钢钉扎死了……")
		
#def baozang():
	#print"一个装饰精美的宝箱展现在你面前，宝箱盖上有一把密码锁，大概是需要你输入密码吧……"	
	#psw = int(raw_input())
	
	#if psw == guess:
		#print "咔嚓，宝箱开了，里边装有各式各样的珠宝和金币"
		#print "恭喜你，获得了宝藏，下次再见"
	#while psw!=num:
		#print "你好像记错了密码，再想想吧"
def dead(why):
	print why,"再见"
origin()
