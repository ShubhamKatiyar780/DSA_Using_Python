def insertion_sort(data_list):
    n = len(data_list)
    for i in range(1, n):
        temp = data_list[i]
        j = i - 1
        while j >= 0 and temp < data_list[j]:
            data_list[j + 1] = data_list[j]
            j -= 1
        data_list[j + 1] = temp
arr = [50,20,60,0,2,100,0]
print(arr)
insertion_sort(arr)
print(arr)
