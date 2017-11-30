# -*-coding:utf-8-*-
# 以特定符号<元素>（！ *等）绘制长a，宽b的长方形
def rect(a, b, fh):
    for i in range (1, b + 1):
        for j in range (1, a + 1):
            print (u'%s' % fh, end="")
        print (u'\n')


a = int (input (u'输入长方形的长度（整数）：'))
b = int (input (u'输入长方形的宽度（整数）：'))
fh = str (input (u'输入长方形的元素（符号）：'))
rect (a, b, fh)
