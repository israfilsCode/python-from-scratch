def create_profile(name: str, age: int, language: str) -> dict:
    profile = {
        "name": name,
        "age": age,
        "language": language
    }

    return profile


result = create_profile("Israfil", 20, "Python")

print(result)