data = {
    'name':"Abdulla Avloniy",
    "description":"This book is to create a histotical list",
    "input":"A",
    "year":'2021'

}

key = input('key:')
if key in data.keys():
    del data[key]
else:
    print("Mavjud emas")
        