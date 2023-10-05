import http.client
import json

KEY = "7bbe453c5d1a4898943e72969588c96a"

conn = http.client.HTTPSConnection("rawg-video-games-database.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "c1f3560e9dmshfdc1351948c8ed1p108ee4jsn0bcb17954627",
    'X-RapidAPI-Host': "rawg-video-games-database.p.rapidapi.com"
}

conn.request("GET", f"/games/3939?key={KEY}", headers=headers)

res = conn.getresponse()
data = res.read()

print(json.loads(data.decode("utf-8")))