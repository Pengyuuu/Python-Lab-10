'''
    Name: Eric Truong
    ID: 018149311
    Instructor: Minhthong Nguyen
    Date: November 13, 2018
'''
import random

def partOne():
    names = ['Ian', 'John', 'Dave', 'Steve', 'Steven']
    for n in names:
        print(n)

def getTotal(value_list):
    total = 0
    for n in value_list:
        total += n
    return total

def partTwo():
    numbers = []
    x = 0
    while x < 5:
        random.seed()
        rand = random.randint(1, 100)
        numbers.append(rand)
        x += 1
    print('The total is', getTotal(numbers))

def partThree():
    numbers = []
    x = 0
    while x < 5:
        random.seed()
        rand = random.randint(1, 50)
        numbers.append(rand)
        x += 1
    n = 16
    for i in numbers:
        if n < i:
            print(i)

        

partOne()
print('\n')
partTwo()
print('\n')
partThree()
