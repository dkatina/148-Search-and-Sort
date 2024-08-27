
def binary_search(arr, target):
    high = len(arr) - 1 #sstarting our high pointer at the last index of the list
    low = 0 #low pointer starts at first index 0

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid #return the index we found it at
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        
    return -1


alist = [2,1,5,4,7]

alist.sort(reverse=True)
print(alist)



        