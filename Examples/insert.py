'''

Insertion Sort
The Insertion Sort algorithm uses one part of the array to hold the sorted values, 
and the other part of the array to hold values that are not sorted yet.


'''


arr = [64, 34, 25, 12, 22, 11, 90, 5]

min_val = 0

for i in range(len(arr)-1):

    if arr[min_val] > arr[i]:
        arr[min_val], arr[i] = arr[i], arr[min_val]

    else:
        print(arr)
        pass
    
