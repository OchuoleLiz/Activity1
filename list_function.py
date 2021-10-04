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

if list_size == 0:
    print("List must contain Numbers")
else:
    print("Constructing List...")

list_one = [(int(input("Enter single number and press enter:\n "))) for _ in range(int(list_size))]
print("List contains: ", list_one)
print("The Even numbers in the list are: ")

even_number_finder(list_one)