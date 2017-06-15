# -*- coding: utf-8 -*-
import urllib3
import sys
from bs4 import BeautifulSoup
import xlwt
tags = ['title','h1','h2','h3','h4','h5','h6']
if len(sys.argv) > 1:
	http = urllib3.PoolManager()
	html = http.request("get",sys.argv[1])
	bsObj = BeautifulSoup(html.data,'html.parser')
	workbook = xlwt.Workbook(encoding = 'utf-8')
	worksheet = workbook.add_sheet('Titres')
	for column, tag in enumerate(tags):
		worksheet.write(0, column, label = tag)
		indice = 1
		for content in bsObj.find_all(tag):
			worksheet.write(indice, column, label = content.text)
			indice += 1
	workbook.save('SEO.xls')