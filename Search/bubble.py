def bubbleSort(my_list):
    for i in range(len(my_list)-1):
        for j in range(len(my_list)-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+ 1] = my_list[j+1], my_list[j]
    print(my_list)


the_list = [2,1,7,6,5,3,4,9,8]
bubbleSort(the_list)
