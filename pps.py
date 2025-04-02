import numpy as np

def question1():
    # Arrage the elements
    print("arrange the elements")
    a = np.arange(10)
    print(a)

def question2():
    # 1D array, 2D array, ndarray, vector, matrix
    print("1D array, 2D array, ndarray, vector, matrix")
    one_d = np.array([1, 2, 3, 4, 5])
    print("1D array:", one_d)
    two_d = np.array([[1, 2, 3], [4, 5, 6]])
    print("2D array:\n", two_d)
    ndarr = np.arange(10)  
    print("ndarray:", ndarr)
    vector = np.array([10, 20, 30])
    print("Vector:", vector)
    mat = np.matrix([[1, 2], [3, 4]])
    print("Matrix:\n", mat)
    
def question3():
    # Create an initial array
    print("Create an initial array")
    arr = np.array([1, 3, 5, 7, 9])
    print("Original array:", arr)
    arr = np.append(arr, 4)
    print("After appending 4:", arr)
    arr = np.delete(arr, 2)
    print("After removing element at index 2:", arr)
    sorted_arr = np.sort(arr)
    print("Sorted array:", sorted_arr)

def question4():
    # Concatenate
    print("Concatenate")
    a = np.array([1, 2, 3, 4,5])
    b = np.array([5, 6, 7, 8])
    res=np.concatenate((a, b))
    print(res)


def question5():
    # To know the shape and size of the array
    print("To know the shape and size of the array")
    a = np.array([[1, 2], [3, 4]])
    print("Array:\n", a) 
    print("Number of dimensions:", a.ndim)
    print("Size (total number of elements):", a.size)
    print("Shape (array dimensions):", a.shape)

def question6():
    # To know the shape and size of the array
    print("To know the shape and size of the array")
    a = np.array([[1, 2], [3, 4]])
    print(a.ndim) 
    print(a.size)
    print(a.shape)

def question7():
    # Convert a 1D array into a 2D array
    print("Convert a 1D array into a 2D array")
    a = np.array([1, 2, 3, 4, 5, 6])
    print("Original 1D array:", a)
    print("Shape of 1D array:", a.shape)

    a_2d_newaxis = a[np.newaxis, :]
    print("2D array using np.newaxis:")
    print(a_2d_newaxis)
    print("Shape of 2D array:", a_2d_newaxis.shape)
    
def question8():
    #Indexing & Slicing
    print("Indexing & Slicing")
    data = np.array([1, 2, 3,4,5,6,7,8])
    print(data[0:])
    print(data[0:2])
    print(data[-3:])

def question9():
    #Create an array from existing data
    print("Create an array from existing data")
    a = np.array([1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
    arr1 = a[3:8]
    print(arr1)
    
def question10():
    #High Dimensional Arrays Multidimensional Array concept can be explained as a technique of defining and storing the data on a format with more than two dimensions (2D).
    print("High Dimensional Arrays")
    phd=[[1,2,3],[2,3,1],[3,2,1]]
    print(phd)
    c = 4
    r = 3
    Array = [ [0] * c for i in range(r) ]
    print(Array)
     
def question11():
    #How to create multi-dimensional arrays using NumPy
    print("How to create multi-dimensional arrays using NumPy")
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(arr)

def question12():
    #How to Access and Modify Multi-dimensional Arrays Using NumPy
    print("How to Access and Modify Multi-dimensional Arrays Using NumPy")
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(arr[1, 2]) 
    arr[0, 3] = 20
    print(arr)

def question13():
    #How to Perform Operations on Multi-dimensional Arrays NumPy provides a wide range of mathematical and statistical functions that you can use to perform operations on multi-dimensional arrays efficiently.
    print("How to Perform Operations on Multi-dimensional Arrays")
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print("sum- ",np.sum(arr))  
    print("Mean- ",np.mean(arr, axis=1)) 
    b = np.array([[2, 3], [4, 5], [6, 7], [8, 9]])
    print("Product of Two matrices", np.dot(arr, b)) 

# 5. Calculate the sum of two numbers entered by the user.
def sum_two_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    total = a + b
    print("The sum is:", total)

# 6. Find the largest among three numbers entered by the user.
def largest_of_three():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))
    largest = max(a, b, c)
    print("The largest number is:", largest)

# 7. Print all even numbers from 1 to 20.
def print_evens_1_to_20():
    print("Even numbers from 1 to 20:")
    for num in range(1, 21):
        if num % 2 == 0:
            print(num, end=" ")
    print()  # for a newline

# 8. Calculate the sum of all numbers from 1 to a given number.
def sum_numbers_to_n():
    n = int(input("Enter a number: "))
    total = sum(range(1, n + 1))
    print("The sum of numbers from 1 to", n, "is:", total)

# 9. Check if a given string is a palindrome.
def check_palindrome():
    s = input("Enter a string: ")
    # Normalize the string: remove spaces and convert to lowercase.
    s_clean = s.replace(" ", "").lower()
    if s_clean == s_clean[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

# 10. Count the number of vowels in a given string.
def count_vowels():
    s = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    print("The number of vowels in the string is:", count)

# 11. Find the square root of a number.
import math
def find_sqrt():
    num = float(input("Enter a number: "))
    if num < 0:
        print("Square root of a negative number is not defined in real numbers.")
    else:
        sqrt_val = math.sqrt(num)
        print("The square root of", num, "is:", sqrt_val)

# 12. Calculate the area of a triangle.
def area_of_triangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print("The area of the triangle is:", area)

# 13. Convert Fahrenheit to Celsius.
def fahrenheit_to_celsius():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit} Fahrenheit is {celsius:.2f} Celsius")

# 14. Check if a number is positive, negative, or zero.
def check_sign():
    num = float(input("Enter a number: "))
    if num > 0:
        print("The number is positive.")
    elif num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

# 15. Determine if a number is odd or even.
def odd_or_even():
    num = int(input("Enter an integer: "))
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

# Example usage:

question1()
question2()
question3()
question4()
question5()
question6()
question7()
question8()
question9()
question10()
question11()
question12()
question13()
sum_two_numbers()
largest_of_three()
print_evens_1_to_20()
sum_numbers_to_n()
check_palindrome()
count_vowels()
find_sqrt()
area_of_triangle()
fahrenheit_to_celsius()
check_sign()
odd_or_even()