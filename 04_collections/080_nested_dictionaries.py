school = {
    "name": "Python Academy",
    "classes": {
        "math": {"teacher": "Mr. Smith", "students": 30},
        "science": {"teacher": "Ms. Jones", "students": 25},
    },
}

print(school["name"])
print(school["classes"]["math"]["teacher"])
print(school["classes"]["science"]["students"])

for subject, info in school["classes"].items():
    print(f"{subject}: {info['teacher']} ({info['students']} students)")

school["classes"]["english"] = {"teacher": "Mrs. Brown", "students": 28}
print(list(school["classes"].keys()))
