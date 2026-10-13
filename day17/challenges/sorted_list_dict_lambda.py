developers = [
    {"name": "Israfil", "age": 21},
    {"name": "Alice", "age": 25},
    {"name": "Dave", "age": 19}
]

sorted_devs_youngest_to_oldest = sorted(
    developers,
    key=lambda developer: developer["age"]
)

sorted_devs_oldest_to_youngest = sorted(
    developers,
    key=lambda developer: developer["age"],
    reverse=True
)

print(sorted_devs_youngest_to_oldest)
print(sorted_devs_oldest_to_youngest)