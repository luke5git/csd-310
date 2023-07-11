from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.q1hbcug.mongodb.net/?retryWrites=true&w=majority"
#print (db.list_collection_names())
client = MongoClient(url, tls = True, tlsAllowInvalidCertificates=True)
#db = client["mydb"]
db = client.pytech
print(db.list_collection_names())
records = [
    {
        "student_id": "1007",
        "first_name": "Tim",
        "last_name": "Scott"
    },
    {
        "student_id": "1008",
        "first_name": "Olivia",
        "last_name": "John"
    },
    {
        "student_id": "1009",
        "first_name": "Mark",
        "last_name": "Williams"
    }
]
collection = db["students"]

#insert all three students

tim_id = collection.insert_one(records[0]).inserted_id
olivia_id = collection.insert_one(records[1]).inserted_id
mark_id = collection.insert_one(records[2]).inserted_id

print(tim_id)
print (olivia_id)
print(mark_id)