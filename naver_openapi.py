import requests
import pprint

headers = {
    'X-Naver-Client-Id':'dBcQnCr01YVGlz_Rf2l9',
    'X-Naver-Client-Secret':'cgYtf0efrN',
}

payload = {
    'query':'파이썬',
    'display':100
}

url = 'https://openapi.naver.com/v1/search/blog'

res = requests.get(url, headers=headers, params=payload)
print('request sends..')
result = res.json()['items'][3]['title']
print(result)
