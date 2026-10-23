
def main():
    word = input("Input: ")

    for char in word:
        if char == "a" or char == "i" or char == "e" or char == "o" or char == "u":
            word = word.replace(char, "")
    print(f"Output: {word}")
           

main()
#print word without vowels