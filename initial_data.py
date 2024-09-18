import Product_class
import Warehouse_class


def init():

    product1 = Product_class.Product("p1", 132, 1.99)
    product2 = Product_class.Product("p2", 432, 123.33)
    product3 = Product_class.Product("p3", 31, 120.73)

    listOfProduct = [product1,product2,product3]
    initial_account_balance=10000

    main_warehouse= Warehouse_class.Warehouse(initial_account_balance, listOfProduct)

    return  main_warehouse

def empty():
    return Warehouse_class.Warehouse(0,[])
     