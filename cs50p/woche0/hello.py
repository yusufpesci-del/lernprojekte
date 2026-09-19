#Ask user for their name

# Remove whitespace from str and capitalize the first letter of the name
name = input("What is your name? ").strip().title()  

# Split user's name into first and last name
first_name, last_name = name.split(" ")


# Say hello to the user
print(f"hello, {first_name}")
print(f"hello, {last_name}")

