
'''
this module parses the time from the given url from a client webpage.
shoudl be included in the generic Client?

-----------------------
parameter: url of instrument's fits file 
           pattern to parse for 

-----------------------
return: datetime.time object of the time the url represents  

'''
import datetime
import time
from bs4 import BeautifulSoup
import urllib2 
import re

def scrape_all_fits_urls(day_url):
    page = urllib2.urlopen(day_url)
    soup = BeautifulSoup(page.read())
    
    lst = soup.body.find_all(href = re.compile(".fits$"))
    soup.decompose()
    page.close()
    urls = [x['href'] for x in lst]
    
    
    return urls





def timefurl(url,timePattern):
    # firstDate = url
#     firstDate = soup[0]['href']
#     print (url) #string
    timePattern = re.compile(timePattern) 
#     print timePattern.search(url).group()[1:7]
    urlTime = timePattern.search(url).group()[1:7]
#     urlFirstTime = parse_time(urlFirstTime) #check if this is the right one, need to normalise the time to compare
    hour0 =urlTime[0:2]
    hour0.lstrip()
    hour = int(hour0)
    min0 = (urlTime[2:4])
    min0.strip()
    min_ = int(min0)
    sec0 = (urlTime[4:6])
    sec0.lstrip()
    sec= int(sec0)
    
    urlTime = datetime.time(hour,min_,sec)
#     print type(urlFirstTime)
    return urlTime