# -*-coding:utf-8-*-
# 每回合猜测8次，统计胜利和失败回合数次，平均次数
# BUG：首回合重复
# python 2.7.3
from random import randint


# compar() 返回每回合次数
def compar(num1, s):
    i = 8
    while True:
        num2 = input (u'请猜测数字（你有%d次机会）：' % (9 - s))
        if num1 > num2:
            print u'太小了，重新来过^-^'
            s += 1
            i -= 1
            if i == 0:
                break
        elif num1 < num2:
            print u'太大了，重新来过^-^'
            s += 1
            i -= 1
            if i == 1:
                break
        else:
            print u'!猜中了!'
            break
    return s


round_win = 0  # 胜利的回合次数
round_fail = 0  # 失败的回合次数
time = 0  # 猜测次数

new = input (u'1:新游戏  2:退出')  # 1:开始新游戏 2:退出游戏
s = 1
while new == 1:
    num1 = randint (1, 100)  # 生成目标数字
    if compar (num1, s) <= 8:
        time += compar (num1, s)
        round_win += 1
        new = input (u'回合胜利>>1:新游戏 2:退出')
    else:
        time += 8
        round_fail += 1
        new = input (u'回合失败>>1:新游戏 2:退出')
round = round_fail + round_win
if round != 0:
    print u"您共进行了%d回合游戏\n%d 次胜利  %d次失败" % (round, round_win, round_fail)
    if (round_win == 0) and (round_fail >= 0):
        print u'您没有猜中1次，哈哈'
    else:
        print u'平均%.1f次猜中1个数字' % float (time / round)
else:
    print u'您共进行了 0 回合游戏'
