class Item:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity 


    def __str__(self):
        #display item info
        pass

    def __eq__(self, other):
        #compare items by name and price
        return self.name == other and self.price == other

    def __lt__(self, other):
        #compare items by price (less than)
        return self.price < other

    def totalValue(self):
        #price times quantity
        return self.price * self.quantity

    def restock(self, amount):
        #increase quantity
         self.quantity += amount

    def purchase(self, amount):
        #decrease quantity
        if self.quantity > amount:
            self.quantity -= amount
        else:
            self.quantity = 0
        


class Inventory:

    def __init__(self):
        self.items = []

    def __len__(self):
        #number of items
        return(len(self.items))

    def __getitem__(self, index):
        #get item by index
        return self.items[index]

    def __setitem__(self, index, item):
        #replace an item
        self.items[index] = item

    def __add__(self, item):
        #add a new item 
        self.items.append(item)

    def __str__(self):
        #inventory contents
        return 

    def findItem(self, name):
        #find item by name
        for item in self.items:
            if item.name == name:
                return item
            else:
                return None

    def removeItem(self, name):
        #remove item by name
        newList = []
        for item in self.items:
            if item.name != name:
                newList.append(item)
        return newList

    def totalInventoryValue(self):
        #add all values in inventory
        total = 0

        for item in self.items:
            total += item.totalValue()
        return total