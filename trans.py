#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import json

while True:
	search = raw_input('Enter the words: ')
	url = "http://fanyi.youdao.com/openapi.do"
	values = {
		'keyfrom': 'mytranslater',
		'key' : '1075388304',
		'type' : 'data',
		'doctype' : 'json',
		'version' : '1.1',
		'q' : search
	}#request data

	data = urllib.urlencode(values)#url encode
	data = data.encode('utf-8')
	req = urllib2.Request(url, data)
	try:
		resp = urllib2.urlopen(req)
		transed = resp.read()
		myjson = json.loads(transed)#parse json to python dic
		
		for item in myjson['translation']:
			print item.encode('UTF-8')
		for item in myjson['basic']['explains']:
			print item.encode('UTF-8')
	except Exception as e:
		print (str(e))
