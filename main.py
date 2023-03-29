from Learn2 import Robot
from Learn1 import Computer

if __name__ == '__main__':
    user_input =str(input())
    if user_input=="robot":
        robotObj=Robot("roshan",2).say_hi()
        robotObj
    elif user_input=="computer":
        Computerobj=Computer().config()
        Computerobj


