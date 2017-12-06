import os
import time
import requests
import urllib2, json
import random
from bs4 import BeautifulSoup
from slackclient import SlackClient
import string
import encodings
import titlecase




def processUserInput(hotel_dict):

    hotel_dict['hotel_city']=titlecase.titlecase(hotel_dict['hotel_city'])
    hotel_dict['hotel_city'] = "%20".join( hotel_dict['hotel_city'].split() )
    return hotel_dict


def scrape_website(hotel_dict):
    # print hotel_dict
    # print hotel_dict['hotel_city']

    # hotel_dict ={'hotel_city': 'los angeles',
    #           'rooms': '1',
    #           'checkin_year': '2017',
    #           'checkin_month': '12',
    #           'checkin_day': '9',
    #           'checkout_year': '2017',
    #           'checkout_month': '12',
    #           'checkout_day': '15'
    #           }


    # hotel_dict = {
    # 'checkout_year': '2018',
    # 'checkout_day': '10',
    # 'rooms': '1',
    # 'checkin_year': '2018',
    # 'hotel_city': 'los angeles',
    # 'hotel_name': '',
    # 'checkout_month': '9',
    # 'room_type': '',
    # 'amenities': '',
    # 'checkin_day': '9',
    # 'checkin_month': '9'}
    hotel_dict.pop('amenities')
    hotel_dict.pop('hotel_name')
    hotel_dict.pop('room_type')

    hotel_dict = processUserInput(hotel_dict)
    print(hotel_dict)

    city=(hotel_dict['hotel_city'])
    checkin_day = hotel_dict['checkin_day']         
    checkin_year= hotel_dict['checkin_year']
    checkin_month = hotel_dict['checkin_month']
    checkout_year = hotel_dict['checkout_year']
    checkout_month = hotel_dict['checkout_month']
    checkout_day = hotel_dict['checkout_day']
    rooms = '1' #hotel_dict['rooms']
    
    
    url="https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggJCAlhYSDNiBW5vcmVmcgV1c19jYYgBAZgBMbgBB8gBDNgBAegBAfgBApICAXmoAgM;sid=9428a9c8de49fd886b9075dd0822efd9&age=1&age=1&age=2&checkin_month="+checkin_month+"&checkin_monthday="+checkin_day+"&checkin_year="+checkin_year+"&checkout_month="+checkout_month+"&checkout_monthday="+checkout_day+"&checkout_year="+checkout_year+";class_interval=1&dest_type=city&dtdisc=0&from_sf=1&group_adults=2&group_children=0&inac=0&index_postcard=0&label_click=undef&no_rooms="+rooms+"&offset=0&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&src=index&src_elem=sb&ss="+city+"%2C%20California%2C%20USA&ss_all=0&ss_raw=san&ssb=empty&sshis=0&ssne_untouched=San%20Francisco&nflt=oos%3D1%3B&lsf=oos%7C1%7C-1&unchecked_filter=out_of_stock&hide_soldouts=1"
   
    # print url
    # url = "https://www.booking.com/searchresults.html?label=gen173nr-1DCAEoggJCAlhYSDNYBHIFdXNfY2GIAQGYATG4AQfIAQzYAQPoAQH4AQKSAgF5qAID&sid=9cba56f10b8617d55e137c61b27b1016&age=1&age=1&age=2&checkin_month=12&checkin_monthday=6&checkin_year=2017&checkout_month=12&checkout_monthday=8&checkout_year=2017&city=-1109108&class_interval=1&dest_id=20013069&dest_type=city&dtdisc=0&fe_new_tab=0&group_adults=1&group_children=0&inac=0&index_postcard=0&label_click=undef&no_rooms=1&postcard=0&raw_dest_type=city&room1=A&sb_price_type=total&sb_travel_purpose=business&search_selected=1&src=searchresults&ss=San%20Francisco%2C%20California%2C%20USA&ss_all=0&ss_raw=fre&ssb=empty&sshis=0&ssne_untouched=San%20Jos%C3%A9&nflt=oos%3D1%3B&lsf=oos%7C1%7C-1&unchecked_filter=out_of_stock&hide_soldouts=1"

    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    
    request = urllib2.Request(url, headers=hdr)
    response = urllib2.urlopen(request)
    the_page = response.read()
    the_page = unicode(the_page, 'utf-8')
    soup = BeautifulSoup(the_page, "html.parser")

    hotels = []
   
    amenity_list = ['Free Parking', 'Free Wifi', 'Complimentary Breakfast', 'Airport Shuttle', 'Outdoor Pool',
                    'Restaurant on Site', 'Meeting/Banquet Facilities',
                    'Pet Friendly', 'Fitness Centre', 'Facilities for Disabled Guests', 'Laundry', 'Car Rental', 'Safe',
                    'Daily Housekeeping', 'Air Conditioning/Heating',
                    '24 hour front desk', ]

    hotel_name = soup.find_all('span', {'class': 'sr-hotel__name'})
    price = soup.find_all('strong', {'class': ' price availprice no_rack_rate '})
    rating = soup.find_all('span', {'class': 'review-score-badge'})
    room_type = soup.find_all('span', {'class': 'room_link'})
    hotel_link = soup.find_all('a', {'class': 'hotel_name_link url'})

    id = 1
    for hname, hprice, hrating, hroom, hlink in zip(hotel_name, price, rating, room_type, hotel_link):
        hotel_dict = {}
        hotel_dict['hotel_id'] = id
        hotel_dict = {}
        hotel_dict['hotel_id'] = id
        hotel_dict['name'] = hname.text.strip()
        hotel_dict['price'] = hprice.text.strip()
        hotel_dict['rating'] = hrating.text.strip()
        hotel_dict['room'] = (hroom.text.replace("\n", " ")).encode('ascii',errors='ignore')
        #hotel_dict['link'] = "https://www.booking.com" + hlink.get('href').strip()
        hotel_dict['link'] = "https://www.booking.com" + "".join(hlink.get('href').split())
        random.shuffle(amenity_list)
        # # random.shuffle(amenity_list)
        am_rand = amenity_list[0] + ", " + amenity_list[1] + ", " + amenity_list[2] + ", " + amenity_list[3]
        hotel_dict['amenities'] = am_rand

        hotels.append(hotel_dict)
        id = id + 1

    # print("hotels")
    return hotels

if __name__ == "__main__":
    scrape_website({})


