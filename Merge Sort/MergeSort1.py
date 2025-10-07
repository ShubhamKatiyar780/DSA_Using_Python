def merge_sort(arr):
    """
    Performs merge sort on the given list.
    
    :param arr: List of numbers to be sorted
    """
    # Base case: If the array has 1 or no elements, it is already sorted
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle index of the array

        # Divide the array into two halves
        left_half = arr[:mid]   # Left half from index 0 to mid-1
        right_half = arr[mid:]  # Right half from index mid to end

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves back into arr
        i = j = k = 0  # Initialize pointers for left_half, right_half, and merged array

        # Compare elements of left_half and right_half and merge them in sorted order
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:  # If left element is smaller, add it to arr
                arr[k] = left_half[i]
                i += 1  # Move the left_half pointer forward
            else:  # If right element is smaller, add it to arr
                arr[k] = right_half[j]
                j += 1  # Move the right_half pointer forward
            k += 1  # Move the merged array pointer forward

        # Copy any remaining elements from left_half (if any)
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy any remaining elements from right_half (if any)
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Take input from the user as a string of numbers separated by spaces
input_str = input("Enter numbers separated by spaces: ")

# Convert the input string into a list of integers
# 1. `input_str.split()` splits the string into a list of substrings (e.g., "5 1 4" -> ["5", "1", "4"])
# 2. `map(int, ...)` converts each substring to an integer
# 3. `list(...)` converts the map object to a list
arr = list(map(int, input_str.split()))

# Print the original array
print("Original array:", arr)

# Call the insertion sort function to sort the array
merge_sort(arr)

# Print the sorted array
print("Sorted array is:", arr)
