student = {"name": "Ojas", "age": 18, "course": "Python"}

print(student["name"])
print(student["age"])

student["age"] = 19
student["city"] = "Delhi"

student.pop("course")

extra = {"grade": "A"}
student.update(extra)

print(student)
