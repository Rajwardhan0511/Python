#!/user/bin/python3
import json, requests, pickle

def getData():
    urls = [
    "https://reqres.in/api/users?page=1",
    "https://reqres.in/api/users?page=2"
    ]
    header = {"user-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0","Content-Type":"application/json"}
    
    total = []
    for url in urls:
        data = requests.get(url,headers=header,timeout=10,allow_redirects=True)
        json_byte = pickle.dumps(data.text)
        plain = pickle.loads(json_byte)
        plain1 = json.loads(plain)
        total.append(plain1)
    details(total)


def details(total): 
    did = input("Enter the usei id to retrive details: ")
    count=0
    c=len(total)
    for data in total:
        count += len(data['data'])
        c -= 1
        if did!='all':
            try:
                did=int(did)
                if did>count:
                    if c==0:
                        print("ID NOT FOUND!!!")
                        return None
                    continue
                    
            except Exception:
                print("Enter Valid ID!!!")
                break
    
        for i in data['data']:
            if did=='all':
                print(f"id: {i['id']}\nfirst_name: {i['first_name']}\nlast_name: {i['last_name']}\nemail: {i['email']}\navatar: {i['avatar']}\n")
            else:
                if did==i['id']:
                    print(f"first_name: {i['first_name']}\nlast_name: {i['last_name']}\nemail: {i['email']}\navatar: {i['avatar']}")
                
        
if __name__ == "__main__":
    getData()
