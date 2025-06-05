import ctypes
import numpy as np
# Load the shared interface library
lib = ctypes.CDLL('./libfortran_interface.so')
# Define the argument and return types for each function
lib.for_alloc.argtypes = [ctypes.c_int]
lib.get_ptr  .argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_int)]
# Allocate the array using the Fortran function
n = 128
lib.for_alloc(128)
# Declare the pointer array and a pointer to the size of the array
ptr = ctypes.c_void_p()
n   = ctypes.c_int()
# Call the fortran interface to get the pointer and the size
lib.get_ptr( ctypes.byref(ptr) , ctypes.byref(n) )
print(n.value)
# Transform the pointer from Fortran into a numpy array of the appropriate size
arr = np.ctypeslib.as_array(ctypes.cast(ptr,ctypes.POINTER(ctypes.c_double*n.value)).contents)
# Set the array to one
arr[:] = 1
# Print the sum of the array from Fortran to demonstrat it's using the same memory
lib.print_sum()
