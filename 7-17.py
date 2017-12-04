# -*-coding:utf-8-*-
# e,s,w,n 分别代表黑桃，红桃，梅花，方块四种花色，大小写jester为大小王
import random

cards = ['Ae', 'As', 'Aw', 'An', '2e', '2s', '2w', '2n', '3e', '3s', '3w', '3n', '4e', '4s', '4w', '4n', '5e', '5s',
         '5w', '5n', '6e', '6s', '6w', '6n', '7e', '7s', '7w', '7n', '8e', '8s', '8w', '8n', '9e', '9s', '9w', '9n',
         '10e', '10s', '10w', '10n', 'Je', 'Js', 'Jw', 'Jn', 'Qe', 'Qs', 'Qw', 'Qn', 'Ke', 'Ks', 'Kw', 'Kn', 'JESTER',
         'jester']
if __name__ == '__main__':
    player1 = random.sample (cards, 17)
    tem1=set(cards) - set(player1)
    tem1_cards = [i for i in tem1]
    player2 = random.sample (tem1_cards,17)
    tem2 = tem1 - set(player2)
    tem2_cards = [j for j in tem2]
    player3 = random.sample (tem2_cards, 17)
    tem3 = tem2 - set(player3)
    last = [k for k in tem3]
    print('玩家1的牌：%s\n玩家2的牌：%s\n玩家3的牌：%s\n底牌：%s\n'%(player1,player2,player3,last))
