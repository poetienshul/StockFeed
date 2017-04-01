import requests 

password = "347a3af09d984f40aa7c18d811745b83"
url = "https://api.cognitive.microsoft.com/bing/v5.0/news/search?q=Sears Holding Company&count=10&offset=0&mkt=en-us&safeSearch=Off&freshness=month"
headers = {'Ocp-Apim-Subscription-Key' : password}
r = requests.get(url, headers=headers)
print (r.status_code)
data = r.json()
for entry in data['value']:
	print (entry['url'] + "\n")
	