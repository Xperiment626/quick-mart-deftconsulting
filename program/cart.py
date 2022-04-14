class Cart:
    def __init__(self, items):
        self.items = []
        
    def size(self):
        return len(self.items)
    
    def show(self, membership):
        counter = 0
        print("\n\t\tCurrent CART\n")
        print ("{:<8} {:<15} {:<15} {:<15} {:<15}".format("Item #",'Name','Quantity', 'Unit Price','Total'))
        for item in self.items:
            print ("{:<8} {:<15} {:<15} ${:<15} ${:<15}".format(counter + 1, item.name, item.quantity, round(item.getPrice(membership), 2), round(item.getPrice(membership) * item.quantity, 2)))
            counter += 1
        
    def getItemNames(self):
        names = []
        for i in range(len(self.items)):
            names.append(self.items[i].name)
        return names
        
    #TODO: PRE UPDATED THE INVENTORY WHEN AN ITEM IS ADDED
    def addItem(self, name, item):
        names = self.getItemNames()
        if name not in names:
            self.items.append(item)
        if name in names:
            index = names.index(name)
            self.items[index].quantity += item.quantity
            
    def removeItem(self, item):
        names = self.getItemNames()
        if item.name in names:
            item.quantity -= 1
            if item.quantity == 0:
                self.items.remove(item)
                return print("\nItem removed from cart")
            print("\nItem quantity decreased successfully")
        else:
            return print("Not in cart")
    
    def emptyCart(self):
        self.items.clear()
        
    def validateCash(self, membership):
        total = 0
        subtotal = 0
        tax = 0
        for item in self.items:
            subtotal += item.getPrice(membership) * item.quantity
            if item.taxStatus.lower() == "taxable":
                tax += (item.getPrice(membership) * item.quantity) * 0.065
            
        total = subtotal + tax
        return total
    
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
        data = "***********************************\nTOTAL NUMBER OF ITEMS SOLD: {}\nSUB-TOTAL: ${}\nTAX (6.5%): ${}\nTOTAL: ${}\nCASH: ${}\nCHANGE: ${}\n***********************************\nYOU SAVED: ${}!".format(itemsSold, round(subtotal, 2), round(tax, 2), round(total, 2), round(cash, 2), round(change, 2), round(change, 2))
        
        print (headers)
        
        for item in self.items:
            print (itm.format(item.name, item.quantity, item.getPrice(membership), item.getPrice(membership) * item.quantity))
            showItems.append(itm.format(item.name, item.quantity, item.getPrice(membership), item.getPrice(membership) * item.quantity))
            
        print(data)
        
        return [headers, showItems, data, itemNames, itemQuantities]
            
            
            