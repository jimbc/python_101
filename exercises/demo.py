def crossfoot(numbers):
    list_of_numbers = list(str(numbers))
    result = 0

    for s in list_of_numbers:
        number = int(s)
        result = result + number
    return result

def crossfoot2(number):

num = 12345
result = crossfoot(num)
print(result)