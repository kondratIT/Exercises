import os
import Product_class
from typing import List 

class Warehouse:
    def __init__(self, account_balance:float, list_of_products: List[Product_class.Product]):
        self.account_balance = float(account_balance)
        self.list_of_products = list(list_of_products)
        self.list_of_command = []

    def __repr__(self):
        products = ""
        commands=""
        for product in self.list_of_products:
            products+=f"{product}\n"
        for comand in self.list_of_command:
            commands+=f"{comand}\n"
        return "Account balance: "+str(round(self.account_balance,2))+"\nList of products:\n"+products+"\nList of commands:\n"+commands

    def if_enough_money(self,value:float):
        if self.account_balance+value<0:
            return False
        else:
            return True

    def balance(self, value:float):#zamiana wartości konta
        temp=self.account_balance
        sign= "+"
        if value<0 :
            sign=""
        self.account_balance+=value#zrobić check czy saldo nie jest ujemne
        print(f"Account balance: {temp:.2f} {sign} {value} = {self.account_balance:.2f}")

    def sale(self, product_name:str, quantity:int):#sprzedarz
        for product in self.list_of_products:
            if product_name == product.name:
                product.quantity-=quantity
                self.account_balance+=quantity*product.price
                return
    
    def purchase(self, product:Product_class.Product):#zakup dodanie do magazynu produktu - utworzenie nowego produktu; można dodatkowo sprawdzić czy taki produkt już jest i go dodać do istniejącej pozycji
        if self.if_enough_money(product.quantity*product.price*-1):#nie mam pewności czy tem minus nie wywal jak tak to pomnożyć razy -1
            self.list_of_products.insert(len(self.list_of_products),product)
            self.account_balance-=(product.quantity*product.price)
        else:
            print(f"The account balance is {self.account_balance:.2f}, which is not enough to buy the product: {product.name} in the amount of {product.quantity} for the price of {product.price} (total {(product.quantity*product.price)})")
    
    def displayBalance(self): #account
        print(f"Account balance = {self.account_balance:.2f}")

    def displayList(self):
        #os.system('clear')
        for product in (self.list_of_products):
            print(f"{product}")
    
    def displayOne(self, product_name):
        for product in self.list_of_products:
            if product_name == product.name:
                return print(f"{product}")
        return print(f"Product {product_name} is not in warehouse")

    def warehouse(self):
        os.system('clear')
        for product in (self.list_of_products):
            print(f"{product}")

    def checkInList(self, product_name:str):
        
        for product in self.list_of_products:
            if product_name == product.name:
                return True
        return False
            
    def howManyProductInWarehouse(self, product_name:str):
        for product in self.list_of_products:
            if product_name == product.name:
                return product.quantity
        return 0
    
    def addToList(self, new_product:Product_class.Product):
        self.list_of_products.insert(len(self.list_of_products),new_product)
        print(f"New product added to warehouse:\n{new_product}")
    
    def addCommandToList(self, command:str):
        self.list_of_command.insert(len(self.list_of_command),command)

    def displayListOfCommandRange(self, from_position:int, to_position:int):
        print(f"List of command:\n")
        for inex in range(from_position,to_position):
            print(f"{self.list_of_command[inex]}")
        
    def displayListOfCommand(self):
        print(f"List of command:\n")
        for inex in range(len(self.list_of_command)):
            print(f"{self.list_of_command[inex]}")



#product1 = Product_class.Product("produkt1", 132, 1.99)
#product2 = Product_class.Product("produkt2", 432, 123.33)
#product3 = Product_class.Product("produkt3", 31, 120.73)
#listOfProduct = [product1,product2,product3]
#initial_account_balance=10000
#main_warehouse= Warehouse(initial_account_balance, listOfProduct)
#
#print(f"{main_warehouse}")
#main_warehouse.addToList(product2)
#print(f"{main_warehouse}")
#
#
#main_warehouse.displayList()
#prd= "produkt3"
#print(f"{main_warehouse.checkInList(prd)}")

