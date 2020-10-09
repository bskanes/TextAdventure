import random


def enter():
    input('\033[91mPress Enter')


def error():
    print('\033[91minvalid input')
    input('\033[91mPress Enter')
# Enemy's


goblin_one_stats = {'Health': 20}
goblin_one_attack = (random.randint(1, 3))

print('\033[34mWelcome to my text based fantasy adventure game! simply type and hit enter to play!')
enter()
player_name = input('\033[34mWhat is your name adventurer?:')
playerclass = ''
knight_health_potions = 1
knight_stats = {'Health': 20, 'Attack': 'D6', 'Gold': 5, 'Potions': knight_health_potions}
knight_attack = (random.randint(1, 6))
knight_items = []
mage_health_potions = 2
mage_stats = {'Health': 14, 'Attack': 'D10', 'Gold': 5, 'Potions': mage_health_potions}
mage_attack = (random.randint(1, 10))
mage_items = []
dumbass_health_potions = 1
dumbass_stats = {'Health': 16, 'Attack': 'D8', 'Gold': 5, 'Ketchup Bottles': dumbass_health_potions}
dumbass_attack = (random.randint(1, 8))
dumbass_items = []

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
      'here but have been unsuccessful with removing the pests."')
input('\033[91mPress Enter')

while True:
    q = input('\033[1;36m"Will you assist us during this trying time?":')
    if q.lower() == 'y' or q.lower() == 'yes' or q.lower() == 'sure' \
            or q.lower() == 'ok' or q.lower() == 'why not' or q.lower() == 'yee' \
            or q.lower() == 'yeet' or q.lower() == 'yep' or q.lower() == 'yup':
        print('\033[1;36m"Great!! You must set out at once! Take this rope, it may come in handy"')
        input('\033[91mPress Enter')
        print('\033[34m*Obtained Rope*')
        knight_items.append('Rope')
        mage_items.append('Rope')
        dumbass_items.append('Rope')
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
            knight_items.append('Rope')
            mage_items.append('Rope')
            dumbass_items.append('Rope')
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
                knight_items.append('Rope')
                mage_items.append('Rope')
                dumbass_items.append('Rope')
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
print('\033[34mYou walk through the city gates looking back upon the massive walls towering over you. Turning around\n'
      'you see the vast farm lands stretching for miles outside the city walls.')
enter()
if playerclass == 'Dumbass':
    print('\033[34mYou turn around once more confused... Did I come from that way or this way? I uhhh... looking at\n'
          'the ground you see a butterfly. COOL! you proceed to walk in and out of the city before a guard sees you,\n'
          'turns you around and shoves you in the direction youre supposed to head')
    enter()
print('\033[34mafter walking for a few hours you begin to see the effects the goblin raids have had on the outer\n'
      'farms. Many crop fields lay barren and farm animals dead. You can see most families have boarded up their\n'
      'windows and are peering out the window at you')
enter()
if playerclass == 'Mage':
    print('\033[34mUsing some healing magic you are able to help some of the injured animals. A thankful\n'
          'disney esque bird comes toward you and offers you one of its feathers')
    enter()
    print('\033[34m*Obtained Feather*')
    mage_items.append('Feather')
    enter()
if playerclass == 'Dumbass':
    print('\033[34mWow these animals sure are tired!')
    enter()
print('\033[34mYou travel past the farmlands and arrive at a cave opening fortified with spikes and bones.\n'
      'Out of the corner of your eye you notice a fallen knight haphazardly buried in the ground')
enter()
if playerclass == 'Knight':
    print('\033[34mSeeing a fallen homie you give him a proper burial... after searching his corpse')
    print('\033[34m*Obtained Dead Guys Dagger*')
    knight_items.append('Dead Guys Dagger')
    enter()
print('\033[34mEntering the cave you see it is cold and nasty. REAL nasty. Like trash and green snot everywhere...\n'
      'wait thats not green snot! THATS A GOBLIN! FIGHT!!!')
enter()
while True:
    goblin_one_attack = (random.randint(1, 3))
    knight_attack = (random.randint(1, 6))
    mage_attack = (random.randint(1, 10))
    dumbass_attack = (random.randint(1, 8))

    # Fight Stuff

    print('\033[31mGoblin {}'.format(goblin_one_stats))
    dostuff = input('\033[31m[Attack] [Items] [Stats] [Potions]:')
    if dostuff.lower() == 'a' or dostuff.lower() == 'attack':
        if playerclass == 'Knight':
            damage = int(knight_attack)
            print('\033[31mYou did {} damage!'.format(damage))
            goblin_one_stats['Health'] -= damage
        if playerclass == 'Mage':
            damage = int(mage_attack)
            print('\033[31mYou did {} damage!'.format(damage))
            goblin_one_stats['Health'] -= damage
        if playerclass == 'Dumbass':
            damage = int(dumbass_attack)
            print('\033[31mYou did {} damage!'.format(damage))
            goblin_one_stats['Health'] -= damage
        enter()
        if goblin_one_stats['Health'] <= 0:
            break
        goblindamage = int(goblin_one_attack)
        print('\033[31mThe goblin did {} damage to you'.format(goblindamage))
        if playerclass == 'Knight':
            knight_stats['Health'] -= goblindamage
        if playerclass == 'Mage':
            mage_stats['Health'] -= goblindamage
        if playerclass == 'Dumbass':
            dumbass_stats['Health'] -= goblindamage
        enter()
        if knight_stats['Health'] <= 0 or mage_stats['Health'] <= 0 or dumbass_stats['Health'] <= 0:
            print('You Died. GAME OVER')
            quit()
    elif dostuff.lower() == 'i' or dostuff.lower() == 'item' or dostuff.lower() == 'items':
        if playerclass == 'Knight':
            print('\033[31m*Items*')
            print(knight_items)
            useitem = input('\033[31mWhat item would you like to use? Press enter to go back:')
            if useitem.lower() == 'rope' or useitem.lower == 'r':
                print('\033[31mYou swiftly tie the goblin up')
                knight_items.remove('Rope')
                break
            if useitem.lower() == 'dagger' or useitem.lower() == 'dead guys dagger' or useitem.lower() == 'd':
                print('\033[31mYou throw the dagger through the goblins heart!')
                knight_items.remove('Dead Guys Dagger')
                break
            else:
                continue
        elif playerclass == 'Mage':
            print('\033[31m*Items*')
            print(mage_items)
            useitemmage = input('\033[31mWhat item would you like to use? Press enter to go back:')
            if useitemmage.lower() == 'feather' or useitemmage.lower() == 'f':
                print('\033[31mYou tickle him till he explodes!')
                mage_items.remove('Feather')
                break
            if useitemmage.lower() == 'rope' or useitemmage.lower == 'r':
                print('\033[31mYou swiftly tie the goblin up')
                mage_items.remove('Rope')
                break
            else:
                continue
        elif playerclass == 'Dumbass':
            print('\033[31m*Items*')
            print(dumbass_items)
            useitemdumbass = input('\033[31mWhat item would you like to use? Press enter to go back:')
            if useitemdumbass.lower() == 'rope' or useitemdumbass.lower == 'r':
                print('\033[31mYou swiftly tie the goblin up')
                dumbass_items.remove('Rope')
                break
            else:
                continue
    if dostuff.lower() == 'potions' or dostuff.lower() == 'p' or dostuff.lower() == 'potion':
        heal = input('\033[31mWould you like to use a health potion?:')
        if heal.lower() == 'y' or heal.lower() == 'yes' or heal.lower() == 'sure' \
                or heal.lower() == 'ok' or heal.lower() == 'why not' or heal.lower() == 'yee' \
                or heal.lower() == 'yeet' or heal.lower() == 'yep' or heal.lower() == 'yup':
            if playerclass == 'Knight':
                if knight_health_potions > 0:
                    knight_health_potions -= 1
                    amount_added = (random.randint(1, 8))
                    knight_stats['Health'] += amount_added
                    print('\033[31mYou healed yourself for {}'.format(amount_added))
                    enter()
                    continue
                else:
                    print('\033[31mYou are out of Health Potions')
                    enter()
                    continue
            if playerclass == 'Mage':
                if mage_health_potions > 0:
                    mage_health_potions -= 1
                    amount_added = (random.randint(1, 8))
                    mage_stats['Health'] += amount_added
                    print('\033[31mYou healed yourself for {}'.format(amount_added))
                    enter()
                    continue
                else:
                    print('\033[31mYou are out of Health Potions')
                    enter()
                    continue
            if playerclass == 'Dumbass':
                if dumbass_health_potions > 0:
                    dumbass_health_potions -= 1
                    amount_added = (random.randint(1, 8))
                    dumbass_stats['Health'] += amount_added
                    print('\033[31mYou healed yourself for {}'.format(amount_added))
                    enter()
                    continue
                else:
                    print('\033[31mYou are out of Health Potions')
                    enter()
                    continue
    if dostuff.lower() == 'stats' or dostuff.lower() == 's' or dostuff.lower() == 'stat':
        if playerclass == 'Knight':
            print(knight_stats)
            enter()
            continue
        if playerclass == 'Mage':
            print(mage_stats)
            enter()
            continue
        if playerclass == 'Dumbass':
            print(dumbass_stats)
            enter()
            continue
        break
print('\033[34mYOU WIN!')
enter()
if playerclass == "Dumbass":
    print('\033[34mYou notice as you move deeper in the cave that wow it is really bright. Youre.... you went outside\n'
          'its the sun... you idiot. You know what take this!')
    enter()
    print('\033[34m*Obtained Map*')
    dumbass_items.append('Map')
    enter()
    print('\033[34mJeez')
    enter()
print('\033[34mMoving past your fallen foe you see bright lights emerging from deep inside. There seems to be\n'
      'a fork in the cave with two massive bonfires on both sides lighting up each tunnel')
enter()
print('\033[34mPeering down the left tunnel you see bones, rotting flesh and a large wooden table coated with blood.\n'
      'standing atop the table is a grubby goblin wearing a "Kiss the cook" apron sharpening a butchers knife,\n'
      'he hasnt noticed you yet')
enter()
print('looking away from that disturbing sight, you look down the right tunnel. You see several empty cages with\n'
      'shackles hanging from them. A small puppy has his head down amd is sniffing inside one of the open cages')
enter()
if playerclass == 'Dumbass':
    print('')
choice = ('will you go left or right?:')

