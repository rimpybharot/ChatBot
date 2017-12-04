import time
import os
import MySQLdb
import uuid


def generateQuery(response):
    db = MySQLdb.connect("localhost","root","passw0rd","Hotels" )
    for i in response:
    	hotel_name = response[hotel_name]
    	rooms=response[rooms]
    	checkin = response[checkin_year]+"/"+response[checkin_month]+"/"+response[checkin_day]
    	checkout = response[checkout_year]+"/"+response[checkout_month]+"/"+response[checkout_day]
    	amenities=response[amenities]
    	room_type=response[room_type]
    cursor = db.cursor()
    booking_id = "booking" + str(uuid.UUID.hex)
    cursor.execute(("Insert into reservation values ("  + booking_id + "," +hotel_name+ "," +
                    "," + checkin + "," + checkout + "," + str(rooms) + "," +amenities+ "," + room_type ")" ))


# if __name__ == "__main__":
#     generateQuery()

