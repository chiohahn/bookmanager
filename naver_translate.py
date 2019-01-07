from requests import Session, Request

s = Session()

headers = {
    'X-Naver-Client-Id':'dBcQnCr01YVGlz_Rf2l9',
    'X-Naver-Client-Secret':'cgYtf0efrN',
}

text = "本日上京しますが、問題は天候です こればかりはどうにもなりませんが、予定通り行って帰ってこれる事を祈るだけ では、いってきます"

payload = {
    'source':'ja',
    'target':'ko',
    'text':text,
}

url = "https://openapi.naver.com/v1/papago/n2mt"

wf = open('trans.txt', 'w', encoding='utf-8')
#with open('text.txt', 'r', encoding='utf-8') as file:
rf = open('text.txt', 'r', encoding='utf-8')
lines = rf.readlines()
for line in lines:
    payload = {
        'source':'ja',
        'target':'ko',
        'text':line,
    }
    req = Request('POST', url, data=payload, headers=headers)
    prepped = req.prepare()
    res = s.send(prepped)
    result = res.json()['message']['result']['translatedText']
    wf.write(result+'\n')
    print(result)