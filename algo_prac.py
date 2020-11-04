# !/usr/bin/python3
import re

with open('address copy.txt', 'r') as file:
    data = file.read()

file.close()
adds = []


def gather_data(my_data, file_data):
    regex = '.+\n*.+\n*.*\n?.*'
    my_data.append(re.findall(regex, data))


def check_entry(my_list):
    ind_str = ''
    ind_entry = []
    check_list = []
    for i in range(len(my_list)):
        ind_entry = my_list[i]
        # ind_str = ''.join(map(str,ind_entry))
        # ind_str.split('\n')
        print(ind_entry[2])
        # print('\n')
        # for j in range(ind_str.count('\n')):

        # print('---3--- ')
        # print(ind_str[i])
        # elif ind_str.count('\n') == 2:
        # print('4')


def eval_list(my_list):
    ind_str = ''
    new_list = []
    addy = False
    name_stuff = False
    town_stuff = False
    for i in range(len(my_list)):  # num of entries
        ind_str = ''.join(map(str, my_list[i]))  # make indiv entry into one str
        new_list = ind_str.split('\n')  # split into indiv lines
        # to eval one at a time
        for j in range(len(new_list)):  # iterate num of times there are
            regex = '[^\s|0-9]{1,}\s[^\s0-9]{1,}'
            if re.match(regex, new_list[0]):
                name_stuff = False
            else:
                name_stuff = True
            regex = '\d*\s[A-Z]{1,}.*'
            if  re.match(regex, new_list[-2]) or re.match(regex,new_list[-3]):
                addy = False
            else:
                addy = True
            regex = '\D*\s[A-Z]{2,}\s\d{5}.*'
            if  re.match(regex, new_list[-1]) or re.match(regex, new_list[-2]):
                town_stuff = False
            else:
                town_stuff = True
        if addy is False and name_stuff is False and town_stuff is False:
            print(i+1, ' Correct')
        elif name_stuff is True:
            print(i+1, '- Name is written wrong')
        elif addy is True:
            print(i+1, '- Address is incorrect')
        elif town_stuff is True:
            print(i+1, '- Town/zip/state is written wrong')


#        print('ok then')
#        print(j)
#        print(i)


gather_data(adds, data)
adds = adds[0]
eval_list(adds)
