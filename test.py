for i in range(30000):
    with open(f'files/text{i}.txt', "x")as file:
        file.write(f"{i}")
        print(f"written {i}")