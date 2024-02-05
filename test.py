import json
for i in range(30000):
    with open(f"data/{i}.txt", "w") as f:
        
        f.write(str(i))
