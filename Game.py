print('\033[34mWelcome to my text based fantasy adventure game! simply type and hit enter to play!')
input('\033[91mPress Enter')


player_name = input('\033[34mWhat is your name adventurer?:')
playerclass = ''
knight_health = 20
mage_health = 14
dumbass_health = 16
while True:
    print('\033[34m-Available classes-\n*MAGE*\n*KNIGHT*\n*DUMBASS*')
    player_class = input('\033[34mChoose your class:')

    if player_class == 'K' or player_class == 'Knight' or player_class == 'KNIGHT' or \
            player_class == 'k' or player_class == 'knight':
        print('\033[1;36m"The mighty Sir {}, the honorable! Noble white Knight, You wield the great master sword,\n'
              'bane of all evil and totally not a possible lawsuit, you have one health potion and\na total '
              'HP of 20"'.format(player_name))
        input('\033[91mPress Enter')
        a = input('\033[34mIs KNIGHT the class for you?:')

        if a == 'yes' or a == 'Yes' or a == 'y' or a == 'Y' or a == 'YES':
            playerclass = 'Knight'
            break

        elif a == 'no' or a == 'No' or a == 'n' or a == 'N' or a == 'NO':
            continue
        else:
            print('\033[91minvalid input')
            input('\033[91mPress Enter')
            continue
    elif player_class == 'M' or player_class == 'm' or player_class == 'MAGE' \
            or player_class == 'Mage' or player_class == 'mage':
        print(
            '\033[1;36m"Ah yes, The Master of Mystics himself, {} The Wise! Your skills as a sorcerer are unmatched!\n'
            'You wield your staff of fireball, carry two health potions and have a total HP of 14"'.format(player_name))
        input('\033[91mPress Enter')
        b = input('\033[34mIs MAGE the class for you?:')
        if b == 'yes' or b == 'Yes' or b == 'y' or b == 'Y' or b == 'YES':
            playerclass = 'Mage'
            break

        elif b == 'no' or b == 'No' or b == 'n' or b == 'N' or b == 'NO':
            continue
        else:
            print('\033[91minvalid input')
            input('\033[91mPress Enter')
            continue
    elif player_class == 'D' or player_class == 'd' or player_class == 'DUMBASS' or \
            player_class == 'Dumbass' or player_class == 'dumbass':
        print('\033[1;36m"Oh... Dumpy {} the Dumbass... I was expecting someone uhhhh more suited for\n'
              'this kind of tale... oh I see you are wielding a half eaten sandwich, carrying a bottle of ketchup\n'
              'and have a HP total of 16)"'.format(player_name))
        input('\033[91mPress Enter')
        c = input('\033[34mdo you want to be a Dumbass?:')
        if c == 'yes' or c == 'Yes' or c == 'y' or c == 'Y' or c == 'YES':
            playerclass = 'Dumbass'
            break

        elif c == 'no' or c == 'No' or c == 'n' or c == 'N' or c == 'NO':
            continue
        else:
            print('\033[91minvalid input')
            input('\033[91mPress Enter')
            continue
    else:
        print('\033[91minvalid input')
        input('\033[91mPress Enter')
        continue

print('\033[1;36m"My name is Drucan, I assist the king with his kingly duties! The king has requested I ask\n'
      'you, great {} {}, to help with an urgent matter"'.format(playerclass, player_name))
input('\033[91mPress Enter')
print('\033[1;36m"Goblins have been raiding nearby farms. We have tracked them down to a cave south of\n'
      'here but have been unsuccessful on removing the pests."')
input('\033[91mPress Enter')

while True:
    q = input('\033[1;36m"Will you assist us during this trying time?":')
    if q == 'y' or q == 'Y' or q == 'YES' or q == 'yes' or q == 'Yes' or q == 'sure' or q == 'Sure' \
            or q == 'SURE' or q == 'ok' or q == 'OK' or q == 'Ok' or q == 'why not' or q == 'Why not' or q == 'yee' \
            or q == 'Yeet' or q == 'YEET' or q == 'yeet' or q == 'Why not' or q == 'yep' or q == 'Yep' \
            or q == 'yup or q == Yup':
        print('\033[1;36m"Great!! You must set out at once! Take this rope, it may come in handy"')
        input('\033[91mPress Enter')
        print('\033[34mObtained Rope')
        input('\033[91mPress Enter')
        break
    else:
        print('\033[91minvalid input')
        input('\033[91mPress Enter')
        continue

