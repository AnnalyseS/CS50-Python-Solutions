#prompt for input and check if input is valid
def main():
    total = 50   
    valid_coins = [5, 10, 25]

    while True:
        print(f"Amount Due: {total}")
        coin = int(input("Insert Coin: "))
        if coin not in valid_coins:
            continue
        else:
            total = total - coin
        if total <= 0:
            print(f"Change Due: {total + coin}")
            break
        
main()