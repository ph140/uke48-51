def f(x):
    return 2*x + 1


def g(x):
    return x**2-x-6


# Lager startverdier
start_a1 = -2
start_b1 = 3
start_a2 = 6
start_b2 = -5

# Lager startpunkter
a1 = [start_a1, f(start_a1)]
b1 = [start_b1, f(start_b1)]
a2 = [start_a2, g(start_a2)]
b2 = [start_b2, g(start_b2)]

midtpunkt1 = (start_a1 + start_b1)/2
midtpunkt2 = (start_a1 + start_b1)/2

c = [midtpunkt1, f(midtpunkt1)]
d = [midtpunkt2, g(midtpunkt2)]

# Kjører loopen helt til y-veriden av c-punktet er 0.0001 unna 0.
# Bruker halveringsmetoden.
while abs(c[1]) > 0.0001:
    if c[1]*a1[1] > 0:
        a1 = c
    else:
        b1 = c
    c = [(b1[0]+a1[0])/2, f((b1[0]+a1[0])/2)]

# Samme som forrige, med punktet d.
while abs(d[1]) > 0.0001:
    if d[1]*a2[1] > 0:
        a2 = d
    else:
        b2 = d
    d = [(b2[0]+a2[0])/2, g((b2[0]+a2[0])/2)]

# Printer ut svarene
print(c[0])
print(d[0])
