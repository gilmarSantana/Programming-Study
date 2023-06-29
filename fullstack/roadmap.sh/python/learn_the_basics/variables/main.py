# in python variables are created when you assign a values to it
# Variables are containers for storing data values

x = 5
y = "Hello, world"
nome = "Gilmar"
print(x, y, nome)
print(type(x))

# examples of legal variables names
myvar= ""
my_var= ""
_my_var= ""
myvar= ""
MYVAR= ""
myvar2= ""

#example of illegal variable names
##2myvar = ""
##my-var = ""
##my var = ""

#The variable name are case-sensitive

# ASSING MANY VALUES TO MULTIPLE VARIABLES
x, y, z =  "banana", "apple", "pineapple"
print(x, y, z)


# GLOBAL VARIABLES

xx = "awesome"
def myfunc():
    xx = "boring"
    print(xx)
myfunc()

#global keyword
global xc
xc = 'moto'



