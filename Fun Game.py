
def funGame(a, b):

    a_points = 0
    b_points = 0

    n = len(a)
    summ = list(map(lambda x,y:x+y, a, b))
    indices = [x[0] for x in sorted(enumerate(summ), key=lambda x: -x[1])]

    for i in range(n):
        if i%2 == 0:
            a_points += a[indices[i]]
        else:
            b_points += b[indices[i]]

    if a_points > b_points:
        return "First"
    elif a_points < b_points:
        return "Second"
    else:
        return "Tie"

print funGame([20, 2, 0], [1, 1000, 1000])
    

