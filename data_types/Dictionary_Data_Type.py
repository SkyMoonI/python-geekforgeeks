Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
print("\nDictionary with the use of Integer Keys: ") 
print(Dict) 
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict) 
Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 
Dict = dict([(1, 'Geeks'), (2, 'For')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict) 

Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'} 
print("Accessing a element using key:") 
print(Dict['name']) 
print("Accessing a element using get:") 
print(Dict.get(3)) 


# dictionary = a changeable, unordered collection of unique key:value pairs
#              fast because they use hashing, allow us to access a value quickly

capitals = {'USA': 'Washington DC',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}

# capitals.update({'Germany':'Berlin'})
# capitals.update({'USA':'TOKAT'})
# capitals.pop("China") # removes china
# capitals.clear()

# print(capitals['USA'])
# print(capitals['Germany'])
# print(capitals.get('Germany')) # safer to call with get
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

# for key, value in capitals.items():
#    print(key, value)

# Create a new dictionary 
d = dict() # or d = {} 

# Add a key - value pairs to dictionary 
d['xyz'] = 123
d['abc'] = 345

# print the whole dictionary 
print (d) 

# print only the keys 
print (d.keys()) 

# print only values 
print (d.values()) 

# iterate over dictionary 
for i in d : 
	print ("%s %d" %(i, d[i])) 

# another method of iteration 
for index, key in enumerate(d): 
	print (index, key, d[key]) 

# check if key exist 
print ('xyz' in d) 

# delete the key-value pair 
del d['xyz'] 

# check again 
print ("xyz" in d)
