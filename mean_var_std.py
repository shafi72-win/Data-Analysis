# Author: Shafin khan
# Occupation : Student @ UBC vancouver

# Q-

#Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

#The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.

#The returned dictionary should follow this format:

#{
  #'mean': [axis1, axis2, flattened],
  #'variance': [axis1, axis2, flattened],
  #'standard deviation': [axis1, axis2, flattened],
  #'max': [axis1, axis2, flattened],
  #'min': [axis1, axis2, flattened],
  #'sum': [axis1, axis2, flattened]
#}
#If a list containing less than 9 elements is passed into the function, it should raise a ValueError exception with the message: "List must contain nine numbers." The values in the returned dictionary should be lists and not Numpy arrays.

#For example, calculate([0,1,2,3,4,5,6,7,8]) should return:

#{
  #'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  #'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  #'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  #'max': [[6, 7, 8], [2, 5, 8], 8],
  #'min': [[0, 1, 2], [0, 3, 6], 0],
  #'sum': [[9, 12, 15], [3, 12, 21], 36]
#}

from ast import Break
import numpy as np
import array as arr

b = []
i = 1
x = ''
r = 0

print("please enter 9 value, and to end the program type 'end' when asked to continue ot else type 'yes'")

while x  != "end":

    c = int(input('input value'))
    b.append(c)
    x = input("Do you want to continue?") 
    r = r +1

def calculate(b):


    p = np.array(b)
    l = np.reshape(b,(3,3))

    print("mean:",np.mean(l,axis=0),np.mean(l,axis=1),np.mean(l))
    print("variance:",np.var(l,axis=0),np.var(l,axis=1),np.var(l))
    print("standard deviation",np.std(l,axis=0),np.std(l,axis=1),np.std(l))

    print("max:",np.max(l,axis=0),np.max(l,axis=1),np.max(l))
    print("min:",np.min(l,axis=0),np.min(l,axis=1),np.min(l))
    print("sum:",np.sum(l,axis=0),np.sum(l,axis=1),np.sum(l))

if (r != 9):
    print( "List must contain nine numbers.")
    Break
else:
    calculate(b)
    
