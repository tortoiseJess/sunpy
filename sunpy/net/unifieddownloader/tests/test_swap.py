'''
Created on Mar 21, 2015

@author: jessey
'''
import datetime
# import pytest

import sunpy
from sunpy.time.timerange import TimeRange
from sunpy.net.vso.attrs import Time,Instrument,Source 
from sunpy.net.unifieddownloader.client import QueryResponse
import swap
from myParserUrl import scrape_all_fits_urls, timefurl
# import sunpy.net.unifieddownloader.sources.swap as swap
# from sunpy.net.unifieddownloader.myParserUrl import scrape_all_fits_urls, timefurl

'''
TODO:
test for the same day
test for more than one day
test invalid input
integrate and more testing with different dates --> pytest and git commit
transfer result to client interface, how?

'''

# @pytest.mark.parametrize("t1,url_start_of_page, url_end_of_page",
# [
# 
# (datetime.datetime(2013,04,12,03,11,55), 
# 'swap_lv1_20130412_000033.fits'
# 'swap_lv1_20130412_235914.fits'    ),
# # (second test case parameter value),
# 
# 
# 
# ])

def test_get_suitable_urls_for_datetime(day,t1,t2,urls0,urlsn1):
    LCClient = swap.SWAPClient()
    urls = LCClient._get_suitable_urls_for_datetime(day,t1,t2)
    assert urls[0] == urls0
    assert urls[-1] == urlsn1
    
def test_fail_get_suitable_urls_for_datetime(day,t1,t2):
    LCClient = swap.SWAPClient()
    try:    
        urls = LCClient._get_suitable_urls_for_datetime(day,t1,t2)
    except ValueError:
        pass

def test_get_url_for_time_range(timerange, urls0, urlsn1):
    LCClient = swap.SWAPClient() 
    urls = LCClient._get_url_for_timerange(timerange) 
    assert urls[0] == urls0
    assert urls[-1] == urlsn1
          

# def test_scrape_all_fits_urls(day_url, url_start_of_page, url_end_of_page):
#     urls = scrape_all_fits_urls(day_url)
#     assert urls[0] == url_start_of_page
#     assert urls[-1] == url_end_of_page 

def main():
#     #case 1
#     t1 = datetime.datetime(2013,04,12,23,01,00)
#     t2 = datetime.datetime(2013,04,12,23,59,13)
#     day = datetime.date(2013,04,12) 
#     urls0 = 'swap_lv1_20130412_230254.fits'
#     urlsn1 = 'swap_lv1_20130412_235454.fits' 
#     test_get_suitable_urls_for_datetime(day,t1,t2,urls0,urlsn1)
#     
#     #case2
#     t1 = datetime.datetime(2013,04,11,23,01,00)
#     t2 = datetime.datetime(2013,04,13,23,59,13)
#     day = datetime.date(2013,04,12) 
#     urls0 = 'swap_lv1_20130412_000033.fits'
#     urlsn1 = 'swap_lv1_20130412_235914.fits' 
#     test_get_suitable_urls_for_datetime(day,t1,t2,urls0,urlsn1)    
#     
#     #case3
#     day = datetime.date(2013,05,12)
#     test_fail_get_suitable_urls_for_datetime(day,t1,t2)
    
#===========================================================================================
#     timerange1 = TimeRange('2013/04/12 23:01:00', '2013/04/12 23:59:13') 
#     urls0 = 'swap_lv1_20130412_230254.fits'
#     urlsn1 = 'swap_lv1_20130412_235454.fits'   
#     test_get_url_for_time_range(timerange1, urls0, urlsn1) 
#     
#     timerange2 = TimeRange('2013/04/11 23:05:00', '2013/04/12 23:59:13')
#     urls0 = 'swap_lv1_20130411_230623.fits'
#     urlsn1 = 'swap_lv1_20130412_235454.fits' 
#     test_get_url_for_time_range(timerange2, urls0, urlsn1) 
#     
#     timerange3 = TimeRange('2013/04/11 23:05:00', '2013/04/13 23:56:15')
#     urls0 = 'swap_lv1_20130411_230623.fits'
#     urlsn1 = 'swap_lv1_20130413_235607.fits' 
#     test_get_url_for_time_range(timerange3, urls0, urlsn1) 
    
    #funny inputs
    timerange4 = TimeRange('2013/04/12', '2013/04/12')
    timerange5 = TimeRange('2013/04/11', '2013/04/13')
    #unspecified time will assume 00:00:00
    timerange6 = TimeRange('2013/04/11' , '2013/04/13 23:59:15')
    
    

    
if __name__ == '__main__':
    main()
