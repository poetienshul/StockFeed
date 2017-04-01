import csv


tickers = open('secwiki_tickers.csv', 'r')
reader = csv.reader(tickers)
fo = open('out.csv','w')

for line in reader:
	k,v = line
	v = v.replace("Inc.", "")
	v = v.replace(",","")
	v = v.replace("Corporation", "")
	v = v.replace("Corp.", "")
	v = v.replace("Group", "")
	v = v.replace("Co.", "")
	v = v.replace("Holdings","")
	v = v.replace("Group","")
	v = v.replace("Ltd.","")
	v = v.replace("Company","")
	v = v.replace("Holdings","")
	
	newline = k + "," + v + "\n"
	fo.write(newline)
	
tickers.close()
fo.close()
