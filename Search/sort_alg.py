import math

def bubbleSort(my_list):
    for i in range(len(my_list)-1):
        for j in range(len(my_list)-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+ 1] = my_list[j+1], my_list[j]
    print(my_list)

# go through pick min put it in next used index (starting at 0)
# increase num of elements sorted
# repeat until no elements left 
def selection_sort(my_list):
    for i in range(len(my_list)):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[min_index] > my_list[j]:
                min_index = j
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    print(my_list)

#divide into two parts 
#take first element from unsorted and find correct position
#repeat
# 2 4 7 3 5
'''
key 4
j = 0
while j >= 0 and 4<2
false 
so 
4 = key
-- 3
key = 3
j=2
3 is less than 7 
so 
3 swap 7
j goes back to comapre again 
stay in while
compare swap stay in.....
'''
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        key = my_list[i]
        j = i-1
        while j>=0 and key < my_list[j]:
            my_list[j+1]=my_list[j]
            j -= 1
        my_list[j+1] = key
    print(my_list)


#bucket sort
# sq root of number items (round if needed)
# item bucket = ceiling(value * number of buckets / max Value)
# sort buckets (any way)
# merge buckets

def bucket_sort(my_list):
    num_buckets = round(math.sqrt(len(my_list)))
    max_value = max(my_list)
    arr = []

    for i in range(num_buckets):
        arr.append([])
    for j in my_list:
        index_b = math.ceil(j*num_buckets/max_value)
        arr[index_b-1].append(j)

    for i in range(num_buckets):
        arr[i] = insertion_sort(arr[i])

    k = 0
    for i in range(num_buckets):
        for j in range(len(arr[i])):
            my_list[k] = arr[i][j]
            k += 1
    return my_list


# extra space needed
def merge_sort(my_list):
    if len(my_list) > 1:
        mid = len(my_list)//2
        left = my_list[:mid]
        right = my_list[mid:]
        merge_sort(left)
        merge_sort(right)

        i=j=k=0

        while i< len(left) and j< len(right):
            if left[i] < right[j]:
                my_list[k] = left[i]
                i+=1
            else:
                my_list[k] = right[j]
                j+=1
            k+=1

        while i< len(left):
            my_list[k] = left[i]
            i+=1
            k+=1

        while j<len(right):
            my_list[k] = right[j]
            j+=1
            k+=1


def print_merged(my_list):
    for i in range(len(my_list)):
        print(my_list[i], end=" ")
    print()


# O(n)
def partition(my_list, low, high):
    i = low - 1
    pivot = my_list[high]
    for j in range(low, high):
        if my_list[j] <= pivot:
            i+=1
            my_list[i], my_list[j] = my_list[j], my_list[i]
    my_list[i+1], my_list[high] = my_list[high], my_list[i+1]
    return(i+1)

# no extra space needed
# O(nLogN) - average
# O(n^2) - worst
def quick_sort(my_list, low, high):
    if low<high:
        pi=partition(my_list, low, high)
        quick_sort(my_list, low, pi-1)
        quick_sort(my_list, pi+1, high)



the_list = [2,1,7,6,5,3,4,9,8]
#bubbleSort(the_list)
#selection_sort(the_list)
insertion_sort(the_list)
#print(bucket_sort(the_list))
#merge_sort(the_list)
#print_merged(the_list)
#quick_sort(the_list, 0, 8)
print(the_list)







