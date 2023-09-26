# students = ["Hermione", "Harry", "Ron", "Draco"]
# houses = ["Grffindor", "Grffindor", "Grffindor", "Slytherin"]

# students = {"Hermione": "Grffindor", 
# "Harry": "Grffindor", 
# "Ron": "Grffindor", 
# "Draco": "Slytherin"
# }

# for student in students:
#     print(student, students[student], sep=",")

students = [
    {"name": "Hermione", "house": "Gryffindor", "patrous": "Otter" },
    {"name": "Harry", "house": "Gryffindor", "patrous": "Stag" },
    {"name": "Ron", "house": "Gryffindor", "patrous": "Jack Russell Terrier" },
    {"name": "Draco", "house": "Slytherin", "patrous": None }]

for student in students:
    print(student["house"], student["name"], student["patrous"], sep="," )