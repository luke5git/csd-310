from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.q1hbcug.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url, tls = True, tlsAllowInvalidCertificates=True)

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
students = list(db.students.find({}))
student = db.students.find_one({"student_id": "1007"})
print(students)
print(student)
print("--DISPLAYING STUDENTS DOCUMENT FROM find() QUERY--")
for s in students:
    print("Student ID: ", s["student_id"])
    print("First Name: ", s["first_name"])
    print("Last Name:  ", s["last_name"])
    print("")
print("--DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY--")
print("Student ID: ", student["student_id"])
print("First Name: ", student["first_name"])
print("Last Name:  ", student["last_name"])
print("")