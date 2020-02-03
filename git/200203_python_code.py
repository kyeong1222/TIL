def F(x):
    if x < 0:
        return 0
    if x > 360:
        return 1
    elif x < 180:
        return (2/3) * (x/180)
    elif x >= 180:
        return (2/3) + (1/3) * ((x - 180) / 180)

print(F(180)-F(50))
