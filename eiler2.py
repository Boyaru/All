

# 1) Простые числа
# 2) Узнать наибольшее 600851475143

dead = int(input('Число: '))
lst = []
ko = []
gg = int(dead / 2)
for l in range(3, gg, 2):
    for k in range (3, l, 2):
        if l % k == 0:
            break
    else:
        lst.append(l)
for da in lst:
    if dead % da == 0:
        ko.append(da)
chida = ko[-1]
print(chida)

    
