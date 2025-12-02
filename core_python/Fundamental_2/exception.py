

acronyms = {
    "API": "Application Programming Interface",
    "OOP": "Object-Oriented Programming",
    "IDE": "Integrated Development Environment"
}

try:
    print(acronyms["API"])
    print(acronyms["XYZ"])  # This will raise a KeyError
except KeyError as e:
    print(f"KeyError encountered: {e}. Please check if the acronym exists in the dictionary.")
finally:
    print("Execution completed.")

try:
    raise ValueError("This is a custom ValueError for demonstration.")
except ValueError as e:
    print(f"Caught an exception: {e}")

try:
    raise Exception("This is a general exception.")
except Exception as e:
    print(f"Caught a general exception: {e}")