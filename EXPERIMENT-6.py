
# Program to implement List Methods

my_list = []

# Add an element using append()
my_list.append(1)
print("After adding an item:", my_list)

# Append an element
my_list.append(2)
print("After appending an item:", my_list)

# Extend the list with multiple elements
my_list.extend([3, 4, 5])
print("After extending the list:", my_list)

# Insert an element at a specific position
my_list.insert(1, 10)
print("After inserting an item:", my_list)

# Remove a specific element
my_list.remove(3)
print("After removing an item:", my_list)

# Delete and return the last element
my_list.pop()
print("After pop operation:", my_list)

# Delete an element using del
del my_list[0]
print("After deleting an item:", my_list)

