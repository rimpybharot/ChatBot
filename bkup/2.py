import os
import time
from slackclient import SlackClient
from getwitty import wit_response
import db_conn
import datetime
import re
from sendReciept import sendreceipt
from scraper import scrape_website

# import emoji


hotel_index = 0
decided = False
canceled = False
asked = False
emailidasked = False


asking_questions_done = False
inputs = False
hotel_dict = {'hotel_city': '',
              'rooms': 0,
              'checkin_year': '',
              'checkin_month': '',
              'checkin_day': '',
              'checkout_year': '',
              'checkout_month': '',
              'checkout_day': ''
              }
lastQuestion = ''
searchOn = False

BOT_ID = "U85HY9ZKM"

AT_BOT = "<@" + BOT_ID + ">"

slack_client = SlackClient("xoxb-277610339667-Jo6uVnf3qUA3ayicMGH4QO6g")


def send_repsonse(response):
    slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)


def handle_commands(command , channel):
    # global emailidasked
    # global inputs
    # global decided
    # global lastQuestion

    # if "bye" in str(command):
    #     send_repsonse("Ok bye!")
    #     return
    command = str(command)
    if str(command) == "":
        send_repsonse("Empty Response!\n Retry")
        return
    
    # if emailidasked:
    #     if not re.match(r"... regex here ...", command):
    #         book_and_reply(command)
    #     else:
    #         send_repsonse("Wrong emailid! Try again!")
    #         return
    # elif inputs and not searchOn:
    #     save_data(command, channel)
    # elif not inputs and searchOn:
    #     start_second_set_of_questions(command, channel)
    # elif not inputs and not canceled:
    #     # category = wit_response(command)
    #     # print(category)
    #     if "hi" in command or "hello" in command or "hey there" in command or "hey" in command:
    #         response = "Hi There! How may I help you today? :raised_hand_with_fingers_splayed:"
    #         send_repsonse(response)
    #         return
    #     # elif category == "Reservation":
    #     elif "reservation" in command or "book a hotel" in command:
    #         response = "Sure I can help you with that!\nBut first I will need some inputs from you!"
    #         send_repsonse(response)
    #         inputs = True
    #         save_data(command, channel)
    #         return
    #     elif "bye" in command or "goodye" in command:
    #         send_repsonse("Goodbye! :wave:")
    #     else:
    #         response = "I don't understand"
    #         send_repsonse(response)
    # else:
    #     response = "I don't understand"
    #     send_repsonse(response)

    elif "bye" in command or "goodye" in command:
        send_repsonse("Goodbye! :wave:")
    else:
        category = wit_response(command)
        print(category)
        if category == "greeting":
            response = "Hi There! How may I help you today?"
            send_repsonse(response)
            return
        elif category == "Reservation":
            response = "Sure I can help you with that!\nBut first I will need some inputs from you!"
            send_repsonse(response)
            inputs = True
            save_data(command, channel)
            return
        else:
            response = "I don't understand"
            send_repsonse(response)


def start_second_set_of_questions(command, channel):
    global hotel_index
    global decided
    global canceled
    global hotel_dict
    global asked
    global emailidasked
    global searchOn

    if canceled:
        hotel_dict = {}
        return
    elif decided:
        print("here")
        hotel_index = str(command)
        send_repsonse("Please give an emailid")
        emailidasked = True
        return
    elif not decided:
        if not asked:
            send_repsonse("Here is the list of hotels matching your search query!")
            hotels = scrape_website()
            for hotel in hotels:
                for k,v in hotel.iteritems():
                    send_repsonse(str(v))
            send_repsonse("Would you like to book one? Reply with yes or no")
            asked = True
            return
        else:
            searchOn = False
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
        send_repsonse("Wrong Input!")
        return


def book_and_reply(emailid):

    emailid = emailid.split('|')[1]
    print(emailid)
    send_repsonse("Booking hotel , expect to receive an email shortly!")
    sendreceipt(emailid, hotel_dict)


def save_data(command , channel):
    print("in save data")
    global lastQuestion
    global inputs
    global searchOn
    if lastQuestion == '':
        send_repsonse("Which city")
        lastQuestion = 'city'
    elif lastQuestion == 'city':
        hotel_dict['hotel_city'] = str(command)
        send_repsonse('Enter a checkin date in YYYY-MM-DD format')
        lastQuestion = 'checkin'
    elif lastQuestion == 'checkin':
        try:
            hotel_dict['checkin_year'], hotel_dict['checkin_month'], hotel_dict['checkin_day'] = str(command).split('-')
            # hotel_dict['checkin'] = datetime.date(year, month, day)
        except ValueError:
            send_repsonse("Wrong format, try again")
            lastQuestion = 'checkin'
            return
        send_repsonse('Enter a checkout date in YYYY-MM-DD format')
        lastQuestion = 'checkout'
    elif lastQuestion == 'checkout':
        try:
            hotel_dict['checkout_year'], hotel_dict['checkout_month'], hotel_dict['checkout_day'] = str(command).split('-')
            # hotel_dict['checkout'] = datetime.date(year, month, day)
        except ValueError:
            send_repsonse("Wrong format, try again")
            lastQuestion = 'checkout'
            return
        send_repsonse("How many rooms?")
        lastQuestion = 'rooms'
    elif lastQuestion == 'rooms':
        hotel_dict['rooms'] = int(command)
        send_repsonse("Thanks!")
        inputs = False
        searchOn = True
        print(hotel_dict)
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

