# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

def print_hi(name):
    #Use a breakpoint in the code line below to debug your script.

    guessesTaken = 0

    print('what is your name?')
    myName = input()

    number = random.randint(1, 20)
    print('well,' + myName + ' I am thinking about a number between 1 and 20.')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
