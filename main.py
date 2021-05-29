from random import randint

response = input('Do you want to roll the dice? ')
response = response.lower()
if response in ['yes', 'y']:
    while True:
        print(randint(1, 6))
        cont = input("Another one? y/n :) ")
        cont = cont.lower()
        while cont.lower() not in ("yes", "no", 'y', 'n'):
            cont = input("Another one? yes/no > ")
        if cont in ["no", 'n']:
            print('\nHave a great time NOT PLAYING WITH ME. MUAHAHAHAA')
            break
else:
    print('\nHave a great time NOT PLAYING WITH ME MUAHAHAHAA')
