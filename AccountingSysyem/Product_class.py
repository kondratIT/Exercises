class Product:
    def __init__(self, name:str, quantity:int, price:float):
        self.name = str(name)
        self.quantity = int(quantity)
        self.price = float(price)

    def __repr__(self):
        return "Product name: "+str(self.name)+"\tquantity: "+str(self.quantity)+"\tprice: "+str(self.price)#string 