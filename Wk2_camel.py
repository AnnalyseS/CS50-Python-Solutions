#prompt user for input
def main():
    cC = input("camelCase: ")
    print("snake_case: ", end="")
    
#get the input to be iterated over and search for captials via for loop
    for char in cC:
        if char.isupper():
            print(f"_{char.lower()}", end="")
        else:
            print(char, end="")
    print()


main()