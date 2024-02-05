import json
for i in range(10):
    with open(f"data/post-{i}.txt", "w") as f:
        
        f.write(str(i))
