import numpy as np

# Original 2x2 array
array_2d = np.array([[0, 1], [2, 3]])
print("Original flattened array:")
print(array_2d)

# Flatten the array and find max/min
flattened_array = array_2d.flatten()
max_value = np.max(flattened_array)
min_value = np.min(flattened_array)

print("Maximum value of the above flattened array:", max_value)
print("Minimum value of the above flattened array:", min_value)


