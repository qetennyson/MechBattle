import random
import time

#TODO import dicts/functions
# import game_data as gd

game_stats = {
    'game_state': True,
    'combat_texts': ["THE BATTLE BEGINS", "CHAOS ENSUES", "TOTAL WAR!"],
}

combat_mech = {
    'name': "Combat Mech",
    'power': 3,
}
tank_mech = {
    'name': "Tank Mech",
    'power': 2,
}

arti_mech = {
    'name': "Artillery Mech",
    'power': 1,
}

xeno = {
    'name': "Xenomorph Queen",
    'power': 4,
}

bit_8 = {
    'name': "Just 8 Green Pixels",
    'power': 0,
}

aliens = [xeno, bit_8]
mechs = [combat_mech, tank_mech, arti_mech]

def print_header():
    print("-------------------------")
    print("*** ** MECH BATTLE ** ***")
    print("-------------------------")
    print()
    print("Welcome to Mech Battle.\n")
    time.sleep(1)
    print("Aliens are attacking.  Choose a mech to defend the city!")
    print()


def update_state(result, mech, alien):
    if result:
        print("Well done, you defeated the %s \n" % alien.get('name'))
    else:
        print("The %s defeated your %s" % (alien.get('name'), mech.get('name')))
        mechs.remove(mech)


def combat(mech, alien):
    print(random.choice(game_stats['combat_texts']))
    print()
    time.sleep(2)
    mech_score = mech.get('power')
    alien_score = alien.get('power')

    if mech_score < alien_score:
        return False
    else:
        return True

def choose_alien():
    return random.choice(aliens)

# chooses a mech if one is available.
# this was cool to t/s because I didn't think about the list
# being reduced in size at first :D

# TODO handle mech in and out of list operation
# Figured out above, just a conditional problem.
def choose_mech(choice):
    if choice.lower() == 'c' and combat_mech in mechs:
        try:
            return mechs[mechs.index(combat_mech)]
        except:
            print("Mech offline...")
    elif choice.lower() == 't' and tank_mech in mechs:
        try:
            return mechs[mechs.index(tank_mech)]
        except:
            print("Mech offline...")
    elif choice.lower() == 'a' and arti_mech in mechs:
        try:
            return mechs[mechs.index(arti_mech)]
        except:
            print("Mech offline...")
    else:
        print("That Mech is gone, commander...")
        return False

def main():
    print_header()

    while True:
        cmd = input("Choose your mech: [C]ombat, [T]ank, [A]rtillery | or E[x]it\n")
        choice_mech = choose_mech(cmd)
        if not choice_mech:
            continue
        random_alien = choose_alien()
        print("A %s appears!\n" % random_alien.get('name'))

        result = combat(choice_mech, random_alien)
        update_state(result, choice_mech, random_alien)

        if len(mechs) == 0:
            print("Game over.")
            break

        print("%s lies in a heap on the battlefield... send in another mech?\n" % choice_mech.get('name'))


if __name__ == '__main__':
    main()