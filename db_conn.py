import time
import os
import MySQLdb
import random



def get_reservations():
    db = MySQLdb.connect("localhost","root","passw0rd","hotel_reservation" )
    cursor = db.cursor()
    cursor.execute("select * from `reservation`")
    
    bookings = cursor.fetchall()
    db.close()
    return bookings

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
    # q = "INSERT INTO `reservation` values ('EY-87D2C2FAKYMO','The Row Hotel','San%20Jose','2018/9/9','2018/10/9','4','Outdoor Pool, Air Conditioning/Heating, Free Wifi, Pet Friendly',' Double Room     Max people: 2  ')"
    cursor.execute(q)
    db.commit()
    db.close()



if __name__ == "__main__":

    # generateQuery("")
    get_reservations()