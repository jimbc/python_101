a = [1,2,3,4,5,6,7,8,9]

i = len(a)

a_reversed = []
while i > 0:
    last = a.pop()
    a_reversed.append(last)
    # a_reversed.append(a.pop())
    i -= 1

print(a_reversed)