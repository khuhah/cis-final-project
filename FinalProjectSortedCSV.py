#Created by Khushi Shah 2077293
#8/9/2024
import csv

'''Class to store the attributes of an item and sort/output an array containing those attributes'''

class Item():
    itemdata : list

    def __init__(self, itemdata):
        id = itemdata[0]
        name = itemdata[1]
        type = itemdata[2]
        price = itemdata[3]
        date = itemdata[4]
        condition = itemdata[5]
        #constants for mapping attribute labels to values
        self.consts = {
            "id" : id,
            "name" : name,
            "type" : type,
            "price" : price,
            "date" : date,
            "condition" : condition
        }
        self.data = [id, name, type, price, date, condition]

    #Takes in the an array/string of what to include in a output list and returns that
    def listBy(self, includes) -> list:
        if includes == "all":
            return self.data
        else:
            data = []
            for code in includes:
                data.append(self.consts.get(code))
            return data
        
    def __str__(self):
        return str(self.data)
        
'''Class to compile data from multiple files and create output data with items in sorted order'''
class SortedCSV(): 

    def __init__(self, nameDict, priceDict, dateDict):
        self.items = [] #array that contains all the items with all their attributes, default sort is FullInventory
        #constants for mapping the labels to indexes
        self.consts = {
            "id" : 0,
            "name" : 1,
            "type" : 2,
            "price" : 3,
            "date" : 4,
            "condition" : 5
        }
        for key in nameDict:
            nameData = nameDict.get(key) 
            priceData = priceDict.get(key)
            dateData = dateDict.get(key)
            self.items.append(Item([key, nameData[0], nameData[1], priceData[0], dateData[0], nameData[2]]))

    #Returns the sorted items array by what to include, is sorted by the code
    def sortBy(self, code, includes, reverse) -> list:
        itemsList = []
        includes.insert(0, code)
        for item in self.items:
            itemsList.append(item.listBy(includes))
        itemsList.sort(reverse=reverse)
        for item in itemsList:
            item.pop(0)
        return itemsList

    def __str__(self):
        return "\n".join(str(item) for item in self.items)

    
