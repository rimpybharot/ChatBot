import os
import time
from slackclient import SlackClient
from getwitty import wit_response
from db_conn import *
import datetime
import re
from sendReciept import sendreceipt
from scraper import scrape_website
from getwitty import wit_response
import requests
import json

# import emoji

now = datetime.datetime.now()
today = datetime.date(now.year, now.month, now.day )

hotel_index = 0
decided = False
canceled = False
asked = False
emailidasked = False
cindate = datetime.datetime.date
coutdate = datetime.datetime.date
hotels = []
cancelation_asked = False


asking_questions_done = False
inputs = False
hotel_dict = {
    'hotel_city': '',
    'hotel_name': '',
    'room_type': '',
    'rooms': '',
    'checkin_year': '',
    'checkin_month': '',
    'checkin_day': '',
    'checkout_year': '',
    'checkout_month': '',
    'checkout_day': '',
    'amenities' : ''
    }
lastQuestion = ''
searchOn = False

BOT_ID = "U85HY9ZKM"

AT_BOT = "<@" + BOT_ID + ">"

slack_client = SlackClient("xoxb-277610339667-Jo6uVnf3qUA3ayicMGH4QO6g")


def send_repsonse(response):
    slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)


def handle_commands(command , channel):
    global emailidasked
    global inputs
    global decided
    global lastQuestion
    global cancelation_asked
    global hotel_index
    global decided
    global canceled
    global hotel_dict
    global asked
    global emailidasked
    global searchOn
    global hotels

    if "bye" in str(command):
        send_repsonse("Ok bye!")
        return

    if str(command) == "":
        send_repsonse("Empty Response!\n Retry")
        return
    command = str(command)

    #Get intent of the conversation

    # intent = wit_response(command)
    # print intent

    # if 'booking' in intent:
    #     show_bookings(command, channel)
    #     return
    # if 'bye' in intent:
    #     send_repsonse("Ok bye!")
    #     return

    if cancelation_asked or \
        str(command) == "cancel my booking" or \
        str(command) == "cancel booking" or \
        str(command) == "cancel bookings" or \
        str(command) == "cancel my bookings":
        # cancelation_asked = True
        cancel_booking(command, channel)
        return
    if str(command) == "show my bookings" \
        or str(command) == "show booking" \
        or str(command) == "show my bookings" \
        or str(command) == "show bookings":
        show_bookings(command, channel)
        return
    if emailidasked:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", command):
            book_and_reply(command)
        else:
            send_repsonse("Wrong emailid! Try again!")
            return
    elif inputs and not searchOn:
        save_data(command, channel)
    elif not inputs and searchOn:
        start_second_set_of_questions(command, channel)
    elif not inputs and not canceled:
        # category = wit_response(command)
        # print(category)
        if "hi" in command or "hello" in command or "hey there" in command or "hey" in command:
            response = "Hi There! How may I help you today? :raised_hand_with_fingers_splayed:"         
            send_repsonse(response)
            return
        # elif category == "Reservation":
        elif "reservation" in command or "book a hotel" in command or "search" in command:
            # asked=False
            # canceled=False
            # emailidasked = False
            # searchOn = False
            # hotel_dict={}
            # hotels =[]
            # canceled = False
            # decided = False
            # lastQuestion = ''
            # inputs = False
		

            response = "Sure I can help you with that!\nBut first I will need some inputs from you!"

            
            send_repsonse(response)
            inputs = True
            save_data(command, channel)
            return
        elif "bye" in command or "goodye" in command:
            send_repsonse("Goodbye! :wave:")
        else:
            response = "I don't understand"
            send_repsonse(response)
    else:
        response = "I don't understand"
        send_repsonse(response)


def cancel_booking(command, channel):
    global cancelation_asked
    if cancelation_asked:
        print command
        if (str(command)).upper().startswith("SB-"):
            print "some SB id"
            row_to_cancel = get_one_reservations(str(command).upper())
            if row_to_cancel == 1:
                cancel_reservation(str(command).upper())
                send_repsonse("Booking has been canceled!")
                cancelation_asked = False
                return
            else:
                send_repsonse("You have no booking with this ID")
                return
        else:
            send_repsonse("Wrong booking ID, give correct booking ID")
            return
    else:
        send_repsonse("Specify Booking ID which you want to cancel")
        cancelation_asked = True
        return
    



def start_second_set_of_questions(command, channel):
    global hotel_index
    global decided
    global canceled
    global hotel_dict
    global asked
    global emailidasked
    global searchOn
    global hotels

    if canceled:
        hotel_dict = {}
        return
    if decided:
        print("here")
        try:
            hotel_index = int(command)
        except ValueError:
            send_repsonse("Give a numeric input from 1-15")
            return
        print hotel_index
        # for hotel in hotels:
        #     print hotel['hotel_id']
        #     # print(type(hotel['hotel_id']))
        #     # print type(hotel_index)
        #     # for k,v in hotel.iteritems():
        if hotel_index in range(1, len(hotels)+1):
            for hotel in hotels:
                if hotel['hotel_id'] == (hotel_index):
                    print hotel
                    TEXT = ">>>*Hotel ID : * " + str(hotel['hotel_id']) + "\n" + \
                           "*Hotel Name : * " + hotel['name'] + "\n" + \
                           "*Price : * " + hotel['price'] + "\n" + \
                           "*Rating : * " + hotel['rating'] + "\n" + \
                           "*Room : * " + hotel['room'] + "\n" + \
                           "*Amenities : * " + hotel['amenities'] +"\n"+ \
	 	                   "*Link : * <"+hotel['link'] +"|Click Here> for details"+"\n"
                    send_repsonse("You selected:")
                    send_repsonse(TEXT)
                    hotel_dict['hotel_name'] = (hotel['name']).replace("'","")
                    hotel_dict['room_type'] = hotel['room']
                    hotel_dict['amenities'] = hotel['amenities']
                    make_reservation(hotel_dict)
                    send_repsonse("Please give an emailid")
                    emailidasked = True
                    return

        else:
            send_repsonse("Choose from 1-"+str(len(hotels)-1)+" only!")
            return

    elif not decided:
        if not asked:
            send_repsonse("Here is the list of hotels matching your search query!")
            hotels = scrape_website(hotel_dict)
            for hotel in hotels:
                TEXT = ">>>*Hotel ID : * " + str(hotel['hotel_id']) + "\n" + \
                "*Hotel Name : * " + hotel['name'] + "\n" + \
                "*Price : * " + hotel['price'] + "\n" + \
                "*Rating : * " + hotel['rating'] + "\n" + \
                "*Room : * " + hotel['room'] + "\n" + \
                "*Amenities : * " + hotel['amenities'] +"\n"+ \
		        "*Link : * <"+hotel['link'] +"|Click Here> for details"+"\n"
                send_repsonse(TEXT)
                time.sleep(1)

            send_repsonse("Would you like to book one? Reply with yes or no")
            asked = True
            return
        else:
            # searchOn = False
            if command in ["yes", "yeah", "Yeah", "Ok", "ok"]:
                send_repsonse("Please specify which one?")
                decided = True
                return
            elif command in ["no", "naah", "im good", "nope", "Nope"]:
                send_repsonse("Ok :neutral_face:")
                send_repsonse("You can restart you search or quit, goodbye!")
                hotel_dict = {}
                asked = False
                canceled = True
                return
            else:
                send_repsonse("please reply with a yes or no!")
                return

    else:
        send_repsonse("Wrong Input!")
        return


def show_bookings(command, channel):
    bookings = get_reservations()

    if len(bookings)==0:
        send_repsonse("You have no bookings!")
        return

    for booking in bookings:
        TEXT = "\n*Booking ID : *" + booking[0] + "\n" + \
        "*Hotel Name : *" + booking[1] + "\n" + \
        "*Hotel City : *" + booking[2] + "\n" + \
        "*Check In Date : *" + booking[3] + "\n" + \
        "*Check Out Date: *" + booking[4] + "\n" + \
        "*Number of Rooms : *" + booking[5] + "\n" + \
        "*RoomType : *" + booking[7] + "\n" + \
        "*Amenities : *" + booking[6] + "\n"

        send_repsonse("_________________________________________________________________")
        send_repsonse(TEXT)


def book_and_reply(emailid):

    global hotel_index
    global decided
    global canceled
    global hotel_dict
    global asked
    global emailidasked
    global searchOn
    global hotels

    emailid = emailid.split('|')[1]
    send_repsonse("Booking hotel , expect to receive an email shortly!")
    text = sendreceipt(emailid, hotel_dict)
    send_repsonse("Booking Details")
    send_repsonse(text)
    decided = False
    asked = False
    searchOn = False
    emailidasked = False
    hotel_dict = {}
    hotels = []


def save_data(command , channel):
    print("in save data")
    global lastQuestion
    global inputs
    global searchOn
    global today
    global cindate
    global coutdate
    if lastQuestion == '':
        send_repsonse("Which city")
        lastQuestion = 'city'
    elif lastQuestion == 'city':
        hotel_dict['hotel_city'] = str(command)
        send_repsonse('Enter a checkin date in YYYY-MM-DD format')
        lastQuestion = 'checkin'
    elif lastQuestion == 'checkin':
        try:
            y, m, d = map(int, str(command).split('-'))
            cindate = datetime.date(y, m, d)
        except ValueError as error:
            send_repsonse("Wrong format, try again")
            return
        try:
            if cindate < today:
                raise ValueError("Date is in the past, error a future date")
        except ValueError as error:
            error = str(error)
            send_repsonse(error)
            return
        hotel_dict['checkin_year'], hotel_dict['checkin_month'],\
                    hotel_dict['checkin_day'] = str(y), str(m), str(d)
        send_repsonse('Enter a checkout date in YYYY-MM-DD format')
        lastQuestion = 'checkout'
        return
    elif lastQuestion == 'checkout':
        try:
            y, m, d = map(int, str(command).split('-'))
            coutdate = datetime.date(y, m, d)
        except ValueError as error:
            send_repsonse("Wrong format, try again")
            return
        # try:
        #     if coutdate < today:
        #         raise Exception("Date is in the past, error a future date")
        # except Exception as error:
        #     error = str(error)
        #     send_repsonse(error)
        #     return
        try:
            if coutdate < cindate:
                raise ValueError("Checkout can not be earlier than checkin, try again")
        except ValueError as error:
            error = str(error)
            send_repsonse(error)
            return
        hotel_dict['checkout_year'], hotel_dict['checkout_month'],\
                    hotel_dict['checkout_day'] = str(y), str(m), str(d)
        send_repsonse("How many rooms?")
        lastQuestion = 'rooms'
        return
    elif lastQuestion == 'rooms':
        hotel_dict['rooms'] = command
        send_repsonse("Thanks!")
        inputs = False
        searchOn = True
        print hotel_dict
        start_second_set_of_questions(command, channel)

    else:
        send_repsonse("Something went wrong!")
        return

def parse_output(rtm_op):
    op_list = rtm_op
    if len(op_list) == 0:
        return None, None
    if op_list and len(op_list) > 0:
        for op in op_list:
            if op in op_list:
                if op and 'text' in op and AT_BOT in op['text']:
                    print(op['text'])
                    return op['text'].split(AT_BOT)[1].strip().lower(), op['channel']
                else:
                    return None, None


if __name__ == "__main__":

    READ_WEBSOCKET_DELAY = 1
    if slack_client.rtm_connect():
        # print "Houston we are online!"
        while True:
            # print slack_client.rtm_read()
            command, channel = parse_output(slack_client.rtm_read())
            if command is not None:
                if channel is not None:
                    handle_commands(command, channel)
                    time.sleep(READ_WEBSOCKET_DELAY)
                else:
                    continue
            else:
                continue

    else:
         print "Houston we have a problem"
