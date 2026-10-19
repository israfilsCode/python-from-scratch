def learning_logger(function):
    def wrapper(*args, **kwargs):
        print("Starting function")
        
        result = function(*args, **kwargs)

        print("Function finished")

        return result
    
    return wrapper


@learning_logger
def introduce(name, language):
    return f"{name} is learning {language}"


result = introduce(name="Israfil", language="Python")

print(result)