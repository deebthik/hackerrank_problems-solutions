def highestValuePalindrome(s, n, k):

    sl = [int(x) for x in s]
    c = 0
    changes = [False for _ in range(n)]

    for i in xrange(len(s)/2):
        #if sl == list(reversed(sl)):
            #break

        if sl[i] == sl[len(s)-1-i]:
            pass
        else:
            maxx = max(sl[i], sl[len(s)-1-i])
            sl[i] = maxx
            sl[len(s)-i-1] = maxx
            c += 1
            changes[i] = True

                
    if c > k:
        return "-1"

          
    elif c < k:
        
        for i in xrange(n):
            
            if c >= k:
                break

            if (i == n-1-i):
                if sl[i] != 9:
                    sl[i] = 9
                    c += 1
            else:
                if sl[i] != 9:
                    if changes[i] == True:
                        sl[i], sl[n-1-i] = 9, 9
                        c += 1
                    else: 
                        if k-c >= 2:
                            sl[i], sl[n-1-i] = 9, 9
                            c += 2
                
        return "".join(list(map(str, sl)))
    
    else:
        return "".join(list(map(str, sl)))
