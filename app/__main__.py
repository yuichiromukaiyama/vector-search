import json
from app.api.data import X, Y
from app.api import qdrant, embeddings

print(">>> initialize qdrant")
# print("qdrant:", qdrant.init())

# print(">>> uploads")
# for index, item in enumerate(X):
#     qdrant.upload(item)
#     print(str(index) + " ", end="")

print(">>> test")
for index, item in enumerate(Y):
    res = qdrant.search(item)
    print(">>> similar result")
    print("input: ", item)

    for i, r in enumerate(res):
        print(i, "result: ", json.loads(r.payload["content"]))
