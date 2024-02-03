import json
for i in range(10):
    with open(f"data/post-{i}.json", "w") as f:
        jsondata = {
            "title":f'This is Post Number {i}',
            "content": f"This is simple lorem ipsum for number {i}"
        }
        f.write(json.dumps(jsondata))
