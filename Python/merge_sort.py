def mergesort(arr):
    if(len(arr) > 1):
        middle = len(arr)//2
        arr1 = arr[:middle]
        arr2 = arr[middle:]
        mergesort(arr1)
        mergesort(arr2)

        i = 0
        j = 0
        k = 0
        while(i < len(arr1) and j < len(arr2)):
            if arr1[i] < arr2[j]:
                arr[k] = arr1[i]
                i += 1
            else:
                arr[k] = arr2[j]
                j += 1
            k+=1
        while(i < len(arr1)):
            arr[k] = arr1[i]
            i += 1
            k += 1
        while(j < len(arr2)):
            arr[k] = arr2[j]
            j += 1
            k += 1

n = int(input())
arr = [None]*n

for i in range(n):
    arr[i] = int(input())

print(arr)
mergesort(arr)
print(arr)

