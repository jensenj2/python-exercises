import random

list1_len = int(input("How long should the first list be? "))
list2_len = int(input("How long should the second list be? "))

list1 = random.sample(range(list1_len), list1_len)
list2 = random.sample(range(list2_len), list2_len)
overlap = []

for num in list1:
    if (num in list1) and (num in list2):
        overlap.append(num)
print("Overlapping values: " + str(overlap))
