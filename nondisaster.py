import feedparser
import wget
feeds = [ 'http://timesofindia.indiatimes.com/rssfeeds/7098551.cms',
          'http://timesofindia.indiatimes.com/rssfeeds/1898055.cms',
          'http://timesofindia.indiatimes.com/rssfeeds/4719161.cms',
          'http://timesofindia.indiatimes.com/rssfeeds/3908999.cms',
          'http://timesofindia.indiatimes.com/rssfeeds/-2128672765.cms',
          'http://timesofindia.indiatimes.com/rssfeeds/5880659.cms',
          'http://timesofindia.indiatimes.com/rssfeeds/2886704.cms',
          'http://feeds.bbci.co.uk/news/health/rss.xml',
          'http://feeds.bbci.co.uk/news/education/rss.xml',
          'http://feeds.bbci.co.uk/news/science_and_environment/rss.xml',
          'http://feeds.bbci.co.uk/news/technology/rss.xml',
          'http://feeds.bbci.co.uk/news/world/asia/rss.xml',
          'http://www.deccanherald.com/rss/election-news.rss',
          'http://www.deccanherald.com/rss/national.rss',
          'http://www.deccanherald.com/rss/sports.rss',
          'http://www.deccanherald.com/rss/economy-business.rss',
          'http://www.thehindu.com/news/?service=rss',
          'http://www.thehindu.com/business/Industry/?service=rss',
          'http://www.thehindu.com/business/markets/?service=rss',
          'http://www.thehindu.com/sport/?service=rss',
          'http://www.thehindu.com/features/education/?service=rss',
          'http://www.thehindu.com/features/metroplus/fitness/?service=rss',
          'http://www.thehindu.com/features/metroplus/Motoring/?service=rss',
          'http://www.thehindu.com/entertainment/entertainment-history/?service=rss',
          'http://www.thehindu.com/sci-tech/?service=rss',
          'http://www.thehindu.com/entertainment/entertainment-art/?service=rss',
          'http://www.thehindu.com/elections/?service=rss',
          'http://www.thehindu.com/news/national/?service=rss',
          'http://www.telegraphindia.com/feeds/rss.jsp?id=7',
          'http://www.telegraphindia.com/feeds/rss.jsp?id=4',
          'http://feeds.reuters.com/reuters/INtopNews',
          'http://feeds.reuters.com/reuters/INbusinessNews',
          'http://feeds.reuters.com/reuters/INsouthAsiaNews',
          'http://feeds.reuters.com/reuters/INsportsNews',
          'http://feeds.reuters.com/reuters/INtechnologyNews',
          'http://feeds.reuters.com/reuters/INhealth',
          'http://feeds.reuters.com/reuters/INlifestyle'
]

i = 11
d = '/home/emanon/Desktop/Kludge/Dataset/not/temp/'

for feed in feeds:
    p = feedparser.parse(feed)
    for entry in p.entries:
        wget.download(entry.link,out=d + str(i))
        i += 1
        
