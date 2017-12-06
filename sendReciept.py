import smtplib
import datetime
import time


def sendreceipt(recipient, response):
    FROM = 'SlackBot'
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = 'Booking Successful!'
    hotel_name = response['hotel_name']
    hotel_city = response['hotel_city']
    rooms=response['rooms']
    checkin = response['checkin_year']+"/"+response['checkin_month']+"/"+response['checkin_day']
    checkout = response['checkout_year']+"/"+response['checkout_month']+"/"+response['checkout_day']
    amenities=response['amenities']
    room_type=response['room_type']
    now = datetime.datetime.now()
    today = datetime.date(now.year, now.month, now.day )
    TEXT = "Hotel Name : " + (hotel_name).replace("%20"," ") + "\n" + \
    "Hotel City :" + hotel_city + "\n" + \
    "Check In Date :" + checkin + "\n" + \
    "Check Out Date:" + checkout + "\n" + \
    "Number of Rooms :" + rooms + "\n" + \
    "RoomType :" + room_type + "\n" + \
    "Amenities :" + amenities + "\n" +\
    "Booking Time :" + \
        str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))



    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login('273slackbot@gmail.com', 'slackbot123')
        server.sendmail(FROM, TO, message)
        server.close()
        return TEXT
    except:
        print "failed to send mail"

