import json
from app.api.data import X, Y
from app.api import qdrant
import time

print(">>> initialize qdrant")
print("qdrant:", qdrant.init())

print(">>> uploads")
for index, item in enumerate(X):
    qdrant.upload(item)
    print(str(index) + " ", end="")

for index, item in enumerate(Y):
    time.sleep(1)
    res = qdrant.search(item)
    print("\n>>> --- 似ているお客様を検索します ---")
    print("> あなたの情報:")
    print(
        "性別:",
        item["性別"],
        "| 履歴:",
        ", ".join(item["直近5件の訪問した飲食店名"]),
        "| 訪問数計:",
        item["訪問した店舗数"],
    )

    time.sleep(1)

    # wait をいい感じに入れて、何軒かテストする

    print("\n> あなたに近い人: ")
    for i, r in enumerate(res):
        content = json.loads(r.payload["content"])
        print(
            "ユーザ:",
            i,
            "| 性別:",
            content["性別"],
            "| 履歴:",
            ", ".join(content["直近5件の訪問した飲食店名"]),
            "| 訪問数計: ",
            content["訪問した店舗数"],
        )
