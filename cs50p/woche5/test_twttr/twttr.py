
def main():
    twitter = input("Input: ")
    print("Output:", shorten(twitter))

def shorten(word):
    ergebnis = ""
    for zeichen in word:
        if zeichen not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            ergebnis += zeichen
    return ergebnis
if __name__ == "__main__":
    main()
