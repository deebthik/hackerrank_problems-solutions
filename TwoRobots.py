def twoRobots(m, queries):
    
    r1 = queries[0][0]
    r2 = queries[1][0]
    distances = []
    
    for i in queries:
        
        if (i == queries[0]):
            d1 = abs(i[1] - r1)
            r1 = i[1]
            distances += [d1]
        
        elif (i == queries[1]):
            d2 = abs(i[1] - r2)
            r2 = i[1]
            distances += [d2]
            
        else:

            d1 = abs(i[0] - r1) + abs(i[1] - i[0])
            d2 = abs(i[0] - r2) + abs(i[1] - i[0])
            
            if (d1 <= d2):
                r1 = i[1]
            else:
                r2 = i[1]
                
            distances += [min(d1, d2)]
            
    return sum(distances)

print twoRobots(5, [[1, 5], [3, 2], [4, 1], [2, 4]])

        
    
