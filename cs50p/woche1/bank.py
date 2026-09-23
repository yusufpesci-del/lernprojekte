# Home federal savings bank

greeting = input("Greeting: ").strip().lower()

if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
# greetings with "hello" are free, greetings that start with "h" cost $20, and all other greetings cost $100.
# what's up, How are you, Hello, hello, hi, hey, good morning, good evening, good afternoon, good night, greetings, salutations