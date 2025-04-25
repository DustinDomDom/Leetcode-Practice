'''
Bubble Sort
Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value.

'''

arr = [9,8,7,5,4,3,2,4,2,8,5,3,7]




for j in range(len(arr)):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    
            

