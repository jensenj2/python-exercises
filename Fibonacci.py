def fibonacci(number):
    fib_list = [1, 1]
    count = 0
    a = 0
    b = 1
    while count != number:
        fib_list.append(fib_list[a] + fib_list[b])
        a += 1
        b += 1
        count += 1
    print(fib_list)

num = int(input("How many fibonacci numbers (excluding the first two 1s)? "))
fibonacci(num)