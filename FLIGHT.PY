import http.client

conn = http.client.HTTPSConnection("aerodatabox.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "7179d2b5demsh8508333ef1dfc8fp1f2cebjsn53804e6a43a2",
    'X-RapidAPI-Host': "aerodatabox.p.rapidapi.com"
    }

conn.request("GET", "/flights/number/UAL1122/%7BdateLocal%7D?withAircraftImage=false&withLocation=false", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))