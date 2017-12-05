import time
import os
import MySQLdb
import random



def get_reservations():
    db = MySQLdb.connect("localhost","root","passw0rd","hotel_reservation" )
    cursor = db.cursor()
    data = cursor.execute(("select * from hotel_reservation.reservation"))
    return data


def generateQuery(response):
    db = MySQLdb.connect("localhost","root","passw0rd","hotel_reservation" )
    hotel_name = response['hotel_name']
    hotel_city = response['hotel_city']
    rooms=response['rooms']
    checkin = response['checkin_year']+"/"+response['checkin_month']+"/"+response['checkin_day']
    checkout = response['checkout_year']+"/"+response['checkout_month']+"/"+response['checkout_day']
    amenities=response['amenities']
    room_type=response['room_type']
    cursor = db.cursor()
    booking_id = 'SB-'+''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(12))
    q = ("Insert into reservation values ("
    + "\'" + booking_id + "\'"
    + "," + "\'" + hotel_name + "\'"
    + "," + "\'" + hotel_city + "\'"
    + "," + "\'" + checkin + "\'"
    + "," + "\'" + checkout + "\'"
    + "," + "\'" + rooms + "\'"
    + "," + "\'" + amenities + "\'"
    + "," + "\'" + str(room_type) + "\'"
    +")")
    print q
    cursor.execute(q)



# if __name__ == "__main__":
#     generateQuery()
