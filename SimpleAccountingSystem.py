import check_type
import os
import Warehouse_class
import Product_class
import initial_data

options = ["balance", "sale", "purchase", "account", "list", "warehouse", "review", "end"]

main_warehouse = initial_data.init()
#main_warehouse = initial_data.empty()
selected_option = True

print(f"{main_warehouse}")

def view_menu(opt:list):
    #os.system('clear')
    for index in range(len(opt)):
        print(f"{index+1}. {opt[index]}")
        
def get_option(opt:list):
    option=0
    while (option<1 or option > len(opt)+1):
        view_menu(opt)
        print(f"Select option using number from 1 to {len(opt)}")
        option = check_type.get_int() 
    return option-1


def balance(warehouse:Warehouse_class.Warehouse):
    print("Enter the value you want to add or subtract from the account value")
    value = check_type.get_float()
    if warehouse.if_enough_money(value):
        warehouse.balance(value)
    else:
        print(f"Not enough money to subtracting the {value} from the account")
        print("Command interrupted")

def sale(warehouse:Warehouse_class.Warehouse):
    
    print("Select the product you want to sell")
    warehouse.displayList()
    product_name = input()
    if not(warehouse.checkInList(product_name)):
        print(f"Product {product_name} is not in warehouse")
        print("Command interrupted")
        return
    
    print("How many products do you want to sell?")
    quantity = check_type.get_positive_number()
    in_warehouse = warehouse.howManyProductInWarehouse(product_name)
    if in_warehouse<quantity:
        print(f"There are only {in_warehouse} products in warehouse, would you like to sell all of them?(Write Y)")
        if input()!="Y":
            print("Command interrupted")
            return
        quantity = in_warehouse
    warehouse.sale(product_name, quantity)#odjęcie z magazynu i dodanie do salda
    

def end(warehouse:Warehouse_class.Warehouse):
    print(f"{main_warehouse}")
    print("Good bye!")





while options[selected_option]!="end":
    selected_option = get_option(options)
    print(f"Selected option:\n{selected_option+1}. {options[selected_option]}")
    locals()[options[selected_option]](main_warehouse)




