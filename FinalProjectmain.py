#Created by Khushi Shah 2077293
#8/9/2024
import csv
from FinalProjectSortedCSV import SortedCSV
from datetime import datetime
from datetime import date

def main():

    #Reading each file and initializing the sorted CSV class
    nameData = {}
    with open('ManufacturerList.csv', mode ='r') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            nameData.update({lines.pop(0): lines})

    priceData = {}
    with open('PriceList.csv', mode ='r') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            priceData.update({lines.pop(0): lines})

    dateData = {}
    with open('ServiceDatesList.csv', mode ='r') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            dateData.update({lines.pop(0): lines})

    sorter = SortedCSV(nameData, priceData, dateData)

    #Writing the full inventory
    with open('FullInventory.csv', mode ='w', newline='') as file:
        csvFile = csv.writer(file)
        csvFile.writerows(sorter.sortBy("name", ["id", "name", "type", "price", "date", "condition"], False))

    #Writing item type inventory after getting all types and going through
    types = set()
    typesData = sorter.sortBy("id", ["id", "name", "price", "date", "condition", "type"], False)
    for val in typesData:
        types.add(val[5][:1].upper() + val[5][1:])
    size = len(typesData)
    for type in types:
        with open(f'{type}Inventory.csv', mode ='w', newline='') as file:
            csvFile = csv.writer(file)
            i = 0
            while i<size:
                val = typesData[i]
                if val[5].lower() == type.lower():
                    val.pop()
                    typesData.remove(val)
                    i-=1
                    size-=1
                    csvFile.writerow(val)
                i+=1

    #Writing the date inventory after determining date
    curdate = datetime.now().strftime('%m/%d/%Y') # date as mm/dd/yyyy
    curdate = date(int(curdate[curdate.rfind("/")+1:]), int(curdate[:curdate.find("/")]),int(curdate[curdate.find("/")+1:curdate.rfind("/")]))
    dateData = sorter.sortBy("date", ["id", "name", "type", "price", "date", "condition"], False)
    with open('PastServiceDateInventory.csv', mode ='w', newline='') as file:
        csvFile = csv.writer(file)
        for val in dateData:
            year = val[4][val[4].rfind("/")+1:]
            month = val[4][:val[4].find("/")]
            day = val[4][val[4].find("/")+1:val[4].rfind("/")]
            valdate = date(int(year), int(month), int(day))
            if valdate < curdate:
                csvFile.writerow(val)

    #writing the damaged inventory
    damagedData = sorter.sortBy("price", ["id", "name", "type", "price", "date", "condition"], True)
    with open('DamagedInventory.csv', mode ='w', newline='') as file:
        csvFile = csv.writer(file)
        for val in damagedData:
            val : list
            if val[5] == "damaged":
                val.pop()
                csvFile.writerow(val)

if __name__ == "__main__":
    main()
