# -*_coding:utf-8-*-
import string
import random
def get_random(j):
    all_yh = []
    for i in range (1, j+1):
        yh = ''.join (random.sample (sour, 8))
        all_yh.append (yh)
    return all_yh

sour = string.ascii_letters
# print(sour)
j = int(input('你需要多少优惠码？'))
all_yh1 = get_random(j)
all_yh2 = {}.fromkeys(all_yh1).keys()
while len(all_yh2) < j:
    all_yh1.append(get_random(j=10-len(all_yh2)))
    all_yh2 = {}.fromkeys (all_yh1).keys ()
print(all_yh1)