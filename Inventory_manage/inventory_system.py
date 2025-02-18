import pandas as pd

df =pd.read_csv("inventory_manage\\inventory_database.csv",names=["product","price","quantity"])

def add_product():
    product = input("\nNew product: ")
    price = input("\nPrice: ")
    quantity = input("\nQuantity: ")
    try: 
        price = float(price)
        quantity = int(quantity)
        new_product = {"product": [product], "price": [price], "quantity": [quantity]}
        adding_newP = pd.DataFrame(new_product)
        adding_newP.to_csv("inventory_manage\\inventory_database.csv", mode='a', header=False, index=False)
    except:
        input("Value error.")

        
add_product()
