import numpy

# Follow the tasks below to practice basic Python concepts.
# Write your code in between the dashed lines.
# Don't import additional packages. Numpy suffices.

# Task 1: 
# Instructions:
#Write a function that takes one numeric argument as input. 
#If the number is larger than zero, the function should return 1, otherwise is should return -1.
#The name of the function should be step

# Your code here:
# -----------------------------------------------

def step(number):
    if number > 0:
      return 1
    else:
      return -1

step(5)
step(0)
step(-1)


# -----------------------------------------------


# Task 2:
# Instructions:
#Write a function that takes in two arguments: a numpy array, and an integer (call argument "cutoff" and set default to 0).
#The function should return a numpy array of the same length, with all elements smaller than the cutoff being set to cutoff).
#The name of the function should be ReLu


# Your code here:
# -----------------------------------------------
def ReLu(array, cutoff = 0):
    array_copy = numpy.array(array)             # Convert input to numpy array if it's not already
    array_copy[array_copy < cutoff] = cutoff    # Set elements smaller than cutoff to cutoff
    return array_copy                           # Return modified array

array1 = [-5, -4, 0, 3, 8]

ReLu(array1)

# -----------------------------------------------


# Task 3:
# Instructions:
#Write a function that takes in a two-dimensional numpy array of size (n, p) and a one-dimensional numpy array of size p.
#The function should start by multiplying the two numpy arrays (matrix multiplication).
#Next, apply the ReLu function from above to the resulting matrix and return the result.
#Name the function neural_net_layer

# Your code here:
# -----------------------------------------------

def neural_net_layer(matrix, vector):
    result = numpy.dot(matrix, vector)  # matrix multiplication
    result = ReLu(result) # apply ReLu function
    return result

# test the function
matrix = numpy.array([[4, 2, 3], [7, 9, -2]])
vector = numpy.array([4, 1, 6])
neural_net_layer(matrix, vector)

# ------------------------------------------
