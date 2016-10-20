from cleanhtml import clean_html

feeds = [
    'http://www.sfgate.com/rss/feed/Tech-News-449.php',
    'http://feeds.feedburner.com/TechCrunch/startups',
    'http://news.cnet.com/8300-1001_3-92.xml',
    'http://www.zdnet.com/news/rss.xml',
    'http://www.computerweekly.com/rss/Latest-IT-news.xml',
    'http://feeds.reuters.com/reuters/technologyNews',
    'http://www.tweaktown.com/news-feed/'
]

import feedparser
import nltk
corpus = []
titles=[]
ct = -1

for feed in feeds:
    d = feedparser.parse(feed)
    for e in d.entries:
        cleaned = clean_html(e['description'])
        #cleaned
        words = nltk.word_tokenize(cleaned)
        words.extend(nltk.wordpunct_tokenize(e['title']))
        lowerwords=[x.lower() for x in words if len(x) > 1]
        ct += 1
        # print ct, "TITLE",e['title']
        corpus.append(lowerwords)
        titles.append(e['title'])
