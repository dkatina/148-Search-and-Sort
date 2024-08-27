# Algorithm goes through each element in the collection, comparing the elements 
# to the target until it either finds a match, or reaches the end of the collection. 
# Linear Search have linear time complexity O(n)

def linear_search(alist, target):

    for idx, ele in enumerate(alist):
        if ele == target:
            return idx #returns the position of the target
    
    return "Target not Found"
        

alist = [1,2,3,4,5,6,7]



print(linear_search(alist, 9))

print(alist.index(5))