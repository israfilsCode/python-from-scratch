class LearningSession:
    def __enter__(self):
        print("Starting learning session")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Ending learning session")


with LearningSession():
    print("Learning Python")


print(type(LearningSession()))