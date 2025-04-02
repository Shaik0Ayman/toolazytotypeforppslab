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
