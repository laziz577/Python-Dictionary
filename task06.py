data = {
    'a':5,
    'b':9
}

key = input()

value = data.get(key)
if value == None:
    print("Topilmadi")
else:
    print(value)
        