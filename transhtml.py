# -*- coding: utf8 -*-

__author__ = 'meng'

import os
import sys
import shutil
import re
from bs4 import BeautifulSoup

htmlfilename = sys.argv[1]
outfilename = re.sub('\.html','-new.html',htmlfilename)

filedir = os.path.split(os.path.abspath(htmlfilename))[0]

with open(htmlfilename) as infile:
    lines = infile.read()
    soup = BeautifulSoup(lines)
    imgs = soup.find_all('img')

    # 把img的绝对路径修改为相对路径，并把img复制到html文件所在目录
    for img in imgs:
        if os.path.isabs(img['src']):
            imgfile = os.path.split(img['src'])[1]
            if not os.path.exists(filedir+'/'+imgfile):
                try:
                    shutil.copy(img['src'],filedir)
                    print "Copy %s to %s"%(img['src'],filedir)
                except IOError as e:
                    print e
            img['src'] = imgfile

    # 生成新的html文件
    with open(outfilename,'w+') as outfile:
        outstr = soup.prettify()
        outfile.write(outstr.encode('utf8'))