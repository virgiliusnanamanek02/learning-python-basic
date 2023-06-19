# Lists in Python
# Lists are mutable, ordered sequences of elements

# Create a list

my_list = [1, 2, 3, 4, 5]
print(my_list)
my_list.pop()
print(my_list)
my_list.append(6)
print(my_list)
my_list.remove(3)
print(my_list)


def my_function():
    my_list = [1, 2, 3, 4, 5]
    for i in my_list:
        print(i)


my_function()
