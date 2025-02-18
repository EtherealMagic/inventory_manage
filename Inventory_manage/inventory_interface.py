import pandas as pd
import inventory_system as system

while True:

    #create the interface to interact with the program.
    interface = input("Hi! welcome to your Inventory manager.\nTry any of the options bellow.\n1-add a product to the inventory.\n2-Exit\ninput: ")

    #try any of the options in the interface.
    try:
        if interface == "1":
            #use the function from the system module.
            system.add_product()

        elif interface == "2":
            #close the interface.
            break
        
    except:
        input("Invalid entry, try again.")