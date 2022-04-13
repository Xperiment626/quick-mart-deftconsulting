class Cart:
    def __init__(self, items):
        self.items = []
        
    def size(self):
        return len(self.items)
    
    def show(self, membership):
        counter = 0
        print("\n\t\tCurrent CART\n")
        print ("{:<8} {:<15} {:<15} {:<15}".format("Item #",'Name','Quantity','Price'))
        for item in self.items:
            print ("{:<8} {:<15} {:<15} {:<15}".format(counter + 1, item.name, item.quantity, item.getPrice(membership) * item.quantity))
            counter += 1
        
    def getItemNames(self):
        names = []
        for i in range(len(self.items)):
            names.append(self.items[i].name)
        return names
        
    def addItem(self, name, item):
        names = self.getItemNames()
        if name not in names:
            self.items.append(item)
        if name in names:
            index = names.index(name)
            self.items[index].quantity += item.quantity
            
    def removeItem(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            return print("Not in cart")
    
    def emptyCart(self):
        self.items.clear()
        
    def checkOut(self, cash, membership):
        total = 0
        subtotal = 0
        tax = 0
        itemsSold = 0
        change = 0
        itemNames = []
        itemQuantities = []
        
        for item in self.items:
            subtotal += item.getPrice(membership) * item.quantity
            itemsSold += item.quantity
            itemNames.append(item.name)
            itemQuantities.append(item.quantity)
            if item.taxStatus.lower() == "taxable":
                tax += (item.getPrice(membership) * item.quantity) * 0.065
            
        total = subtotal + tax
        change = cash - total
            
        print("\n\t\tCHEACKOUT\n")
        
        headers = "{:<10} {:<15} {:<15} {:<15}".format("ITEM",'QUANTITY','UNIT PRICE','TOTAL')
        itm = "{:<10} {:<15} {:<15} {:<15}"
        showItems = []
        data = "***********************************\nTOTAL NUMBER OF ITEMS SOLD: {}\nSUB-TOTAL: ${}\nTAX (6.5%): ${}\nTOTAL: ${}\nCASH: ${}\nCHANGE: ${}\n***********************************\nYOU SAVED: ${}!".format(itemsSold, round(subtotal), round(tax), round(total), round(cash), round(change, 2), round(change, 2))
        
        print (headers)
        
        for item in self.items:
            print (itm.format(item.name, item.quantity, item.getPrice(membership), item.getPrice(membership) * item.quantity))
            showItems.append(itm.format(item.name, item.quantity, item.getPrice(membership), item.getPrice(membership) * item.quantity))
            
        print(data)
        
        return [headers, showItems, data, itemNames, itemQuantities]
            
            
            