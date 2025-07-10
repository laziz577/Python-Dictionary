config = {}


for i in range(3):
    task = input(f"{i + 1} - taskni kiriting:")
    value = input(f"{task} qiymatini kiriting:")
    config[task] = value

    print("qiymatlangan config:",config)
    