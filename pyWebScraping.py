from bs4 import BeautifulSoup

# Open the html file
with open('simpleHtml.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# Finds all the instances of fiv element with class as article
articles = soup.findAll('div', class_='article')

for article in articles:
    print()
    headline = article.h2.a.text
    print("Headline : " + headline)
    summary = article.p.text
    print("\t Summary  : " + summary)
