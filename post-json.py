import requests
import json

jsonfile = open("C:\\Users\\sujit\\Downloads\\devices_Devices.json","r")
jsondata = jsonfile.read()

obj=json.loads(jsondata)
print(type(obj))
bucket_name="openmv-devices"
key = "openmv.json"

r = requests.post("https://fc2vjsbsad.execute-api.us-east-1.amazonaws.com/prod/upload?bucket="+bucket_name+"&key="+key,json=obj)
print(r.text)
