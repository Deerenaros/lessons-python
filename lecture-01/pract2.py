#распечатать последовательность чисел 
#первое число - единица
#второе число - единица
#каждое последующее - сумма двух предыдущих
#остановись на сотом
#############


x = 1
print (1)
y = 1
print (1)
n = 3
while n < 101:
    x = y + x 
    print (x/y)
    n += 1 
    x, y = y, x