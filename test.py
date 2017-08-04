#coding=utf-8
import time
import urllib
import urllib2
import HTMLParser
import re
import scrapy

def post(page_num):

    t = int(time.time()*1000)
    #所要请求数据的url
    url="http://www.gdcredit.gov.cn/infoTypeAction!xzTwoPublicList.do?refresh" + str(t)

    print url

    parameters = {
        'type': 7,
        'keyWord': '',
        'depId': '',
        'depType': 0,
        'page': page_num,
        'pageSize': 10,
        }

    data = urllib.urlencode(parameters)
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
    content = response.read()

    return content

# hrefs = re.findall(r'(?<=href=\").+?(?=\")', content)
#hrefs = re.findall(r'<a.*?href=.*?<\/a>', content)
#for i in hrefs:
#    print i

class MyParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
    def handle_starttag(self, tag, attrs):
        # 这里重新定义了处理开始标签的函数
        if tag == 'a':
            # 判断标签<a>的属性
            for name,value in attrs:
                if name == 'href':

                    print 'http://www.gdcredit.gov.cn' + value

if __name__ == '__main__':
   # a = '<html><head><title>test</title><body>< a href=" vhfhfh">链接到163</ a>焦点</body></html>'
    for page_num in range(21):
        page_num += 1
        a = post(page_num)
        my = MyParser()
        # 传入要分析的数据，是html的。
        my.feed(a)