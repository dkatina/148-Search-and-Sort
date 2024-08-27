

def bubble_sort(alist):
    n = len(alist)
    for i in range(n):
        print("Pass", i+1)
        for j in range(0, n-i-1):
            print("comparing", alist[j], alist[j+1])
            if alist[j] > alist[j+1]: 
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist


alist = [1,1243561246,2,5,34,7,3,4657,34,54678]


bubble_sort(alist)

print(alist)