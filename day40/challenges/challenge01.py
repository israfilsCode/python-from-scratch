def learning_logger(function):
    def wrapper():
        print("Starting function")
        function()
        print("Function finished")

    return wrapper


@learning_logger # decorator function
def study():
    print("I'm studying Python")


study()