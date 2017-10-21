def get_divisors(number):
    divisors = []
    for x in range(1, number + 1):
        if number % x == 0:
            divisors.append(x)
    return divisors

number = int(input("Please provide a number: "))
divisors = (get_divisors(number))

#This assumes that 0 and 1 are not considered to be prime
if len(divisors) != 2:
    print("Your number is not a prime! ")
    print("Divisors: " + str(divisors))
else:
    print("Your number is prime! ")
