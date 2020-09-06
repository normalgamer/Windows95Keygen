'''

XXXXX-OEM-XXXXXXX-XXXXX

Segment 1:
    5 digits long
    A date, Julian date + year
    3 digits date, 001-366
    2 digits year, can't be lower than 95 or higher than 03
        Valid years 95,96,97,98,99,00,01,02,03

Segment 2:
    OEM
    
Segment 3:
    7 digits long
    Sum of digits must be divisible by 7
    Last digit can't be 0,8,9
    First digit must be 0
    
Segment 4:
    5 digits long, doesn't matter

'''

import random as rd

segment1Date = rd.randint(1, 366)
segment1ValidYear = [95, 96, 97, 98, 99, 0, 1, 2, 3]
segment1Year = segment1ValidYear[rd.randint(0, 8)]


x = len(str(segment1Date))
if x == 1:
    s1 = "00"+str(segment1Date)
elif x == 2:
    s1 = "0"+str(segment1Date)
elif x == 3:
    s1 = str(segment1Date)

x = len(str(segment1Year))
if x == 1:
    s1 = s1+"0"+str(segment1Year)
elif x == 2:
    s1 = s1+str(segment1Year)

print("SEGMENT 1: "+s1)

###

segment3 = rd.randint(0, 999999)
bannedSegment3 = [0, 8, 9]
segment3sum = 0

x = len(str(segment3))
print("segment3: " + str(segment3))
for i in str(segment3):
    # print(i)
    segment3sum = int(segment3sum)+int(i)
print("SEGMENT2SUM :"+str(segment3sum))

while (segment3sum % 7 != 0) | (str(segment3)[-1:] in bannedSegment3):
    #print("ERROR: "+str(segment3))
    segment3 = rd.randint(0, 9999999)
    segment3sum = 0
    for i in str(segment3):
        # print(i)
        segment3sum = int(segment3sum)+int(i)
    #print("segment3: "+str(segment3))

x = len(str(segment3))
if x == 1:
    s3 = "000000"+str(segment3)
elif x == 2:
    s3 = "00000"+str(segment3)
elif x == 3:
    s3 = "0000"+str(segment3)
elif x == 4:
    s3 = "000"+str(segment3)
elif x == 5:
    s3 = "00"+str(segment3)
elif x == 6:
    s3 = "0"+str(segment3)

print("SEGMENT 3: "+str(segment3))

###

segment4 = rd.randint(0, 99999)

x = len(str(segment4))
if x == 1:
    s4 = "0000"+str(segment4)
elif x == 2:
    s4 = "000"+str(segment4)
elif x == 3:
    s4 = "00"+str(segment4)
elif x == 4:
    s4 = "0"+str(segment4)
elif x == 5:
    s4 = str(segment4)

print("SEGMENT 4 :" + str(segment4))

print("Key: "+s1+"-OEM-"+s3+"-"+s4)
input()
