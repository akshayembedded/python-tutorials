import http.client

conn = http.client.HTTPSConnection("airport-info.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "7179d2b5demsh8508333ef1dfc8fp1f2cebjsn53804e6a43a2",
    'X-RapidAPI-Host': "airport-info.p.rapidapi.com"
    }

conn.request("GET", "/airport?iata=trv", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))