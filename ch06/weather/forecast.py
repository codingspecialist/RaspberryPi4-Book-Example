from urllib.parse import urlencode, unquote
import requests
import json

def get_forecast(base_date, base_time):
    url = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastGrib"
    queryString = "?" + urlencode(
        {
            "ServiceKey" : unquote("wJmmW29e3AEUjwLioQR22CpmqS645ep4S8TSlqtSbEsxvnkZFoNe7YG1weEWQHYZ229eNLidnI2Yt5EZ3Stv7g%3D%3D"), 
            "base_date" : base_date, 
            "base_time" : base_time, 
            "nx" : "59", 
            "ny" : "127", 
            "numOfRows" : "10", 
            "pageNo" : "1", 
            "_type" : "json" 
        }
    )

    response = requests.get(url + queryString)

    # parsing
    r_dict = json.loads(response.text)
    r_response = r_dict.get("response")
    r_body = r_response.get("body")
    r_items = r_body.get("items")
    r_item = r_items.get("item")

    result = {}
    for item in r_item:
        if(item.get("category") == "T1H"):
            result = item
            break
            
    return result