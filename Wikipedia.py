

import requests
from bs4 import BeautifulSoup


def get(url):
    u = BeautifulSoup(requests.get(url).text, features="lxml")
    u = u.find("table", class_="infobox")
    name = u.find("th", class_="org").text
    iata, icao = [i.text for i in u.find_all("span", class_="nickname")[:2]]
    print("{},{},{}".format(name, iata, icao))


for i in ["春秋航空",
          "长安航空",
          "奥凯航空",
          "九元航空",
          "瑞丽航空",
          "东海航空",
          "成都航空",
          "福州航空",
          "长龙航空",
          "桂林航空",
          "北部湾航空",
          "首都航空",
          "幸福航空",
          "昆明航空",
          "河北航空",
          "西部航空",
          "江西航空",
          "西藏航空",
          "乌鲁木齐航空",
          "金鹏航空"
          "中国联合航空",
          ]:
    get("https://zh.wikipedia.org/wiki/{}".format(i))
