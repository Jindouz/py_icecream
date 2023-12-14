'''
Fizz Buzz and other functions that make use of the icecream library.  

To install the necessary libraries go into VE and run:
pip install -r requirements.txt

'''

import os, enum
import icecream as ic


class actions(enum.Enum):
    IC_FIZZBUZZ = 1
    IC_MULTIPLY = 2
    IC_SUM = 3
    EXIT = 4


def menu():
    ic.ic("==Menu==")
    for x in actions:
        print(f'({x.value}) {x.name}')
    return input("Enter your selection: ")


def main():
    os.system("cls")
    while(True):
        user_selection = menu()
        match actions(int(user_selection)):
            case actions.IC_FIZZBUZZ: ic_fizzbuzz()
            case actions.IC_MULTIPLY: ic_multiply()
            case actions.IC_SUM: ic_sum([1, 2, 3, 4, 5])
            case actions.EXIT: ic_exit()



def ic_fizzbuzz():
    os.system("cls")
    ic.ic("==ic_fizzbuzz==")
    for i in range (1,101):
        if i % 3 == 0 and i % 5 == 0:
            ic.ic(i, "FizzBuzz")
        elif i % 3 == 0:
            ic.ic(i, "Fizz")
        elif i % 5 == 0:
            ic.ic(i, "Buzz")
        else:
            ic.ic(i)
            
    return ic.ic("Fizz Buzz Completed")


def ic_multiply():
    os.system("cls")
    x = ic.ic(int(input("Enter a number to multiply: ")))
    y = ic.ic(int(input("By how much: ")))
    ic.ic("==ic_multiply==")
    result = x * y
    return ic.ic(result)


def ic_sum(numbers):
    os.system("cls")
    ic.ic("==ic_sum==")
    total = 0
    ic.ic(numbers)  
    for number in numbers:
        total += number
        ic.ic(number, total)
    return ic.ic(total)

def ic_exit():
    os.system("cls")
    ic.ic("Exiting")
    exit()



if __name__ == '__main__': main()


