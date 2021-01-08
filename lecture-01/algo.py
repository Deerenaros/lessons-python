
x = 1
while x <= 100:
    print(x, x**3)
    if x != 1 and not any(x % n == 0 for n in range(2, x)):
        x += 10
    else:
        x += 1

print()

x = 1
while x <= 100:
    print(x, x**3)

    is_x_prime = x != 1
    for n in range(2, x):
        if x % n == 0:
            is_x_prime = False

    if is_x_prime:
        x += 10
    else:
        x += 1

print()

for x in range(1, 101):
    print(x, x**3)
    is_x_prime = x != 1
    for n in range(2, x):
        if x % n == 0:
            is_x_prime = False

    if is_x_prime :
        x += 10
    else:
        x += 1