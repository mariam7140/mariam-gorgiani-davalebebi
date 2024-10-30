def convert(temperature, type):
    if type == "celsius":
        return(temperature * 9 / 5 + 32)
    elif type == "fahrenheit":
        return((temperature - 32) * 5 / 9)
    else:
        return("incorrect input, please try again")


def main():
    print("25 degree celsius is", convert(25, "celsius"))
    print("25 degree fahrenheit is", convert(25, "fahrenheit"))
    print("-10 degree celsius is", convert(-10, "celsius"))
    print("What is 75 degree fahrenheit in celsius?", "It is", convert(75, "fahrenheit"))


if __name__ == "__main__":
    main()