#!/usr/bin/env python3


# For Loop: a statement that will execute it's block of code
#           a limited amount of times
#           
#           While Loop  = unlimited
#           For Loop    = limited


# for i in range(10): # 'range' default value is 0
#     print(i+1)


# for i in range(50, 101, 5): # start, stop, step
#     print(i)


# for i in "Dliyaulhaq Mufliansyah":
#     print(i)


import time

for sec in range(10, 0, -1):
    print(sec)
    time.sleep(1)
print("Happy New Year!")
