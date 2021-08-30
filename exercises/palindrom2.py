word = 'Kajak'
# word = Legovogel
word = word.lower()

reversed_word = ''
index = len(word) - 1
while index >= 0:
    reversed_word += word[index]
    index -= 1

if reversed_word == word:
    print('PALINDROM')
else:
    print('kein Palindrom')
