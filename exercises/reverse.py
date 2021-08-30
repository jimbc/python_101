liste = [1,2,3,4,5,6,7,8,9]

reversed_liste = []
for i in range(len(liste)):
    last = liste.pop()
    # reversed_liste.append(last)
    reversed_liste.extend([last])
print(reversed_liste)
