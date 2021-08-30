word = 'Kajak'
# word = Legovogel
word =  word.lower()
reversed_word = word[::-1]

if reversed_word == word:
    print('PALINDROM')
else:
    print('kein Palindrom')
