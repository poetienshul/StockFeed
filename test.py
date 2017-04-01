from newspaper import Article
import newspaper
import requests
import csv

tickers = open('secwiki_tickers.csv', 'r')
reader = csv.reader(tickers)
TICKERS = {}								#DEfine dictionary to match tickers w/ company name
for row in reader:
   k, v = row
   TICKERS[k] = v
tickers.close()
exceptions = 0

def main():
	exceptions = 0
	company = TICKERS['GOOG']
	print(company)
	bingNewsSearch(company, exceptions)
	nyTimes(company)
	print(exceptions)
	
def bingNewsSearch(company, exceptions):
	password = "347a3af09d984f40aa7c18d811745b83"
	url = "https://api.cognitive.microsoft.com/bing/v5.0/news/search?q=Sears Holding Company&count=50&offset=0&mkt=en-us&safeSearch=Off&freshness=month"
	headers = {'Ocp-Apim-Subscription-Key' : password}
	
	fli = open('bing.txt', 'w')
	
	r = requests.get(url, headers=headers)
	data = r.json()
	for entry in data['value']:
		articleUrl = entry['url']
		print("accessing ")
		try:
			article = Article(articleUrl)
			article.download()
			article.parse()
			what = article.text
			sentences = what.split("\n")
				
			for sentence in sentences:
				fli.write(sentence + "\n")
		except:
			print("exception handled")
			exceptions += 1
			pass
		fli.write("\n\n\n")
	fli.close()

def nyTimes(company):
	fi = open('words.txt','w')
	#get the REST url
	url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=68b1851f45504416a077c13ac02dd9a2&q=" + company
	url += "&fl=web_url&begin_date=20170301"
	
	response = requests.get(url)
	data = response.json()

	list = data['response']['docs']

	for dict in list:
		try:
			articleUrl = dict['web_url']
			print ("accessing " + articleUrl)
			article = Article(articleUrl)

			article.download()
			
			words = []
			article.parse()
			what = article.text
			sentences = what.split("\n")
			for sentence in sentences:
				fi.write(sentence + "\n")
		except:
			pass
		fi.write("\n\n\n")
	
main()
	