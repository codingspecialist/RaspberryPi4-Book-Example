from urllib.parse import unquote
import requests
import json

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
params ={
    'serviceKey' : unquote('일반인증키'), 
    'pageNo' : '1', 
    'numOfRows' : '1000', 
    'dataType' : 'JSON', 
    'base_date' : '20240824', 
    'base_time' : '0600', 
    'nx' : "59", 
    'ny' : "127" 
}

response = requests.get(url, params=params)
r_dict = json.loads(response.text)
r_response = r_dict.get("response")
r_body = r_response.get("body")
r_items = r_body.get("items")
r_item = r_items.get("item")
result = {}
for item in r_item:
   if(item.get("category") == "T1H"):
       result=item
       break
print("============= data start ==================")
print(result)
print("============= data start ==================")
