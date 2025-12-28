import os, pathlib
output_file = os.path.join(pathlib.Path(__file__).parent.resolve(), "output.txt")

def add_acronym_definition():
    acronym = input("Enter an acronym you want to add: ")
    definition = input(f"Enter the definition for {acronym}: ")

    # append mode to add without overwriting existing content
    with open(output_file, "a") as file:
        file.write(f"{acronym}: {definition}\n")

def init_acronym_definition():
    acronym = input("Enter a first acronym you want to add: ")
    definition = input(f"Enter the definition for {acronym}: ")

    # attention: using 'w' mode will overwrite existing content
    with open(output_file, "w") as file:
        file.write(f"{acronym}: {definition}\n")

def main():
    while True:
        choice = input("Do you want to (i)nitialize or (a)dd an acronym definition? (i/a): ").strip().lower()
        if choice == 'i':
            init_acronym_definition()
        elif choice == 'a':
            add_acronym_definition()
        else:
            print("Invalid choice. Program will exit.")
            break

if __name__ == "__main__":
    main()