# finding smallest element in the list with complexity of order of n
import random


# taking the first element as smallest
# iterating the list from 2nd element to the end
# if new smaller than smallest found
# make it smallest
def find_smallest_in_n(my_list):
    smallest = my_list[0]
    for i in range(1, len(my_list)):
        if smallest > my_list[i]:
            smallest = my_list[i]
    return smallest


# creating a list with ransom elements
def initialize_list():
    my_list = []
    for i in range(0, 100):
        number = random.randrange(0, 1000)
        my_list.append(number)
        print number
    return my_list


number_list = initialize_list()
print "smallest element is :", find_smallest_in_n(number_list)
