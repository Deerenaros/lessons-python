#возведи число в квадрат если оно делится на 2
#возведи число в куб если делится на 3
#просто число если делится и на 2 и на 3
#ничего в ином случае

x = 1
while x <= 100:
    if x % 2 == 0:
        print (x**2)
    x +=1
x = 1
while x <= 100:
    if x % 3 == 0:
        print (x**3)
    x +=1  
x = 1
while x <= 100:
    if x % 2 == 0 and x % 3 == 0:
        print (x) 
    x +=1
