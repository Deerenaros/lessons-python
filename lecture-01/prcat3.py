s = "((43 + 21)*101 - 123/11 + 13)*11 - 134"
s = "43 21 + 101 * 123 11 / - 13 + 11 * 134 -"
t = s.split(" ")
s = []

for o in t:
    if o in "+-*/":
        o2, o1 = s.pop(), s.pop()
        if o == "+":
            s.append(o1 + o2)
        elif o == "-":
            s.append(o1 - o2)
        elif o == "*":
            s.append(o1 * o2)
        elif o == "/":
            s.append(o1 // o2)
    else:
        s.append(int(o))

print(s[-1])