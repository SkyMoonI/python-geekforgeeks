# syntax : input().split(separator, maxsplit)

## Python program showing how to [# Python program showing how to] 
## multiple input using split
# 
## taking two inputs at a time
#x, y = input("Enter two values: ").split()
#print("Number of boys: ", x)
#print("Number of girls: ", y)
#
## taking three inputs at a time
#x, y, z = input("Enter three values: ").split()
#print("Total number of students: ", x)
#print("Number of boys is : ", y)
#print("Number of girls is : ", z)
#
## taking two inputs at a time
#a, b = input("Enter two values: ").split()
#print("First number is {} and second number is {}".format(a, b))
 
# taking multiple inputs at a time 
# and type casting using list() function
#x = list(map(int, input("Enter multiple values: ").split()))
#print("List of students: ", x)

# Python program showing
# how to take multiple input
# using List comprehension
 
## taking two input at a time
#x, y = [int(x) for x in input("Enter two values: ").split()]
#print("First Number is: ", x)
#print("Second Number is: ", y)

## taking three input at a time
#x, y, z = [int(x) for x in input("Enter three values: ").split()]
#print("First Number is: ", x)
#print("Second Number is: ", y)
#print("Third Number is: ", z)

## taking two inputs at a time
#x, y = [int(x) for x in input("Enter two values: ").split()]
#print("First number is {} and second number is {}".format(x, y))
 
## taking multiple inputs at a time 
#x = [int(x) for x in input("Enter multiple values: ").split()]
#print("Number of list is: ", x) 

## taking multiple inputs at a time separated by comma
#x = [int(x) for x in input("Enter multiple value: ").split(",")]
#print("Number of list is: ", x) 

#x = list(map(int, input().split(",", 5)))
#print(x)

#y = [int(x) for x in input().split()]
#print(y)