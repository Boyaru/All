def unique_in_order(iterable):
    gg = []
    lo = ['f']
    if iterable == str(iterable):
        for i in iterable:
            gg.append(i)
    else:
        gg = iterable


           
    for g in gg: 
        if g!= lo[-1]:
                lo.append(g)   
    del lo[0] 
    print(lo)  
    return lo

unique_in_order([1, 2, 2, 3])