def quick_sort(data_list):
    """
    Quick Sort implementation using a recursive approach.
    
    Steps:
    1. Select the first element as the pivot.
    2. Partition the list into:
       - `lesser`: Elements less than or equal to the pivot.
       - `greater`: Elements greater than the pivot.
    3. Recursively apply quick sort to both partitions.
    4. Return the sorted list as `sorted lesser + pivot + sorted greater`.
    """
    
    # Base case: If the list has one or no elements, it's already sorted
    if len(data_list) <= 1:
        return data_list  
    else:
        # Choose the first element as the pivot
        pivot = data_list[0]

        # Partition: Create two lists, one for elements <= pivot and another for elements > pivot
        lesser = [i for i in data_list[1:] if i <= pivot]  # Elements smaller than or equal to pivot
        greater = [i for i in data_list[1:] if i > pivot]   # Elements greater than pivot

        # Recursively sort the `lesser` and `greater` lists and concatenate
        sorted_list = quick_sort(lesser) + [pivot] + quick_sort(greater)

        return sorted_list


# Prompt the user to enter numbers as a space-separated string
input_str = input("Enter numbers separated by spaces: ")

# Convert the input string into a list of integers
# 1. `split()` splits the string into a list of substrings (e.g., "5 1 4" -> ["5", "1", "4"])
# 2. `map(int, ...)` converts each substring to an integer
# 3. `list(...)` converts the map object to a list of integers
arr = list(map(int, input_str.split()))

# Print the original unsorted array
print("Original array:", arr)

# Call the Quick Sort function to sort the array and print the result
print("Sorted array:", quick_sort(arr))
