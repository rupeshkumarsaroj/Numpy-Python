# Write a python program to create  3*3 mtrix with values ranging from 0 to 8.
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)



# Question 2. Write a python progrm to create a 2d array wth one on the border and 0 inside.
print("Question 2.")
arr2=np.array([[4,5,6],[7,8,9]])
print(arr2)

# Question 3. Write a python program to replace all odd numbers in the given array with -1.
arr3=np.array([1,2,3,4,5,6,7,8])
for i in range(0,7):
    if arr3[i]%2==1:
        arr3[i]=-1
print(arr3)

# Question 4. Write a python program to convert 1d arrays into 2d array 3 rows.
arr4=np.array([1,2,3,4,5,6,7,8,9])
arr5=arr4.reshape(3,3)
print(arr5)

# Question 5. Write a pthon program tht multiply to 3*3 matrices using numpy's dot() function

a1=np.array([[1,2,3],[4,5,6],[7,8,9]])
a2=np.array([[1,2,3],[4,5,6],[7,8,9]])
a3=np.dot(a1,a2)
print(a3)

# Question 6 Write a python program to create a numpy array from 1 to 20 and sle the array to print the first five  element and last five elements and elements are even indices.

arrr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(arrr[0:5])
print(arrr[20:14:-1])
print(arrr[0:20:2])

# Question 7. creteatwo numpy arrays and perform -+*/
a=np.array([1,2,3])
b=np.array([4,5,6])
add=np.add(a,b)
print(add)
subtract=np.subtract(a,b)
print(subtract)
multiply=np.multiply(a,b)
print(multiply)
divide=np.divide(a,b)
print(divide)


# Question 8. 
data=np.array([10,15,7,22,17])
print("Mean ",np.mean(data))
print("Standard Deviation ",np.std(data))
print("Median ",np.median(data))
print("Sum ",np.sum(data))








