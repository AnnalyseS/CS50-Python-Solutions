#main function will ask user for input, call convert, and output the desired output
def main():
    time = input("What time is it? ").strip("a.m.").strip("p.m.")
    hr, min = time.split(":")
    time = convert_h(hr) + convert_m(min)
    #put in the parameters
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
            print("dinner time")
    

#convert to float
def convert_h(h):
    h = float(h)
    return h
def convert_m(m):
    m = float(m) / 100
    if m == .3:
        return m +.2
    else:
        return m

if __name__ == "__main__":
    main()