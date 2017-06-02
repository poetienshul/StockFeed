from newspaper import Article
url = 'http://www.bbc.co.uk/zhongwen/simp/chinese_news/2012/12/121210_hongkong_politics.shtml'

a = Article(url, language='zh') # Chinese

a.download()
a.parse()

print(a.text[:150])

sprint(a.title)