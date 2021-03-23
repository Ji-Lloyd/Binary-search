# This program shows the Binary Search when the user is finding the value and index number in the list
loc = -1  # This variable is to locate the index number of the given value by the user within the list


def search(list, n):  # This function act as the searching method if the user's input is within the given list

    l = 0  # This variable signified as the 'lower bound'
    u = len(list) - 1  # This variable assigned for the length of 'list'

    while l <= u:  # If the lower bound is less than the upper bound or the length of the list, this loop will execute
        mid = (l + u) // 2  # This is the formula when doing the binary search!!

        if list[mid] == n:  # If the result of 'mid' variable is equals to the output of the user, this will execute
            globals()['loc'] = mid  # The 'globals()' will get the specific variable from the outside
            return True  # Returns true if this condition is met
        else:
            if list[mid] < n:  # If the 'mid' variable is less than the output of the user this condition will execute
                l = mid + 1  # The 'l' variable or lower  bound will append if the 'mid' is less the 'n'
            else:
                u = mid - 1  # If 'mid' is greater the 'n' or user's input then the 'mid' value will decrease

    return False  # returns false


list = [41, 21, 54, 6, 8, 31, 13]  # predetermined unorganised list

print("Original list:", list)  # prints the predetermined unorganised list
list.sort()  # This will sort the list from least to greatest value
print("Sorted list:", list)  # prints the predetermined 'sorted list'

n = int(input("Enter number:"))  # This variable will ask the user for input, that may be on the given list

if search(list, n):  # This condition is for the 'search' function that will find the user's input in the list
    print('found at index number:', loc + 1)  # prints the location or index value of the given value by the user
else:
    print("lost")  # If the list does not have the user's output value this will be executed

print("hello world")
print("lloyd")