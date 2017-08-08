### 系统是 Win7，Python2.7.9版本。 安装配置Scrapy

- 1.安装Python​ 2.7.9：双击安装即可，在Windows命令行中输入 python提示版本号2.7.9，并进入Python 命令行，表明安装成功。注意，安装时选择pip工具安装，在Windows命令行输入pip --version，提示版本号，则安装成功。

- 2.安装pywin32​：，必须是32位版本的，下载对应版本的pywin32（py2.7），直接双击安装即可，安装完毕之后验证：在python命令行下输入import win32com，没有提示错误，则证明安装成功。

- 3.​安装pyOPENSSL：在https://sourceforge.net/projects/pyopenssl/下载，必须是32位版本的，下载对应版本的pyOpenSSL（py2.7），直接双击安装即可，安装完毕之后验证：在python命令行下输入import OpenSSL，没有提示错误，则证明安装成功。

- 4.安装 lxml​：在Windows命令行中进入C:\Python27\Scripts，输入pip install lxml安装，安装完毕之后验证：在python命令行下输入import lxml，没有提示错误，则证明安装成功。

- 5.安装Twisted：Twisted is an event-driven networking engine written in Python and licensed under the open source。

+ 1) 安装setuptools​：

- 下载地址：http://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11.win32-py2.7.exe    

- 安装完毕之后验证：在python命令行下输入import setuptools，没有提示错误，则证明安装成功​。

+ 2) 安装Zope.Interface​：

- 下载地址：http://pypi.python.org/packages/2.7/z/zope.interface/zope.interface-4.0.1-py2.7-win32.egg

- 安装过程：Windows命令行输入D:\>cd C:\Python27\Scripts C:\Python27\Scripts>easy_install.exe zope.interface-4.0.1-py2.7-win32.egg

- 验证安装：在python命令行下输入​import zope.interface，没有提示错误，则证明安装成功​。

+ 3) 安装Twisted​:

- 下载地址：http://pypi.python.org/packages/2.7/T/Twisted/Twisted-12.1.0.win32-py2.7.msi​

​- 直接安装。 

- 6.安装Scrapy​：在Windows命令行中进入C:\Python27\Scripts，输入pip install Scrapy安装。输入scrapy显示版本号，安装成功。​

- 所以安装的包都在C:\Python27\Lib\site-packages文件夹中可以找到。

### Mysql数据库 + 使用SQLAlchemy
+ 在Mac或Linux上，需要编辑MySQL的配置文件，把数据库默认的编码全部改为UTF-8。MySQL的配置文件默认存放在/etc/my.cnf或者/etc/mysql/my.cnf：
```
[client]
default-character-set = utf8

[mysqld]
default-storage-engine = INNODB
character-set-server = utf8
collation-server = utf8_general_ci
```
```
可以通过MySQL的客户端命令行检查编码：
show variables like '%char%';
```

+ 安装MySQL驱动
```
由于MySQL服务器以独立的进程运行，并通过网络对外服务，所以，需要支持Python的MySQL驱动来连接到MySQL服务器。

目前，有两个MySQL驱动：
mysql-connector-python：是MySQL官方的纯Python驱动；
MySQL-python：是封装了MySQL C驱动的Python驱动。

可以把两个都装上，使用的时候再决定用哪个：
$ easy_install mysql-connector-python
$ easy_install MySQL-python
```

+ 我们以mysql-connector-python为例，演示如何连接到MySQL服务器的test数据库：
```
# 导入MySQL驱动:
>>> import mysql.connector
# 注意把password设为你的root口令:
>>> conn = mysql.connector.connect(user='root', password='password', database='test', use_unicode=True)
>>> cursor = conn.cursor()
# 创建user表:
>>> cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
>>> cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
>>> cursor.rowcount
1
# 提交事务:
>>> conn.commit()
>>> cursor.close()
# 运行查询:
>>> cursor = conn.cursor()
>>> cursor.execute('select * from user where id = %s', ('1',))
>>> values = cursor.fetchall()
>>> values
[(u'1', u'Michael')]
# 关闭Cursor和Connection:
>>> cursor.close()
True
>>> conn.close()
```

- SQLalchemy + mysql 连接 廖雪峰 
[参考0](https://www.liaoxuefeng.com)
[参考1](http://www.jb51.net/article/88375.htm)
[参考2](https://stackoverflow.com/questions/20744277/sqlalchemy-create-all-does-not-create-tables)
[参考3](http://blog.csdn.net/gobitan/article/details/49132031)
[参考4](http://blog.csdn.net/will130/article/details/48502053)
```
$ easy_install sqlalchemy
利用上次我们在MySQL的test数据库中创建的user表，用SQLAlchemy来试试：
```
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='5', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭Session:
session.close()
```

- mysql5.7 Mac 无法解决插入数据乱码的问题，暂且建表的时候设置为UTF8,windows下是没有问题的
