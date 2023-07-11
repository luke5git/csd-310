from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.q1hbcug.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url, tls = True, tlsAllowInvalidCertificates=True)

db = client.pytech
print(db.list_collection_names())

students = list(db.students.find({}))
print("--DISPLAYING STUDENTS DOCUMENT FROM find() QUERY--")
for s in students:
    print("Student ID: ", s["student_id"])
    print("First Name: ", s["first_name"])
    print("Last Name:  ", s["last_name"])
    print("")
result = db.students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Roberts"}})
student = db.students.find_one({"student_id": "1007"})
print (result.modified_count)
print("--DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY--")
print("Student ID: ", student["student_id"])
print("First Name: ", student["first_name"])
print("Last Name:  ", student["last_name"])
print("")