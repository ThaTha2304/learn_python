'''
    Pengenalan Numpy
'''

import numpy as np

# Perbedaan List dengan Numpy
list_a = [1,2,3,4]
vector_a = np.array([1,2,3,4])

print(f"list_a: {list_a}") # [1, 2, 3, 4]
print(f"vector_a: {vector_a}") # [1 2 3 4] --> berbentuk vector
# print(f"list_a: {list_a**2}") # List gabisa dilakukan operasi aritmatika
print(f"vector_a^2: {vector_a**2}") # [ 1  4  9 16]
print(f"vector_a*6: {vector_a*6}") # [ 6 12 18 24]

# Buat Matrix
matrix_b = np.array([(1,2),(3,4)])
print(f"matrix_b: \n{matrix_b}") 
# [[1 2]
#  [3 4]]
print(f"matrix_b^2: \n{matrix_b**2}") 
# [[1 4]
#  [9 16]]

# Matrix dengan elemen 0
zeros_c = np.zeros((2,2))
print(f"zeros_c: \n{zeros_c}") 
# [[0. 0.]
#  [0. 0.]]

# Matrix dengan elemen 1
ones_d = np.ones((2,2))
print(f"ones_d: \n{ones_d}") 
# [[1. 1.]
#  [1. 1.]]

# Operasi Aritmatika matrix
jumlah = matrix_b + ones_d - matrix_b**4
print(f"\n{matrix_b} \n\t+ \n{ones_d} \n\t- \n{matrix_b**4} \n\t= \n{jumlah}")