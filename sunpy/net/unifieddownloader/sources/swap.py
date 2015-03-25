# import datetime
# import urlparse

# from sunpy.net.unifieddownloader.client import GenericClient
# from sunpy.net.unifieddownloader.myParserUrl import *

'''
Created on Mar 11, 2015, then on 21st

@author: jessey
'''
import datetime
import urlparse

from sunpy.net.unifieddownloader.client import GenericClient
from myParserUrl import scrape_all_fits_urls, timefurl

__all__ = ['SWAPClient']

class SWAPClient(GenericClient):


    def _get_url_for_timerange(self, timerange, **kwargs):
        """
        Returns list of URLS corresponding to TimeRange.
        Parameters
    ----------
        timerange: TimeRange for which data is to be downloaded.
        Returns
    -------
    List of urls
        """
        if not timerange:
            return []
    
        days = timerange.get_dates() #.get_datetimes ?
        t1 = timerange.start()
        t2 = timerange.end()
        urls = []
        for day in days:
            urls = urls + self._get_suitable_urls_for_datetime(day,t1,t2) # day --> datetime
        return urls
        ####
        # SET T1, T2 ATTRIBUTES FOR THIS CLASS?
        ####

    def _get_suitable_urls_for_datetime(self,day,t1,t2):
        """
        parameter:  day
                    t1 = start datetime
                    t2 = end datetime 
        eg?
        ------------
        determines which urls to gather. 
        If : start and end date.  call functions 
        otherwise,                _scrape_all_urls_for_day
        ------------
        return: all urls after starting time for one day 
        """

        urls = self._get_all_fits_urls_for_date(day) # day or date?
        startUrlIndex =0
        endUrlIndex =len(urls)

        if day == t1.date():
            startUrlIndex  =  self._get_start_url_index(urls,t1)
        if day == t2.date():
            endUrlIndex  =  self._get_end_url_index(urls,t2)
            endUrlIndex +=1
        if (day < t1.date() or day > t2.date()):
            raise ValueError
        
        return urls[startUrlIndex : endUrlIndex]            

    def _get_all_fits_urls_for_date(self,day):
        day_url = self._get_url_for_date(day)
        urls = scrape_all_fits_urls(day_url)
        return urls 



    def _get_url_for_date(self, day, **kwargs): #date --> datetime
        """
        Return URL which contains all fits file corresponding to date and instrument 
    Parameters
    ----------
    date : datetime 

        Returns
    -------
    string representing URL
    """
        format = "%Y/%m/%d/"
        date_string = datetime.datetime.strftime(day, format) # = 2013/04/12/
        day_url = 'http://proba2.oma.be/swap/data/bsd/' + date_string
        return day_url
            # need to test if equal='http://proba2.oma.be/swap/data/bsd/'+ date_string

    def _get_timePattern_from_url(self):
        timePattern ='_\d{6}.fits$'
        return timePattern  


    def _get_start_url_index(self,urls,t1):

        timePattern = self._get_timePattern_from_url()
        for url in urls:
            if t1.time() <= timefurl(url,timePattern): # = urlFirstTime
                break 
#         print url
        return urls.index(url)
        #returns true if queryStartTime later than urlFirstTime

    def _get_end_url_index(self,urls,t2):

        timePattern = self._get_timePattern_from_url()
        for url in urls:
            if t2.time() < timefurl(url,timePattern):
                break
#         print url
        return urls.index(url)-1
        
        



    def _makeimap(self):
        '''Helper Function:used to hold information about source. '''
        self.map_['source'] = 'Proba2'
        self.map_['instrument'] = 'swap'
        self.map_['phyobs'] = 'irradiance'  #????
        self.map_['provider'] = 'esa'

    @classmethod
    def _can_handle_query(cls, *query):
        """Boolean Function:Answers whether client can service the query.
        """
        chkattr =  ['Time', 'Instrument', 'Level']
        chklist =  [x.__class__.__name__ in chkattr for x in query]
        for x in query:
            if x.__class__.__name__ == 'Instrument' and x.value == 'lyra':
                return all(chklist)
        return False












