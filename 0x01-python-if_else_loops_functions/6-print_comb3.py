#!/usr/bin/python3
number = 0
while number <= 89:
    if number % 10 == 0:
        number += 1 + number // 10
    print("{:02d}".format(number), end='\n' if number == 89 else ", ")
    number += 1



import random

number = 1
picked_number = random.randint(1, 50)

while number <= 50:
    if picked_number <= 25:
        print(f"{picked_number} is less than or equal to 25.")
        break
    else:
        print(f"{picked_number} is greater than 25.")
        break
    number += 1
