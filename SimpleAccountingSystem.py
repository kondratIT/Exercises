import check_int
import os
options = ["balance", "sale", "purchase", "account", "list", "warehouse", "review", "end"]
balance=0 
account_balance=0


def view_menu(opt:list):
    os.system('clear')
    for index in range(len(opt)):
        print(f"{index+1}. {opt[index]}")
        


def get_option(opt:list):
    option=0
    while (option<1 or option > len(opt)+1):
        view_menu(opt)
        print(f"Select option using number from 1 to {len(opt)+1}")
        option = check_int.get_int() 
    return option


get_option(options)