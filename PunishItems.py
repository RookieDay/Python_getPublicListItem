# coding=utf-8
import HTMLParser
import time
import urllib
import urllib2
from bs4 import BeautifulSoup
from sqlalchemy import Column, String, Sequence, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# 创建对象的基类:
Base = declarative_base()

# 定义punIshMsg对象:
class PunishMsg(Base):
    # 表的名字:
    __tablename__ = 'guangdongMsg'

    # 表的结构:
    id = Column(Integer, Sequence('id'),primary_key=True)
    case_no = Column(String(200))
    case_name = Column(String(200))
    punish_type1 = Column(String(200))
    punish_type2 = Column(String(200))
    punish_reason = Column(String(500))
    law_item = Column(String(800))
    punish_result = Column(String(800))
    entity_name = Column(String(200))
    credit_no = Column(String(200))
    org_code = Column(String(200))
    reg_no = Column(String(200))
    tax_no = Column(String(200))
    identity_card = Column(String(200))
    legal_man = Column(String(200))
    punish_date = Column(String(200))
    punish_agent = Column(String(200))
    area_code = Column(String(200))
    current_status = Column(String(200))
    offical_updtime = Column(String(200))
    note = Column(String(200))

#数据插入表中
def insertToTable(data_list):
    # 初始化数据库连接:
    engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/t_guangdong')
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    # 创建session对象:
    session = DBSession()
    # 创建新PunishMsg对象:
    pun_msg = PunishMsg(case_no = data_list[0].strip(),
                    case_name = data_list[1].strip(),
                    punish_type1 = data_list[2].strip(),
                    punish_type2 = data_list[3].strip(),
                    punish_reason = data_list[4].strip(),
                    law_item = data_list[5].strip(),
                    punish_result = data_list[6].strip(),
                    entity_name = data_list[7].strip(),
                    credit_no = data_list[15].strip(),
                    org_code = data_list[16].strip(),
                    reg_no = data_list[17].strip(),
                    tax_no = data_list[18].strip(),
                    identity_card = data_list[19].strip(),
                    legal_man = data_list[8].strip(),
                    punish_date = data_list[9].strip(),
                    punish_agent = data_list[10].strip(),
                    area_code = data_list[11].strip(),
                    current_status = data_list[12].strip(),
                    offical_updtime = data_list[13].strip(),
                    note = data_list[14].strip())
    # 添加到session:
    session.add(pun_msg)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()

# post请求获取数据
def postFormData(page_num,num_retries = 2):
    #时间戳
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
    try:
        data = urllib.urlencode(parameters)
        request = urllib2.Request(url, data)
        response = urllib2.urlopen(request)
        postContent = response.read()
    except urllib.URLError as e:
        print('Download error:' % e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP errors
                return postFormData(url, num_retries-1)
    return postContent

# get请求获取数据
def getHTMLContent(url,num_retries = 2):
    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        getContent = response.read()
    except urllib.URLError as e:
        print('Download error:' % e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP errors
                return getHTMLContent(url, num_retries-1)
    return getContent

#获取分析详情页每个链接的HTML
def itemsContent(htmlContent):
    data_list = []
    soup0 = BeautifulSoup(htmlContent,'lxml')
    # 获取所有 <td class="value">
    sfind = soup0.find_all("td", class_=["value"])
    for sitem in sfind:
        data_list.append(sitem.get_text())
    #删除内嵌<td class="value table-inner">内嵌table里的值 下面重新获取
    del data_list[8]
    # 解析内嵌table的td值
    sfindInner = soup0.find_all("tr", class_=["value"])
    for sitem in sfindInner:
        for tdContent in sitem.findAll('td'):
            data_list.append(tdContent.getText())
    #插入数据库
    insertToTable(data_list)

# get 获取每个详情页的链接
def listItemsURL():
    for page_num in range(1):
        page_num += 1
        postContent = postFormData(page_num,3)
        soup = BeautifulSoup(postContent,'lxml')
        for link in soup.find_all('a'):
            itemLink = 'http://www.gdcredit.gov.cn/' + link.get('href')
            print itemLink
            itemsContent(getHTMLContent(itemLink,3))

#入口
if __name__ == '__main__':
    listItemsURL()
