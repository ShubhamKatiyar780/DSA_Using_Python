# Define a function to perform insertion sort on a list
def insertion_sort(data_list):
    # Get the length of the list
    n = len(data_list)
    
    # Start iterating from the second element (index 1) to the end of the list
    for i in range(1, n):
        # Store the current element in a temporary variable
        temp = data_list[i] 
        
        # Initialize a variable to track the previous index
        j = i - 1
        
        # Move elements of the list that are greater than the current element
        # to one position ahead of their current position
        while j >= 0 and temp < data_list[j]:
            data_list[j + 1] = data_list[j]
            j -= 1
        
        # Place the current element in its correct position
        data_list[j + 1] = temp

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
insertion_sort(arr)

# Print the sorted array
print("Sorted array is:", arr)