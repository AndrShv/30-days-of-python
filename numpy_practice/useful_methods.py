import numpy as np

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

# Sorting
print("Original array:", arr)
print("\n--- Sorting--")
print("Sorted array:", np.sort(arr))

# Returns sorted copy
print("Original unchanged:", arr)
arr.sort() # In-place sort
print("After in-place sort:", arr)



# Unique elements
arr_with_duplicates = np.array([1, 2, 2, 3, 3, 3, 4])
print("\n--- Unique Elements ---")
print("Array:", arr_with_duplicates)
print("Unique values:", np.unique(arr_with_duplicates))


# Searching
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("\n--- Searching ---")
print("Array:", arr)
print("Where is value > 5?", np.where(arr > 5))
print("Values where condition is True:", arr[np.where(arr > 5)])


# Stacking Arrays

a1 = np.array([1, 2, 3])
b1 = np.array([4, 5, 6])
print("\n--- Stacking---")
print(f"Stack vertically: \n {np.vstack((a1, b1))}")
print(f"Stack horizontally: \n {np.hstack((a1, b1))}")
print(f"Stack as columns: \n {np.column_stack((a1, b1))}")