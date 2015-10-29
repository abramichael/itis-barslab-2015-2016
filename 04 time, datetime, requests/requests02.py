import requests

r = requests.get("http://i.obozrevatel.ua/6/1172785/gallery/188178.jpg")
f = open("2.jpg", "wb")
f.write(r.content)
f.close()