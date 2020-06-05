from baike import Baike
import os

keyword = input('请输入查找关键字：')
b=Baike(keyword)
url = b.get_url()
html = b.downlaod_baidubaike_html(url)
a,c,d,x = b.html_parse(html)
print(a,c,d,'相关分词：\n',x)

os.system('pause')
