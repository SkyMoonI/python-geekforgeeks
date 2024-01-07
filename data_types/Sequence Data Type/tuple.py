#--------------------Tuple---------------------------
"""
Ordered: Elements maintain a specific order.
Allow duplicates: Elements can repeat.
Immutable: Elements cannot be changed after creation.
Syntax: Created using parentheses () or the tuple() function.
Use cases:
Representing fixed collections of data that shouldn't be modified.
Returning multiple values from functions.
Storing data that needs to maintain a specific order.
"""
# tuple = collection which is ordered and unchangeable
#         used to group together related data
Tuple1 = () 
print("Initial empty Tuple: ") 
print(Tuple1) 
Tuple1 = ('Geeks', 'For') 
print("\nTuple with the use of String: ") 
print(Tuple1) 
list1 = [1, 2, 4, 5, 6] 
print("\nTuple using List: ") 
print(tuple(list1)) 
Tuple1 = tuple('Geeks') 
print("\nTuple with the use of function: ") 
print(Tuple1) 
Tuple1 = (0, 1, 2, 3) 
Tuple2 = ('python', 'geek') 
Tuple3 = (Tuple1, Tuple2) 
print("\nTuple with nested tuples: ") 
print(Tuple3) 


student = ("Bro", 21, "male")

print(student.count("Bro")) # counts how many times tuple has the item, case sensetive
print(student.index("male")) # checks the index of the item
for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here!")