# Windows95Keygen

A Windows 95 key generator written in Python. Python 3 is required to run it

# How to use

Double-click the Python file, it will generate a valid key.

- CD: generates a valid key for Windows 95 installation CDs
- OEM: generates a valid key for Windows 95 OEM

# How does it work

## Key structure (CD)

**XXX-XXXXXXX**

The first part can be any number between 000 and 999, tough 333, 444, 555, 666, 777, 888 and 999 are invalid.

The second part is a bit trickier. The sum of the seven digits must be divisible by 7, and the last number can't be 0, 8 or 9.

## Key structure (OEM)

**XXXXX-OEM-XXXXXXX-XXXXX**

The first part is a date. The first three numbers are the day of the year, anywhere from 001 to 366. The next 2 digits are the year, they can't be lower than 95 or higher than 03

Second part is always OEM

The third part is similar to the CD key. The sum of the seven digits must be divisible by 7, the first number has to be 0 and the last number can't be 0, 8 or 9
The fourth part is 5 digits long. This part doesn't matter.
