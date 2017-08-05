# coding=utf-8
import HTMLParser
import time
import urllib
import urllib2
import re
language = ''
# python get post data
def postFormData(page_num):
    t = int(time.time() * 1000)
    # 所要请求数据的url
    url = "http://www.gdcredit.gov.cn/infoTypeAction!xzTwoPublicList.do?refresh" + str(t)

    parameters = {
        'type': 7,
        'keyWord': '',
        'depId': '',
        'depType': 0,
        'page': page_num,
        'pageSize': 10,
    }
    # post请求获取数据
    data = urllib.urlencode(parameters)
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
    content = response.read()
    return content

def getHTMLContent(url):
    # get请求获取数据
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    content = response.read()
    return content

class MyParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
    def handle_starttag(self, tag, attrs):
        # 这里重新定义了处理开始标签的函数
        if tag == 'tr':
            # 判断标签<a>的属性
            for name,value in attrs:
                print('a')



# get list items url
def listItemsURL():
    for page_num in range(1):
        page_num += 1
        postContent = postFormData(page_num)
        itemsURL = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')",postContent)
        for item in itemsURL:
            if(item.startswith('/infoTypeAction')):
                item = "http://www.gdcredit.gov.cn" + item
                css = getHTMLContent(item)
                my = MyParser()
                # 传入要分析的数据，是html的。
                my.feed(css)
                # print(css)


if __name__ == '__main__':
    listItemsURL()


