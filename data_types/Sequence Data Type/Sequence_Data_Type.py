"""
----------------------Sets

Unordered: Elements have no specific order.
Unique: No duplicates allowed.
Mutable: Elements can be added or removed after creation.
Syntax: Created using curly braces {} or the set() function.
Use cases:
Removing duplicates from a list.
Performing set operations like union, intersection, difference.
Checking for membership efficiently.


--------------------Tuples

Ordered: Elements maintain a specific order.
Allow duplicates: Elements can repeat.
Immutable: Elements cannot be changed after creation.
Syntax: Created using parentheses () or the tuple() function.
Use cases:
Representing fixed collections of data that shouldn't be modified.
Returning multiple values from functions.
Storing data that needs to maintain a specific order.


----------------Key Differences Summary Table

Feature	        Sets	        Tuples
Order	        Unordered	    Ordered
Mutability	    Mutable	        Immutable
Duplicates	    Not allowed	    Allowed
Syntax	        {} or set()	    () or tuple()


Choosing the Right Data Structure:

Use a set when you need to store a collection of unique elements without any specific order, and you may need to modify it later.
Use a tuple when you need to represent a fixed collection of elements that should maintain their order and cannot be changed.
"""

my_set = {1, 2, 3}  # Creates a set
my_tuple = (1, 2, 3)  # Creates a tuple

# Trying to add a duplicate to the set
my_set.add(2)  # No change, as 2 is already in the set

# Trying to change an element in the tuple
my_tuple[0] = 4  # Raises a TypeError: 'tuple' object does not support item assignment


