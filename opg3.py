from numpy import sin, pi, cos

g = 9.81
tetha = pi/10


def y(t):
    return (-0.5*g*t**2)+(18*(sin(tetha))*t)


def x(t):
    return 18*cos(tetha)*t


h = 0.0001
x0 = 1


while abs(y(x0)) > 0.0001:
    x0 -= y(x0)/((y(x0+h)-y(x0))/h)

print(f"Ballen ble kastet {round(x(x0), 2)} meter langt.")
print('dsafdsadsfdasfdas')
