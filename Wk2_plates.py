def main():
    plate = input()
    plate = is_valid(plate)
    if plate != True:
        print("Invalid")
    else:
        print("Valid")

def is_valid(plate):

    i = 0
    while i < len(plate) and (2 <= len(plate) <= 6):
        if not plate[0:6].isalnum():
            return False
        elif test(plate) != True:
            return False
        else:
            return True
    i += 1

def test(plate):
    i = 0
    while i < len(plate):
        i += 1
        if not plate[0:2].isalpha():
            return False
        else:
            return True      
    k = 2
    while k < len(plate) and not ("0" <= plate[k] <= "9"):
        i += 1
    j = i
    while j < len(plate) and ("0" <= plate[j] <= "9"):
        j += 1
    if plate[k:j].isnumeric() and plate[j:].isalpha():
        if plate[k] == "0":
            return False
        else:
            return True
    
main()