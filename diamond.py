def diamond(size=6):
    
    items=["#", "/", "*"]
    
    space=" "

    rows=[]

    n = int(size)
    nspace = n-1
    nPounds=1
    
    ii=0
    for i in range(n):
        front = ""
        front += space*nspace
        
        front += items[ii]*nPounds
        
        rows.append(front)
            
        nPounds += 2
        nspace -= 1
        ii += 1
        ii = ii % len(items)

    for r in range(len(rows)-2,-1,-1):
        rows.append(rows[r])
    
    return rows

dArr=[]

dArr.append(diamond(10))
    
for d in dArr:
    for dd in d:
        print(dd)
