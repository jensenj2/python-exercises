def get_divisors():
    number = int(input("Please enter a number: "))
    divisors = []

    for x in range(1, number):
        if number % x == 0:
            divisors.append(x)
    print(divisors)

get_divisors()