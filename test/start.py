# -*- coding: utf-8 -*-
import sys
import pip
modules_dependances = ["urllib3",'beautifulsoup4','xlwt']
for m in modules_dependances:
	if not (m in sys.modules):
		pip.main(['install','--user', m]) 