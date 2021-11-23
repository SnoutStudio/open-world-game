#Test Game

import time
import random
import constants

Alive = True

def startGame(): 
    help_information()

def help_information():
    print()
    print("Tips and Tricks...")
    print()
    print("Hunger - Your hunger must be kept at zero! If it exceeds 100 you will die.")
    print()
    print("Thirst - Your thirst must be kept at zero! If it exceeds 100 you will die.")
    print()
    print("Health - Your health will be decreased when hit! If it decreases to 0 you will die.")
    print()
    print("Reputation - This game has a reputation system, being rude will lose reputation and storekeepers won't sell to you.")
    print("You can increase damaged reputation by helping others and slaying monsters.")
    print()
    print("Gold - Get gold from killing monsters and claiming bounties, you can use gold to buy items and fast travel.")
    print()
    print("Exploration - The higher your exploration the shorter time it takes to travel!")
    print()
    print("Attack - The higher your attack the more damage you do to enemies!")
    print()
    print("Ready to continue?")
    print()
    print("Y. Yes")
    print()
    ready_continue = input("Choice: ")

    if ready_continue.upper() == "Y":
        game_introduction()

def game_introduction():
    print()
    print("Friendly Innkeeper - Hello traveller! Welcome to my inn, you can use it as a waypoint to get to other cities and towns")
    print("and even hire sailors to take you accross the great sea!")
    print()
    print("Here you can also buy full meals that will sustain you better than items purchased from that blasted grocer's...")
    print()
    print("Before I serve you may I dare to ask your name?")
    print()
    print("Be Friendly. F")
    print("Be Rude. R")
    print()
    ask_name = input("Choice: ")

    if ask_name.upper() == "F":
        print()
        print("My name is...")
        print()
        name = input("Your name: ")
        print()
        print("Nice to meet you " + name + ", you're definitely not from these parts but it's a pleasure to welcome you!")

    if ask_name.upper() == "R":
        print()
        print("You - That is my own business, not yours.")
        print()
        print("Friendly Innkeeper - Oh, my apologies dear man, I did not mean any offense...")
        print()
        constants.reputation += 10
        print("You have damaged your reputation! Your reputation is now at", constants.reputation, ", if it exceeds 100 shopkeeps will refuse to deal with you!")

    time.sleep(3)
    print()
    print("Well... er... as I was saying, you can view items and routes here, weapons and armour are upstairs as well as the monster bounty posters.")

    innkeep_choices()

def fast_travel():
    print()
    print(" - FAST TRAVEL - ")
    print()
    print("Travel to:")
    print()
    if constants.atTheCapital == False:
        print("1. The Capital - 5 Gold")
    print("2. The Establishment - 5 Gold")
    print("3. Blaviken - 5 Gold")
    print("4. Rivermoor - 10 Gold")
    print("5. Swampland Plains - 10 Gold")
    if constants.atTheDunes == False:
        print("6. The Dunes - 12 Gold")
    print("7. Salt Wave Harbour - 15 Gold")
    print()
    print("B. Back")
    print()
    print("You have", constants.gold, "gold.")
    print()
    fast_travel_choices = input("Choice: ")

    if fast_travel_choices.upper() == "1":
        if constants.gold >= 5:
            print()
            print("You - Take me to The Capital.")
            print()
            print("Friendly Innkeep - Sure thing, that'll be 5 Gold.")
            print()
            constants.gold -= 5
            print("You now have", constants.gold, "gold.")
            constants.atTheCapital = True
            constants.atTheDunes = False
            print()
            print("Travelling to The Capital...")
            print()
            time.sleep(2)
            print("...")
            time.sleep(2)
            print()
            print("Arrived...")
            time.sleep(2)
            the_capital()
        elif constants.gold < 5:
            print()
            print("You - Take me to The Capital.")
            print()
            print("Friendly Innkeep - Sorry mister, you're", 5 - constants.gold, "gold short. You can earn gold by claiming the monster bounties upstairs.")
            fast_travel()

    if fast_travel_choices.upper() == "2":
        if constants.gold >= 5:
            print()
            print("You - Take me to The Establishment.")
            print()
            print("Friendly Innkeep - Sure thing, that'll be 5 Gold.")
            print()
            constants.gold -= 5
            print("You now have", constants.gold, "gold.")
            the_establishment()
        elif constants.gold < 5:
            print()
            print("You - Take me to The Establishment.")
            print()
            print("Friendly Innkeep - Sorry mister, you're", 5 - constants.gold, "gold short. You can earn gold by claiming the monster bounties upstairs.")
            fast_travel()

    if fast_travel_choices.upper() == "3":
        if constants.gold >= 5:
            print()
            print("You - Take me to Blaviken.")
            print()
            print("Friendly Innkeep - Sure thing, that'll be 5 Gold.")
            print()
            constants.gold -= 5
            print("You now have", constants.gold, "gold.")
            the_blaviken()
        elif constants.gold < 5:
            print()
            print("You - Take me to Blaviken.")
            print()
            print("Friendly Innkeep - Sorry mister, you're", 5 - constants.gold, "gold short. You can earn gold by claiming the monster bounties upstairs.")
            fast_travel()

    if fast_travel_choices.upper() == "4":
        if constants.gold >= 10:
            print()
            print("You - Take me to Rivermoor.")
            print()
            print("Friendly Innkeep - Sure thing, that'll be 10 Gold.")
            print()
            constants.gold -= 10
            print("You now have", constants.gold, "gold.")
            the_rivermoor()
        elif constants.gold < 10:
            print()
            print("You - Take me to Rivermoor.")
            print()
            print("Friendly Innkeep - Sorry mister, you're", 10 - constants.gold, "gold short. You can earn gold by claiming the monster bounties upstairs.")
            fast_travel()

    if fast_travel_choices.upper() == "5":
        if constants.gold >= 10:
            print()
            print("You - Take me to the Swampland Plains.")
            print()
            print("Friendly Innkeep - Sure thing, that'll be 10 Gold.")
            print()
            constants.gold -= 10
            print("You now have", constants.gold, "gold.")
            the_swampland_plains()
        elif constants.gold < 10:
            print()
            print("You - Take me to the Swampland Plains.")
            print()
            print("Friendly Innkeep - Sorry mister, you're", 10 - constants.gold, "gold short. You can earn gold by claiming the monster bounties upstairs.")
            fast_travel()

    if fast_travel_choices.upper() == "6":
        if constants.gold >= 12:
            print()
            print("You - Take me to The Dunes.")
            print()
            print("Friendly Innkeep - Sure thing, that'll be 12 Gold.")
            print()
            constants.gold -= 12
            print("You now have", constants.gold, "gold.")
            print()
            print("Travelling to The Dunes...")
            print()
            time.sleep(2)
            print("...")
            time.sleep(2)
            print()
            print("Arrived...")
            time.sleep(2)
            the_dunes()
        elif constants.gold < 12:
            print()
            print("You - Take me to The Dunes.")
            print()
            print("Friendly Innkeep - Sorry mister, you're", 12 - constants.gold, "gold short. You can earn gold by claiming the monster bounties upstairs.")
            fast_travel()

    if fast_travel_choices.upper() == "7":
        if constants.gold >= 15:
            print()
            print("You - Take me to Salt Wave Harbour.")
            print()
            print("Friendly Innkeep - Sure thing, that'll be 15 Gold.")
            print()
            constants.gold -= 15
            print("You now have", constants.gold, "gold.")
            the_saltwave_harbour()
        elif constants.gold < 15:
            print()
            print("You - Take me to Salt Wave Harbour.")
            print()
            print("Friendly Innkeep - Sorry mister, you're", 15 - constants.gold, "gold short. You can earn gold by claiming the monster bounties upstairs.")
            fast_travel()

    if fast_travel_choices.upper() == "B":
        innkeep_choices()        

def the_capital():
    print()
    print(" - THE CAPITAL - ")
    print()
    print("1. Visit Inn")
    print("2. Visit Grocers")
    print("3. Visit Butchers")
    print("4. Visit Bank")
    print("5. Visit BlackSmith")

def the_establishment():
    print()
    print("Travelling to The Establishment...")
    print()
    time.sleep(2)
    print("...")
    time.sleep(2)
    print()
    print("Arrived...")
    time.sleep(2)
    print()
    print(" - THE ESTABLISHMENT - ")

def the_blaviken():
    print()
    print("Travelling to Blaviken...")
    print()
    time.sleep(2)
    print("...")
    time.sleep(2)
    print()
    print("Arrived...")
    time.sleep(2)
    print()
    print(" - BLAVIKEN - ")

def the_rivermoor():
    print()
    print("Travelling to Rivermoor...")
    print()
    time.sleep(2)
    print("...")
    time.sleep(2)
    print()
    print("Arrived...")
    time.sleep(2)
    print()
    print(" - RIVERMOOR - ")

def the_swampland_plains():
    print()
    print("Travelling to the Swampland Plains...")
    print()
    time.sleep(2)
    print("...")
    time.sleep(2)
    print()
    print("Arrived...")
    time.sleep(2)
    print()
    print(" - THE SWAMPLAND PLAINS - ")

def the_dunes():
    constants.atTheCapital = False
    constants.atTheDunes = True
    print()
    print(" - THE DUNES - ")
    print()
    print("1. Visit Inn")
    print("2. Visit Grocers")
    print("3. Visit Wizard's Tower")
    if constants.TrackingNorthernSlyder_dunes == True:
        print()
        print("4. Find Northern Slythern")
    print()
    the_dunes_choices = input("Choice: ")

    if the_dunes_choices.upper() == "1":
        innkeep_choices()

    if the_dunes_choices.upper() == "2":
        grocer_choices()

    if the_dunes_choices.upper() == "3":
        print()

    if the_dunes_choices.upper() == "4":
        print()
        print("Tracking Nothern Slythern...")
        print()
        print("You find it, lurking under a sand dune on the border of the city.")
        print()
        print("Do you fight it?")
        print()
        print("F. Fight the Slythern")
        print("R. Return to The Dunes and come back later.")
        print()
        fightorflightslythern = input("Choice: ")

        if fightorflightslythern.upper() == "F":
            print()
            print("You approach the Northern Slythern carefully.")
            fight_monster()

        if fightorflightslythern.upper() == "R":
            print()
            print("You back off quietly, and return to The Dunes. To cancel a bounty go to where you accepted it and choose cancel.")
            the_dunes()

def fight_monster():
    if constants.TrackingNorthernSlyder_dunes == True:
        print()
        print(" - NORTHERN SLYTHERN - ")
        print()
        print("It sits back on its haunches and hisses at you.")
        print()
        print("You have", constants.health, "health.")
        print()
        slythernhealth_random = random.randrange(100, 200)
        constants.northernslythernhealth += slythernhealth_random
        print("The Northern Slythern has", constants.northernslythernhealth, "health.")
        print()
        print("The Northern Slythern has a random chance of attacking, blocking attacks or nothing at all.")
        print()
        print("If you attack at the same time the Northern Slythern will deal damage and you will too.")
        print()
        print("Parrying can only be used twice per fight, it is a half percent chance of parrying the Slythern but if it")
        print("is successful you can deal great amounts of damage.")
        print()
        print("Retreating will cancel the bounty and cause you to lose 10 reputation.")
        fight_northernslythern()

def fight_northernslythern():
    print()
    print("What will you do?")
    print()
    print("1. Attack the Northern Slythern")
    print("2. Parry Attack, you have", constants.parries, "left.")
    print("3. Use Consumables")
    print("4. Retreat")
    print()
    fighting_northernslythern = input("Choice: ")

    if fighting_northernslythern.upper() == "1":
        print()
        print("You attack the Northern Slythern.")
        slythernmove_random = random.randrange(1, 8)
        if slythernmove_random <= 3:
            print()
            print("The Slythern blocks your attack.")
            fight_northernslythern()
        elif slythernmove_random > 3:
            slythernmove_random = random.randrange(1, 6)
            if slythernmove_random <= 3:
                print()
                print("You and the Slythern attack at the same time.")
                print()
                slytherndamage_random = random.randrange(15, 25)
                constants.health -= slytherndamage_random
                print("The Slythern grazes you with its barbed tail.")
                print()
                print("The Slythern dealt", slytherndamage_random, "damage to you.")
                print()
                print("You now have", constants.health, "health.")
                damagetoslythern_random = random.randrange(15, 20)
                constants.northernslythernhealth -= damagetoslythern_random
                print()
                print("At the same time you manage to weave close enough to strike its unprotected stomach.")
                print()
                print("You dealt", damagetoslythern_random, "damage to the Slythern.")
                print()
                print("The Slythern now has", constants.northernslythernhealth, "health.")
                if constants.northernslythernhealth <= 0:
                    print()
                    constants.northernslythernhealth = 0
                    constants.TrackingNorthernSlyder_dunes = False
                    constants.KilledNorthernSlythern = True
                    constants.parries = 2
                    print("In a split second your sword finds its way into the Slythern's heart and it falls dead at your feet, twitching and oozing blood.")
                    print()
                    constants.health = 100
                    print("You regain all health for emerging victorious.")
                    print()
                    print("To claim the gold go to any inn.")
                    the_dunes()
                elif constants.northernslythernhealth > 0:
                    fight_northernslythern()  
            elif slythernmove_random >= 4:
                print()
                print("The Slythern fails to block or attack and you successfully damage it.")
                damagetoslythern_random = random.randrange(25, 35)
                constants.northernslythernhealth -= damagetoslythern_random
                print()
                print("You dealt", damagetoslythern_random, "damage to the Slythern.")
                print()
                print("You now have", constants.health, "health.")
                print()
                print("The Slythern now has", constants.northernslythernhealth, "health.")
                if constants.northernslythernhealth <= 0:
                    print()
                    constants.northernslythernhealth = 0
                    constants.TrackingNorthernSlyder_dunes = False
                    constants.KilledNorthernSlythern = True
                    constants.parries = 2
                    print("In a split second your sword finds its way into the Slythern's heart and it falls dead at your feet, twitching and oozing blood.")
                    print()
                    constants.health = 100
                    print("You regain all health for emerging victorious.")
                    print()
                    print("To claim the gold go to any inn.")
                    the_dunes()
                elif constants.northernslythernhealth > 0:
                    fight_northernslythern()  
    
    if fighting_northernslythern.upper() == "2":
        if constants.parries > 0:
            print()
            print("You ready yourself to parry an attack.")
            slythernattack_random = random.randrange(1, 2)
            if slythernattack_random == 1:
                print()
                print("The Slythern attacks and you parry aside its claw, leaving its chest unprotected. You take a large swing.")
                print()
                print("You dealt 50 damage to the Slythern.")
                constants.northernslythernhealth -= 50
                print()
                constants.parries -= 1
                print("You have used 1 parry.")
                print()
                print("You now have", constants.parries, "parries left.")
                print()
                print("You now have", constants.health, "health.")
                print()
                print("The Slythern now has", constants.northernslythernhealth, "health.")
                if constants.northernslythernhealth <= 0:
                    print()
                    constants.northernslythernhealth = 0
                    constants.TrackingNorthernSlyder_dunes = False
                    constants.KilledNorthernSlythern = True
                    constants.parries = 2
                    print("In a split second your sword finds its way into the Slythern's heart and it falls dead at your feet, twitching and oozing blood.")
                    print()
                    constants.health = 100
                    print("You regain all health for emerging victorious.")
                    print()
                    print("To claim the gold go to any inn.")
                    the_dunes()
                elif constants.northernslythernhealth > 0:
                    fight_northernslythern()  
            elif slythernattack_random == 2:
                print()
                print("You ready yourself to parry an attack which never comes.")
                print()
                constants.parries -= 1
                print("You have wasted 1 parry.")
                print()
                print("You now have", constants.parries, "parries left.")
                print()
                print("You now have", constants.health, "health.")
                print()
                print("The Slythern now has", constants.northernslythernhealth, "health.")
                if constants.northernslythernhealth <= 0:
                    print()
                    constants.northernslythernhealth = 0
                    constants.TrackingNorthernSlyder_dunes = False
                    constants.KilledNorthernSlythern = True
                    constants.parries = 2
                    print("In a split second your sword finds its way into the Slythern's heart and it falls dead at your feet, twitching and oozing blood.")
                    print()
                    constants.health = 100
                    print("You regain all health for emerging victorious.")
                    print()
                    print("To claim the gold go to any inn.")
                    the_dunes()
                elif constants.northernslythernhealth > 0:
                    fight_northernslythern()  
        elif constants.parries <= 0:
            print()
            print("You have no more parries!")
            fight_northernslythern()

    if fighting_northernslythern.upper() == "4":
        constants.TrackingNorthernSlyder_dunes = False
        print()
        print("You back away in defeat as the Northern Slythern hisses and bears its fangs.")
        print()
        print("Coward... you have", constants.health, "health.")
        print()
        constants.parries = 2
        constants.reputation += 10
        print("You have damaged your reputation! Your reputation is now at", constants.reputation, ", if it exceeds 100 shopkeeps will refuse to deal with you!")
        the_dunes()

def the_saltwave_harbour():
    print()
    print("Travelling to Salt Wave Harbour...")
    print()
    time.sleep(2)
    print("...")
    time.sleep(2)
    print()
    print("Arrived...")
    time.sleep(2)
    print()
    print(" - SALT WAVE HARBOUR - ")

def buy_inn_items():
    print()
    print(" - BUY ITEMS - ")
    print()
    print(" - Consumables - ")
    print()
    print("1. Apple - 1 Gold")
    print("2. Banana - 1 Gold")
    print("3. Loaf of Bread - 1 Gold")
    print("4. Salted Meat - 5 Gold")
    print("5. Flask of Mead - 5 Gold")
    print("6. Flask of Wine - 8 Gold")
    print()
    print(" - Medical Items - ")
    print()
    print("7. Bandage - 2 Gold")
    print("8. Morphine - 10 Gold")
    print("9. Sewing Kit - 6 Gold")
    print("10. Adrenaline - 8 Gold")
    print()
    print("B. Back")
    print("C. Check your Items")
    print()
    buy_item = input("Choice: ")

    if buy_item.upper() == "1":
        if constants.gold >= 1:
            print()
            print("Purchased 1 Apple.")
            constants.apples += 1
            constants.gold -= 1
            print()
            print("You now have", constants.gold, "gold.")
            print()
            print("You now have", constants.apples, "apples.")
            buy_inn_items()
            
        elif constants.gold < 1:
            print()
            print("You cannot afford this item! Earn money by claiming monster bounties, the posters are upstairs.")
            print()
            print("You have", constants.gold, "gold.")
            buy_inn_items()

    elif buy_item.upper() == "2":
        if constants.gold >= 1:
            print()
            print("Purchased 1 Banana.")
            constants.bananas += 1
            constants.gold -= 1
            print()
            print("You now have", constants.gold, "gold.")
            print()
            print("You now have", constants.bananas, "bananas.")
            buy_inn_items()

        elif constants.gold < 1:
            print()
            print("You cannot afford this item! Earn money by claiming monster bounties, the posters are upstairs.")
            print()
            print("You have", constants.gold, "gold.")
            buy_inn_items()

    elif buy_item.upper() == "3":
        if constants.gold >= 1:
            print()
            print("Purchased 1 Loaf of Bread.")
            constants.loavesofbread += 1
            constants.gold -= 1
            print()
            print("You now have", constants.gold, "gold.")
            print()
            print("You now have", constants.loavesofbread, "loaves of bread.")
            buy_inn_items()

        elif constants.gold < 1:
            print()
            print("You cannot afford this item! Earn money by claiming monster bounties, the posters are upstairs.")
            print()
            print("You have", constants.gold, "gold.")
            buy_inn_items()

    elif buy_item.upper() == "4":
        if constants.gold >= 5:
            print()
            print("Purchased 1 Salted Meat.")
            constants.saltedmeat += 1
            constants.gold -= 5
            print()
            print("You now have", constants.gold, "gold.")
            print()
            print("You now have", constants.saltedmeat, "salted meat.")
            buy_inn_items()

        elif constants.gold < 5:
            print()
            print("You cannot afford this item! Earn money by claiming monster bounties, the posters are upstairs.")
            print()
            print("You have", constants.gold, "gold.")
            buy_inn_items()

    elif buy_item.upper() == "5":
        if constants.gold >= 5:
            print()
            print("Purchased 1 Flask of Mead.")
            constants.flaskofmead += 1
            constants.gold -= 5
            print()
            print("You now have", constants.gold, "gold.")
            print()
            print("You now have", constants.flaskofmead, "flasks of mead.")
            buy_inn_items()

        elif constants.gold < 5:
            print()
            print("You cannot afford this item! Earn money by claiming monster bounties, the posters are upstairs.")
            print()
            print("You have", constants.gold, "gold.")
            buy_inn_items()

    elif buy_item.upper() == "6":
        if constants.gold >= 8:
            print()
            print("Purchased 1 Flask of Wine.")
            constants.flaskofwine += 1
            constants.gold -= 8
            print()
            print("You now have", constants.gold, "gold.")
            print()
            print("You now have", constants.flaskofwine, "flasks of wine.")
            buy_inn_items()

        elif constants.gold < 8:
            print()
            print("You cannot afford this item! Earn money by claiming monster bounties, the posters are upstairs.")
            print()
            print("You have", constants.gold, "gold.")
            buy_inn_items()

    elif buy_item.upper() == "7":
        if constants.gold >= 2:
            print()
            print("Purchased 1 Bandage.")
            constants.gold -= 2
            constants.bandages += 1
            print()
            print("You now have", constants.gold, "gold.")
            print()
            print("You now have", constants.bandages, "bandages.")
            buy_inn_items()

        elif constants.gold < 2:
            print()
            print("You cannot afford this item! Earn money by claiming monster bounties, the posters are upstairs.")
            print()
            print("You have", constants.gold, "gold.")
            buy_inn_items()

    elif buy_item.upper() == "8":
        if constants.gold >= 10:
            print()
            print("Purchased 1 shot of Morphine.")
            constants.shotsofmorphine += 1
            constants.gold -= 10
            print()
            print("You now have", constants.gold, "gold.")
            print()
            print("You now have", constants.shotsofmorphine, "shots of morphine.")
            buy_inn_items()

        elif constants.gold < 10:
            print()
            print("You cannot afford this item! Earn money by claiming monster bounties, the posters are upstairs.")
            print()
            print("You have", constants.gold, "gold.")
            buy_inn_items()

    elif buy_item.upper() == "9":
        if constants.gold >= 6:
            print()
            print("Purchased 1 Sewing Kit.")
            constants.sewingkits += 1
            constants.gold -= 6
            print()
            print("You now have", constants.gold, "gold.")
            print()
            print("You now have", constants.sewingkits, "sewing kits.")
            buy_inn_items()

        elif constants.gold < 6:
            print()
            print("You cannot afford this item! Earn money by claiming monster bounties, the posters are upstairs.")
            print()
            print("You have", constants.gold, "gold.")
            buy_inn_items()

    elif buy_item.upper() == "10":
        if constants.gold >= 8:
            print()
            print("Purchased 1 shot of Adrenaline.")
            constants.shotsofadrenaline += 1
            constants.gold -= 8
            print()
            print("You now have", constants.gold, "gold.")
            print()
            print("You now have", constants.shotsofadrenaline, "shots of adrenaline.")
            buy_inn_items()

        elif constants.gold < 8:
            print()
            print("You cannot afford this item! Earn money by claiming monster bounties, the posters are upstairs.")
            print()
            print("You have", constants.gold, "gold.")
            buy_inn_items()

    elif buy_item.upper() == "B":
        print()
        innkeep_choices()

    elif buy_item.upper() == "C":
        print()
        print(" - INVENTORY - ")
        print()
        print("You have", constants.gold, "gold.")
        print()
        print("You have", constants.apples, "apples.")
        print()
        print("You have", constants.bananas, "bananas.")
        print()
        print("You have", constants.loavesofbread, "loaves of bread.")
        print()
        print("You have", constants.saltedmeat, "salted meat.")
        print()
        print("You have", constants.flaskofmead, "flasks of mead.")
        print()
        print("You have", constants.flaskofwine, "flasks of wine.")
        print()
        print("You have", constants.bandages, "bandages.")
        print()
        print("You have", constants.shotsofmorphine, "shots of morphine.")
        print()
        print("You have", constants.sewingkits, "sewing kits.")
        print()
        print("You have", constants.shotsofadrenaline, "shots of adrenaline.")
        buy_inn_items()

def go_upstairs():
    print()
    print(" - Weapons - ")
    print()
    print(" - Armour - ")
    print()
    print(" - Monster Bounties - ")
    print()
    print("Track:")
    if constants.TrackingNorthernSlyder_dunes == False:
        print()
        print("1. 200 Gold Reward - DEAD - Northern Slythern, last seen near The Dunes.")
    print()
    print("B. Back")
    print()
    track_monster = input("Choice: ")

    if track_monster.upper() == "1":
        print()
        print("You have tracked this bounty, travel to The Dunes to find it.")
        constants.TrackingNorthernSlyder_dunes = True
        go_upstairs()

    if track_monster.upper() == "B":
        innkeep_choices()

def innkeep_choices():
    print()
    print("You have", constants.gold, "gold.")
    print()
    print("Actions:")
    print()
    print("F. Fast Travel")
    print("B. Buy Items")
    print("U. Go Upstairs")
    print("E. Exit Store")
    print("R. Rob Store")
    if constants.KilledNorthernSlythern == True:
        print()
        print("1. Claim Northern Slythern Bounty")
    print()    
    inside_innkeep_choices = input("Choice: ")

    if inside_innkeep_choices.upper() == "F":
        print()
        print("Friendly Innkeep - Can't be bothered to get around on foot eh? Have a look at our options...")
        fast_travel()

    elif inside_innkeep_choices.upper() == "B":
        print()
        print("Friendly Innkeep - Take a look at our items, the weapons and armour are upstairs.")
        buy_inn_items()

    elif inside_innkeep_choices.upper() == "U":
        print()
        print("We've got a fine selection of weapons and armour up there, take a look around...")
        go_upstairs()

    elif inside_innkeep_choices.upper() == "E":
        print()

    elif inside_innkeep_choices.upper() == "R":
        print()

    elif inside_innkeep_choices.upper() == "1":
        constants.KilledNorthernSlythern = False
        print()
        print("Friendly Innkeep - Thank you for ridding us of that Northern Slythern, it was a troublesome beast. Here is your gold. You've earned it.")
        constants.gold += 200
        print()
        print("You earned 200 gold!")
        innkeep_choices()

def grocer_choices():
    print()

#Starting Game

if Alive == True:
    print("GAME TITLE")
    time.sleep(2)
    print()
    print("P. Play")
    print("Q. Quit")
    print()
    play_game = input("Choice: ")

    if play_game.upper() == "P":
        startGame()

    elif play_game.upper() == "Q":
        Alive = False

def startGame():
    help_information()

#Game End

if Alive == False:
    print("Play Again Function")
