import requests

r = requests.get("http://kpfu.ru")
print r.status_code
print r.headers['Content-type']

f = open("page.html", "wb")

for line in r.text:
    f.write(line.encode("windows-1251"))
f.close()