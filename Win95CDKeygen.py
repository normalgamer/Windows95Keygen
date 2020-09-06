'''

Segment 1:
    3 digits long
    Can't be 333,444,555,666,777,888,999
    
Segment 2:
    Sum of digits must be divisible by 7
    Last digit can't be 0,8,9
    
'''

import os
import random as rd
keys = []


def generateKey():
    # Segment 1 logic
    segment1 = rd.randint(0, 998)
    bannedSegment1 = [333, 444, 555, 666, 777, 888, 999]
    bannedSegment2 = [0, 8, 9]
    segment2sum = 0

    while segment1 in bannedSegment1:
        segment1 = rd.randint(0, 998)

    x = len(str(segment1))
    if x == 1:
        s1 = "00"+str(segment1)
    elif x == 2:
        s1 = "0"+str(segment1)
    elif x == 3:
        s1 = str(segment1)

    segment2 = rd.randint(0, 9999999)

    x = len(str(segment2))
    #print("SEGMENT2: " + str(segment2))
    for i in str(segment2):
        # print(i)
        segment2sum = int(segment2sum)+int(i)
    #print("SEGMENT2SUM :"+str(segment2sum))

    while (segment2sum % 7 != 0) | (str(segment2)[-1:] in str(bannedSegment2)):
        #print("ERROR: "+str(segment2))
        segment2 = rd.randint(0, 9999999)
        segment2sum = 0
        for i in str(segment2):
            # print(i)
            segment2sum = int(segment2sum)+int(i)
        #print("SEGMENT2SUM: "+str(segment2sum))

    x = len(str(segment2))
    if x == 1:
        s2 = "000000"+str(segment2)
    elif x == 2:
        s2 = "00000"+str(segment2)
    elif x == 3:
        s2 = "0000"+str(segment2)
    elif x == 4:
        s2 = "000"+str(segment2)
    elif x == 5:
        s2 = "00"+str(segment2)
    elif x == 6:
        s2 = "0"+str(segment2)
    elif x == 7:
        s2 = str(segment2)

    return(s1+"-"+s2)


print(generateKey())
input()
