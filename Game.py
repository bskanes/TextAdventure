import random
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

    if player_class.lower() == 'k' or player_class.lower() == 'knight':
        print('\033[1;36m"The mighty Sir {}! Noble white Knight, You wield the great master sword,\n'
              'bane of all evil and totally not a possible lawsuit, you have one health potion and\na total '
              'HP of 20"'.format(player_name))
        input('\033[91mPress Enter')
        a = input('\033[34mIs KNIGHT the class for you?:')

        if a.lower() == 'yes' or a.lower() == 'y':
            playerclass = 'Knight'
            break

        elif a.lower() == 'no' or a.lower() == 'n':
            continue
        else:
            print('\033[91minvalid input')
            input('\033[91mPress Enter')
            continue
    elif player_class.lower() == 'm' or player_class.lower() == 'mage':
        print('\033[1;36m"Ah yes, The Master of Mystics himself, {} The Wise! Your skills as a sorcerer are\n'
              'unmatched! You wield your staff of fireball and some edgy eyeliner. You have two health potions\n'
              'and have a total HP of 14"'.format(player_name))
        input('\033[91mPress Enter')
        b = input('\033[34mIs MAGE the class for you?:')
        if b.lower() == 'yes' or b.lower() == 'y':
            playerclass = 'Mage'
            break

        elif b.lower() == 'no' or b.lower() == 'n':
            continue
        else:
            print('\033[91minvalid input')
            input('\033[91mPress Enter')
            continue
    elif player_class.lower() == 'd' or player_class.lower() == 'dumbass':
        print('\033[1;36m"Oh... Dumpy {} the Dumbass... I was expecting someone uhhhh more suited for\n'
              'this kind of tale... oh I see you are wielding a half eaten sandwich, carrying a bottle of ketchup\n'
              'and have a HP total of 16)"'.format(player_name))
        input('\033[91mPress Enter')
        c = input('\033[34mdo you want to be a Dumbass?:')
        if c.lower() == 'yes' or c.lower() == 'y':
            playerclass = 'Dumbass'
            break

        elif c.lower() == 'no' or c.lower() == 'n':
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
    if q.lower() == 'y' or q.lower() == 'yes' or q.lower() == 'sure' \
            or q.lower() == 'ok' or q.lower() == 'why not' or q.lower() == 'yee' \
            or q.lower() == 'yeet' or q.lower() == 'yep' or q.lower() == 'yup':
        print('\033[1;36m"Great!! You must set out at once! Take this rope, it may come in handy"')
        input('\033[91mPress Enter')
        print('\033[34m*Obtained Rope*')
        input('\033[91mPress Enter')
        break
    elif q.lower() == 'n' or q.lower() == 'no' or q.lower() == 'nope' or q.lower() == 'nah' \
            or q.lower() == 'screw off' or q.lower() == 'shut up' or q.lower() == 'no thanks'\
            or q.lower() == 'another time' or q.lower() == 'im good':
        comeon = input('\033[1;36m"Oh come on please?":')
        if comeon.lower() == 'y' or comeon.lower() == 'yes' or comeon.lower() == 'sure' \
                or comeon.lower() == 'ok' or comeon.lower() == 'why not' or comeon.lower() == 'yee' \
                or comeon.lower() == 'yeet' or comeon.lower() == 'yep' or comeon.lower() == 'yup':
            print('\033[1;36m"Great!! You must set out at once! Take this rope, it may come in handy"')
            input('\033[91mPress Enter')
            print('\033[34m*Obtained Rope*')
            input('\033[91mPress Enter')
            break
        elif comeon.lower() == 'n' or comeon.lower() == 'no' or comeon.lower() == 'nope' or comeon.lower() == 'nah' \
                or comeon.lower() == 'screw off' or comeon.lower() == 'shut up' or comeon.lower() == 'no thanks' \
                or comeon.lower() == 'another time' or comeon.lower() == 'im good':
            lastchance = input('\033[1;36m"If you do it ill throw in a hefty chunk of gold and a swift booty slap":')
            if lastchance.lower() == 'y' or lastchance.lower() == 'yes' or lastchance.lower() == 'sure' \
                    or lastchance.lower() == 'ok' or lastchance.lower() == 'why not' or lastchance.lower() == 'yee' \
                    or lastchance.lower() == 'yeet' or lastchance.lower() == 'yep' or lastchance.lower() == 'yup':
                print('\033[1;36m"Great!! You must set out at once! Take this rope, it may come in handy"')
                input('\033[91mPress Enter')
                print('\033[34m*Obtained Rope*')
                input('\033[91mPress Enter')
                break
            elif lastchance.lower() == 'n' or lastchance.lower() == 'no' or lastchance.lower() == 'nope'\
                    or lastchance.lower() == 'nah' or lastchance.lower() == 'screw off'\
                    or lastchance.lower() == 'shut up' or lastchance.lower() == 'no thanks'\
                    or lastchance.lower() == 'another time' or lastchance.lower() == 'im good':
                print('\033[1;36m"Fine then...... dick"')
                print('\033[34mAnd thus the adventure ends! Thanks for playing')
                quit()
            else:
                print('\033[91minvalid input')
                input('\033[91mPress Enter')
                continue
        else:
            print('\033[91minvalid input')
            input('\033[91mPress Enter')
            continue
    else:
        print('\033[91minvalid input')
        input('\033[91mPress Enter')
        continue
