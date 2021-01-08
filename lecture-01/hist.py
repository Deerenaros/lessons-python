x = 1
while True:
    print(x**2)
    x = x + 1
    if x > 100:
        break

#################

x = 1
while x <= 100:
    print(x**2)
    x += 1

#################

x = 1
while (x := x + 1) <= 100:
    print(x**2)

#################

x = 1
while not ((x := x + 1) > 100):
    print(x**2)

#################

for x in range(1, 101):
    print(x**2)

#################

list(map(lambda x: print(x**2), range(1, 101)))

#################

print("\n".join("%5d" % x**2 for x in range(1, 101)))

#################

x = 1
while x <= 100:
    print(x, x**3)
    if x != 1 and not any(x % n == 0 for n in range(2, x)):
        x += 10
    else:
        x += 1

#################

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

#################

for x in range(1, 101):
    print(x, x**3)

    is_x_prime = x != 1
    for n in range(2, x):
        if x % n == 0:
            is_x_prime = False

    if is_x_prime:
        x += 10
    else:
        x += 1