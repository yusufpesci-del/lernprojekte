
import emoji

text = input("Input: ")
smiley = emoji.emojize(text, language="alias")
print(f"Output: {smiley}")

