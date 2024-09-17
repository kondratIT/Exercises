class Product:
    def __init__(self, name:str, quantity:int, price:float):
        self.name = str(name)
        self.quantity = int(quantity)
        self.price = float(price)

    #def displayProduct(self):
    #        print(f"Product name: {self.name}\tquantity: {self.quantity}\tprice: {self.price}")

    def __repr__(self):
        return "Product name: "+str(self.name)+"\tquantity: "+str(self.quantity)+"\tprice: "+str(self.price)#string 

#class ListOfProducts:
#     def __init__(self, list )


#produkt = Product("kiełbasa", 20, 2.50)
#produkt.displayProduct()
#print(f"{produkt}")