player_name = input('\033[35mWhat is your name adventurer?:')
playerclass = ()

while True:
    print('\033[35m-Available classes-\n*MAGE*\n*KNIGHT*\n*DUMBASS*')
    player_class = input('\033[35mChoose your class:')

    if player_class == 'K' or player_class == 'Knight' or player_class == 'KNIGHT' or \
            player_class == 'k' or player_class == 'knight':
        print('\033[1;36m"The mighty Sir {}, the honorable! Noble white Knight, You wield the great master sword,\n'
              'bane of all evil and totally not a possible lawsuit, you have one health potion and\na total '
              'HP of 20"'.format(player_name))
        input()
        a = input('\033[35mIs KNIGHT the class for you?:')

        if a == 'yes' or a == 'Yes' or a == 'y' or a == 'Y' or a == 'YES':
            playerclass = 'KNIGHT'
            break

        elif a == 'no' or a == 'No' or a == 'n' or a == 'N' or a == 'NO':
            continue
        else:
            print('invalid input')
            input()
            continue
    elif player_class == 'M' or player_class == 'm' or player_class == 'MAGE' \
            or player_class == 'Mage' or player_class == 'mage':
        print(
            '\033[1;36m"Ah yes, The Master of Mystics himself, {} The Wise! Your skills as a sorcerer are unmatched!\n'
            'You wield your staff of fireball, carry two health potions and have a total HP of 14"'.format(player_name))
        input()
        b = input('\033[35mIs MAGE the class for you?:')
        if b == 'yes' or b == 'Yes' or b == 'y' or b == 'Y' or b == 'YES':
            playerclass = 'MAGE'
            break

        elif b == 'no' or b == 'No' or b == 'n' or b == 'N' or b == 'NO':
            continue
        else:
            print('invalid input')
            input()
            continue
    elif player_class == 'D' or player_class == 'd' or player_class == 'DUMBASS' or \
            player_class == 'Dumbass' or player_class == 'dumbass':
        print('\033[1;36m"Oh... Dumpy {} the Dumbass... I was expecting someone uhhhh more suited for\n'
              'this kind of tale... oh I see you are wielding a half eaten sandwich, carrying a bottle of ketchup\n'
              'and have a HP total of 16)"'.format(player_name))
        input()
        c = input('\033[35mdo you want to be a Dumbass?:')
        if c == 'yes' or c == 'Yes' or c == 'y' or c == 'Y' or c == 'YES':
            playerclass = 'DUMBASS'
            break

        elif c == 'no' or c == 'No' or c == 'n' or c == 'N' or c == 'NO':
            continue
        else:
            print('invalid input')
            input()
            continue
    else:
        print('invalid input')
        input()
        continue
