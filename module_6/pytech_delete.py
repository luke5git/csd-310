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
tim_id = db.students.insert_one(    {
        "student_id": "1010",
        "first_name": "Brian",
        "last_name": "Johnson"
    }).inserted_id
student = db.students.find_one({"student_id": "1010"})
print("--DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY--")
print("Student ID: ", student["student_id"])
print("First Name: ", student["first_name"])
print("Last Name:  ", student["last_name"])
print("")
student = db.students.delete_one({"student_id": "1010"})
students = list(db.students.find({}))
print("--DISPLAYING STUDENTS DOCUMENT FROM find() QUERY--")
for s in students:
    print("Student ID: ", s["student_id"])
    print("First Name: ", s["first_name"])
    print("Last Name:  ", s["last_name"])
    print("")