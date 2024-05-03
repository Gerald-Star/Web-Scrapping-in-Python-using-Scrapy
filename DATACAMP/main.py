

monthly_savings = 10
num_months = 12
intro = "Hello! How are you?"

# Calculate year_savings using monthly_savings and num_months
year_savings = monthly_savings + num_months

# Print the type of year_savings
print(year_savings)

# Assign sum of intro and intro to doubleintro
doubleintro = intro + intro
print(doubleintro)


  """
  # Definition of savings and total_savings
savings = 100
total_savings = 150

# Fix the printout
print("I started with $" + savings + " and now have $" + total_savings + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float

Similar functions such as int(), float() and bool() 
will help you convert Python values into any type.
  """
  
# Definition of savings and total_savings
savings = 100
total_savings = 150

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(total_savings) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)  

  
# LIST EXERCISE  

  """
  Create a list
As opposed to int, bool etc., a list is a compound data type; 
you can group values together:

a = "is"
b = "nice"
my_list = ["my", "list", a, b]
After measuring the height of your family, you decide to collect 
some information on the house you're living in. 
The areas of the different parts of your house are stored in separate variables for now, as shown in the script.
 
 
 Create a list, areas, that contains the area of the hallway 
 (hall), kitchen (kit), living room (liv), bedroom (bed) and 
 bathroom (bath), in this order. Use the predefined variables.
Print areas with the print() function.
 
  """
  
# Area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]  

  """
  Create list with different types
A list can contain any Python type. Although it's not really common, a list can also contain a mix of Python types
including strings, floats, booleans, etc.
  """

"""
Can you tell which ones of the following lines of Python code are valid ways to build a list?

A. [1, 3, 4, 2] B. [[1, 2, 3], [4, 5, 7]] C. [1 + 2, "a" * 5, 3]

"""  

# EXERCISE

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

# Print out the type of house
print(type(house))


  """

Subsetting Python lists is a piece of cake. Take the code sample below, which creates a list x and then selects "b" from it. Remember that this is the second element, so it has index 1. You can also use negative indexing.

x = ["a", "b", "c", "d"]
x[1]
x[-3] # same result!
  """
  
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])


"""
Subset and calculate
After you've extracted values from a list, you can use them to perform additional calculations. Take this example, where the second and fourth element of a list x are extracted. The strings that result are pasted together using the + operator:


"""  

x = ["a", "b", "c", "d"]
print(x[1] + x[3])


  """
  Using a combination of list subsetting and variable assignment, create a new variable, eat_sleep_area, that contains the sum of the area of the kitchen and the area of the bedroom.
Print the new variable eat_sleep_area.
  """

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[3] + areas[-3]

# Print the variable eat_sleep_area
print(eat_sleep_area)


"""
Slicing and dicing
Selecting single values from a list is just one part of the story. 
It's also possible to slice your list, which means selecting 
multiple elements from your list. Use the following syntax:

my_list[start:end]
The start index will be included, while the end index is not.

The code sample below shows an example. A list with "b" and "c", corresponding to indexes 1 and 2, are selected from a list x:

x = ["a", "b", "c", "d"]
x[1:3]
The elements with index 1 and 2 are included, while the element
with index 3 is not.

"""  
z = ["a", "b", "c", "d"]
print(z[1:3])


  """
  
  Use the brackets [0:6] to build downstairs.
Use the brackets [6:10] to build upstairs.
Simply add two print() calls to the script to print out 
downstairs and upstairs.
  """

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:10]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)


"""
However, it's also possible not to specify these indexes. If you don't specify the begin index, Python figures out that you want to start your slice at the beginning of your list. If you don't specify the end index, the slice will go all the way to the last element of your list. To experiment with this, try the following commands in the IPython Shell:

x = ["a", "b", "c", "d"]
x[:2]
x[2:]
x[:]

"""  

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create downstairs
downstairs = areas[:6]

# Alternative slicing to create upstairs
upstairs = areas[6:]


# SUBNETTING LISTS OF LISTS

  """
  
  Subsetting lists of lists
You saw before that a Python list can contain practically anything; even other lists! To subset lists of lists, you can use the same technique as before: square brackets. Try out the commands in the following code sample in the IPython Shell:

x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
x[2][0]
x[2][:2]
x[2] results in a list, that you can subset again by adding additional square brackets.

What will house[-1][1] return? house, the list of lists that you created before, is already defined for you in the workspace.
You can experiment with it in the IPython Shell.
  """
  
  
# LIST MANIPULATIONS - ADDING AND REMOVING ELEMENTS


# REPLACE LIST ELEMENTS

  """
  Replace list elements
Replacing list elements is pretty easy. Simply subset the list 
and assign new values to the subset. You can select single elements or you can change entire list slices at once.

Use the IPython Shell to experiment with the commands below.
Can you tell what's happening and why?

x = ["a", "b", "c", "d"]
x[1] = "r"
x[2:] = ["s", "t"]
  """

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"

# LIST OF LISTS  


# extend a list using operartor + or extend() method
"""
Extend a list
If you can change elements in a list, you sure want to be able to add elements to it, right? You can use the + operator:
"""
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]

# Create the areas list (updated version)
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]


# deleting elements from a list
"""
Delete list elements
Finally, you can also remove elements from your list. You can do this with the del statement:
"""
x = ["a", "b", "c", "d"]
del(x[1])

areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]


del(areas[-4:-2])


# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)


# FUNCTIONS

# what is a function?



# Function that returns multiple values
# type() function returns the type of the variable
# round() function rounds the number to the nearest integer
# help(round) to get help on round function
# round(1.68, 1) rounds the number to 1 decimal place
# round(1.68) rounds the number to the nearest integer
# max() function returns the maximum value in the list

max = max(1, 2, 3)
print(max)

max2 = [1, 2, 3]

print(max(max2))

print(max2)
# max(1, 2, 3) returns the maximum value in the list
# complex() function returns the complex number
# complex(4, 3) returns the complex number
# complex(4) returns the complex number

# Define shout with the parameter, word
def shout(word):
    """Return a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Return shout_word
    return shout_word
  
# Pass 'congratulations' to shout: yell
yell = shout('congratulations')

# Print yell
print(yell)



# TUPLES

# Tuples are similar to lists but they are immutable

# Create a tuple
even_nums = (2, 4, 6)

# Unpack the tuple into two variables

a, b, c = even_nums

# Access the second element of the tuple

print(even_nums[1])

# Create a list of tuples

avocados = (200, 250, 300)

# Print the second element of the second tuple

print(avocados[1][1])

# Create a dictionary

world = {"afghanistan": 30.55, "albania": 2.77, "algeria": 39.21}

# Print the keys of the dictionary

print(world.keys())

# Print the value of the dictionary

print(world["albania"])

# Print the value of the dictionary


# DICITONARIES

"""
Use the index() method on countries to find the index of 'germany'. Store this index as ind_ger.
Use ind_ger to access the capital of Germany from the capitals list. Print it out.

"""

# Definition of countries and capital - not best method
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])

# Best method to define countries and capitals using key value pairs