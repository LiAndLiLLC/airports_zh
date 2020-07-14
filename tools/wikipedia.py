import time

import requests
from bs4 import BeautifulSoup

last_request = 0


def 获取所有语言(英文名):
    filename = "cache/{}.html".format(英文名)
    html = ""
    try:
        with open(filename, encoding="utf-8") as w:
            html = w.read()
        print("缓存", 英文名)
    except FileNotFoundError:
        global last_request
        pux = 3 - (time.time() - last_request)
        if pux > 0:
            time.sleep(pux)
        last_request = time.time()
        print("获得", 英文名)
        url = requests.get("https://en.wikipedia.org/w/index.php?search={}"
                           .format(英文名.replace(" ", "+")))
        html = url.text

        with open(filename, "w", encoding="utf-8") as w:
            w.write(html)

    s = BeautifulSoup(html, "lxml")

    r = {}
    for lang in s.find(id="p-lang").find_all("li"):
        if lang.a['lang'] != "zh":
            continue
        a = lang.a['title'].split(" – ")
        r[lang.a['lang']] = " - ".join(a[:-1])

    return r
