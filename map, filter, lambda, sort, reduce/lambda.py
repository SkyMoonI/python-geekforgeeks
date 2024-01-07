# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one experssion.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
# lambda parameter:expression

double = lambda x:x*2
print(double(5))
multiply = lambda x,y:x*y
print(multiply(5,10))
add = lambda x,y,z:x+y+z
print(add(5,3,4))
full_name = lambda first_name, last_name:first_name+ " " + last_name
print(full_name("bro", "code"))
age_check = lambda age:True if age >= 12 else False
print(age_check(5))
print(lambda x:x[1])

# first parentheses contains a lambda form, that is   
# a squaring function and second parentheses represents 
# calling lambda 
print( (lambda x: x**2)(5)) 

# Make function of two arguments that return their product 
print ((lambda x, y: x*y)(3, 4))