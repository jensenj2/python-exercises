import sys

while True:
    string = input("Please enter a string: ")
    if string == string[::-1]:
        print("Palindrome!")
        sys.exit(0)
    else:
        print("Not a palindrome!\n")