import requests

res = requests.get("http://google.com")

print(len(res.text))

# print(res.text)
with open("myGoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)


