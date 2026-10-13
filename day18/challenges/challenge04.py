developers = [
    {"name": "Israfil", "age": 21, "role": "Software Engineer"},
    {"name": "Alice", "age": 25, "role": "AI Engineer"},
    {"name": "Dave", "age": 19, "role": "Web Developer"},
    {"name": "Bob", "age": 23, "role": "Software Engineer"}
]

software_engineers = list(
    filter(lambda developer: developer["role"] == "Software Engineer", developers)
)

names = list(
    map(lambda eng: eng["name"], software_engineers)
)

print(names)