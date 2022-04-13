class Customer:
    def __init__(self, membership):
       self.membership = membership
       
    def setMembership(self, membership):
        self.membership = membership
        
    def getMembership(self):
        return self.membership