def timeInWords(h, m):

    o_clock = "o' clock"
    ones_teens = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    teens_hundred = ["twenty", "thirty", "forty", "fifty"]
    intervals = ["quarter", "half"]

    time = ""

    if m == 0:
        time += ones_teens[h-1] + " " + o_clock

    elif m == 30:
        time += intervals[1] + " past " + ones_teens[h-1]

    elif m < 30:
        if m == 15:
            time += intervals[0] + " past " + ones_teens[h-1]
        else:
            if m == 1:
                time += ones_teens[m-1] + " minute past " + ones_teens[h-1]
            elif m < 20:
                time += ones_teens[m-1] + " minutes past " + ones_teens[h-1]
            else:
                time += teens_hundred[[int(x) for x in str(m)][0]-2] + " " + ones_teens[[int(x) for x in str(m)][1]-1] + " minutes past " + ones_teens[h-1]

    else:
        if m == 45:
            time += intervals[0] + " to " + ones_teens[h if h != 12 else 0]
                
        else:
            m = 60-m
            if m < 20:
                    time += ones_teens[m-1] + " minutes to " + ones_teens[h if h != 12 else 0]
            else:
                    time += teens_hundred[[int(x) for x in str(m)][0]-2] + " " + ones_teens[[int(x) for x in str(m)][1]-1] + " minutes to " + ones_teens[h if h != 12 else 0]


    return time.strip()

print timeInWords(1, 1)
