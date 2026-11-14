import sys


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

# lines = []
# try:
#     with open(sys.argv[1]) as file:
#         lines = file.readlines()
# except FileNotFoundError:
#     sys.exit("File does not exist")

# print(len(lines))


line_count = 0
try:
    with open(sys.argv[1]) as file:
        for line in file:
            stripped_line = line.lstrip()
            if stripped_line.strip() and not stripped_line.startswith("#"):
                line_count += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(line_count)
