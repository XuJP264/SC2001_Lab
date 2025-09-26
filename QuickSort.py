import random
def partition(A,l,r):
    mid=(l+r)//2
    pivot=A[mid]
    A[mid],A[r]=A[r],A[mid]
    i=l-1
    for j in range(l,r):
        if A[j] < pivot:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quickSort(A,low=0,high=None):
    if high==None:
        high=len(A)-1
    if low<high:
        pivot=partition(A,low,high)
        quickSort(A,low,pivot-1)
        quickSort(A,pivot+1,high)
    return A

A=[random.randint(0,10000) for _ in range(100)]
print(A)
A=quickSort(A)
print(A)