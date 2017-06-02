# -*- coding: utf-8 -*-
import subprocess
import json
import requests
import csv

from textblob import TextBlob





# tickers = open('secwiki_tickers.csv', 'r')
# reader = csv.reader(tickers)
# TICKERS = {}								#DEfine dictionary to match tickers w/ company name
# for row in reader:
#    k, v = row
#    TICKERS[k] = v
# tickers.close()
#
# company = TICKERS['GOOG']
# print(company)
# bingNewsSearch(company)
# nyTimes(company)
# print(exceptions)
#CAN CONFIRM THIS WORKS (calling python3 inside a 2.7 script)
#subprocess.call("python3 test.py", shell=True)

#out = subprocess.check_output(["python3", "test.py"])

#make all tweets put into twitterOutput.csv file
def getTweets():
    for ele in companies:
        for x in range(1, 8):
        	startDate = "2017-03-0" + str(x)
        	endDate = "2017-03-0" + str(x + 1)
        	print (startDate + " " + endDate)
        	subprocess.call("python Exporter.py --querysearch '"+ele+"' --since "+ startDate + " --until "+endDate+ " --maxtweets 20", shell=True)
        startDate = "2017-03-09"
        endDate = "2017-03-10"
        print (startDate + " " + endDate)
        subprocess.call("python Exporter.py --querysearch '"+ele+"' --since "+ startDate + " --until "+endDate+ " --maxtweets 20", shell=True)

        for x in range(10, 31):
        	startDate = "2017-03-" + str(x)
        	endDate = "2017-03-" + str(x + 1)
        	print (startDate + " " + endDate)
        	subprocess.call("python Exporter.py --querysearch '"+ele+"' --since "+ startDate + " --until "+endDate+ " --maxtweets 20", shell=True)

#feed twitter into CNN and output data into twitterSentiment.csv
def getTwitterSentiment():
    tweets = open("/Users/ethantien/Documents/hackathons/hackGSU/gsu/data/twitterOutput.csv", "r+")
    #to
    newFile = open("/Users/ethantien/Documents/hackathons/hackGSU/gsu/data/twitterSentiments.csv", "a+")

    for line in tweets.readlines():
    	temp = line.split(",")
        print(temp[2])
        if temp:
            numDay = int(temp[1][9:])
            # blob = TextBlob(temp[2].decode('utf-8'))
            # if not blob.sentiment.polarity == 0:
            #     newFile.write(('%s, %d, %f\n' % (temp[0], numDay, blob.sentiment.polarity)))
            r = requests.post("http://text-processing.com/api/sentiment/", "text= " + temp[2])
            data = json.loads(r.text)
            num1 = (data['probability']['pos'], 1)[0]
            print(num1)
            newFile.write(('%s, %d, %f\n' % (temp[0], numDay, num1)))

        	### NN LOGIC HERE
        	# nnTrainedData = #enter file name here
        	# nnInput = 'I love neural networks!'
        	#### command = "python3 twitter-sentiment-cnn.py --load " + nnTrainedData + " --custom_input " + nnInput

        	# out = subprocess.check_output(["python3", "twitter-sentiment-cnn.py", "--load", nnTrainedData, "--custom_input", nnINPUT])
        	#out is a string of the NN output



    newFile.close()
    tweets.close()

def calcTwitter():
    curCompany = "Apple"
    curDate = 1;
    curSum = 0.0;
    curCount = 0.0;
    sentiment = open("/Users/ethantien/Documents/hackathons/hackGSU/gsu/data/twitterSentiments.csv", "r+")
    final = open("/Users/ethantien/Documents/hackathons/hackGSU/gsu/data/twitterFinal.csv", "a+")
    for line in sentiment.readlines():
        temp = line.replace(" ", "").split(",")
        if curCompany == temp[0]:
            if curDate == int(temp[1]):
                curSum += float(temp[2])
                curCount += 1
            else :
                final.write('%s,%d,%f\n' % (curCompany, curDate, curSum / curCount))
                curDate = int(temp[1])
        else:
            final.write('%s,%d,%f\n' % (curCompany, curDate, curSum / curCount))
            curCompany = temp[0]
            curDate = int(temp[1])
            curCount = 0
            curSum = 0
    sentiment.close()
    final.close()

def calcBing():
    curCompany = "Apple"
    curSum = 0.0;
    curCount = 0.0;
    sentiment = open("/Users/ethantien/Documents/hackathons/hackGSU/gsu/data/bingSentiments.csv", "r+")
    final = open("/Users/ethantien/Documents/hackathons/hackGSU/gsu/data/bingFinal.csv", "a+")
    for line in sentiment.readlines():
        temp = line.replace(" ", "").split(",")
        if curCompany == temp[0]:
            curSum += float(temp[1])
            curCount += 1
        else :
            final.write('%s,%f\n' % (curCompany, curSum / curCount))
            curCompany = temp[0]
            curCount = 0
            curSum = 0
    sentiment.close()
    final.close()

def calcNYT():
    curCompany = "Apple"
    curSum = 0.0;
    curCount = 0.0;
    sentiment = open("/Users/ethantien/Documents/hackathons/hackGSU/gsu/data/NYTSentiments.csv", "r+")
    final = open("/Users/ethantien/Documents/hackathons/hackGSU/gsu/data/NYTFinal.csv", "a+")
    for line in sentiment.readlines():
        temp = line.replace(" ", "").split(",")
        if curCompany == temp[0]:
            curSum += float(temp[1])
            curCount += 1
        else :
            final.write('%s,%f\n' % (curCompany, curSum / curCount))
            curCompany = temp[0]
            curCount = 0
            curSum = 0
    sentiment.close()
    final.close()








#feed bings into CNN and output data into bingSentiment.csv
#newFile = open("/Users/ethantien/Documents/hackathons/hackGSU/sentiments.csv", "a+")
def getBingSentiment():
    #from
    bing = open("/Users/ethantien/Documents/hackathons/hackGSU/gsu/data/bing.csv", "r+")
    #to
    newFile = open("/Users/ethantien/Documents/hackathons/hackGSU/gsu/data/bingSentiments.csv", "a+")

    for line in bing.readlines():
        temp = line.split(",")
        print(temp[1])

        r = requests.post("http://text-processing.com/api/sentiment/", "text= " + temp[1])
        data = json.loads(r.text)

        num1 = (data['probability']['pos'], 1)[0] # i made to many api calls fuck this
        print(num1)
        newFile.write(('%s, %f\n' % (temp[0], num1)))
        # blob = TextBlob(temp[1].decode('utf-8'))
        # if not blob.sentiment.polarity == 0:
        #     newFile.write(('%s, %f\n' % (temp[0], blob.sentiment.polarity)))
    newFile.close()
    bing.close()


def getNYTSentiment():
    #from
    bing = open("/Users/ethantien/Documents/hackathons/hackGSU/gsu/data/nyTimes.csv", "r+")
    #to
    newFile = open("/Users/ethantien/Documents/hackathons/hackGSU/gsu/data/NYTSentiments.csv", "a+")

    for line in bing.readlines():
        temp = line.split(",")
        print(temp[1])
        if temp[1]:
            r = requests.post("http://text-processing.com/api/sentiment/", "text= " + temp[1])
            data = json.loads(r.text)
            num1 = (data['probability']['pos'], 1)[0] # i made to many api calls fuck this
            newFile.write(('%s, %f\n' % (temp[0], num1)))
            # blob = TextBlob(temp[1].decode('utf-8'))
            # newFile.write(('%s, %f\n' % (temp[0], blob.sentiment.polarity)))
    newFile.close()
    bing.close()
            #print(temp[1])
            # r = requests.post("http://text-processing.com/api/sentiment/", "text= " + temp[1])
            # data = json.loads(r.text)
            # num1 = (data['probability']['pos'], 1)[0] # i made to many api calls fuck this



            ### NN LOGIC HERE
            # nnTrainedData = #enter file name here
            # nnInput = 'I love neural networks!'
            #### command = "python3 twitter-sentiment-cnn.py --load " + nnTrainedData + " --custom_input " + nnInput

            # out = subprocess.check_output(["python3", "twitter-sentiment-cnn.py", "--load", nnTrainedData, "--custom_input", nnINPUT])
            #out is a string of the NN output
    # news = open("/Users/ethantien/Documents/hackathons/hackGSU/gsu/data/bing.txt", "r+")
    # sentiData = open('data/sentiData.csv', 'w')
    # bingValues = []
    # for line in news.readlines():
    # 	#temp = line.split(",")
    # 	#numDay = int(temp[1][9:])
    #     if not line == "\n":
    #         print (line)
    #         r = requests.post("http://text-processing.com/api/sentiment/", "text= " + line)
    #         data = json.loads(r.text)
    #         num1 = (data['probability']['pos'], 1)[0]
    #         sentiData.write(company + "," + str(num1) + "\n")
    # news.close()
# sum = 0
# for x in bingValues:
#     sum = sum + x;
#print ("avg: " + str(sum / len(bingValues)))
#subprocess.call(command, shell=True)


##lol main
#sentiData = open('data/sentiData.csv', 'w')



companyFile = open('data/companies.csv', 'r')
#f = open("/Users/ethantien/Documents/hackathons/hackGSU/companies.txt", "r+")

#f = open("/Users/ethantien/Documents/hackathons/hackGSU/output_got.csv", "r+")
#firstLine = f.readlines()[0]
#companies = firstLine.split(", ")

companies = [];
for line in companyFile.readlines():
    companies.append(line.split(",")[1].replace("\n", ""))



getTweets(companies);
#getTwitterSentiment();
#getBingSentiment()
#getNYTSentiment();
#calcTwitter()
#calcBing()
#calcNYT()
#getTweets()
