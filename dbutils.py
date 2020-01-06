from pymongo import MongoClient

MONGO_URI = 'mongodb+srv://miguel:testing2020@cluster0-7ogms.mongodb.net/test?retryWrites=true&w=majority'

def db_connect(MONGO_URI, db_name, col_name):
    client = MongoClient(MONGO_URI)
    database = client[db_name]
    collection = database[col_name]
    return collection

def db_insert_product(collection, product):
    return collection.insert_one(product)

def db_find_one(collection, query={}):
    return collection.find_one(query)

def db_update_one(collection, query={}):
    return collection.update(query)

if __name__ == '__main__':
    print("MongoClient imported successfully!")