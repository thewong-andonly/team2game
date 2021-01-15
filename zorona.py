import sys
from time import sleep
import random
import os
from playsound import playsound

basedir = os.path.abspath(os.path.dirname(__file__))

songs = [
    "Ring of Fire - Johnny Cash",
    "Popcorn - Crazy Frog",
    "Corinne Bailey Rae - I'd Do It All Again",
    "Lonely - Akon",
    "Kayne West- Power",
    "Boney M - Rasputin"]

zombie_list = [
    "Postman", 
    "Jay", 
    "Nurse", 
    "Doctor", 
    "Homeless man", 
    "Cat Lady"]


def text_reader(paragraph):
    for word in paragraph:
        sleep(0.0169)
        sys.stdout.write(word)
        sys.stdout.flush()


def console_wipe():
    os.system("\n\ncls")
    pass


def rng_roll():
    global rng
    rng = random.randint(1,20)


def welcome():
    console_wipe()
    console_wipe()
    print("\33[1;35;40m      _                  _ _   _ _ _ _ _      _           _ _ _ _ _ _                                                  _ _ _ _ _ _ _                       ")
    print("\33[1;35;40m    /\ \      _        / / /  /\_ _ _ _ _\   /\_\        /\ _ _ _ _ _\                   _ _ _ _ _ _       _ _ _ _    /_  _ _ _ _ _  /                     ")
    print("\33[1;35;40m    \ \ \    / \ \    / / /  / /   _ _ _ /  / / /       / /   _ _ _ _/_ _ _ _ _ _ _     /  _ _ _   /\     /  _ _  /\  \  \     _ _ _\                      ")
    print("\33[1;35;40m     \ \ \  /   \ \  / / /  / /   /_ _ _   / / /       / /  /     / \   _ _ _ _ _   \   \ \ \    \ \ \   / /   \  \ \  \  \   \/ _ _ _                     ")
    print("\33[1;35;40m      \ \ \/ /\  \ /  / /  / /   _ _ _ /  / / /       / /  /      \  \  \        \   \   \ \ \    \ \ \ / /     \  \ \  \  \     _ _ _\                    ")
    print("\33[1;35;40m       \ \/ / / \    / /  / /   /__ _    / / /       / /  /        \  \  \ _ _ _ _\   \   \ \ \    \ \ / /       \  \ \  \  \  \/ _ _                      ")
    print("\33[1;35;40m        \  / /   \  / /  / /         /  / / / _ _ _ \_/  /_ _ _ _   \  \ _ _ _ _ _ _ _ \   \ \ \    \_ _/         \  \ \  \  \_ _ _ _ _ \                  ")
    print("\33[1;35;40m         \/_/     \/_/   \/_ _ _ _ _/   \/_ _ _ _ _ _/_ _ _ _ _ _/   \ /_ _ _ _ _ _ _  /    \_\/                   \_ \/   \/_ _ _ _ _ _ /                 ")
    print("\33[1;35;40m                                                                                                                                                           ")
    print("\33[1;35;40m                                                                                                                                                           ")
    print("\33[1;35;40m  -------------------------------------------------------------------------------------------------------------------------------------------------------- ")
    print("\33[1;35;40m                                                                                                                                                           ")
    print("\33[1;35;40m                     _ _ _ _ _                                                                                                                             ")
    print("\33[1;35;40m                    /\_ _    _ _\      _ _ _ _                                                    .         .        .             .                       ")
    print("\33[1;35;40m                    \ _ _/\ \        /\    _   \                                                 ..       :.:       :..:           .. .                    ")
    print("\33[1;35;40m                        \  \ \       \ \  \  \  \                                                '''       :..:      :...:         .....                   ")
    print("\33[1;35;40m                         \  \ \       \ \  \_ \  \                                              ''''':       :...:    :....:       :     :                 ")
    print("\33[1;35;40m                          \  \_\       \ \_ _ _ _ \                                             ':    ':       :.  :   :.   .:     :     :           ./:   ")
    print("\33[1;35;40m                           \ /_ /       \/_ _ _ _ /                                             ' :   ':       :.  :  :.    :     :    :         .. ..:    ")
    print("\33[1;35;40m                                                                                                 ':    ':.     :.  :  :.    :    :    :      .  . .:.      ")
    print("\33[1;35;40m                                                                                                  ':     :.    :.  :  .:    :    :     .     . .  :..      ")
    print("\33[1;35;40m                                                                                                   '::    :.  .:    . ..    :   ::     :   . : .           ")
    print("\33[1;35;40m                                                                                                     ':    :. .:     :.     :   :     . . . :              ")
    print("\33[1;35;40m                  _ _ _                                                                 _ _ _         ':    ..:    .:      :  :        . ::                ")
    print("\33[1;35;40m                /\ _ _ _\ _ _ _ _        _ _ _ _ _             _ _ _ _ _ _             /    \ \        ':    .:    .:      : :         ::                  ")
    print("\33[1;35;40m                \/_ _   /_ _ _ _  /\   /   _ _ _  / _ _ _     /   _ _ _   /\          /  /\  \ \        ':        ..       :           :                   ")
    print("\33[1;35;40m                   / / /\   _ _   \ \   \  \ \  /\    _ _  \  \  \ \    \ \ \        /  /_ \  \ \        ':                         :                      ")
    print("\33[1;35;40m                  / / /  \ \    \  \  \  \  \ \ \ \  \   \  \  \  \ \    \ \ \      /  /_ _ \  \ \        ':                       :.                      ")
    print("\33[1;35;40m                 / / /    \ \    \  \  \  \  \ \ \ \  \_ _\  \  \  \ \    \ \ \    /  /      \  \ \        ':                     :                        ")
    print("\33[1;35;40m                / / / _ _  \ \_ _ _  \  \  \  \ \ \ \ _ _ _  _\  \  \ \    \ \ \  /  /        \  \ \        ':  :                 .:                       ")
    print("\33[1;35;40m                \/_ _ _ _/  \ _ _ _ _ \ /   \_ \/  \/_ _ _ _  /   \ _\/     \_\/ /_ /          \ _\/         '::                 :                         ")
    print("\33[1;35;40m                                                                                                                :                 :                        ")
    print("\33[1;35;40m                                                                                                                @: @               :                       ")
    print("\33[1;35;40m                                                                                                                : @ @@              :                      ")
    print("\33[1;35;40m                                                                                                                 :  @ @             :                      ")
    print("\33[1;35;40m                                                                                                                 @ :@ @              :                     ")
    print("Disclaimer:\nAll views and underlying messages expressed in this game are for entertainment purposes only and not to be taken seriously.")
    print('\nLoading game...(enjoy the intro music)')
    playsound(basedir + "/sounds/welcome_screen.mp3")
    input("\nPress enter to start your zorona experience!")
    start_game()


def start_game():
    console_wipe()
    text_reader("The Coronavirus Pandemic has been rampaging through society for the past year although that is all about to change...")
    text_reader("\n\n...With great anticipation, multiple vaccine candidates have been announced and are being rolled out!")
    text_reader("\n\nYou are one of the lucky few in the quaint market town of Market Harborough going to receive their innoculation.")
    sleep(1)
    text_reader("\n\nAlthough all is not as it seems...")
    sleep(2)
    text_reader(f"\n\nYou make your way down to the local hospital of Market Harborough to receive your Coronavirus vaccine, listening to {random.choice(songs)} on your mobile phone.\n\nYou see the local crazy cat lady looking more derranged than usual...")
    text_reader("\n\n...She starts running towards you abruptly and is yelling although you can’t hear her.  After taking off your headphones, you hear her shouting, ‘THE VACCINE WILL BE THE END OF US ALL!’.")
    text_reader("\n\nRegardless, you carry on...")
    text_reader("\n\nAs you approach the hospital you see that a small queue has formed leading out of the door so, RESPONSIBLY, you wear your mask and join the socially distanced queue.")
    text_reader("\n\nWhilst waiting patiently, you see a nurse shamble forwards with her head down. ")
    text_reader("\n\nA fellow vaccine receiver in the queue steps forward and asks if the nurse is okay...")
    sleep(0.5)
    text_reader("\n\n...suddenly, the nurse lunges forward with a scream and bites the person’s neck.")
    playsound(basedir + "/sounds/girlfriendzombieattack.mp3")
    text_reader("\n\nChaos breaks out and everybody begins running away in terror.  Confused and scared, you sprint away from the scene trying to understand what just happened.")
    sleep(0.5)
    text_reader("\n\nYou find a quiet alley to collect your thoughts.  With shaking hands, you instinctively pull out your phone...")
    sleep(0.5)
    while True:
        try:
            choice = int(input("\n\nWhat do you do?\n1. Call partner to warn them\n2. Check phone for news\n3. Use social media\n\nPlease enter a choice: "))
        except ValueError:
            text_reader("\n\nPlease input a number between 1 and 3.")
            continue
        if 1 <= choice <= 3:
            break
        else:
            text_reader("\n\nPlease input a number between 1 and 3.")
    console_wipe()
    if choice == 1:
        text_reader("You call your partner and tell them what’s just happened at the hospital and tell them to stay indoors.")
    if choice == 2:
        text_reader("You check the news and find out all sources are broadcasting news of vaccinated patients going feral and biting other people.")
    if choice == 3:
        text_reader("A zombie behind is extremely busy feasting on it’s poor victim.  You make a video and upload it online to increase awareness.")
    packing()


def packing():
    global drink_choice
    global weapon_choice
    global food_choice
    text_reader("\n\nWith distant screams and murmouring, you check the coast is clear before sprinting down side roads and backflipping over cars until you see your porch way is still untouched.")
    sleep(0.5)
    text_reader("\n\nYou pull out your keys and stumble into the house. Despite feeling discombobulated, you begin packing.")
    sleep(0.5)
    text_reader("\n\n'Should probably pack something to drink...'\n1. Special brew\n2. Evian water\n3. Blue WKD\n4. Lambrini")
    while True:
        try:
            drink = int(input("\n\nWhat drink do you choose? (Please enter a number): "))
            console_wipe()
        except ValueError:
            text_reader("\n\nYou did not pick a number!") 
            continue
        if 1<= drink <=4:
            break
        else:
            text_reader("\n\nThat's not an option!") 
    if drink == 1:
        drink_choice = "Special Brew"
    if drink == 2:
        drink_choice = "Evian water"
    if drink == 3:
        drink_choice = "Blue WKD"
    if drink == 4:
        drink_choice = "Lambrini"
    text_reader("'Going to need some food too...'\n1. Rice and peas\n2. Spaghetti bolognese\n3. Cheese sandwich\n4. Tinned beans")
    while True:
        try:
            food = int(input("\n\nWhat food do you pick? (Please enter a number): "))
            console_wipe()
        except ValueError:
            text_reader("\n\nYou did not pick a number!") 
            continue
        if 1<= food <=4:
            break
        else:
            text_reader("\n\nThat's not an option!")
    console_wipe() 
    if food == 1:
            food_choice = "Rice and peas"
    if food == 2:
            food_choice = "Spaghetti bolognese"
    if food == 3:
            food_choice = "Cheese sandwich"
    if food == 4:
            food_choice = "Tinned beans"
    sleep(0.5)
    text_reader("'I'm going to need to defend myself...'\n1. Cricket bat.\n2. Kitchen knife.\n3. Magazine.\n4. Box of cornettos")
    while True:
        try:
            weapon = int(input("\n\nWhat weapon do you choose? (Please enter a number): "))
        except ValueError:
            text_reader("\n\nYou did not pick a number!") 
            continue
        if 1<= weapon <= 4:
            break 
        else:
            text_reader("\n\nThat's not an option!")
    
    if weapon == 1:
        weapon_choice = "Cricket bat"
    if weapon == 2:
        weapon_choice = "Kitchen Knife"
    if weapon == 3:
        weapon_choice = "Magazine"
    if weapon == 4:
        weapon_choice = "Box of cornettos"
    
    console_wipe()
    text_reader(f"You pack some {drink_choice.lower()}, {food_choice.lower()}, and a {weapon_choice.lower()} into your rucksack and prepare to get going.")
    text_reader("\n\nAs you finish packing, you suddenly hear a strange alarm. It's your mobile phone - a national announcement for the public to evacuate blares and flashes, taking up the whole screen...")
    text_reader("\n\n'Come to the Isle of Wight! People who have not been jabbed are welcome...We are your salvation'")
    text_reader("\n\nSnatching the last of the loo roll, you receive a text from a mate.  Informing you to take refuge at their uncle's farmhouse... ") 
    sleep(0.5)
    text_reader("\n\n'What should I do...?'\n1. Get to the farmhouse.\n2. Head straight to the coast.\n3. Go collect up your partner.\n4. Stay at your house and get bloody wasted!")
    while True:
        try:
            choice = int(input("\n\nWhat do you do? (Please enter a number): "))
        except ValueError:
            text_reader("\n\nYou did not pick a number!") 
            continue
        if 1 <= choice <= 4:
            break 
        else:
            text_reader("\n\nThat's not an option!")
    console_wipe()
    if choice == 1:
        farmhouse()
    if choice == 2:
        coast()
    if choice == 3:
        partner()
    if choice == 4:
        return game_lose("home")
    
    
def farmhouse():
    text_reader("You ask your friend for directions to his uncle's farmhouse and realise you will need a vehicle to get there.")
    if zombie_attack() == True:
        vehicle()
        text_reader("\n\nAfter a long and arduous journey, you finally reach the isolated farmhouse.")
        sleep(0.5)
        text_reader("\n\nApproaching slowly and carefully, weapons in hand, you knock on the aged, wooden door of the farmhouse. With three echoing knocks and an anxious wait, the locks open up and you see your friend who is ecstatic to have company.")
        sleep(0.5)
        text_reader("\n\nYour friend invites you in and asks if you want to see his horses...")
        sleep(0.5)
        text_reader("\n\nAs you enter the stable, a bloodthirsty zombie lunges out from behind a horse..!!!")
        playsound(basedir + "/sounds/Zombie-Attack.mp3")
        text_reader("\n\nYou look around and make use of your surroundings...")
        sleep(0.5)
        text_reader("\n\nFriend: 'OH SHIT OH SHIT. KILL IT. KILL IT QUICK!'\n1. Grab a spade.\n2. Grab a pitchfork\n3. Grab a bale of hay.\n4. Grab a lasso")
        while True:
            try:
                selected = int(input("\n\nWhat do you do? (Please enter a number): "))
            except ValueError:
                text_reader("\n\nYou did not pick a number! Please enter an option from the list.") 
                continue
            if 1 <= selected <= 4:
                break 
            else:
                text_reader("\n\nThat's not an option! Please enter a number between 1 and 4") 
        console_wipe()
        if selected == 1:
            text_reader("\n\nYou grab the spade and using you full body weight you smack the zombie across the head, knocking it down suddenly it gets back up and starts running at you!\n")
            sleep(0.5)
            text_reader("\n\nYou lift the spade above your head and smack it again and again and again until the walls are painted with blood.")
        elif selected == 2:
            text_reader("\n\nUsing the pitchfork you pierce the zombie through its cornea, narrowly missing your friend's head!!! The zombie becomes lifeless as both you and your friend breathe a sigh of relief.")
            sleep(0.5)
        elif selected == 3:
            return game_lose("hay")
        elif selected == 4:
            text_reader("\n\nYou grab the lasso and like Wonder Woman you spin it around and catch the zombie from its neck.\nYou pull and the zombie falls on its back and impales itself on a wooden stake.") 
            sleep(0.5)
        text_reader("\n\nAfter the zombie attack, you and your friend, shaken by the danger, go back into the main house and lock all the doors and windows.") 
        sleep(3)   
        text_reader("\n\nNow the house has been secured, you both sit down and discuss what to do next.")
        sleep(3)
        text_reader("\n\nChoose an action.\n1. 'This island sounds promising, lets go there.'\n2. 'I think we've both had the worst day ever and could do with a drink to relax.'\n3. 'We have food for months in here, let's barricade all of the windows, have a pint and wait for this all to blow over.'")
        while True:
            try:
                selected_farmhouse = int(input("\n\nWhat do you do? (Please enter a number): "))
            except ValueError:
                text_reader("\n\nYou did not pick a number! Please enter a number between 1 and 3.") 
                continue
            if 1 <= selected_farmhouse <= 3:
                break
            else:
                text_reader("\n\nThat's not an option! Please enter a number between 1 and 3.") 
        console_wipe()
        if selected_farmhouse == 1:
            coast()
            #run coast function
        elif selected_farmhouse == 2:
            playsound(basedir + "/sounds/Zombie-Attack.mp3")
            return game_lose("fridge")
        elif selected_farmhouse == 3:
            text_reader("\n\nYou have spent 3 weeks in the bunker...") 
            text_reader("\n\nYou and your friend are anxious and bored he decides to go out for some fresh air")
            sleep(0.5)
            text_reader("\n\nAfter a few hours you get worried and start to wonder where has he gone..")
            while True:
                try:
                    choice = int(input("\n\nWhat do you do?\n1. Go and try to find him?\n2. Fuck him he's an idiot\n"))
                except ValueError:
                    text_reader("\n\nPlease input a number between 1 and 2:\n")
                    continue
                if 1 <= choice <= 2:
                    break
                else:
                    text_reader("\n\nPlease input a number between 1 and 2:\n")
            console_wipe()
            if choice == 1:
                text_reader(f"\n\nYou gear up with your trusty {weapon_choice.lower()} and some {food_choice.lower()} for a light snack and head out into the vast countryside to find your friend")
                sleep(0.5)
                text_reader("\n\nAfter searching for a while..")
                if zombie_attack() == True:
                    text_reader("\n\nAfter defeating the zombie you hear a cry for help in the distance.\nYou run forwards and find your friend surrounded by a hoard of zombies.")
                    while True:
                        try:
                            choice = int(input("\n\n1. Try to save your dear friend\n2. It's not too late to go back now...\n\n(Pick a number): "))
                        except ValueError:
                            text_reader("\n\nPlease input a number between 1 and 2: ")
                            continue
                        if 1 <= choice <= 2:
                            break
                        else:
                            text_reader("\n\nPlease input a number between 1 and 2: ")
                    console_wipe()                          
                    if choice == 1:
                        rng_roll()
                        text_reader(f"\n\nYou run towards your friend wielding your {weapon_choice.lower()} like a madman!")
                        if rng >= 10:
                            playsound(basedir + "/sounds/Zombie-Attack.mp3")
                            text_reader("\n\nYou smack zombies out of the way. Screaming like a madman as you run towards your friend you push a zombie off his back and you both fight off the hoard...")
                            sleep(1)
                            text_reader("\n\nLuckily you both make it.")
                            text_reader("\n\nYou make your way back to the farmhouse and hide out...")
                            text_reader("\n\nAfter a while you hear a helicopter above the farmhouse suddenly...")
                            text_reader("\n\n'Hello.... Hello....'\nYou are rescued by the UN anti zombie force.\nThey have wiped out most of the zombies with a few left in other remote areas.\nYou and your freind survive its a shame about your partner though.")
                            return game_win("farmhouse")
                        else:
                            playsound(basedir + "/sounds/Zombie-Attack.mp3")
                            text_reader("\n\nYou smack zombies out of the way. Screaming like a manman as you run towards your friend you trip off a branch and fall forwards into the hoard.")
                            sleep(0.5)
                            text_reader("\n\nThey make quick work of you.")
                            return game_lose("farmhouse_rescue")
                    if choice == 2:
                        text_reader("\n\nYou selfishly decide to go back to the cabin and look after your own skin.")
                        if zombie_attack() == True:
                            sleep(0.5)
                            text_reader("\n\nAfter a while you hear a helicopter above the farmhouse suddenly...")
                            text_reader("\n\n'Hello.... Hello....'\nYou are rescued by the UN anti zombie force.\nThey have wiped out most of the zombies with a few left in other remote areas.\nYou survived but all your loved ones have died.")
                            return game_win("farmhouse")
            if choice == 2:
                text_reader("\n\nYou selfishly decide to stay safely indoors and look after your own skin")
                sleep(0.5)
                text_reader("\n\nAfter a while you hear a helicopter above the farmhouse suddenly...")
                text_reader("\n\n'Hello.... Hello....'\nYou are rescued by the UN anti zombie force.\nThey have wiped out most of the zombies with a few left in other remote areas.\nYou survived but all your loved ones have died.")
                return game_win("farmhouse")


def coast():
    text_reader("You realise that to get to the coast you will need a car...")
    if zombie_attack() == True:
        vehicle()
        text_reader("\n\nAfter a long and tiring drive, you see the coast and have finally made it.\n\nIn the distance you see a boat is filling with people and is about to depart.  After driving as fast as you can, the boat sets off without you... ")
        text_reader("\n\n...and the sound of your vehicle has attracted a horde of zombies behind...")
        sleep(0.5)
        text_reader("\n\nThe boat which left doesn’t seem that far away...\nyou also find a box of flares on the pier and several other boats tied up.")
        sleep(0.5)
        text_reader("\n\nChoose an option: ")
        while True:
            try:
                choice = int(input("\n\n1. Swim for the departed boat.\n2. Signal the boat with flares.\n3. Get your own boat.\n\nWhat do you do?: "))
            except ValueError:
                text_reader("\n\nPlease input a number between 1 and 3: ")
                continue
            if 1 <= choice <= 3:
                break
            else:
                text_reader("\n\nPlease input a number between 1 and 3: ")
        console_wipe()
        if choice == 1:
                rng_roll()
                if rng >= 10:
                    text_reader("\n\nYou jump into the ocean and swim with all of your might luckily the ships captain see's you frantically swimming towards it and decides to go back to save you, they manage to pull you up with a rope.")
                    game_win("ship")
                else:
                    game_lose("drowning")
        if choice == 2:
                game_lose("flare")
        if choice == 3:
                text_reader("\n\nYou uncover a nearby boat and see it’s in decent working order.\n\nWith the zombie horde nearby, you start pulling on the cord to power the outboard... ")
                sleep(2)
                for i in range(4):
                    rng_roll()
                    if rng > 12:
                        text_reader("\n\nThe engine comes to life and you begin speeding away towards the distant lights of the island")
                        return game_win("boat")
                    elif i == 3:
                        text_reader("\n\nYou took too long and the zombie hoard caught up they rip you appart!\n")
                        return game_lose("slowboat")
                    else:
                        text_reader("\n\nYou pull, and pull....and swear, and pull...\n\n...but the engine refuses to start")
                        text_reader("\n\nA singular zombie ahead of the hoard starts limping towards your boat...")
                        text_reader("\n\nYou have two choices: Fight or Swim.")
                        text_reader("\n\nWhat do you do?")
                        while True:
                            try:
                                choice = int(input("\n\n1. Fight the zombie\n2. Jump into the water and swim to the ship.\n"))
                            except ValueError:
                                text_reader("\n\nPlease input a number between 1 and 2: ")
                                continue
                            if 1 <= choice <= 2:
                                break
                            else:
                                text_reader("\n\nPlease input a number between 1 and 2: ")
                        console_wipe()
                        if choice == 1:
                            rng_roll()
                            if rng >= 5:
                                text_reader(f"\n\nUsing your {weapon_choice} you overpower the zombie and attack it until it's dead.")
                                text_reader("  You quickly move your attention back to the engine...")
                            else:
                                game_lose("fightboat")
                        if choice == 2:
                            rng_roll()
                            if rng >= 10:
                                text_reader("\n\nYou jump into the ocean and swim with all of your might luckily the ships captain sees you frantically swimming towards it and decides to go back to save you, they manage to pull you up with a rope.")
                                game_win("ship")
                            else:
                                game_lose("drowning")

                        sleep(2)
                        text_reader("\n\nYou try to frantically start the engine again...")


def partner():
    text_reader('\n\nAfter packing up your gear, you make your way to your partners house.')
    zombie_attack()
    text_reader("\n\nAfter that bollocks you make your way to your partners house.")
    text_reader('\n\nYou start knocking on the door only to find no response. You knock louder and start shouting for their name.  After looking through the living room window, you see them being attacked by a zombie.')
    playsound(basedir + "/sounds/Zombie-Attack.mp3")
    text_reader('\n\nYou kick the door down and rush into the living room.\n\n"GET IT THE FUCK OFF ME!", they shout as you frantically begin looking for something to use...')
    
    while True:
        try:
            text_reader('\n\nYour partner is getting attacked! Choose a weapon to save them!')
            text_reader('\n\n1: Vase\n2: TV\n3: TV remote\n4: Sofa cushion')
            attack_dict = {
            1: "You pick up the priceless Ming dynasty vase and smash it over the zombie's head in a panic, killing it instantly. Your partner is both relieved you killed the zombie and raging over the vase.",
            2:'You summon your inner rockstar, picking up the TV and beat the zombie to death with it.',
            3: "Thinking it was an excellent idea, you throw the TV remote at the zombie, causing it to pause and divert it's attention to you...",
            4:'With nothing else being nearby, you begin to helplessly bash the zombie repeatedly with the cushion...'}
            weapon_dict = {
                1: 'Vase',
                2: 'TV',
                3: 'TV remote',
                4: 'Sofa cushion'
            }
            attack_choice = int(input("\n\nWhat do you choose?: "))
            console_wipe()
            text_reader('\n\n'+attack_dict[attack_choice])
            break
        except KeyError: 
            text_reader("\n\nPlease pick an option from the list!")
        except ValueError:
            text_reader("\n\nPlease enter a number from the list!")
    console_wipe()
    # Good decision -> fight partner -> choose scenario
    # Bad decision -> both people die
    # Bad decision, but successful rng -> fight partner -> choose scenario
    # Good decisions:
    if attack_choice == 1 or attack_choice == 2:
        partner_fight = True
        choose_scenario = True
    # Bad decisions: 
    if attack_choice == 3 or attack_choice == 4:
        rng_roll()
        # Successful RNG:
        if rng >= 15:
            text_reader("\n\n...surprisingly, your poor decision making has paid off! The zombie begins frantically throwing it's hands around in annoyance and wanders away.")
            partner_fight = True
            choose_scenario = True
        else:
            text_reader(f"\n\n...why would you ever use a {weapon_dict[attack_choice].lower()} to kill a freaking ZOMBIE??")
            text_reader("\n\nNeedless to say, the zombie bites your partner and the two of them are just too much for you to overcome...")
            partner_fight = False
            choose_scenario = False
    # Fighting partner as a zombie
    if partner_fight == True:
        text_reader("After the surprise attack, both of you are relieved to see each other and are thankful both of you are still alive and have a long, drawn out hug...")
        playsound(basedir + "/sounds/girlfriendzombieattack.mp3")   
        text_reader("\n\n...but it's too little too late. You feel the wet feeling of an oozing wound...your bitten partner, already turned, snarls and lunges at you!")
        # RNG
        rng_roll()
        if rng < 2:  
            sleep(5)
            choose_scenario = False
        else:
            choose_scenario = True
    # Choose scenario == True i.e. player survived
    if choose_scenario == True:
        text_reader("\n\nThe struggle is hard and grim.  You look into the eyes of your partner and see a glimmer of humanity, but, deep down, you know they can't be saved.")
        sleep(0.5)
        text_reader("\n\nCovered in blood and surrounded by two dead bodies, the gravity of the situation is dampened by the shock of what's just happened.")
        sleep(2)
        text_reader("\n\nYou cry alone in your partners house and take a moment to grieve before making your next move.")
        sleep(1)
        while True:
            try:
                # Choose a scenario
                text_reader("\n\n'I need to get out of here...'\n1: Go to the coast.\n2: Go to friends farmhouse.\n3: Barricade house and bunker down.")
                partner_choice = int(input('\n\nWhat do you do? Enter an option: '))
                partner_choice_dict = {
                    1: "You decide to pack up what supplies you can and escape to the small island off the coast, hoping it's not too late.",
                    2: "You prepare for the journey ahead to your friends isolated farmhouse and hope they're still alive.",
                    3: "'This is it. This is the end of the world'. You use the remaining household items available and barricade all the entrances and wait for the end of world..."
                    }
                console_wipe()
                text_reader(partner_choice_dict[partner_choice])
                sleep(1)
                break
            # Error captures
            except KeyError: 
                text_reader("\n\nPlease pick an option from the list!")
            except ValueError:
                text_reader("\n\nPlease enter a number from the list!")
        if partner_choice == 1:
            return coast()
        # Farmhouse scenario 
        if partner_choice == 2:
            return farmhouse()
        # Lose screen
        if partner_choice == 3:
            return game_lose("home")
    # Choose Scenario == False i.e. player died
    else:
        sleep(3)
        return game_lose("partner")


def zombie_attack():
    text_reader(f"\n\nSuddenly! A zombie {random.choice(zombie_list)} jumps forwards and starts staggering towards you!")
    playsound(basedir + "/sounds/Zombie-Attack.mp3")
    text_reader("\n\nThe zombie is slowly approaching you...")
    sleep(0.5)
    while True:
        try:
            choice=int(input("\n\nWhat do you do?\n1. Run \n2. Fight!\n\nMake a decision!: "))
        except ValueError:
            text_reader("\n\nThat's not a number.")
            continue
        if 1 <= choice <= 2:
            break
        else:
            text_reader("\n\nPick a number between 1 and 2!")

    console_wipe()

    # Choice 1: Run
    if choice == 1:
        text_reader(f"You instantly throw your {food_choice.lower()} at the zombie turn around and start sprinting away!")
        sleep(0.5)
        rng_roll()
        if rng >= 12:
            text_reader(f"\n\nYour {food_choice.lower()} was a great distraction and you manage to escape from the zombie!")
            text_reader(f"\n\nMagically, your {food_choice.lower()} returns to you - as if you're in a computer game!")
            return True
        else:
            return game_lose("zombie_run")

    # Choice 2: Fight
    if choice == 2:
        text_reader(f"You quickly use your {weapon_choice.lower()} and attack the zombie!")
        sleep(0.5)
        rng_roll()
        if rng >= 5:
            text_reader(f"\n\nYou manage to smash the zombie on the head using your {weapon_choice.lower()}, knocking it out temporarily.")
            return True
        else:
            return game_lose("zombie_fight")


def vehicle():
    """
    vehicle function docstring:

    Runs the vehicle() scenario:
        - Goes through roleplay text until it asks to pick a vehicle:
            1. Is 100 % chance of winning.
            2. and 3. Calls the rng_roll function to roll a random number and base the outcome on the result.
            4. Is 100% lose. 
    """
    # Roleplay text
    text_reader("\n\nAfter scanning the road outside littered with abandoned vehicles, you see four potential options in front of you...")
    text_reader(f"\n\nBefore heading into the unknown, you take a hefty swig of your {drink_choice}...")
    # User input
    while True:
        try:
            car_choice = int(input("\n\n'I hope none of these are lemons...'\n1. VW Passat\n2. Ford Focus\n3. Honda Civic\n4. Mazda MX5\n\nPlease choose an option: "))
        except ValueError:
            text_reader("\n\nPlease input a number between 1 and 4: ")
            continue
        if 1 <= car_choice <= 4:
            break
        else:
            text_reader("\n\nPlease input a number between 1 and 4: ")
    
    console_wipe()
    
    # Choice 1: 100% win
    if car_choice == 1:
        text_reader("As you get into the VW Passat, you’re lucky it’s in full working order with a full tank and you set off without any problems.")
    
    # Choice 2: RNG aspect
    if car_choice == 2:
        text_reader("The car starts up without any problems although part way to the destination, the petrol light comes on.  You see a Shell garage with a few shambling zombies by the pumps... ")
        text_reader("\n\nYou drive in slowly to the fuel pumps and try not to disturb any of the surrounding zombies...")
        rng_roll()
        if rng >= 10:
            text_reader("\n\nYou quietly fill up your vehicle and, miraculously, do not alert any of the zombies in the area.  Once you have finished, you rapidly accelerate out of the petrol station.")
        else:
            if zombie_attack() == True:
                text_reader("\n\nAfter beating the zombie you quietly make your way back to the car and speed off running over 3 other zombies luckily you have just enough fuel.")
            else:
                return game_lose("fuel")
    
    # Choice 3: RNG aspect
    if car_choice == 3:
        text_reader("The car starts up without any problems although part way to the destination, the petrol light comes on.  You see a Shell garage with a few shambling zombies by the pump... ")
        text_reader("\n\nYou drive in slowly to the fuel pumps and try not to disturb any of the surrounding zombies ")
        rng_roll()
        if rng >= 10:
            text_reader("\n\nYou quietly fill up your vehicle and miraculously do not alert any of the zombies in the area.  Once you have finished, you rapidly accelerate out of the petrol station.")
        else:
            if zombie_attack() == True:
                text_reader("\n\nAfter Defeating the zombie you quickly jump into the car and speed off running over 3 other zombies.  Luckily, you have just enough fuel to get to your end destination.")
            else:
                return game_lose("fuel")
    
    # 100% lose
    if car_choice == 4:
        return game_lose("mazda")


def game_lose(how):
    """
    game_lose function docstring:
    Runs the game_lose() function which accepts the argument of "how" as a string.  
        - "how" determines what output will be displayed.
    Uses a dictionary to determine the output:
        - lose_dict = {input string (how): output}
    """
    console_wipe()
    # dictionary for lose scenarios:
    lose_dict = {
        'hay': "You attempt to lift the bale of hay and realise it weighs a ton the zombie sees you bent over and jumps you. Killing you instantly! Your friend doesn't last much longer",
        "fridge": "A zombie was hiding behind the fridge and you are mercilessly mauled in the dim light.\nWASTED!!!",
        "fuel": "Unfortunately the zombies like the smell of petrol.  They notice you, and you are lunch!",
        "partner": "Overwhelmed, there is nothing left to do than to accept fate...",
        "home": "You decided to stay at home and ignore all your problems.  It's okay we have all done it, but, in this case, there is a zombie appocolypse going on.\n\n5 hours into your Netflix binge, your annoying neighbor breaks down your door, and eats your flesh.",
        "mazda": "You’re excited to get into your dream sports car only to find it doesn’t work at all.  During the panic of trying to get the car started, a zombie creeps up to the window and drags you out into the street.\n\nYou picked your dream car and now you lose gg",
        "slowboat": "You took too long and the zombie hoard caught up...they rip you apart!",
        "fightboat": f"You are exhausted and with your final strength you use your {weapon_choice.lower()} to attempt to smack the zombie but it was fruitless the bloodthirsty zombie gets his lunch...",
        "zombie_fight": "Your attempt was futile and the zombie bites your face.  Suddenly three OAP zombies jump up and start attacking you, ripping you apart with their nastly old lady teeth.",
        "zombie_run": f"Your {food_choice.lower()} was a great distraction! However while you were looking back laughing at the zombie eating your {food_choice.lower()}, another Zombie comes around the corner and bites your kneck instantly killing you!\n\nWhat are the chances of that? Damn, that's unlucky",
        "farmhouse_rescue": "You tried to save your friend, how honorable unfortunately you are dead",
        "drowning": "You jump into the ocean and swim with all of your might but the boat just gets further and further away.\nThe current of the ocean is just too strong GLUG GLUG GLUG",
        "flare": "You grab a flare gun and launch a flare into the sky, hoping to get the attention of the other boat.\nUnfortunately, they do not turn around\nand the shambling horde behind catches up with you..."}
    
    text_reader(lose_dict[how])
    sleep(2)
    text_reader("\n")
    print(" @@@@@                                        @@@@@")
    print("@@@@@@@                                      @@@@@@@")
    print("@@@@@@@           @@@@@@@@@@@@@@@            @@@@@@@")
    print(" @@@@@@@@       @@@@@@@@@@@@@@@@@@@        @@@@@@@@")
    print("     @@@@@     @@@@@@@@@@@@@@@@@@@@@     @@@@@")
    print("       @@@@@  @@@@@@@@@@@@@@@@@@@@@@@  @@@@@")
    print("         @@  @@@@@@@@@@@@@@@@@@@@@@@@@  @@")
    print("            @@@@@@@    @@@@@@    @@@@@@")
    print("            @@@@@@      @@@@      @@@@@")
    print("           @@@@@@      @@@@      @@@@@")
    print("             @@@@@@    @@@@@@    @@@@@")
    print("             @@@@@@@@@@@  @@@@@@@@@@")
    print("              @@@@@@@@@@  @@@@@@@@@")
    print("           @@   @@@@@@@@@@@@@@@@@   @@")
    print("           @@@@  @@@@ @ @ @ @ @@@@  @@@@")
    print("          @@@@@   @@@ @ @ @ @ @@@   @@@@@")
    print("        @@@@@      @@@@@@@@@@@@@      @@@@@")
    print("      @@@@          @@@@@@@@@@@          @@@@")
    print("   @@@@@              @@@@@@@              @@@@@")
    print("  @@@@@@@                                 @@@@@@@")
    print("   @@@@@                                   @@@@@")
    text_reader("                   YOU ARE DEAD !!!\n")
    playsound(basedir + "/sounds/losescreendeathbyzombie.mp3")
    text_reader("              Do you want to play again?\n\n")
    while True:
        try:
            choice=int(input("\n\n1 for Yes\n2 for No\n"))
        except ValueError:
            text_reader("\n\nPlease choose 1 or 2: ")
            continue
        if 1 <= choice <= 2:
            break
        else:
            text_reader("\n\nPlease input a number either 1 or 2: ")
    console_wipe()
    if choice == 1:
        start_game()
    else:
        credits()


def credits():
        text_reader("Thanks for playing\n") #or thanks for playing
        sleep(1)
        print(r" _____   ____  ____  ____  _   _____ ")
        print(r"/__  /  / __ \/ __ \/ __ \/ | / /   |")
        print(r"  / /  / / / / /_/ / / / /  |/ / /| |")
        print(r" / /__/ /_/ / _, _/ /_/ / /|  / ___ |")
        print(r"/____/\____/_/ |_|\____/_/ |_/_/  |_|")
        text_reader("\n\nThe post apocalyptic zombie game\n")
        sleep(1)
        print("                                .. ")           
        print("                               C C  /")            
        print("                              /<   /   ")          
        print("              ___ __________/_#__=o    ")         
        print("             /(- /(\_\________   \      ")        
        print("              \ ) \ )_      \o     \     ")        
        print("              /|\ /|\       |'     |     ")        
        print("                            |     _|      ")       
        print("                            /o   __\      ")       
        print("                           / '     |      ")       
        print("                         / /      |       ")      
        print("                         /_/\______|       ")      
        print("                        (   _(    <        ")      
        print("                         \    \    \        ")     
        print("                          \    \    |       ")     
        print("                          \____\____\        ")   
        print("                           ____\_\__\_\        ")  
        print("                         /`   /`     o\        ")  
        print("                         |___ |_______|")
        text_reader("")
        text_reader("")
        text_reader("Written by....\n")
        text_reader("   Zamih\n")
        text_reader("      Ismael\n")
        text_reader("         Mike\n")                                    
        text_reader("            Connor\n")
        text_reader("               and Matt\n")    
        print("\n\nTEAM 2 FTW!!")
        input('\n\nPress the enter key to exit.\n')
        exit()


"""
Calls game_win which displays text and the player's win condition
Accepts argument "how" as a string.  This is then used by win_dict uses this as a key to produce output.
"""
def game_win(how):
    win_dict = {
        "ship": "swimming to the ship and getting to the Isle of Wight!",
        "farmhouse": "bunkering down in the farmhouse!",
        "boat": "stealing a boat and getting to the Isle of Wight!"
    }   
    win_txt1 = "CONGRATULATIONS! YOU HAVE REACHED THE END OF THE GAME!"
    win_txt2=(f'You survived the brutal Zorona apocalypse by {win_dict[how]}')
    win_screen(win_txt1,win_txt2)
    
    
def win_screen(win_text1,win_text2):
    sleep(2)
    print('\n\n')
    print("\033[5;31;40m        ________________ _____ _   _    ___            ")
    print("\033[5;31;40m       |__  /  _  | __  \   _  | \ | | /   \           ")
    print("\033[5;31;40m         / /| | | | |_  /  | | |  \| |/ /_\ \          ")
    print("\033[5;31;40m        / / | | | |    /|  | | |     |   _   |         ")
    print("\033[5;31;40m       / / _\ \_/ / | \ \  \_/ / |\  |  | |  |         ")
    print("\033[5;31;40m       \____/\___/\_|  \_|\___/\_| \_/\_| |_/          ")
    print("\033[5;31;40m                                                       ")
    print("\033[5;31;40m -----------------------------------------------------------")
    print("\033[5;31;40m                                                   ")
    print(                    win_text1    )
    print(                    win_text2    )
    print("\033[5;31;40m                                                       ")
    print("\033[5;31;40m  -----------------------------------------------------------")
    print("\033[5;31;40m    __   _______ _   _        _    _ _____  _   _    _  ")
    print("\033[5;31;40m    \ \ / /     | | | |      | |  | |_   _|| \ | |  | | ")
    print("\033[5;31;40m     \ V /| | | | | | |      | |  | | | |  |  \| |  | | ")
    print("\033[5;31;40m      \ / | | | | | | |      | |/\| | | |  |     |  | | ")
    print("\033[5;31;40m      | | \ \_/ / |_| |      \  /\  /_| |_ | |\  |  |_| ")
    print("\033[5;31;40m      \_/  \___/ \___ /       \/  \/ \____/\_| \_|  (_)  \n \n \n ")
    playsound(basedir + "/sounds/victoryfanfare.mp3")
    while True:
        try:
            choice=int(input("            PRESS 1 TO PLAY AGAIN, 2 TO QUIT"))
        except ValueError:
            text_reader("\n\nPlease choose 1 or 2: ")
            continue
        if 1 <= choice <= 2:
            break
        else:
            text_reader("\n\nPlease input a number either 1 or 2: ")
    console_wipe()
    if choice == 1:
        start_game()
    else:
        credits()

welcome()
