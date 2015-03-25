
# import datetime
# import pytest


# from sunpy.net.unifieddownloader.myParserUrl import scrape_all_fits_urls, timefurl

'''
Created on Mar 11, 2015

@author: jessey
'''

import datetime
import pytest


from myParserUrl import scrape_all_fits_urls, timefurl

# test for the same day
#test for more than one day
#test invalid input


# @pytest.mark.parametrize("day_url,url_start_of_page, url_end_of_page",
# [
# 
# ('http://proba2.oma.be/swap/data/bsd/2013/04/12/', 
# 'swap_lv1_20130412_000033.fits'
# 'swap_lv1_20130412_235914.fits'    ),
# # (second test case parameter value),
# 
# 
# 
# ])
def test_scrape_all_fits_urls(day_url, url_start_of_page, url_end_of_page):
    urls = scrape_all_fits_urls(day_url)
    assert urls[0] == url_start_of_page
    assert urls[-1] == url_end_of_page 

def test_timefurl():
    timePattern =r'_\d{6}.fits$'
    urlTime = timefurl('swap_lv1_20130412_232644.fits',timePattern)
    assert isinstance(urlTime, datetime.time )
    assert urlTime == datetime.time(23,26,44)
    
def main():
    day_url = 'http://proba2.oma.be/swap/data/bsd/2013/04/12/'
    url_start_of_page= 'swap_lv1_20130412_000033.fits'
    url_end_of_page= 'swap_lv1_20130412_235914.fits'
    test_scrape_all_fits_urls(day_url, url_start_of_page, url_end_of_page)
    
    test_timefurl()

if __name__ =='__main__':
    main()