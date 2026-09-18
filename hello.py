#Ask user for their name
name = input("What is your name? ") 

# Remove whitespace from str
name = name.strip()  

# Capitalize the first letter of the name
name = name.capitalize()  

# Say hello to the user
print(f"hello, {name}")