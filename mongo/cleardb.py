import pymongo

def cleardatabase():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["mern-crud"]  # databse
    mycol = mydb["mindmaps"]        # collection

    x = mycol.delete_many({})  # Delete all documents in the "mindmaps" collection
    print(x.deleted_count, " documents deleted.")