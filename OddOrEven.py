number = int(input("Please enter a number: "))
check = int(input("Please enter a divisor: "))

if number % check == 0:
    print ("This division is even!")
    if number % 4 == 0:
        print ("...and 'number' is a multiple of 4!")
else:
    print ("This division is odd!")