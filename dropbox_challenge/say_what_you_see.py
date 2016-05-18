def  say_what_you_see( input_strings):
    mylist = []
    for st in input_strings:
        nums = dict()
        for i in st:
            if i in nums:
                nums[i] += 1
            else:
                nums[i] = 1
        s = ''
        for x in st:
            if nums[x] != 'x':
                s = s + str(nums[x])
                s = s + str(x)
                nums[x] = 'x'
        mylist.append(s)

    return mylist


res = say_what_you_see(["12","32"])
res2 = say_what_you_see(["1232232", "1122112233443"])
print res
print res2
