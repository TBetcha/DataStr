
def strStr(haystack, needle):
    end = len(haystack)-1
    beg = 0
    leng = len(needle)-1
    if leng == 0:
        return 0

    while end > beg:
        if haystack[end] == needle[-1]:
            if haystack[(end-leng):end] == needle:
                return end-leng
            elif haystack[beg] == needle[0]:
                if haystack[beg: (beg+leng)] == needle:
                    return beg
            else:
                beg = beg+1
                end = end-1
                print(beg)
                print(end)
        return -1


print(strStr("hello", "ll"))

str = 'tomb'
