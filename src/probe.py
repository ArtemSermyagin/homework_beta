import requests

url = "https://api.apilayer.com/exchangerates_data/latest?symbols=RUB,USD,AUD,ALL,BRL&base=EUR"

payload = {}
headers= {
  "apikey": "lEuHBJAu3jWUrlPIMNPt4VEYLmGEeNpC"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(result)
