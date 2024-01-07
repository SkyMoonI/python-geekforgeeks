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

"""

set1 = set() 
print("Initial blank Set: ") 
print(set1) 
set1 = set("GeeksForGeeks") 
print("\nSet with the use of String: ") 
print(set1) 
set1 = set(["Geeks", "For", "Geeks"]) 
print("\nSet with the use of List: ") 
print(set1) 
set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks']) 
print("\nSet with the use of Mixed Values") 
print(set1) 

set1 = set(["Geeks", "For", "Geeks"]) 
print("\nInitial set") 
print(set1) 
print("\nElements of set: ") 
for i in set1: 
    print(i, end=" ") 
print("Geeks" in set1) 

# set = collection which is unordered, unindexed. no duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate","cup", "knife"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#utensils.update(dishes) # adds items from dishes to utensils
#dinner_table = utensils.union(dishes) # unions two sets

#print(dishes.difference(utensils))
#print(utensils.intersection(dishes))


#for x in dinner_table:
#    print(x)

