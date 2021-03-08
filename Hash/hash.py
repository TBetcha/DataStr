
my_str = "abB"

str_one = 'pooling'
str_two= 'looping'


def is_dup(the_str):
    for i in range(len(the_str)):
        for j in range(i+1, len(the_str)):
            if the_str[j] == the_str[i]:
                print(i, j, " are equal")
                return False
    print("no letters are equal")
    return True


def check_dup(the_str):
    letters = {}
    for i in range(len(the_str)):
        if ord(the_str[i]) in letters.values():
            print("already exists")
            return False
        else:
            letters[i] = ord(the_str[i])
    print("all are unique")
    return True



def is_perm(str_one, str_two):
    first = []
    second = []
    if len(str_one) != len(str_two):
        print("false")
        return False
    for i in range(len(str_one)):
        first.append(ord(str_one[i]))
    for j in range(len(str_two)):
        second.append(ord(str_two[j]))
    first.sort()
    second.sort()
    for l in range(len(str_two)):
        if first[l] != second[l]:
            print('not perm')
            return False
    print("is perm")
    return True

    

def better_perm(str_one, str_two):
    if sorted(str_one) == sorted(str_two):
        print("are perm")
        return True
    else:
        print("not perm")
        return False



def one_away(first, second):
    size = max(len(first), len(second))
    if len(first) >= len(second):
        big = first
        not_big = second
    else:
        big = second
        not_big = first
    if len(big) - len(not_big) > 1:
        print("never work too many diff")
        return False
    arr = [0] * size
    for i in range(len(big)):
       arr[i] = ord(big[i])
    for i in range(len(not_big)):
        if ord(not_big[i]) in arr:
            arr.remove(ord(not_big[i]))
    print(len(arr))
    if len(arr) > 1:
        print('more than two chars need to be changed')
        print("wont work")
        return False
    else:
        print("less than two chars need to be changed")
        print('will work')
        return True


one_away('orange', 'grean')

#is_perm(str_one, str_two)

#better_perm(str_one, str_two)

