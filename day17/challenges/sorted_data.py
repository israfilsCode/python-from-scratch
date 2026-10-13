developers = [
    {"name": "Israfil", "age": 21, "role": "Software Engineer"},
    {"name": "Alice", "age": 25, "role": "AI Engineer"},
    {"name": "Dave", "age": 19, "role": "Web Developer"},
    {"name": "Bob", "age": 23, "role": "Software Engineer"}
]

sorted_devs_youngest_to_oldest = sorted(
    developers,
    key=lambda developer: developer["age"]
)

sorted_devs_by_name = sorted(
    developers,
    key=lambda developer: developer["name"]
)

sorted_devs_oldest_to_youngest = sorted(
    developers,
    key=lambda developer: developer["age"],
    reverse=True
)

print(sorted_devs_youngest_to_oldest)
print(sorted_devs_by_name)
print(sorted_devs_oldest_to_youngest)