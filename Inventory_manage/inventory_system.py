import pandas as pd

#import the data base with my own fields.
df =pd.read_csv("inventory_manage\\inventory_database.csv",names=["product","price","quantity"])

#make a list of the products init.
list_of_products = df["product"].tolist()

def add_product():

    product = input("\nNew product: ").capitalize() #to avoid duplicates use capitalize().
    price = input("\nPrice: ")
    quantity = input("\nQuantity: ")

    try: 
        #verify if the inputs are numbers.
        price = float(price)
        quantity = int(quantity)

        if product in list_of_products:
            input("The product already exist in the inventory. Try other option.")

        else:
            #make a entry to the database.
            new_product = {"product": [product], "price": [price], "quantity": [quantity]}

            #converting the entries into a dataframe to add it to the main df. 
            adding_newP = pd.DataFrame(new_product)

            #adding it to the main dataframe.
            adding_newP.to_csv("inventory_manage\\inventory_database.csv", mode='a', header=False, index=False)
            
    except:
        input("Value error.")