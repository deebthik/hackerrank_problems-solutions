def superReducedString(s):
    s_l = [x for x in s]
    i = 0
    while i < len(s_l)-1:
        print (i)
        print (s_l)
        if s_l[i] == s_l[i+1]:
            s_l.pop(i)
            s_l.pop(i)
            i = 0
            continue
        i += 1
    if "".join(s_l) == "":
        return "Empty String"
    else:
        return "".join(s_l)

superReducedString("aabccddd")
