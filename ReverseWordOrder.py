def reverse_word_order(input_str):
    new_str = input_str.split()
    count = len(new_str)
    for word in new_str:
        print(new_str[count - 1], end=' ')
        count -= 1

reverse_word_order(input("Please enter a string with several words, separated by spaces!\n"))
