import os
import Product_class

class Warehouse:
    def __init__(self, account_balance:float, list_of_products:list):
        self.account_balance = float(account_balance)
        self.list_of_products = list(list_of_products)

    def showBalance(self):
        print(f"Account balance = {self.account_balance}")

    def AddToBalance(self, value_to_add:float):
        temp=self.account_balance
        self.account_balance +=value_to_add
        print(f"Account balance = {self.account_balance}")
    
    def displayList(self):
        os.system('clear')
        for product in (self.list_of_products):
            print(f"{product}")


product1 = Product_class.Product("produkt1", 132, 1.99)
product2 = Product_class.Product("produkt2", 432, 123.33)
product3 = Product_class.Product("produkt3", 31, 12300.73)

listOfProduct = [product1,product2,product3]
#print(f"{listOfProduct[1]}")
#lista = [
#    ["produkt1", 132, 1.99],
#    ["produkt2", 432, 123.33],
#    ["produkt3", 31, 12300.73]        
#         ]
poczatkowy_stan_konta=0

#main_warehouse= Warehouse(poczatkowy_stan_konta, lista)
main_warehouse= Warehouse(poczatkowy_stan_konta, listOfProduct)







#main_warehouse.showBalance()
main_warehouse.displayList()
