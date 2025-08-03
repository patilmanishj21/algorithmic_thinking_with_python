def binarysearch(lst,n):
    low=0
    high=len(lst)-1

    while low <= high:
        mid= (low+high) // 2
        if lst[mid] == n:
            return mid
        elif lst[mid] < n:
            low=mid+1
        else:
            high=mid-1


lst=[11,22,33,44,55,66,77,88,99]
n=0


print(binarysearch(lst,n))

