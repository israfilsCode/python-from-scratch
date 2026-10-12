developer = {
    "name": "Israfil",
    "age": 20,
    "country": "Bangladesh",
    "role": "Software Engineer",
    "language": "Python",
    "goal": "Build an LLM from scratch",
    "skill": "Full Stack Development"
}

total_info = 0

for key, value in developer.items():
    print(key + ": " + str(value))
    total_info += 1

print("Total information:", total_info)