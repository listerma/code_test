# -*-coding:utf-8-*-
#c 梅花 h 红桃 s 黑桃 d 方片
import random
suit = ['c','h','s','d']
num = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
card = []
for i in range(len(suit)):
    for j in range(len(num)):
        card.append(suit[i]+num[j])
card.append('JESTER')
card.append('jester')
random.shuffle(card)
last_card = card[-3:]
card = card[:-3]
play1 = card[::3]
play2 = card[1::3]
play3 = card[2::3]
print('玩家1的牌：%s\n玩家2的牌：%s\n玩家3的牌：%s\n底牌：%s\n'%(play1,play2,play3,last_card))