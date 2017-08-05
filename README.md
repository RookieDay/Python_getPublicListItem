### 系统是 Win7，Python2.7.9版本。

- 1.安装Python​ 2.7.9：双击安装即可，在Windows命令行中输入 python提示版本号2.7.9，并进入Python 命令行，表明安装成功。注意，安装时选择pip工具安装，在Windows命令行输入pip --version，提示版本号，则安装成功。

- 2.安装pywin32​：，必须是32位版本的，下载对应版本的pywin32（py2.7），直接双击安装即可，安装完毕之后验证：在python命令行下输入import win32com，没有提示错误，则证明安装成功。

- 3.​安装pyOPENSSL：在https://sourceforge.net/projects/pyopenssl/下载，必须是32位版本的，下载对应版本的pyOpenSSL（py2.7），直接双击安装即可，安装完毕之后验证：在python命令行下输入import OpenSSL，没有提示错误，则证明安装成功。

- 4.安装 lxml​：在Windows命令行中进入C:\Python27\Scripts，输入pip install lxml安装，安装完毕之后验证：在python命令行下输入import lxml，没有提示错误，则证明安装成功。

- 5.安装Twisted：Twisted is an event-driven networking engine written in Python and licensed under the open source。

+ 1) 安装setuptools​：

下载地址：http://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11.win32-py2.7.exe    

安装完毕之后验证：在python命令行下输入import setuptools，没有提示错误，则证明安装成功​。

+ 2) 安装Zope.Interface​：

下载地址：http://pypi.python.org/packages/2.7/z/zope.interface/zope.interface-4.0.1-py2.7-win32.egg

安装过程：Windows命令行输入D:\>cd C:\Python27\Scripts C:\Python27\Scripts>easy_install.exe zope.interface-4.0.1-py2.7-win32.egg

验证安装：在python命令行下输入​import zope.interface，没有提示错误，则证明安装成功​。

+ 3) 安装Twisted​:

下载地址：http://pypi.python.org/packages/2.7/T/Twisted/Twisted-12.1.0.win32-py2.7.msi​

​直接安装。 

- 6.安装Scrapy​：在Windows命令行中进入C:\Python27\Scripts，输入pip install Scrapy安装。输入scrapy显示版本号，安装成功。​

所以安装的包都在C:\Python27\Lib\site-packages文件夹中可以找到。
