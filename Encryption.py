import math

def encryption(s):

    ss = s.replace(" ", "")
    l = len(ss)
    sr = math.sqrt(l)
    
    lower = int(math.floor(sr))
    upper = int(math.ceil(sr))

    if (lower * upper) < l:
        if (lower < upper):
            lower += 1
        else:
            upper += 1

    matrix = []

    new_string = ""

    for i in range(0, l, upper):
        matrix += [ss[i:i+upper]]

    for i in range(lower):
        if len(matrix[i]) != upper:
            matrix[i] += " " * (upper - len(matrix[i]))

    for i in range(upper):
        for j in range(lower):
            new_string += matrix[j][i]
        new_string = new_string.strip() + " "

    return new_string
        
        

print encryption("chillout")
