import requests
import json

jsonfile = open("C:\\Users\\sujit\\Downloads\\00000_Info.json","r")
jsondata = jsonfile.read()

obj=json.loads(jsondata)
print(type(obj))
bucket_name="raspi-dev"
key = "0000_info.json"

header_r = {"x-api-key":""}

r = requests.post("https://l1muii6ihk.execute-api.us-east-1.amazonaws.com/v1/uploads",json=obj,headers=header_r)
print(r.headers)