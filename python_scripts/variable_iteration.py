"""not recommended, use dict instead, just here for the memo"""
i = 0
while i < 10:
    exec("var{0}=i+10".format(i))
    print(eval("var{0}".format(i)))
    i += 1
