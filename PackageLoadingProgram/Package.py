class Package:
    def __init__(self, index:int, weight_limit:float ):
        self.index = int(index)
        self.weight_limit = float(weight_limit)
        self.quantity = 0
        self.weight = 0.0
        

#    def __repr__(self):
#        return "Product name: "+str(self.name)+"\tquantity: "+str(self.quantity)+"\tprice: "+str(self.price)#string 

    def AddItem(self,weight:int):
        final_weight=self.weight+weight
        if (final_weight>self.weight_limit):
            return False
        self.weight=final_weight
        quantity+=1
        return True

    def EmptySpace(self):
        return self.weight_limit - self.weight

    
    
