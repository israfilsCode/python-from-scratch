def greet():
    name = "Israfil"
    print("Hello,", name)


greet()
# print(name) # name is not available here

# Global scope
# │
# ├── greet()
# │     │
# │     └── Local scope
# │           └── name = "Israfil"
# │

name = "Global"

def scope():
    name = "Local"
    print("Inside", name)


scope()
print("Outside", name)