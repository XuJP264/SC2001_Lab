def merge(left,right):
    l=r=0
    result=[]
    comps=0
    while l<len(left) and r<len(right):
        comps+=1
        if left[l]<right[r]:
            result.append(left[l])
            l+=1
        else:
            result.append(right[r])
            r+=1
    result.extend(left[l:])
    result.extend(right[r:])
    return result,comps
def traditional_insert_sort(arr):
    comps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comps += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return arr, comps
def traditional_merge_sort(arr):
    if len(arr)<=1:
        return arr,0
    else:
        mid=(len(arr)+1)//2
        left,comps1=traditional_merge_sort(arr[:mid])
        right,comps2=traditional_merge_sort(arr[mid:])
        merged,comps3=merge(left,right)
        return merged,comps1+comps2+comps3
def hybrid_merge_sort(arr,S):
    if len(arr)<=S:
        return traditional_insert_sort(arr)
    else:
        mid=(len(arr)+1)//2
        left,comps1=hybrid_merge_sort(arr[:mid],S)
        right,comps2=hybrid_merge_sort(arr[mid:],S)
        merged,comps3=merge(left,right)
        return merged,comps1+comps2+comps3