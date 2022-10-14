def twoRobots(m, queries):
    
    r1 = queries[0][0]
    r2 = queries[1][0]
    distance = 0
    
    for i in queries:

        d1 = abs(i[0] - r1) + abs(i[1] - i[0])
        d2 = abs(i[0] - r2) + abs(i[1] - i[0])

        distance += min(d1, d2)
                
        for j in locals().keys():
            if locals()[j] == min(d1, d2):
                min_d_var = j
        
        exec("r" + min_d_var[1] + " = i[1]")              
            
    return distance
                
            
print twoRobots(5, [[1, 5], [3, 2], [4, 1], [2, 4]])

        
    
