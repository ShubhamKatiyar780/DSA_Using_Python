# Define the bubble sort function
def bubble_sort(data_list):
    # Outer loop: Iterate through the list from the first element to the last
    # Each iteration of this loop places the next largest element in its correct position
    for i in range(1, len(data_list)):
        # Inner loop: Iterate through the unsorted portion of the list
        # The unsorted portion reduces by 1 after each pass because the largest element "bubbles up" to its correct position
        for j in range(len(data_list) - i):
            # Compare adjacent elements
            if data_list[j] > data_list[j + 1]:
                # Swap the elements if they are in the wrong order
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]

# Take input from the user as a string of numbers separated by spaces
input_str = input("Enter numbers separated by spaces: ")

# Convert the input string into a list of integers
# 1. `input_str.split()` splits the string into a list of substrings (e.g., "5 1 4" -> ["5", "1", "4"])
# 2. `map(int, ...)` converts each substring to an integer
# 3. `list(...)` converts the map object to a list
arr = list(map(int, input_str.split()))

# Print the original array
print("Original array:", arr)

# Call the bubble sort function to sort the array
bubble_sort(arr)

# Print the sorted array
print("Sorted array is:", arr)