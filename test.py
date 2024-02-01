for i in range(0,7000):
    with open(f'file1/text{i}.txt', "x")as file:
        file.write(f"{i}")
        print(f"written {i}")

for i in range(7000, 14000):
    with open(f'file2/text{i}.txt', "x")as file:
        file.write(f"{i}")
        print(f"written {i}")

for i in range(14000, 21000):
    with open(f'file3/text{i}.txt', "x")as file:
        file.write(f"{i}")
        print(f"written {i}")