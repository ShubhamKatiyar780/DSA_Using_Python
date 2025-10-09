def merge_sort(data_list):
    if len(data_list) > 1:
        mid_index = len(data_list) // 2
        left_list = data_list[ : mid_index]
        right_list = data_list[mid_index : ]
        merge_sort(left_list)
        merge_sort(right_list)
        i = j = k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                data_list[k] = left_list[i]
                i += 1
            else:
                data_list[k] = right_list[j]
                j += 1
            k += 1
        while i < len(left_list):
            data_list[k] = left_list[i]
            i += 1
            k += 1
        while j < len(right_list):
            data_list[k] = right_list[j]
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
