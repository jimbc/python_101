import copy
a = [1,2,3,4,5,6,7,8,9]
a = 'legovogel'
a = list(a)
b = copy.deepcopy(a)
list_reversed = []
while len(a) > 0:
    list_reversed.append(a.pop())

if b == list_reversed:
    print('palindrom')
print(b)
print (list_reversed)