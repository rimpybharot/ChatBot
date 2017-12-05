from __future__ import unicode_literals
import os
import time
import requests
import urllib2, json
import random
from bs4 import BeautifulSoup
from slackclient import SlackClient



def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    url="https://www.booking.com/searchresults.html?label=gen173nr-1DCAEoggJCAlhYSDNYBHIFdXNfY2GIAQGYATG4AQfIAQzYAQPoAQH4AQKSAgF5qAID&sid=9cba56f10b8617d55e137c61b27b1016&age=1&age=1&age=2&checkin_month=12&checkin_monthday=6&checkin_year=2017&checkout_month=12&checkout_monthday=8&checkout_year=2017&city=-1109108&class_interval=1&dest_id=20013069&dest_type=city&dtdisc=0&fe_new_tab=0&group_adults=1&group_children=0&inac=0&index_postcard=0&label_click=undef&no_rooms=1&postcard=0&raw_dest_type=city&room1=A&sb_price_type=total&sb_travel_purpose=business&search_selected=1&src=searchresults&ss=Fremont%2C%20California%2C%20USA&ss_all=0&ss_raw=fre&ssb=empty&sshis=0&ssne_untouched=San%20Jos%C3%A9&nflt=oos%3D1%3B&lsf=oos%7C1%7C-1&unchecked_filter=out_of_stock&hide_soldouts=1"
    
    
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    
    request = urllib2.Request(url,headers=hdr)
    response = urllib2.urlopen(request)
    the_page = response.read()
    the_page = unicode(the_page, 'utf-8')
    soup = BeautifulSoup(the_page, "html.parser")

    hotels=[]
    hotel_list=[]
    hotel_link_list=[]
    price_list=[]
    rating_list=[]
    room_list=[]
    amenity_list=['Free Parking','Free Wifi','Complimentary Breakfast','Airport Shuttle','Outdoor Pool','Restaurant on Site','Meeting/Banquet Facilities',
                    'Pet Friendly','Fitness Centre','Facilities for Disabled Guests','Laundry','Car Rental','Safe','Daily Housekeeping','Air Conditioning/Heating',
                    '24 hour front desk',]
    

   
    hotel_name = soup.find_all('span',{'class':'sr-hotel__name'})
    price = soup.find_all('strong',{'class':' price availprice no_rack_rate '})
    rating = soup.find_all('span',{'class':'review-score-badge'})
    room_type = soup.find_all('span',{'class':'room_link'})
    hotel_link = soup.find_all('a',{'class':'hotel_name_link url'})
    
    id=1
    
    for hname,hprice,hrating,hroom,hlink in zip(hotel_name,price,rating,room_type,hotel_link):

        hotel_dict={}
        hotel_dict['hotel_id']= id
        hotel_dict['name']= hname.text.strip()
        hotel_dict['price']= hprice.text.strip()
        hotel_dict['rating']= hrating.text.strip()
        hotel_dict['room']= hroom.text.replace("\n"," ")
        hotel_dict['link']= "https://www.booking.com"+hlink.get('href').strip()
        
        random.shuffle(amenity_list)
        am_rand=amenity_list[0]+", "+amenity_list[1]+", "+amenity_list[2]+", "+amenity_list[3]
        hotel_dict['amenities']= am_rand
        
        hotels.append(hotel_dict)
        id=id+1

    print("hotels")
    print(hotels)
     
    return hotels
