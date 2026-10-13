developers = [
    {"name": "Israfil", "age": 21},
    {"name": "Alice", "age": 25},
    {"name": "Dave", "age": 19}
]

sorted_developers = sorted(
    developers,
    key=lambda developer: developer["age"]
)

print(sorted_developers)