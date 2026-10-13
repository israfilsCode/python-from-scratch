developers = [
    {"name": "Israfil", "age": 21},
    {"name": "Alice", "age": 25},
    {"name": "Dave", "age": 19}
]

sorted_dev_by_name = sorted(
    developers,
    key=lambda developer: developer["name"]
)

print(sorted_dev_by_name)