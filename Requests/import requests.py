import requests
import json



url = "https://api.jikan.moe/v4/anime/235/episodes"

r = requests.get(url)

body_json: dict = r.json()

for episodio in body_json["data"]:
  print(episodio["title_japanese"])
  
 

#print (json.dumps(data, sort_keys=True, indent=4))

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(body_json, file, sort_keys= True, indent=4)
    


"""url = "https://api.jikan.moe/v4/anime/235/episodes"

r = requests.get(url)

data = r.text

for d in data:
  print(d["title"])
print(data)


"""