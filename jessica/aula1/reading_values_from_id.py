import ctypes
a = 5
address = id(a)
print(a)
print(address)

print(ctypes.cast(address, ctypes.py_object).value)
