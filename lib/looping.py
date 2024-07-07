#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i <= 10 and i > 0:
        print(i)
        i-=1  
    else:
        print("Happy New Year!")
    
happy_new_year()

def square_integers(int_list):
    new_list = [i * i for i in int_list]
    return new_list
print(square_integers([2,3,8]))

def fizzbuzz():
    for i in range(1, 101):
        if i%3==0 and i%5 == 0:
            print ("FizzBuzz")
        elif i%3 == 0:
            print ("Fizz")
        elif i%5 == 0:
            print ("Buzz")
        else:
            print (i)
fizzbuzz()
