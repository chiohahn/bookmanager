
import requests
import json
import pprint


text = '코우'
payload = {
	'ttbkey' : 'ttbfusioner0438003', 
	'QueryType' : 'Title',
	'Query':text,
	'SearchTarget':'Book', 
	'MaxResults':'99', 
	'start':'1', 
	'Sort':'title',
	'CategoryId':'2551',
	'output':'js', 
	'inputencoding':'utf-8',
	'Version':'20131101'
}

url = 'http://www.aladdin.co.kr/ttb/api/ItemSearch.aspx'

res = requests.get(url, params=payload)
js_contents = json.loads(res.content.decode("utf-8"))

for item in js_contents['item']:
	print(item['title'])

'''
payload = {
	'ttbkey' : 'ttbfusioner0438003', 
	'QueryType' : 'ItemNewAll', 
	'SearchTarget':'Book',
	'MaxResults':'99', 
	'start':'1', 
	'SearchTarget':'Book', 
	'CategoryId':'2551',
	'output':'js', 
	'outofStockfilter':'1',
	'inputencoding':'utf-8',
	'Version':'20131101'
}

url = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'

res = requests.get(url, params=payload)
js_contents = json.loads(res.content.decode("utf-8"))

for item in js_contents['item']:
	print(item['title'])
'''