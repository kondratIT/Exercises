import datetime
import os

def get_int():
    incorrect=True
    while incorrect:
        try:
            number = int(input())
            incorrect =False
        except ValueError:
            print("Please Enter the number")
    return number

def year_for_age(year: int):
    return datetime.date.today().year-year

def get_year_of_birth():
    year=0
    while (year<1907 or year > datetime.date.today().year):
        print("Please give year of bith")
        year = get_int() 
    return year

def get_name():
    print("Please give name of the birthday girl/boy")
    return str(input()) 

def get_message():
    print("Please give message")
    return str(input()) 
def get_signature():
    print("Please give your name")
    return str(input()) 
    
def generate_card(name: str, age:int, message:str, sender:str):
    os.system('clear')
    print(f"{name}, let's celebrate your {age} years of awesomeness!\nWishing you a day filled with joy and laughter as you turn {age}!\n\n{message}\n\nWith love and best wishes,\n{sender}")
    

generate_card(get_name(), year_for_age(get_year_of_birth()),get_message(),get_signature())




