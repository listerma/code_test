# -*-coding:utf-8-*-
# 屏蔽词，修改为*
f = open (u'E://屏蔽列表.txt', encoding='utf-8')
f_list = f.read ().split (';')
wd = str (input (u'输入弹幕：'))
wd=wd.lower()
for i in f_list:
    # print (i)
    if wd.find (i) != -1:
        wd = wd.replace(i,'*'*len(i))
        # print (u'find')
        break
        # for j in f_list[i].split(''):

f.close ()
print (u'%s' % wd)
