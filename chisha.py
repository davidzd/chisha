#coding=utf-8

import urllib
import json
import random

apiUrl = "http://api.map.baidu.com/place/v2/"
requestUrl = apiUrl + "search?query=小吃&page_size=50&location=39.9842810000,116.3202080000&radius=2000&output=json&ak=82a3d1f26f618030cd18d077c82fce6f"
response = urllib.urlopen(requestUrl)
res_an = response.read()
ddata = json.loads(res_an)
result = []
for i in range(0,20):
    result.append(ddata[u'results'][i][u'name'])
n = random.randint(0,len(result))
a = result[n].encode("utf-8")
print '今天中午吃: %s'%a
