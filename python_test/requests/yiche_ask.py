# -*- coding:utf-8 -*-
# **FILENAME:
# **AUTHOR:  yjy         
# **CREATED TIME:    
# **FUN DESC    :
# **MODIFIED BY :     
# **MODIFIED TIME:    
# **MODIFIED CONTENT:
# **REVIEWED BY:      
# **REVIEWED TIME:  

from bs4 import BeautifulSoup
import requests
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Cookie':'XCWEBLOG_testcookie=yes; XCWEBLOG_testcookie=yes; locatecity=440100; _dadtpqcuq=4a4ec808dc705a79f5f0bea4b98a6855e14b248e; UserGuid=dc66dbd0-423c-4e4c-98c3-a3a3e88a47ed; BitAutoLogId=3493bf91719ef77575cd707b9c3d386f; ASP.NET_SessionId=w533l3mngwnp0tokvcqdaeqd; _dc3c=1; BitautoAskClientId=0640c438837246a9a88d3d72c95b2864; bitauto_ipregion=119.129.75.114%3a%e5%b9%bf%e4%b8%9c%e7%9c%81%e5%b9%bf%e5%b7%9e%e5%b8%82%3b501%2c%e5%b9%bf%e5%b7%9e%2cguangzhou; doubleADCookie=%2C2931%3A0%2C2922%3A0%2C2926%3A1%2C3181%3A0%2C3467%3A0%2C3087%3A0%2C4456%3A0%2C4455%3A0%2C4454%3A0%2C3443%3A0%2C4430%3A0%2C4438%3A1%2C4428%3A0%2C4608%3A0; XCWEBLOG_testcookie=yes; dmt10=65%7C0%7C0%7Cask.bitauto.com%2Fbrowse%2Fl2%2F%7Cask.bitauto.com%2Fbrowse%2Fl2%2Fp1%2F; dmts10=1; dm10=1%7C1487143385%7C0%7C%7C%7C%7C%7C1487141157%7C1487141157%7C0%7C1487141157%7C975982017021514455158a3f91f96c3f%7C0%7C%7C; dm_rff10=guangzhou.bitauto.com%252F%253Freferrer%253Dhttps%253A%252F%252Fwww.baidu.com%252Flink%253Furl%253DFh9hYN5w9EMK19plRSVJrVaD-jECqfJSXsXLnajCTlgmqQW0ZXCm-APQymmo6BE9%2526wd%253D%2526eqid%253D9727aac40000f5d50000000658a3f916%5B%5Dask.bitauto.com%252F%5B%5D0%5B%5D; dcad10=; dc_search10=; CIGDCID=975982017021514455158a3f91f96c3f',
    'Host':'ask.bitauto.com',
    'Refer':'http://ask.bitauto.com/browse/l2/p1/'
}


url = 'http://ask.bitauto.com/browse/l2/p1/'

res = requests.get(url)
soup = BeautifulSoup(res.text,'lxml')
print(soup)

