class Item():
    def __init__(self, name, quantity, regularPrice, memberPrice, taxStatus):
        self.name = name
        self.regularPrice = regularPrice
        self.memberPrice = memberPrice
        self.quantity = quantity
        self.taxStatus = taxStatus
    
    def getName(self):
        return self.name
    
    def getQuantity(self):
        return self.quantity
    
    def getPrice(self, membership):
        if membership == "regular":
            return float(self.regularPrice); 
        return float(self.memberPrice)
    
    def getTaxStatus(self):
        return self.taxStatus