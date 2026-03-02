# Set
# Duplicates are not allowed

Arr = {10,20,30,40,10}
print(Arr)
print(type(Arr))

fruits = {"apple", "Banana", "Cherry"}
print(fruits)

# add an element
fruits.add("Orange")
print(fruits)

# Remove an element
fruits.remove("Banana")
print(fruits)

# Check for Membership(  very eficient)
if "apple" in fruits:
    print("Apple is in the set")

# perform union operation
 
set1 = {1,2,3}
set2 = {3,4,5}
union_set = set1.union(set2)
print(union_set)


# Dictionary

Book = {"Name":"Lets c", "price":350, "Author":"Y.kanetkar"}
print(Book)
print(Book["price"])

# also by using .get() we can access the element
print(Book.get("price"))
print(type(Book))

# Also we can use dict() constructor to create dictionary
employee_dict = dict(name = "karan", age = 30, role = "Data Engineer")
print(employee_dict)
print(type(employee_dict))

# Adding or Modifying the elements from the dictionary
employee_dict["email"] = "karan@gmail.com"

# Modify the age of employee

employee_dict["age"] = 31

print(employee_dict)

# Remove the elements from dictionary
del employee_dict["email"] # Deletes the 'email' key-value pair
print(employee_dict)
employee_dict.pop("role") # Removes and returns the value for 'role'
print(employee_dict)
employee_dict.clear()     # Removes all items from the dictionary
print(employee_dict)

# iterating through the dictionary using the for loop 
# And the methods like .key(), .values(), .items()

grades = {"Ganesh":64, "Shivam": 84, "Atharva": 78}

# Iterate over keys
for name in grades.keys():
    print(name)

# Iterate over the values
for score in grades.values():
    print(score)

# Iterate over both keys and values 


for name, score in grades.items():
    print(f"{name}: {score}")