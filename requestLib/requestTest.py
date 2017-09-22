import requests
from bs4 import BeautifulSoup
# try:
#     kv = {'wd':'python'}
#     r = requests.get("http://www.baidu.com/s",params=kv)
#     r.raise_for_status()        #如果请求的返回码不是200 则抛出异常
#     # 1 用r.status_code去分析返回的状态码   200为正确返回
#     # 2 如果证券返回  使用r.encoding（head中设置的encoding）  r.text(字符串形式)   r.apparent_encoding（从内容分析出来的编码）  r.content（二进制内容如图片）
#     print(r.status_code)
#     print(r.request.url)
#     if r.status_code == 200:
#         print(r.text[:100])
#         print(r.encoding)
#         print(r.apparent_encoding)
#         r.encoding = r.apparent_encoding        #设置当前编码为内容编码
#         print(r.text[:100])
# except:
#     print("err")
#     requests.HTTPError

path = "https://www.ccc860.com/htm/gif0/817.htm"
try:
    r = requests.get(path)
    r.raise_for_status()
    soup = BeautifulSoup(r.text,'html.parser')
    print(soup.body.prettify())
    for theTag in soup.body.descendants:
        if theTag.name == 'img':
            rr = requests.get(theTag.attrs['src'])
            fileName = (theTag.attrs['src']).split('/')[-1]
            f = open(fileName,'wb')
            f.write(r.content)
except:
    print("no")