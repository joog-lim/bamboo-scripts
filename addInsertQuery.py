import pymongo

from config import Config

client = pymongo.MongoClient(Config.URL)
db = client.get_database("bamboo")
collect = db["posts"]

datas = list(collect.find())

def wrap_quot(arg1 : str):
  return arg1.replace("'", "\\'")

with open("./posts.sql", "w", newline="", encoding="utf-8-sig") as file_data:
    for i in datas:
        number = i["number"]
        title = wrap_quot(i["title"])
        status = i["status"] if i["status"] != "DELETED" else "REPORTED"
        content = wrap_quot(i["content"])
        tag = wrap_quot(i["tag"])
        createdAt = i["createdAt"]
        try:
          reason = wrap_quot(i["reason"])
        except(KeyError):
          reason = ""

        file_data.writelines(
            f"insert into algorithm (algorithmNumber, title, content, tag, reason, algorithmStatusStatus, createdAt) values({number},'{title}', '{content}', '{tag}', '{reason}', '{status}', '{createdAt}');"
        )
