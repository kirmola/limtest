for i in range(0,20500):
    with open(f'file1/text{i}.txt', "x")as file:
        file.write(f"{i}")
        print(f"written {i}")
