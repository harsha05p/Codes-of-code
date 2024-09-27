def minimumSumArray(n,arr):
    arr.sort()
    a,b=arr[-1],arr[-2]
    avg=(a+b)/2
    for i in range(n):
        if arr[i]
