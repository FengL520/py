# -*- coding: utf-8 -*-
import sys
import pip
module_dependances = ["urllib3",'hello']
for m in module_dependances:
	if not (m in sys.modules):
		print(m+' n\'est pas installé')