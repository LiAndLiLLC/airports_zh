import requests
from bs4 import BeautifulSoup


def 获取所有语言(英文名):
    html = ""
    url_template = "https://en.wikipedia.org/w/index.php?search={}"
    url = requests.get(url_template.format(英文名.replace(" ", "+")))
    html = url.text

    s = BeautifulSoup(html, "lxml")

    r = {}
    for lang in s.find(id="p-lang").find_all("li"):
        if lang.a['lang'] != "zh":
            continue
        a = lang.a['title'].split(" – ")
        r[lang.a['lang']] = " - ".join(a[:-1])

    return r
