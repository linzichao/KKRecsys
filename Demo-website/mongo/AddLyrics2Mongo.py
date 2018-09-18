import pymongo

mongo_client = pymongo.MongoClient('localhost', 27017)
db_name = mongo_client['kkbox']
collection_name = 'song'
db_cm = db_name[collection_name]


for line in open("./output2"):

    ele = line.split(",")

    db_cm.find_one_and_update({"sond_id": ele[0]},{"$set":{"lyrics": ele[1]}})
