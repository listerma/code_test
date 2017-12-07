# -*- coding: utf-8 -*-

import urllib.request
import traceback

url1 = 'http://m.weather.com.cn/data3/city.xml'
content1 = urllib.request.urlopen (url1).read ().decode ('UTF-8')
provinces = content1.split (',')
result = 'city = {\n'
url = 'http://m.weather.com.cn/data3/city%s.xml'
for p in provinces[1:]:
    p_code = p.split ('|')[0]
    url2 = url % p_code
    content2 = urllib.request.urlopen (url2).read ().decode ('UTF-8')
    cities = content2.split (',')
    # print (cities)
    for c in cities:
        c_code = c.split ('|')[0]
        url3 = url % c_code
        content3 = urllib.request.urlopen (url3).read ().decode ('UTF-8')
        districts = content3.split (',')
        for d in districts:
            d_pair = d.split ('|')
            # print (d_pair)
            d_code = d_pair[0]
            name = d_pair[1]
            url4 = url % d_code
            # print (url4)
            try:
                content4 = urllib.request.urlopen (url4).read ().decode ('UTF-8')
                # print (content4)
                # content4_content = content4.split ('|')
                # print ('哈哈-->%s' % content4_content)
                code = content4.split ('|')[1]
            except:
                break
            else:
                line = "    '%s': '%s',\n" % (name, code)
                result += line
                print (name + ':' + code)
result += '}'
f = open ('city.py', 'w')
f.write (result)
f.close ()
