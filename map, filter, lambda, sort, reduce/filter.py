# filter() = creates a collection of elements from an iterable for 
# which a function returns true

# filter(function, iterable)

friends = [("rachel",19),("monica",18),("phoebe",17),("joey",16),("chandler",21),("ross",20),]

age = lambda data:data[1]>=18

drinking_buddies = list(filter(age, friends))

for friend in drinking_buddies:
    print(friend)

#Using filter function to filter all  
# numbers less than 5 from a list 
number_list = range(-10, 10) 
less_than_five = list(filter(lambda x: x < 5, number_list)) 
print(less_than_five)




# code without using map, filter and lambda 
  
# Find the number which are odd in the list 
# and multiply them by 5 and create a new list 
  
# Declare a new list 
x = [2, 3, 4, 5, 6] 
  
# Empty list for answer 
y = [] 
  
# Perform the operations and print the answer 
for v in x: 
    if v % 2: 
        y += [v*5] 
print(y) 


# above code with map, filter and lambda 
  
# Declare a list 
x = [2, 3, 4, 5, 6] 
  
# Perform the same operation as  in above post 
y = list(map(lambda v: v * 5, filter(lambda u: u % 2, x))) 
print(y) 