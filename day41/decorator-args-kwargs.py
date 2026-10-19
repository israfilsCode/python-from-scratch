def learning_logger(function):
    def wrapper(*args, **kwargs):
        print("Starting function")

        result = function(*args, **kwargs)

        print("Function finished")

        return result

    
    return wrapper


@learning_logger
def calculate_square(number):
    return number ** 2


result = calculate_square(10)
print(result)