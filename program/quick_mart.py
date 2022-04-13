from datetime import date
import os, os.path
import customer as ctm
import cart as crt
import item as it

def readFileInventory(path):
    inventoryTxt = ""

    with open(path, "r", encoding = "utf-8") as f:
        inventoryTxt = f.read()
        
        inventoryItems = inventoryTxt.splitlines()
        auxItem = [item.split(":") for item in inventoryItems]
        auxProps = [item[1].split(",") for item in auxItem]
        itemNames = [item.split(":")[0] for item in inventoryItems]
        itemQuantity = [prop[0].lstrip().rstrip() for prop in auxProps]
        itemRegularPrice = [prop[1].lstrip().rstrip().replace('$','') for prop in auxProps]
        itemMemberPrice = [prop[2].lstrip().rstrip().replace('$','') for prop in auxProps]
        itemTaxStatus = [prop[3].lstrip().rstrip().lower() for prop in auxProps]

    inventory = {}

    for i in range(len(itemNames)):
        inventory[i] = {
                "name": itemNames[i],
                "quantity": itemQuantity[i],
                "regularPrice": itemRegularPrice[i],
                "memberPrice": itemMemberPrice[i],
                "taxStatus": itemTaxStatus[i]
            }
        
    return inventory

inventory = readFileInventory("inventory.txt")

def showInventory(inv = inventory):
    print("\n\t\t\tCURRENT INVENTORY\n")
    print ("{:<8} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Pos",'Name','Quantity','Regular Price','Member Price', 'Tax Status'))

    for k, v in inv.items():
        print ("{:<8} {:<15} {:<15} {:<15} {:<15} {:<15}".format(k ,v["name"], v["quantity"], v["regularPrice"], v["memberPrice"], v["taxStatus"]))

def updateInventory(confirmation, data, inv = inventory):
    
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
    
    for k in inv:
        aux = 0
        for i in range(len(names)):
            if inv[k]["name"] == names[i]:
                aux = int(inv[k]["quantity"])
                aux -= quantities[i]
                inv[k]["quantity"] = str(aux)
        
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
    

    path = f"./transactions/transaction_{str(uniqueCode).zfill(6)}_{numericDate}.txt"
    writeTransaction(path, data)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def writeTransaction(path, data):
    with open(path, 'w') as f:
        f.write(f"\t\tCHECKOUT\n{data[-2]}\nTRANSACTION: {str(data[-1]).zfill(6)}\n")
        f.write(data[0] + "\n")
        for items in data[1]:
            f.write(items + "\n")
        f.write(data[2])
        f.close()

def showFirstOptions():
    print("\n1) New transaction\n2) Exit\n")

def showOptions():
    print("\n1) Show Inventory\n2) Add item to cart\n3) Remove item from cart\n4) Empty Cart\n5) View Cart\n6) Checkout\n7) Cancel\n")

print("\tWELCOME TO JERRY'S QUICK MART by Iñaki Manosalvas!")

while(True):
    showFirstOptions()
    opf = int(input("\nOption: "))
    if(opf == 2):
        break
    cart = crt.Cart([])
    answer = int(input("\nCustomer membership\n1) Rewards member\n2) Regular member\nOption: "))
    membership = "rewards" if answer == 1 else "regular"
    customer = ctm.Customer(membership)
    while(True):
        showOptions()
        op = int(input("\nOption: "))
        if op == 1:
            showInventory()
        if op == 2:
            showInventory()
            op1 = int(input("\nChoose the 'Pos' of the item you want: "))
            if(op1 < 0 or op1 > len(inventory)):
                print("\nInvalid Value")
            else:
                q = int(input("\nQuantity: "))
                if(q <= 0 or q > int(inventory[op1]["quantity"])):
                    print("\nInvalid value")
                else:
                    item = it.Item(inventory[op1]["name"], q, float(inventory[op1]["regularPrice"]), float(inventory[op1]["memberPrice"]), inventory[op1]["taxStatus"])
                    cart.addItem(item.name, item)
        if op == 3:
            cart.show(customer.getMembership())
            opr1 = int(input("\nChoose item #: "))
            if opr1 < 1 or opr1 > cart.size():
                print("\nInvalid value")
            else:
                cart.removeItem(cart.items[opr1 - 1])
                print("\nItem removed succesfully")
            
        if op == 4:
            cart.emptyCart()
            print("Items deleted succesfully")
            
        if op == 5:
            cart.show(customer.getMembership())
            
        if op == 6:
            if len(cart.items) > 0:
                cash = float(input("Cash $: "))
                cheackoutData = cart.checkOut(cash, customer.getMembership())
                print("\n\t\tConfirm Checkout\n1) No\n2) Yes")
                confirmation = bool(int(input("Option: ")) - 1)
                updateInventory(confirmation, cheackoutData)
                break
            else:
                print("No items for CheckOut")
        if op == 7:
            break
            
            
            
        