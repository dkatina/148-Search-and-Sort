from merge import merge



def merge_sort(arr):

    if len(arr) > 1: #recursive case (needs to be split more)
        mid = len(arr) // 2 #gives me the middle index
        left_half = arr[0:mid] #left is a slice from beginning to middle
        right_half = arr[mid:] #right is a slice from middle to end
        print("SPLITTING", arr)
        print("LEFT_HALF", left_half)
        print("RIGHT_HALF", right_half)

        merge_sort(left_half)
        merge_sort(right_half)

        #lists of one len
        print("MERGING:", left_half, right_half)
        merge(arr, left_half, right_half)
    else:
        print("BASE CASE", arr)
    


# alist = [89,12,65,37,100,101,1]

# merge_sort(alist)

# print(alist)

playlist = [
    {"title": "aNNIE", "duration": 180, "upload_date": "2022-01-01"},
    {"title": "Balfonzo Fandoura", "duration": 240, "upload_date": "2021-12-15"},
    {"title": "Calbert the Einstein", "duration": 200, "upload_date": "2022-01-10"},
]


merge_sort(playlist)

print(playlist)