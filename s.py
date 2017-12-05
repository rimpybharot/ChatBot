# a = [1, 2,3]
# b = sorted(a)
# print(b[-1])
# i=1
# while(i<=b[-1] and i<len(b)):
#     if b[i]==b[i-1] or b[i]==1+b[i-1]:
#         i=i+1
#     else:
#         break
# print i

# from autocorrect import spell

# print spell('tocyo')
import datetime

import uuid
import random
# command = "2017-11-1"
# y,m,d = map(int, str(command).split('-'))
# cindate = datetime.date(y, m, d)
# # ci = datetime.date(y+m+d,"%Y%m%d" )

# now = datetime.datetime.now()



# today = datetime.date(now.year, now.month, now.day )

# # now = datetime.datetime.now

# # today = datetime.datetime.now
# # print today.day
# try:
#     if cindate < today:
#         raise ValueError
# except ValueError:
#     print(ValueError)
booking_id = 'SB-'+''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(12))
# booking_id = "booking" + str(uuid.uuid1())
print booking_id
