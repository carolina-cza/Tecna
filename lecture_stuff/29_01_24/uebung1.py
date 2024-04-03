from faker import Faker
import random

fake = Faker()
print(fake.name())

students = []

#generate fake data for 10 students
for _ in range(10):
    student = {
        "name": fake.name(),
        "age": random.randint(18,25),
        "major": random.choice(["Computer Science", "Mathematics", "Physics"]),
        "gpa": round(random.uniform(2.0,4.0),2),
        "is_international": random.choice([True,False])
    }
    students.append(student) 

#Accessing an printing student information
for student in students:
    full_name = student["name"]
    first_name = full_name.split()[0]
    last_name = full_name.split()[1]
    print(first_name,last_name)
    print("Age:", student["age"])
    print("Major:",student["major"])
    print("GPA:", student["gpa"])
    print("Is International Student:", student["is_international"])

#Put all first name ´s of students in a list
first_names = []
for student in students:
    full_name = student["name"]
    first_name = full_name.split()[0]
    first_names.append(first_name)
print(first_name)

#first_names = ["john","JAne", "John", "Alice" "Bob", "JAne"]
duplicate_count = {name: first_names.count(name)
                   for name in set(first_names)
                   if first_names.count(name)>1}
print(duplicate_count)

#test with list that has duplicates
first_names = ["John", "Jane","Alice", "Bob", "Jane"]
print(first_names)
duplicate_count = {name: first_names.count(name)
                   for name in set(first_names)
                   if first_names.count(name)>1}
print(duplicate_count)