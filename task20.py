permissions = {'red':True,'write':False,'delete':True}


for item in permissions.items():
    if item[1]:
        print(item[0])
        