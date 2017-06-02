from newspaper import Article
import newspaper
import requests
import csv
import json


tickers = open('secwiki_tickers.csv', 'r')

reader = csv.reader(tickers)
TICKERS = {}								#DEfine dictionary to match tickers w/ company name
for row in reader:
    k, v = row
    TICKERS[k] = v
tickers.close()

def main():
    companyFile = open('data/companies.csv', 'r')
    companies = [];
    for line in companyFile.readlines():
        companies.append(line.split(",")[1].replace("\n", ""))
    print(companies)
    for ele in companies:
        bingNewsSearch(ele)
        #nyTimes(ele)

def bingNewsSearch(company):
    password = "347a3af09d984f40aa7c18d811745b83"
    url = "https://api.cognitive.microsoft.com/bing/v5.0/news/search?q="+company+"Company&count=10&offset=0&mkt=en-us&safeSearch=Off&freshness=month"
    headers = {'Ocp-Apim-Subscription-Key' : password}

    fli = open('data/bing.csv', 'a')

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
                if sentence:
                    fli.write(company + "," +sentence.replace(",", "") + "\n")
        except:
            print("exception handled")
            pass
    fli.close()

def nyTimes(company):
    fi = open('data/nyTimes.csv','a')
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
                if sentence:
                    fi.write(company + "," +sentence + "\n")
        except:
            print("exception handled")
            pass

main()
