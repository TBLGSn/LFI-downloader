import requests
import re
import sys
from lxml import etree

# 得到真正的图片链接
def getrealurl(url):
    text = requests.get(url).text
    l = ".value.: .(.*).*"
    realurl = re.findall(l, text)
    ans = []
    for a in realurl:
        # print(a)
        ans.append(a)
    realurl = ans[0]
    realurl = "" + realurl
    realurl = realurl.replace('\/','/')
    print("realurl: "+ realurl + "\n")
    return realurl 

# 下载并存储图片
def download_and_Saveimage(realurl, name):
    if( realurl ):
        print( "realurl为"+ realurl + "\n")
    if( name ):
        print( "name为空"+ name +"\n") 
    image = requests.get(realurl)
    with open(name,"wb") as f:
        f.write(image.content)
    print( "下载完毕"+ "\n")

# 解析出图片名称
def get_image_name(realurl):
    name = re.findall("\d/(.*)\"", realurl)
    if (name):
        print("图片名称为" + name[0])
        return ""+ name[0]
    else :
        print("提取图片名称出错")
        return;

####################### main #########################
url = sys.argv[1] # 得到下载链接

realurl = getrealurl(url)
name = get_image_name(realurl)

download_and_Saveimage(realurl, name)

