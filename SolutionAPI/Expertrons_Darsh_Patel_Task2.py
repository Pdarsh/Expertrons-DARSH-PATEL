import requests


url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q={%27Indigo%27}&api-key=lMJi10dwg6xb5ITaa5FR5jNNhV4SIBtP"
response = requests.get(url)
data = response.json()


for x in data["response"]["docs"]:
    f = open('url.txt','a')
    f.write(x["web_url"]+"\n")

f.close()