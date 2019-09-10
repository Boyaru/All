
#Факториал.(Пример !5 = 5 х 4 х 3 х 2 х 1)

def factorial(a):
    c = 1
    if a > 1:
        while a > 1:   #порядок елементов в цикле в данном случае очень важен.
            c *= a   
            a -= 1
    else:
        c == a
    print(c)

factorial(6)

def factoriala(n):
    fact = 1
    for i in range(1, n + 1): 
        fact = fact * i
    print(fact)
        
factoriala(4)
    