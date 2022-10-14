def isValid(s):

    distinct_chars = "".join(set(s))
    counting = []

    for i in distinct_chars:
        counting += [s.count(i)]

    if counting.count(1) > 1:
        return "NO"
    
    counting_distinct = list(set(counting))
    maxx = max(counting_distinct)
    minn = min(counting_distinct)
    print counting_distinct

    if len(counting_distinct) > 2 or (maxx-minn > 1 and minn != 1):
        return "NO"
    elif minn == 1:
        return "YES"
    else:
        return "YES"

print isValid("blabla")
