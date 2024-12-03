#pip install numpy

# Note: Rank = Axes = Dimension

import numpy as np

testArray = np.array([[1,2,3], [4,5,6]])
print("Array: ", testArray)
print("Array type: ", type(testArray))
print("Array dimention: ", testArray.ndim)
print("Array size: ", testArray.size)
print("Array shape: ", testArray.shape)
print("Array elements type: ", testArray.dtype)

testFloatArray = np.array([[1, 2, 3], [4,5,6]], dtype=float)
print("Array: ", testFloatArray)
print("New array elements type: ", testFloatArray.dtype)