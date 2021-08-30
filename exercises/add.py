def summe(x,y):
    res = x + y
    return res

a = 5
b = 6
c = summe(a,b)
print('summe:', c)

a = 6
c = summe(a,b)
print('summe:', c)

a = -100
b = 1e10
print('summe:', summe(a,b))

