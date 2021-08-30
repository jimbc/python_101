def schimpfen(alter):
    if alter <= 25:
        print('Du bist ein Schoßhund!')
    elif 25 > alter > 30:
        print("Du bist ein alter Sack!")
    elif 30 >= alter > 35:
        print("Du bist WIRKLICH ein alter Sack!")
    else:
        print('Du bist eine MUMIE')
    return

while True:
    first_name = input('Geben Sie Ihren Vornamen ein: ')
    last_name = input('Geben Sie Ihren Nachnamen ein: ')
    birth_year = input('Geben Sie Ihr Geburtsjahr ein: ')
    alter = 2020-int(birth_year)
    print('Ihre Initialen lauten: '+str(first_name[0])+'.'+str(last_name[0])+'.')
    print('Sie sind oder werden dieses Jahr', alter , 'Jahre alt!')
    schimpfen(alter)




print('Programmende')