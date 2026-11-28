import numpy as np

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

# Element-wise operations
print("\n--- Element-wise Operations ---")
print("Addition (a + b):", a + b)
print("Subtraction (ab):", a - b)
print("Multiplication (a * b):", a * b) # Element-wise, NOT matrix multiplication
print("Division (a / b):", a / b)
print("Power (a ** 2):", a ** 2)
print("Square root:", np.sqrt(a))



# Scalar operations (broadcasting)
print("\n--- Scalar Operations ---")
print("a + 10:", a + 10 )
print("a * 2:", a * 2)
print("a ** 3:", a ** 3)
# Comparison operations
print("\n--- Comparison Operations ---")
print("a > 2 ([1,2,3,4]):", a > 2 )
print("a == 3 ([1,2,3,4]):", a == 3)
print("a <= 2 ([1,2,3,4]):", a <= 2 )