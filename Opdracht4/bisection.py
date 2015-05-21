def findRoot(f,a,b,epsilon) :
    m = (a + b) / 2
    
    if abs(b - a) <= epsilon or f(m) == 0 :
        return m

    if f(a) == 0 :
        return a
    if f(b) == 0 :
        return b

    if (f(a) < 0 and f(m) > 0) or (f(a) > 0 and f(m) < 0) :
        return findRoot(f,a,m,epsilon)
    if (f(m) < 0 and f(b) > 0) or (f(m) > 0 and f(b) < 0) :
        return findRoot(f,m,b,epsilon)
