N,K = map(int,input().split())
array_A = list(map(int,input().split()))
array_B = list(map(int,input().split()))

def ascending_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return ascending_sort(left_side) + [pivot] + ascending_sort(right_side)


def descending_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x > pivot]
    right_side = [x for x in tail if x <= pivot]
    
    return descending_sort(left_side) + [pivot] + descending_sort(right_side)

sorting_A = ascending_sort(array_A)
sorting_B = descending_sort(array_B)

for i in range(K):
    if sorting_A[i] < sorting_B[i]:
        sorting_A[i], sorting_B[i] = sorting_B[i], sorting_A[i]
    else:
        break
    
print(sum(sorting_A))