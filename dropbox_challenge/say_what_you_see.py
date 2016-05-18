def  say_what_you_see( input_strings):
    mylist = []
    for st in input_strings:
        s = ''
        num = st[0]
        count = 1
        for i in st[1:]:
            if i == num:
                count += 1
            else:
                s = s + str(count) + num
                num = i
                count = 1
        s = s + str(count) + num
        mylist.append(s)

    return mylist


res = say_what_you_see(["12","32"])
res2 = say_what_you_see(["1232232", "1122112233443"])
res3 = say_what_you_see(res + res2)
res4 = say_what_you_see(res3)
print res
print res2
print res3
print res4
