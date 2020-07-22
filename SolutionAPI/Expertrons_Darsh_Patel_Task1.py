import requests

print("1:Query\n2:Source\n")
ch = int(input())
if(ch == 1):
    q = input()
    d = input("Enter Date in yyyy-mm-dd format")
    url = "http://newsapi.org/v2/everything?q="+q+"&from="+d+"&sortBy=publishedAt&apiKey=7cf3eed47172446da6ba5bc5ef43d2c0"
elif(ch == 2):
    q = input()
    url = "http://newsapi.org/v2/top-headlines?sources="+q+"&apiKey=7cf3eed47172446da6ba5bc5ef43d2c0"

response = requests.get(url)
data = response.json()
print(url)
i = 1
for x in data["articles"]:
    if(i<=10):
        print(i,x["url"])
        i += 1