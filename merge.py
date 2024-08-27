

l1 = [1,3,5,7,9]
l2 = [2,4,16,18]

def merged(list1, list2):

    one = 0
    two = 0
    merged = []

    while one < len(list1) and two < len(list2):

        if list1[one] < list2[two]:
            merged.append(list1[one])
            one += 1

        else:
            merged.append(list2[two])
            two += 1

        
    if one == len(list1):
        merged = merged + list2[two:]
    else:
        merged = merged + list1[one:]

    return merged

print(merged(l1,l2))

def merge(arr, left_half, right_half):
    l = 0
    r = 0
    a = 0

    while l < len(left_half) and r < len(right_half): #Will continue to compare until a list is empty

        if left_half[l]["title"].lower() < right_half[r]["title"].lower():
            arr[a] = left_half[l]
            l += 1
            a += 1
        else: 
            arr[a] = right_half[r]
            r += 1
            a += 1

    #once a list is empty I need to add all the elements from the other

    while l < len(left_half):
        arr[a] = left_half[l]
        l += 1
        a += 1

    while r < len(right_half):
        arr[a] = right_half[r]
        r += 1
        a += 1


