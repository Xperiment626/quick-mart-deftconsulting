# imports to work with dates and files, to adhere to the requirements requested in the document 
from datetime import date
import os, os.path
import copy

# importing the classes from the files in the same directory
import customer as ctm
import cart as crt
import item as it

def readFileInventory(path):
    # Stores data from inventory.txt file
    inventoryTxt = ""

    # Open a file al ready created (inventory.txt).
    with open(path, "r", encoding = "utf-8") as f:
        
        inventoryTxt = f.read()
        
        # Stores every line of the file with the items data
        inventoryItems = inventoryTxt.splitlines()
        # Aux var to split by ":" symbol, separate the items names from the item's data
        auxItem = [item.split(":") for item in inventoryItems]
        # Here it takes the rest of the data, split by "," symbol 
        auxProps = [item[1].split(",") for item in auxItem]
        # Stores the items names
        itemNames = [item.split(":")[0] for item in inventoryItems]
        # Stores the items quantity
        itemQuantity = [prop[0].lstrip().rstrip() for prop in auxProps]
        # Stores the items regular price
        itemRegularPrice = [prop[1].lstrip().rstrip().replace('$','') for prop in auxProps]
        # Stores the items member price
        itemMemberPrice = [prop[2].lstrip().rstrip().replace('$','') for prop in auxProps]
        # Stores the items tax status
        itemTaxStatus = [prop[3].lstrip().rstrip().lower() for prop in auxProps]

    # empty inventory object/dict 
    inventory = {}

    # build the object/dict with the data from the inventory.txt file
    for i in range(len(itemNames)):
        inventory[i] = {
                "name": itemNames[i],
                "quantity": itemQuantity[i],
                "regularPrice": itemRegularPrice[i],
                "memberPrice": itemMemberPrice[i],
                "taxStatus": itemTaxStatus[i]
            }
        
    return inventory

# stores the inventory data
inventory = readFileInventory("inventory.txt")
inventoryCopy = copy.deepcopy(inventory)
# show the current items and data from inventory var defined before.
# The method has predefined the inventory var  in the params
def showInventory(inv):
    # Predefine how the data will be shown in console
    print("\n\t\t\tCURRENT INVENTORY\n")
    print ("{:<8} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Pos",'Name','Quantity','Regular Price','Member Price', 'Tax Status'))

    # iterate the inventory in order to populate the table of items
    for k, v in inv.items():
        print ("{:<8} {:<15} {:<15} {:<15} {:<15} {:<15}".format(k ,v["name"], v["quantity"], v["regularPrice"], v["memberPrice"], v["taxStatus"]))

# Using the item in order to pre-updated the inventory then people will not buy anything out of stock
def preUpdateInventory(item, operation, inv):
    if operation == "add":
        for k in inv:
            aux = 0
            if inv[k]["name"] == item.name:
                aux = int(inv[k]["quantity"])
                aux -= item.quantity
                inv[k]["quantity"] = str(aux)
    else:
        for k in inv:
            aux = 0
            if inv[k]["name"] == item.name:
                aux = int(inv[k]["quantity"])
                aux += 1
                inv[k]["quantity"] = str(aux)

# this method is execute when the checkout is confirmed
def updateInventory(confirmation, data, inv = inventory):
    # date formatting
    today = date.today()
    textualDate = today.strftime("%B %d, %Y")
    numericDate = today.strftime("%m%d%Y")
    uniqueCode = len([name for name in os.listdir("./transactions") if os.path.isfile(os.path.join("./transactions", name))]) + 1
    
    data.append(textualDate)
    data.append(uniqueCode)
    
    if not confirmation:
        return print("TRANSACTION CANCELED")
    
    names = data[-4]
    quantities = data[-3]
    
    # Updating inventory obj/dict
    
    for k in inv:
        aux = 0
        for i in range(len(names)):
            if inv[k]["name"] == names[i]:
                aux = int(inv[k]["quantity"])
                aux -= quantities[i]
                inv[k]["quantity"] = str(aux)
    
    # Rewriting the inventory.txt file with the new data update
    try:
        os.remove('./inventory.txt')
        with open('./inventory.txt', 'w') as f:
            for k in inv:
                f.write("{}: {}, ${}, ${}, {}\n".format(inv[k]["name"], inv[k]["quantity"], inv[k]["regularPrice"], inv[k]["memberPrice"], inv[k]["taxStatus"]))
            f.close()
    except IOError:
        with open('./inventory.txt', 'w') as f:
            for k in inv:
                f.write("{}: {}, ${}, ${}, {}\n".format(inv[k]["name"], inv[k]["quantity"], inv[k]["regularPrice"], inv[k]["memberPrice"], inv[k]["taxStatus"]))
            f.close()
    
    # Setting the new path for the receipt and setting the name of the new transaction file 
    path = f"./transactions/transaction_{str(uniqueCode).zfill(6)}_{numericDate}.txt"
    # Creating and writing the new transaction file
    writeTransaction(path, data)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    inventory = readFileInventory("inventory.txt")

# this method is execute when the checkout is confirmed
def writeTransaction(path, data):
    # Writing up everything in the specified path with the transaction data
    with open(path, 'w') as f:
        f.write(f"\t\tCHECKOUT\n{data[-2]}\nTRANSACTION: {str(data[-1]).zfill(6)}\n")
        f.write(data[0] + "\n")
        for items in data[1]:
            f.write(items + "\n")
        f.write(data[2])
        f.close()

# Aux methods to print options in the console app
def showFirstOptions():
    print("\n1) New transaction\n2) Exit\n")

def showOptions():
    print("\n1) Show Inventory\n2) Add item to cart\n3) Remove item from cart\n4) Empty Cart\n5) View Cart\n6) Checkout\n7) Cancel Transaction\n")

print("\tWELCOME TO JERRY'S QUICK MART by Iñaki Manosalvas!")

# The app will run until the client decides to exit the app
while(True):
    # New transaction or exit system
    showFirstOptions()
    try:
        firstOption = int(input("\nOption: "))
        # exit program if is 2
        if(firstOption == 2):
            break
        # starting new transaction
        if(firstOption == 1):
            # Initializing Cart object
            cart = crt.Cart([])
            membershipType = int(input("\nCustomer membership\n1) Rewards member\n2) Regular member\nOption: "))
            # Validating that the input is contained in the options
            if membershipType < 1 or membershipType > 2:
                print("Invalid value")
            else:
                # setting the membership type
                membership = "rewards" if membershipType == 1 else "regular"
                # Initializing Customer object
                customer = ctm.Customer(membership)
                while(True):
                    # Validating that the input is correct
                    try:
                        showOptions()
                        option = int(input("\nOption: "))
                        
                        # Show current inventory
                        if option == 1:
                            showInventory(inventoryCopy)
                        
                        # Add items to cart
                        if option == 2:
                            showInventory(inventoryCopy)
                            posOption = int(input("\nChoose the 'Pos' of the item you want: "))
                            # Validating that the input is contained in the options
                            if(posOption < 0 or posOption >= len(inventoryCopy)):
                                print("\nInvalid Value")
                            else:
                                itemQuantity = int(input("\nQuantity: "))
                                # Validating that the input is contained in the options
                                if(itemQuantity <= 0 or itemQuantity > int(inventoryCopy[posOption]["quantity"])):
                                    print("\nInvalid value")
                                else:
                                    item = it.Item(inventoryCopy[posOption]["name"], itemQuantity, float(inventoryCopy[posOption]["regularPrice"]), float(inventoryCopy[posOption]["memberPrice"]), inventoryCopy[posOption]["taxStatus"])
                                    cart.addItem(item.name, item)
                                    preUpdateInventory(item, operation = "add", inv = inventoryCopy)
                        
                        # Remove individual items from cart
                        if option == 3:
                            cart.show(customer.getMembership())
                            itemNumOption = int(input("\nChoose item #: "))
                            # Validating that the input is contained in the options
                            if itemNumOption < 1 or itemNumOption > cart.size():
                                print("\nInvalid value")
                            else:
                                preUpdateInventory(cart.items[itemNumOption - 1], operation = "remove", inv = inventoryCopy)
                                cart.removeItem(cart.items[itemNumOption - 1])
                        
                        # Empty cart  
                        if option == 4:
                            cart.emptyCart()
                            inventoryCopy = None
                            inventoryCopy = copy.deepcopy(inventory)
                            print("Items deleted succesfully")
                        
                        # Show current cart
                        if option == 5:
                            cart.show(customer.getMembership())
                        
                        # Start checkout  
                        if option == 6:
                            if len(cart.items) > 0:
                                validCash = cart.validateCash(customer.getMembership())
                                print(f"TOTAL BILL: {validCash}")
                                try:
                                    cash = float(input("Cash $: "))
                                    # Validating that the cash is greater than the invoice/bill
                                    if cash < validCash:
                                        print("Invalid value it must be greater than the bill")
                                    else:
                                        cheackoutData = cart.checkOut(cash, customer.getMembership())
                                        print("\n\t\tConfirm Checkout\n1) No\n2) Yes")
                                        confirmation = bool(int(input("Option: ")) - 1)
                                        # Validating that the input is contained in the options
                                        if confirmation == 1:
                                            updateInventory(confirmation, cheackoutData)
                                            break
                                        if confirmation == 0:
                                            inventoryCopy = copy.deepcopy(inventory)
                                except ValueError:
                                    print("Invalid input")
                            else:
                                print("No items for CheckOut")
                        
                        # Cancel transaction
                        if option == 7:
                            # If the transacction is canceled recreated the aux inventory for next transaction
                            inventoryCopy = copy.deepcopy(inventory)
                            break
                    except ValueError:
                        print("Invalid input")
    except ValueError:
        print("Invalid input")