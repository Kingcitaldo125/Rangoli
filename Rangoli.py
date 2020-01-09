def rangoli(n):
    rangols=[]
    dash='-'
    chrNum = 96 + n
    chrr = chr(chrNum) # holds the character
    
    # Get the number of columns in rangoli
    cols = (((ord(chrr) - ord('a'))*2)*2)+1
    print("cols",cols)
    
    # Get the number of rows in rangoli
    rows = (((chrNum - 96) - 1) * 2) + 1
    print("rows",rows)
    
    # Get the outer rows
    letts = 1
    nDashes = int((cols - 1) / 2)
    midLetter = chrNum
    for i in range(n):
        side = ""
        # Append one side of dashes
        side += (dash * nDashes)
        
        # Get the letters in the middle area
        lHoldr = chrNum
        for j in range(letts-1):
            side += (chr(lHoldr))
            side += (dash)
            
            lHoldr -= 1
        
        # Assemble the row as a string
        Row = ""
        Row += side
        Row += chr(midLetter)
        midLetter -= 1
        
        # Assemble the other side
        for ss in range(len(side)-1,-1,-1):
            Row += side[ss]
            
        rangols.append(Row)
        nDashes -= 2
        letts += 1
    
    rangoliStr=""
    
    for rr in rangols:
        rangoliStr += rr
        rangoliStr += "\n"
    
    for r in range(len(rangols)-2,-1,-1):
        rangoliStr += rangols[r]
        rangoliStr += "\n"
    
    
    return rangols

alphabetList = [o for o in range(1,27)]

rlst = rangoli(3)
#rlst = rangoli(4)
#rlst = rangoli(5)
#rlst = rangoli(6)

for rr in rlst:
    print(rr)

for rr in range(len(rlst)-2,-1,-1):
    print(rlst[rr])
