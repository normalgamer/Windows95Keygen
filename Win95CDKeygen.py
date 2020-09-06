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

    segment2 = rd.randint(0, 9999999)

    x = len(str(segment2))
    for i in str(segment2):
        segment2sum = int(segment2sum)+int(i)

    while (segment2sum % 7 != 0) | (str(segment2)[-1:] in str(bannedSegment2)):
        segment2 = rd.randint(0, 9999999)
        segment2sum = 0
        for i in str(segment2):
            segment2sum = int(segment2sum)+int(i)

    return(str(segment1).zfill(3)+"-"+str(segment2).zfill(7))


print(generateKey())
input()
