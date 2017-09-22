import requests
from bs4 import BeautifulSoup
import re
import os
import traceback

path = "http://91.p9a.space/forumdisplay.php?fid=19&page="
rootPath = "http://91.p9a.space/"
count = 5  #爬十页
regex = re.compile(r'.*[成都,武汉].*')

def getImg(text):
    soup = BeautifulSoup(text,'html.parser')
    # print(soup.body.prettify())
    allImg = soup.find_all('img')
    # print(allImg)
    for img in allImg:
        try:
            src = img.attrs['file']
            realPath = rootPath+""+src
            if src:
                print(src)
                name = src.split('/')[-1]
                print(name)
                file = open('pics/'+name,'wb')
                file.write(requests.get(realPath).content)
        except:
            "s"


def scrapyUrl(url,pageNums):
    print(pageNums)
    r = requests.get(url + ''+pageNums)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text,'html.parser')
    # print(soup.body.prettify())
    alla = soup.find_all("a")
    for theA in alla:
        try:
            str = theA.string
            if str:
                if '成都' in str:
                    print(str)
                    realPath = rootPath + theA.attrs['href']
                    print(realPath)
                    print('now  realpath：' + realPath);
                    r = requests.get(realPath)
                    r.raise_for_status()
                    r.encoding = r.apparent_encoding
                    # getImg(r.text)
        except:
            print('no1')

def all():
    for i in range(101,150):
        strs = str(i)
        scrapyUrl(url=path,pageNums=strs)

all()