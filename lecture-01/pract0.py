# 1. распечатать четные числа 

for x in range(1, 101):
    if x % 2 == 0:
        print(x)

# 2. рапечатать кубы каждого одиннадцатого числа
print()
for x in range(1, 101):
    if x % 11 == 0:
        print(x**3)

# 3. распечатать числа которые не делятся на 2 на 3 на 5 на 11
print()
for x in range(1, 101):
    if not (x % 2 == 0 or
            x % 3 == 0 or
            x % 5 == 0 or
            x % 11 == 0):
        print(x)

# 4. распечатать числа взаимно простые с 6

print()
import math
for x in range(1, 101):
    if math.gcd(6, x) == 1:
        print(x)

# 5. то же что и 3, но с гэцэдэ

print()
print()
print()
print()
print()
print()
for x in range(1, 101):
    if math.gcd(2*3*5*11, x) == 1:
        print(x)

# 6. почситать процент простых чисел до одного миилионнна
print()
print()
m = 0
for x in range(1, 10**5):
    is_x_prime = x != 1
    for n in range(2, x//2):
        if x % n == 0:
            is_x_prime = False   
            break     
    if is_x_prime:
        m += 1
        print(x)
print(m / 10**5 * 100)

#