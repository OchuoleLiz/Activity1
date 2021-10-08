def even_number_finder(list=[]):
    for x in list:
        if x % 2 == 0:
            print(x)


while True:
    list_size = (input("Enter number of items in list...\n"))
    try:
        val = int(list_size)
        print("List size is: ", val)
        break;
    except ValueError:
        print("This is not a Number.\nPlease enter a valid Number")

if int(list_size) == 0:
    print("List must contain Numbers")
else:
    print("Constructing List...")
list_one = list(range(int(list_size) + 1))


print("List contains: ", list_one)
print("The Even numbers in the list are: ")

even_number_finder(list_one)