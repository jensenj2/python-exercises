list_len = int(input("How long will your list be? "))
limit = int(input("What is your exclusive limit? "))
list = []
output_list = []

for x in range(0, list_len):
    list.append(int(input("Enter a number: ")))

less_than_limit = 0
for x in list:
    if x < limit:
        less_than_limit += 1
        output_list.append(x)
print "\n%d numbers less than 5 were found in the list!" % (less_than_limit)
print "Input list: %s" % (list)
print "Output list: %s" % (output_list)