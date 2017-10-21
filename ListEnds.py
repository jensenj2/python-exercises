def list_ends(list):
    first_and_last = []
    first_and_last.append(list[0])
    first_and_last.append(list[len(list) - 1])
    print(first_and_last)

list = [1, 2, 3, 4, 5, 6, 34]
list_ends(list)