import pymongo

from config import Config

client = pymongo.MongoClient(Config.URL)
db = client.get_database("bamboo")
collect = db["posts"]

datas = list(collect.find())

with open("./posts.sql", "w", newline="", encoding="utf-8-sig") as file_data:
    for i in datas:
        number = i["number"]
        title = i["title"]
        status = i["status"] if i["status"] != "DELETED" else "REPORTED"
        content = i["content"]
        tag = i["tag"]
        createdAt = i["createdAt"]
        try:
          reason = i["reason"]
        except(KeyError):
          reason = ""

        file_data.writelines(
            f"insert into algorithm (algorithmNumber, title, content, tag, reason, algorithmStatusStatus, createdAt) values({number},'{title}', '{content}', '{tag}', '{reason}', '{status}', '{createdAt}');"
        )
