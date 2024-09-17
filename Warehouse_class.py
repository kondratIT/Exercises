import os
import Product_class

class Warehouse:
    def __init__(self, account_balance:float, list_of_products:list):
        self.account_balance = float(account_balance)
        self.list_of_products = list(list_of_products)

    def if_enough_money(self,value:float):
        if self.account_balance-value<0:
            return False
        else:
            return True

    def balance(self, value:float):#zamiana wartości konta
        temp=self.account_balance
        sign= "+"
        if value<0 :
            sign=""
        self.account_balance+=value#zrobić check czy saldo nie jest ujemne
        print(f"Account balance: {temp}{sign}{value}={self.account_balance}")

    def sale(self, product:Product_class.Product):#sprzedarz
        return
    
    def purchase(self, product:Product_class.Product):#zakup dodanie do magazynu produktu - utworzenie nowego produktu; można dodatkowo sprawdzić czy taki produkt już jest i go dodać do istniejącej pozycji
        #sprawdzić czy nas stać 
        if self.if_enough_money(product.quantity*product.price):
            self.list_of_products.insert(len(self.list_of_products),product)
            self.account_balance-=(product.quantity*product.price)
        else:
            print(f"The account balance is {self.account_balance}, which is not enough to buy the product: {product.name} in the amount of {product.quantity} for the price of {product.price} (total {(product.quantity*product.price)})")
    
    def displayBalance(self): #account
        print(f"Account balance = {self.account_balance}")

    def displayList(self):
        #os.system('clear')
        for product in (self.list_of_products):
            print(f"{product}")

    def warehouse(self):
        os.system('clear')
        for product in (self.list_of_products):
            print(f"{product}")



        

product1 = Product_class.Product("produkt1", 132, 1.99)
product2 = Product_class.Product("produkt2", 432, 123.33)
product3 = Product_class.Product("produkt3", 31, 120.73)

listOfProduct = [product1,product2,product3]
#print(f"{listOfProduct[1]}")
#lista = [
#    ["produkt1", 132, 1.99],
#    ["produkt2", 432, 123.33],
#    ["produkt3", 31, 12300.73]        
#         ]
poczatkowy_stan_konta=10000

#main_warehouse= Warehouse(poczatkowy_stan_konta, lista)
main_warehouse= Warehouse(poczatkowy_stan_konta, listOfProduct)








#main_warehouse.displayBalance()
main_warehouse.displayList()
main_warehouse.purchase(product2)
main_warehouse.displayList()

main_warehouse.purchase(product3)

main_warehouse.displayList()