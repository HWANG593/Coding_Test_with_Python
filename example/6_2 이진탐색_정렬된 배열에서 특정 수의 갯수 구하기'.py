from bisect import bisect_left, bisect_right
n,m = list(map(int,input().split(' ')))
array = list(map(int,input().split()))

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

answer = count_by_range(array, m, m)

if answer == 0:
    answer = -1