def my_sqrt(a,n):
    x = a
    for i in range(n):
        x = ((a/x)+x)/2
    return x

def pi_from_polygon(n):
    a = 1
    b = 1
    v = my_sqrt(a**2 - (a / 2)**2, 100)
    s = 6 * b * v / 2
    #b = my_sqrt((a / 2)**2 + (1 - v)**2, 100)
    for i in range(n):
        b = my_sqrt((b / 2)**2 + (1 - v)**2, 100)
        #print(b)
        v = my_sqrt(a**2 - (b / 2)**2, 100)
        #print(v)
    s = 6 * 2**n * b * v / 2
    return s

def pi_from_series(n):
    
    sum = 0
    a = (1 / 2**4)

    for i in range(n):
        if i == 0:
            sum += (a / (2 * (i+1) + 1))
        else:
            a = a * ((2 * (i+1) - 3) / (2 * (i+1))) * (1 / 2**2)
            sum += (a / (2 * (i+1) + 1))
    
    return 12 * (- (my_sqrt(3,1000) / 8) + (1 / 2) - sum)

