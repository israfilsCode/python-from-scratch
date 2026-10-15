def greet():
    print("Hello Israfil")

def logger(function):
    def wrapper():
        print("Function started")
        function()
        print("Function finished")

    return wrapper


greet = logger(greet)

greet()

# The decorator essentially wraps the original function:
#        logger
#          │
#          ▼
#    ┌─────────────┐
#    │   wrapper   │
#    │             │
#    │ before      │
#    │    ↓        │
#    │ original    │
#    │    ↓        │
#    │ after       │
#    └─────────────┘

# Function started
# Hello Israfil
# Function finished