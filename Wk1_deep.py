
answer = input("What is the Answer to the Great Question of Life, The Universe, and Everything? ").strip().lower()

match answer:
        case "42" | "forty two" | "Fourty Two" | "forty-two" | "FOURTY TWO" | "FORTY TWO" | "fourty two" | "fourty-two":
            print("Yes")
        case _:
            print("No")
