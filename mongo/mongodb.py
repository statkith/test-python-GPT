import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mern-crud"]  # databse
mycol = mydb["mindmaps"]        # collection

def db(mylist):

    # x = mycol.delete_many({})  # Delete all documents in the "mindmaps" collection
    # print(x.deleted_count, " documents deleted.")

    x = mycol.insert_one(mylist)  # insert data
    print(x.inserted_id)


def printdb():
    open("docs\\6_db_save.txt", 'w').close()
    f = open("docs\\6_db_save.txt", "a")

    for x in mycol.find():
        print(x)
        f.write(str(x) + "\n\n")

    f.close()
