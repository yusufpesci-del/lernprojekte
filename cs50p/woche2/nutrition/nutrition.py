#nutrition
#apple, banana, chocolate

fruits = {"apple": 130, "banana": 110, "avocado": 50, "sweet cherries": 100,
        "cantaloupe": 50, "grapefruit": 60, "grapes": 90, "honeydew melon": 50, "kiwifruit": 90, "lemon": 15, "lime": 20,
          "nectarine": 60, "orange": 80, "peach": 60, "pear": 100,
          "pineapple": 50, "plums": 70, "strawberries": 50, "tangerine": 50, "watermelon": 80}
item = input("Item: ").strip().lower()
if item in fruits:
    print(f"Calories: {fruits[item]}")

