#--------------------list---------------------------
List = [] 
print("Initial blank List: ") 
print(List) 
List = ['GeeksForGeeks'] 
print("\nList with the use of String: ") 
print(List) 
List = ["Geeks", "For", "Geeks"] 
print("\nList containing multiple values: ") 
print(List[0]) 
print(List[2]) 
List = [['Geeks', 'For'], ['Geeks']] 
print("\nMulti-Dimensional List: ") 
print(List) 

List = ["Geeks", "For", "Geeks"] 
print("Accessing element from the list") 
print(List[0]) 
print(List[2]) 
print("Accessing element using negative indexing") 
print(List[-1]) 
print(List[len(List)-3]) 

# list = used to store multiple items in a single variable

foods = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

#foods[0] = "sushi"
#print(foods[0])
#print(foods)

#foods.append("ice cream") # adds an element at the end of the sentence
#foods.remove("hotdog") # removes the element
#foods.pop() # removes the last element
#foods.insert(0, "cake") # adds an element at a specified index
#foods.sort() # sorts the list in an alphabetic order
#foods.clear() # clears the list

for food in foods:
    print(food)

my_list = list(range(5))  # Output: [0, 1, 2, 3, 4]