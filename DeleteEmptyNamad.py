import  ANALYZER
analyzer = ANALYZER.ANALYZER()
data=analyzer.getdata()
tableslist=[]
# dicts={"a":{"a":"1"},"b":{"b":"1"},"c":{}}
for namad in data:
    if(not bool(data[namad])):
        tableslist.append(namad)
print("table list that is going to be deleted is :")
print(tableslist)
analyzer.ReturnDB().deletetable(tableslist)