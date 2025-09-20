def quick_sort(data_list):
    # Inner recursive function to perform Quick Sort
    def recursive_quick_sort(data_list, left, right):
        # Base case: If left index is greater or equal to right, return (array is already sorted)
        if left >= right:
            return
        
        # Select the pivot as the last element
        pivot = data_list[right]
        partition_index = left  # Index where elements smaller than pivot will be placed

        # Iterate through the array (excluding pivot at the last index)
        for i in range(left, right):
            if data_list[i] <= pivot:  # If element is smaller than or equal to pivot
                # Swap it with the element at partition_index
                data_list[i], data_list[partition_index] = data_list[partition_index], data_list[i]
                partition_index += 1  # Move partition_index forward

        # Swap pivot with the element at partition_index to place pivot at correct position
        data_list[partition_index], data_list[right] = data_list[right], data_list[partition_index]

        # Recursively apply quick sort to left and right partitions
        recursive_quick_sort(data_list, left, partition_index - 1)  # Sort left partition
        recursive_quick_sort(data_list, partition_index + 1, right)  # Sort right partition

    # Start Quick Sort on the entire list
    recursive_quick_sort(data_list, 0, len(data_list) - 1)


# Prompt the user to enter numbers as a space-separated string
input_str = input("Enter numbers separated by spaces: ")

# Convert the input string into a list of integers
# 1. `split()` splits the string into a list of substrings (e.g., "5 1 4" -> ["5", "1", "4"])
# 2. `map(int, ...)` converts each substring to an integer
# 3. `list(...)` converts the map object to a list of integers
arr = list(map(int, input_str.split()))

# Print the original unsorted array
print("Original array:", arr)

# Call the Quick Sort function to sort the array
quick_sort(arr)

# Print the sorted array
print("Sorted array:", arr)
