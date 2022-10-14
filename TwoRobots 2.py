r1, r2 = 0, 0

def twoRobots(m, queries):
    global r1, r2

    if len(queries) != 0:
    
        if (r1 == 0):
            r1 = queries[0][0]
            d = abs(queries[0][1] - r1)
            r1 = queries[0][1]
            #print d
            return d + twoRobots(m, queries[1::])

        elif (r2 == 0):
            r2 = queries[0][0]
            d = abs(queries[0][1] - r2)
            r2 = queries[0][1]
            #print d
            return d + twoRobots(m, queries[1::])

        else:

            d1 = abs(queries[0][0] - r1) + abs(queries[0][1] - queries[0][0])
            d2 = abs(queries[0][0] - r2) + abs(queries[0][1] - queries[0][0])

            if (d1 <= d2):
                r1 = queries[0][1]
                #print d1
                return d1 + twoRobots(m, queries[1::])
            else:
                r2 = queries[0][1]
                #print d2
                return d2 + twoRobots(m, queries[1::])
        
    else:
        return 0
    
            
            
print twoRobots(5, [[1, 5], [3, 2], [4, 1], [2, 4]])

        
    
