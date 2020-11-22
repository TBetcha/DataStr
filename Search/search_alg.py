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

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        key = my_list[i]
        j = i-1
        while j>=0 and key < my_list[j]:
            my_list[j+1]=my_list[j]
            j -= 1
        my_list[j+1] = key
    print(my_list)


the_list = [2,1,7,6,5,3,4,9,8]
#bubbleSort(the_list)
#selection_sort(the_list)
insertion_sort(the_list)
