#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2

while True:
	search = raw_input('Enter the words')
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
		print transed
	except Exception as e:
		print (str(e))