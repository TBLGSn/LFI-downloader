这是一个用来下载 [lfi-online.de](https://lfi-online.de/ceemes/en/gallery/mastershots/info.html) 的图片的爬虫
在这个网站右击图片并不能保存图片,而通过这个软件你只要 copy 地址栏的地址,就可以下载图片了.

# 依赖
```py
import requests
import re
import sys
from lxml import etree
```
# 用法
```c++
// 激活虚拟环境
source py/bin/activate
python main.py [这里是上面地址出的图片链接]
```