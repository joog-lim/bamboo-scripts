import csv
import pymongo

from config import Config

client = pymongo.MongoClient(Config.URL)
db = client.get_database("bamboo")
collect = db["posts"]

datas = list(collect.find())

with open("./posts.csv", "w", newline="", encoding="utf-8-sig") as file_data:
    wr = csv.writer(file_data)
    wr.writerow(
        [
            "_id",
            "createdAt",
            "title",
            "status",
            "content",
            "tag",
            "number",
            "updatedAt",
            "__v",
            "reason",
            "deleteReqNumber",
        ]
    )
    print(list(datas[0].values()))
    for i in datas:
        wr.writerow(list(i.values()))
