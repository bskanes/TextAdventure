player_name = input('What is your name adventurer?:')

while True:
    print('-Available classes-\n*MAGE*\n*KNIGHT*\n*DUMBASS*')
    player_class = input('Choose your class:')

    if player_class == 'K' or player_class == 'Knight' or player_class == 'KNIGHT' or \
            player_class == 'k' or player_class == 'knight':
        print('\033[1;36m"The mighty Sir {}, the honorable! Noble white Knight, You wield the great master sword,\n'
              'bane of all evil and totally not a possible lawsuit, you have one health potion and\na total '
              'HP of 20"'.format(player_name))
        input()
        a = input('Is KNIGHT the class for you?:')

        if a == 'yes' or a == 'Yes' or a == 'y' or a == 'Y' or a == 'YES':
            break

        elif a == 'no' or a == 'No' or a == 'n' or a == 'N' or a == 'NO':
            continue

    elif player_class == 'M' or player_class == 'm' or player_class == 'MAGE' \
            or player_class == 'Mage' or player_class == 'mage':
        print(
            '\033[1;36m"Ah yes, The Master of Mystics himself, {} The Wise! Your skills as a sorcerer are unmatched!\n'
            'You wield your staff of fireball, carry two health potions and have a total HP of 14"'.format(player_name))

    elif player_class == 'D' or player_class == 'd' or player_class == 'DUMBASS' or \
            player_class == 'Dumbass' or player_class == 'Dumbass':
        print('\033[1;36m"Oh... Dumpy {} the Dumbass... I was expecting someone uhhhh more suited for\n'
              'this kind of tale... oh I see you are wielding a half eaten sandwich, carrying a bottle of ketchup\n'
              ' and have a HP total of 16)"'.format(player_name))
    else:
        print('invalid input')
        input()
        continue
