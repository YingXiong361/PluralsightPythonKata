print("----- Reading file line by line -----")
file = open("input.txt", "r")

for line in file:
    print(line.strip())


file.close()

print("----- Using with statement -----")


with open("input.txt", "r") as file:
    result = file.readlines()
    print("readlines():", result)

    print("Current file position:", file.tell()) # get current position (should be 0)
    file.seek(0)  # reset file pointer to the beginning
    print("Current file position:", file.tell())  # get current position (should be 0)
    next_line = file.readline()
    print("readline():", next_line)

print("----- Reading entire file at once -----")
# with is the shortcut for try-finally to ensure file closure
file = open("input.txt", "r")
try:
    print(file.read())
finally:
    file.close()