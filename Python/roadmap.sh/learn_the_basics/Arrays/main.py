# An array is a special variable, which can hold more than one value at a time

# An array is a special variable, which can hold more than one value at a time###### create an aray containing car names
cars = ['Ford Fiesta', 'Ford Ka', 'Fusca', 'Brasília', 'Celta', 'Palio']

# Access the elements of an array
x = cars[0] # will display: Ford Fiesta

# Modify the valu of the first array item
cars[5] = 'Palio Weekend' # now will display Palio Weekend

# The length of an array
x = len(cars) # will display 6


# Looping array elements
# you can use the for in loop to loop through all the elementes of an array
for x in cars:
    print(x)

# Adding array elements
# you can use the append() method to add an element to an array
cars.append("Honda Civic")
print(cars)

# Removing array elements
# you can use the pop() method to remove an element from the array
cars.pop(1)
print(cars)
# you can also use the remove() method to remove an element from the array
cars.remove("Brasília")
print(cars)


# ARRAY METHODS #
nomes  = ['Marcos','Lucas', 'Pedro', 'João','Pedro', 'Pedro', 'Paulo', 'Tiago', 'Jonas', 'José', 'Antonio', 'Maria']

nomes.append('Gustavo') # Adds an element at the end of the list
print(nomes)

nomes.copy() # Returns a copy of the list
print(nomes)

print(nomes.count('Pedro')) # Returns the number of elements with the specified value

favorite_color = ['blue', 'red', 'brown', 'black']
nomes.extend(favorite_color) #Add the elements of a list (or any iterable), to the end of the current list
print(nomes)

print(nomes.index('Pedro')) # Returns the index of the first element with the specified value

nomes.insert(1, 'Maria') # Adds an element at the specified position
print(nomes)

nomes.pop(3) #	Removes the element at the specified position
print(nomes)

nomes.remove('Pedro') # Removes the first item with the specified value
print(nomes)

nomes.reverse() # Reverses the order of the list
print(nomes)

nomes.sort() # Sorts the list
print(nomes)

nomes.clear() # Removes all the elements from the list
print(nomes)





