# deep Thought
#x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

#if x == "42":
#    print("Yes")
#elif x == "forty-two":
#    print("Yes")
#elif x == "forty two":
#    print("Yes")
#else:
#    print("No")
#-----------------------------------------------------------------------------------------------------------    
#2. und kürzerer Weg.
x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

if x == "42" or x == "forty-two" or x == "forty two":
    print("Yes")
else:
    print("No")