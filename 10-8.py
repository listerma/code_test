# -*-coding:utf-8 -*-
import urllib.request, urllib.parse
import json

city_name = input('查询城市：')
city_name = urllib.parse.quote(city_name)
# url 地址
url = ('http://wthrcdn.etouch.cn/weather_mini?city=%s' % city_name)
# print(url)
req = urllib.request.urlopen(url)
data = req.read()
headers = req.info()
if 'Content-Encoding' in headers and 'gzip' == headers['Content-Encoding']:
    import gzip
    from io import BytesIO

    data = BytesIO(data)
    gz = gzip.GzipFile(fileobj = data)
    data = gz.read().decode('utf8')
    gz.close()
# print(data)
j_data = json.loads(data)
content = j_data['data']
# print(content)

print('城市：%s\n感冒：%s\n当前温度：%s℃'%(content['city'],content['ganmao'],content['wendu']))
print('五日预告：')
for i in content['forecast']:
    for j in i:
        print(i[j])
