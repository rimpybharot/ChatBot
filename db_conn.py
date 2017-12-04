import time
import os
import MySQLdb
import uuid


def generateQuery(checkin, checkout, rooms):
    db = MySQLdb.connect("localhost","root","passw0rd","Hotels" )
    cursor = db.cursor()
    booking_id = "booking" + str(uuid.UUID.hex)
    cursor.execute(("Insert into reservation values (" + booking_id + "," +
                    "," + checkin + "," + checkout + "," + str(rooms) + ")" ))


# if __name__ == "__main__":
#     generateQuery()

