import check_type
import os
import Warehouse_class
import Product_class
import initial_data

options = ["balance", "sale", "purchase", "account", "list", "warehouse", "review", "end"]
selected_option = True

main_warehouse = initial_data.init()
#main_warehouse = initial_data.empty()


os.system('clear')
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
        warehouse.addCommandToList(str(f"balance : {value}"))
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
    quantity = check_type.get_positive_int()
    in_warehouse = warehouse.howManyProductInWarehouse(product_name)
    if in_warehouse<quantity:
        print(f"There are only {in_warehouse} products in warehouse, would you like to sell all of them?(Write Y)")
        if input()!="Y":
            print("Command interrupted")
            return
        quantity = in_warehouse
    warehouse.sale(product_name, quantity)#odjęcie z magazynu i dodanie do salda
    warehouse.addCommandToList(str(f"sale : {product_name}\t{quantity}"))
    

def purchase(warehouse:Warehouse_class.Warehouse):
    
    print("Enter the name of the product you want to buy for the warehouse")
    product_name = input()   
    print("How many products do you want to buy?")
    quantity = check_type.get_positive_int()
    print(f"What is the unit price of the product {product_name}")
    price = check_type.get_positive_float()

    if warehouse.if_enough_money(quantity*price):
        new_product = Product_class.Product(product_name,quantity,price)
        warehouse.addToList(new_product)
        warehouse.balance(quantity*price*-1)
        warehouse.addCommandToList(str(f"purchase : {new_product}"))
    else:
        print(f"Not enough money to buy the {new_product}")
        print("Command interrupted")

def account(warehouse:Warehouse_class.Warehouse):
    warehouse.displayBalance()
    warehouse.addCommandToList(str(f"account : {warehouse.account_balance}"))

def list(warehouse:Warehouse_class.Warehouse):
    warehouse.displayList()
    warehouse.addCommandToList(str(f"list"))

def warehouse(warehouse:Warehouse_class.Warehouse):
    print("Select the product you see")
    product_name = input()
    warehouse.displayOne(product_name)
    warehouse.addCommandToList(str(f"warehouse : {product_name}"))
    

def review(warehouse:Warehouse_class.Warehouse):
    print("From which index to display the list of commands?")
    index_from = check_type.get_range()
    print("To which index to display the list of commands?")
    index_to = check_type.get_range()
    if index_from =="" and index_to=="":
        warehouse.displayListOfCommand()
        warehouse.addCommandToList(str(f"review : all"))
        return
    elif index_from<index_to and index_to<len(warehouse.list_of_command):
        warehouse.displayListOfCommandRange(index_from,index_to)
        warehouse.addCommandToList(str(f"review : {index_from}-{index_to}"))
        return
    print("Incorrect range")
    print("Command interrupted")


def end(warehouse:Warehouse_class.Warehouse):
    print(f"{warehouse}")
    print("Good bye!")





while options[selected_option]!="end":
    selected_option = get_option(options)
    os.system('clear')
    print(f"Selected option:\n{selected_option+1}. {options[selected_option]}")
    locals()[options[selected_option]](main_warehouse)




