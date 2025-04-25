'''

Selection Sort
The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.

'''

arr = [64, 34, 25, 5, 22, 11, 90, 12]





for j in range(0,len(arr)):
    minimum = j

    for i in range(j, len(arr)):
        if arr[minimum] > arr[i]:
            minimum = i
        
    mini_val = arr.pop(minimum)
    insert_val = arr.insert(j,mini_val)



