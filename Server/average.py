import requests
import json
import csv
import time
import datetime


r=requests.get('https://api.thingspeak.com/channels/414360/fields/1.json?api_key=VRK1AH4TKL60MARF&results=2')
data = r.json()
data = data["feeds"][1]["field1"]
data = float(data)
arr = [data]
i = 1
while i <= 75:
    r=requests.get('https://api.thingspeak.com/channels/414360/fields/1.json?api_key=VRK1AH4TKL60MARF&results=2')
    data = r.json()
    data = data["feeds"][1]["field1"]
    data = float(data)
    arr.append(data)
    average = sum(arr)/len(arr)   
    print average
    i = i + 1

while i > 75:
    r=requests.get('https://api.thingspeak.com/channels/414360/fields/1.json?api_key=VRK1AH4TKL60MARF&results=2')
    data = r.json()
    data = data["feeds"][1]["field1"]
    data = float(data)
    arr.append(data)
    arr.pop(1)
    average = sum(arr)/len(arr)   
    print average
    if average > 15:
        a = datetime.datetime.now()
        while (datetime.datetime.now() - a).seconds <= 600:
            r=requests.get('https://api.thingspeak.com/channels/414360/fields/1.json?api_key=VRK1AH4TKL60MARF&results=2')
            data = r.json()
            data = data["feeds"][1]["field1"]
            data = float(data)
            arr.append(data)
            arr.pop(1)
            average = sum(arr)/len(arr)   
            print average
        if average > 150:
            print "MAIL \n MAIL \n MAIL \n MAIL \n " * 100

2