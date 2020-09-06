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


def generateKey():
    segment1Date = rd.randint(1, 366)
    segment1ValidYear = [95, 96, 97, 98, 99, 0, 1, 2, 3]
    segment1Year = segment1ValidYear[rd.randint(0, 8)]

    segment1 = str(segment1Date).zfill(3)+str(segment1Year).zfill(2)

    segment3 = rd.randint(0, 999999)
    bannedSegment3 = [0, 8, 9]
    segment3sum = 0

    for i in str(segment3):
        segment3sum = int(segment3sum)+int(i)

    while (segment3sum % 7 != 0) | (str(segment3)[-1:] in bannedSegment3):
        segment3 = rd.randint(0, 999999)
        segment3sum = 0
        for i in str(segment3):
            segment3sum = int(segment3sum)+int(i)

    segment4 = rd.randint(0, 99999)

    return(str(segment1)+"-OEM-"+str(segment3).zfill(7)+"-"+str(segment4).zfill(5))


print(generateKey())
input()
