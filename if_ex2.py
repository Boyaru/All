

def proverka(Loh, sasi):
    if Loh == str(Loh) and sasi == str(sasi):
        if Loh == sasi:
            return 1
  
        elif Loh > sasi:
            return 2

        elif Loh != sasi and sasi == 'learn':
            return 3
    
    else:
        return 0
    
proverka('gg', 'log')