import json


arr = []

for i in range(10):
    arr.append({"num": i, "num+1": i+1})

jstring = json.dumps(arr)

decode = json.loads(jstring)
print(decode.pop(0))