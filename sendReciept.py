import smtplib


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
    TEXT = "Hotel Name : " + hotel_name + "\n" + \
    "Hotel City :" + hotel_city + "\n" + \
    "Check In Date :" + checkin + "\n" + \
    "Check Out Date:" + checkout + "\n" + \
    "Number of Rooms :" + rooms + "\n" + \
    "RoomType :" + room_type + "\n" + \
    "Amenities :" + amenities


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
        print 'successfully sent the mail'
    except:
        print "failed to send mail"

# if __name__ == '__main__':
#     send_email('rbverses21@gmail.com', 'mypassw0rd24@', 'rimpybharot@gmail.com', 'ok' , 'okkkk')