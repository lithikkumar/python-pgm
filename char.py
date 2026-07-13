c1 = input("Enter a character: ")

if c1 == "a" or c1 == "e" or c1 == "i" or c1 == "o" or c1 == "u":
    print("vowel")
elif c1 == "+" or c1 == "-" or c1 == "*" or c1 == "/":
    print("operator")
elif c1 == "#" or c1 == "_":
    print("special character")
else:
    print("consonant")
