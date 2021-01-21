# Initializing empty lists 
lst1 = []
lst2 = []
#For list of integers
lst1 = [int(item) for item in input("Enter the list1 items : \n ").split()]
lst2 = [int(item) for item in input("Enter the list2 items : \n ").split()]

print(lst1)
print(lst2)

def unique(lst1):

    # intilize a null list
    unique_list = []

    # Looping through all elements of input list
    for x in lst1:
        # check if an element exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
# Uncomment next line if desired O/P is uniquesorted list(ascending order)
            #unique_list.sort()
#Uncomment next line if desired O/P is uniquesorted list(descending order)
            #unique_list.sort(reverse=True)
    # print list
    for x in unique_list:
        print(x)

print("the unique values from 1st list is")
unique(lst1)

print("\nthe unique values from 2nd list is")
unique(lst2)




