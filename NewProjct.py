
#Text based adv game
#Characters - Mitler, Smeg, Kade, Syph, Luke, Muko, Steve, Aurafarmer, WeSeeTheFit, ResidentHomo

import time
import random

class Move:
    def __init__(self, name, requirement=0, stamina_cost=0, damage=0, **attributes):
        self.name = name
        self.requirement = requirement
        self.stamina_cost = stamina_cost
        self.damage = damage

        self.damage_mult = 1.0
        self.move_stun = 0
        self.bleed_damage = 0
        self.self_stun_chance = 0.0
        self.multi_hit = 1
        self.defence_mult = 1.0
        self.stun_reduc_chance = 0.0
        self.dodge_chance_mult = 1.0
        self.stun_chance_reduc = 0.0

        for key, value in attributes.items():
            setattr(self, key, value)

class Characters:
    def __init__(self, Name, Speed, Perception, Power):
        self.name = Name
        self.speed = Speed
        self.critChance = Perception
        self.power = Power
        self.Moves = []
        #player inv
        self.inventory = []
        #stats
        self.Health = 100
        self.AttackBoost = 1
        self.Defence = 1
        self.CritBoost = 1.5
        self.Stamina = 100 
        #likeness
        self.characters_met = [] #AFTER EACH SCENE YOU MUST PLACE ALL NEW CHARACTERS INSIDE 
        self.syph_character_apriciation = 0
        self.steve_character_apriciation = 0
        self.mitler_character_apriciation = 0
        self.smeg_character_apriciation = 0
        self.kade_character_apriciation = 0
        self.luke_character_apriciation = 0
        self.aurafarmer_character_apriciation = 0
        self.weseethefit_character_apriciation = 0
        self.resident_homo_character_apriciation = 0
        self.blacksmith_character_apriciation = 0
        #level handling
        self.Level = 1
        self.BaseExp = 100
        self.Mult = 1.25
        self.ExpBoost = 1
        self.Exp = 0
        self.ExpReq = self.BaseExp * self.Mult * (self.Level - 1) # works as 0 exp for the first level to garuntee a level up
        #skill point stuff
        self.unspent = 0
        self.spent = 0

        def levelup(self):
            self.unspent = self.unspent + 2 #2 sp per level up
            self.level = self.level + 1
            self.exp = 0
            pass

        def UpdateExpReq(self): 
            self.ExpReq = int(self.BaseExp * self.Mult * (self.Level - 1))

        def ScaleCharacter(self): 
            self.Health = 100
            if self.Level > 1: # if this isnt here it sets both of them to 0 from the calculation
                self.Health = self.Health * 1.08 * (self.Level - 1)
                self.AttackBoost = self.AttackBoost * 1.05 * (self.Level - 1)
                self.Stamina = self.Stamina * 1.2 * (self.Level - 1) #large scale amount
        
def spend_skill_points(player_character):
    print(f''' 
    Current Skill Point Investments:
    Speed: {player_character.speed}
    Perception: {player_character.perception}
    Power: {player_character.power}
    You have a total of {player_character.spent} skill points invested.

    You currently have {player_character.unspent} unspent skill points

    ''')
    if player_character.unspent == 0:
        return
    else:
        while player_character.unspent > 0:
            invest_into = int(input('''
            Where would you like to invest into?
            [1] Speed
            [2] Perception
            [3] Power '''))

            if invest_into == 1:
                invest_amount = int(input(f"How much would you like to invest: [YOU HAVE {player_character.unspent} SKILL POINTS]"))
                if invest_amount > player_character.unspent:
                    print("Enter a valid amount of skill points.")
                    continue
                else:
                    player_character.speed = player_character.speed + invest_amount
                    player_character.unspent = player_character.unspent - invest_amount
            elif invest_into == 2:
                invest_amount = int(input(f"How much would you like to invest: [YOU HAVE {player_character.unspent} SKILL POINTS]"))
                if invest_amount > player_character.unspent:
                    print("Enter a valid amount of skill points.")
                    continue
                else:
                    player_character.perception = player_character.perception + invest_amount
                    player_character.unspent = player_character.unspent - invest_amount
            elif invest_into == 3:
                invest_amount = int(input(f"How much would you like to invest: [YOU HAVE {player_character.unspent} SKILL POINTS]"))
                if invest_amount > player_character.unspent:
                    print("Enter a valid amount of skill points.")
                    continue
                else:
                    player_character.power = player_character.power + invest_amount
                    player_character.unspent = player_character.unspent - invest_amount
            else:
                print("Enter a valid option.")
                continue


def unlockable_moves(player_character):

    moves_by_stat = {
        "power": [
            Move("Power Slam", requirement=10, damage=25, stamina_cost=20),
            Move("Gut Punch", requirement=5, damage=12, stamina_cost=10)
        ],

        "speed": [
            Move("Quick Lunge", requirement=6, damage=15, stamina_cost=12)
        ],

        "perception": [
            Move("Eagle Eye", requirement=10, stamina_cost=30, crit_chance_increase=25)
        ]
    }

    for stat, moves in moves_by_stat.items():
        player_value = getattr(player_character, stat)

        for move in moves:
            if player_value >= move.requirement:
                if move.name not in [m.name for m in player_character.Moves]:
                    player_character.Moves.append(move)


    


def SceneIntermission(player_character):
    #intermission between scene switches, give options to check exp, level, skill points, invest skillpoints, learn new moves
    print(f"The scene ends.. {player_character.name} closes their eyes and sees a vision...")
    menu_action = int(input(''' 
    ----------------------------------------------
                    Scene Ended.
    ----------------------------------------------
    | [1] Check skill points                     |                            
    | [2] Check inventory                        |
    | [3] Check character apriciation            |
    | [4] Learn new moves                        |
    | Beware... only 1 action is availible.      |
    |--------------------------------------------|
    '''))

    if menu_action == 1:
        spend_skill_points(player_character)
    if menu_action == 2:
        check_inventory(player_character)
    if menu_action == 3:
        check_character_apriciation(player_character)
    if menu_action == 4:
        unlockable_moves(player_character)

def mini_game():
# rock pull from ni2 yk
    key_selection = ["X", "Z", "C", "V"]
    key_to_press = random.choice(key_selection)
    time_limit_not_reached = True
    while time_limit_not_reached:
        #Create the time limit
        difficulty = int(input("What difficulty? 1: Hard, 2: Medium, 3: Easy"))
        if difficulty == 1:
            difficulty = "Hard"
            time_limit = 3
        elif difficulty == 2:
            difficulty = "Medium"
            time_limit = 5
        elif difficulty == 3:
            difficulty = "Easy"
            time_limit = 10
        #create the timer? i dont know how to do this part so im going in blind
        start_time = time.time()
        score = 0
        while time.time() - start_time < time_limit:
            #NI2 ROCK PULL
            
            key_selection = ["X", "Z", "C", "V"]
            key_to_press = random.choice(key_selection)
            player_presses = input(f"PRESS {key_to_press}").upper()
            if player_presses == key_to_press:
                score = score + 1
                print(score)
                continue
            else:
                continue
        print(f"Game has ended!! you scored {score} points in your alotted {time_limit} seconds!")
        
        if difficulty == "Hard":
            score = score *2
        elif difficulty == "Medium":
            score = score *1.4
        elif difficulty == "Easy":
            score = score
        return score

#USED BY BLACKSMITH SCENE 3 - 4
def create_moves(player_character):

    categories = {
        "burst": {"LegSweep", "SingleSlash", "DropKick", "Warriors_Pride", "Waterfoul"},
        "defence": {"Stance", "PerfectEyesight"},
        "critchance": {"Awaken"}
    }
    
    tutorial = input("Enter Y to see a tutorial for move making. ").upper()
    if tutorial == "Y":
        print('''

There are 3 different types of componants; 
              Burst: Used for damaging and outright killing opponants.
              Defence: Used for bulstering your own defences, granting damage reduction and slight dodge chance.
              Crit Chance: Used to increase player speed and critical hit chances aswell as damage.

There are an infinate possibilities of moves you can create, 
              each move can have a maximum of 3 componants,
              Using a single componant will result in its full power
              Using 2 componants means both will be slightly underpowered
              Using 3 componants maximises varity however those effects can become dulled..

Each componant will have its own unique properties, for example; LegSweep, this is a burst move, dealing low amounts of damage however stuns the opponant for a turn.

''')
    #Create componant functionality:
    possible_components = {
        "LegSweep": Move("LegSweep", damage_mult=1.03, move_stun=1),
        "SingleSlash": Move("SingleSlash", damage_mult=1.07, bleed_damage=13),
        "DropKick": Move("DropKick", damage_mult=1.095),
        "Warriors_Pride": Move("Warriors_Pride", damage_mult=1.2, self_stun_chance=0.3),
        "Waterfoul": Move("Waterfoul", damage_mult=0.80, multi_hit=3),
        "Stance": Move("Stance", defence_mult=1.2, stun_reduc_chance=0.7),
        "PerfectEyesight": Move("PerfectEyesight", dodge_chance_mult=1.3, stun_chance_reduc=0.9)
    }
    print("You have been granted the opportunity to create a move for free...")

    try:
        components_amount = int(input("How many components would you like to use? [1, 2, 3]: "))
    except:
        print("Invalid number.")
        return

    if components_amount not in [1, 2, 3]:
        print("The blacksmith refuses your impossible request...")
        player_character.blacksmith_character_apriciation -= 10
        return

    components_used = []

    while len(components_used) < components_amount:
        print("\nAvailable components:")
        for name in possible_components:
            print("-", name)

        select = input("Choose a component: ").strip()

        if select in possible_components:
            components_used.append(possible_components[select])
        else:
            print("Invalid component.")

    while True:
        new_move_name = input("Give your new move a name (3-12 chars): ")

        if 3 <= len(new_move_name) <= 12:
            break
        else:
            print("Name must be between 3 and 12 characters.")

    #Combine components into one final Move 

    final_move = Move(new_move_name)

    for comp in components_used:
        final_move.damage_mult += (comp.damage_mult - 1)
        final_move.move_stun += comp.move_stun
        final_move.bleed_damage += comp.bleed_damage
        final_move.self_stun_chance += comp.self_stun_chance
        final_move.multi_hit += (comp.multi_hit - 1)
        final_move.defence_mult += (comp.defence_mult - 1)
        final_move.stun_reduc_chance += comp.stun_reduc_chance
        final_move.dodge_chance_mult += (comp.dodge_chance_mult - 1)
        final_move.stun_chance_reduc += comp.stun_chance_reduc

    # Nerf based on number of components
    if components_amount == 2:
        nerf = 0.7
    elif components_amount == 3:
        nerf = 0.5
    else:
        nerf = 1

    final_move.damage_mult *= nerf
    final_move.defence_mult *= nerf

    player_character.Moves.append(final_move)

    print(f"New move created: {final_move.name}")
    


    #uses componant system
    #16 componants
    #8 for burst 4 for defence 4 for critchance
    #each has diff affects (multipliers)

def check_inventory(player_character):
# check player inventory [make a table inside class for it]
# if it is empty give an option to go foraging for health supplys (berrys) 2 berrys at most, make a minigame for it
    if len(player_character.inventory) == 0:
        print("My inventory seems empty... no matter ill go foraging for some supplys.")
        results = mini_game()
        print(f"results - {results}")
        possible_rewards = ["Mixed Berry", "LevelUp Crystal", "ExpUp Crystal","Sword of Doom","HealthUp Crystal", "RandomComponant Crystal","PowerfulComponant Crystal"]

        if results > 10:
            for x in range(1,3):
                given_rewards = random.choice(possible_rewards)
                player_character.inventory.append(given_rewards)
                print(f"Item Found!: {given_rewards}")
        elif results > 15:
            for x in range(1,5): 
                given_rewards = random.choice(possible_rewards)
                player_character.inventory.append(given_rewards)
                print(f"Item Found!: {given_rewards}")
        elif results > 25:
            for x in range(1, 7):
                given_rewards = random.choice (possible_rewards)
                player_character.inventory.append(given_rewards)
                print(f"Item Found!: {given_rewards}")
        else:
            for x in range(1,2):
                given_rewards = random.choice(possible_rewards)
                player_character.inventory.append(given_rewards)
                print(f"Item Found!: {given_rewards}")
            
        #append item into inventory
    else:
        #Create an inventory GUI (like scene intermission with items inside)
        while True:
            for i, item in enumerate(player_character.inventory, start=1):
                print(f"{i}. {item}")

            print("\nOptions:")
            print("U <number> - Use item")
            print("D <number> - Drop item")
            print("Q - Quit inventory")

            choice = input("> ").strip().lower()

            if choice == "q":
                break

            try:
                action, index = choice.split()
                index = int(index) - 1
                item = player_character.inventory[index]

                if action == "u":
                    use_item(player_character, item)
                    player_character.inventory.pop(index)
                elif action == "d":
                    player_character.inventory.pop(index)
                    print(f"You dropped {item}.")
                else:
                    print("Invalid action.")

            except (ValueError, IndexError):
                print("Invalid input.")

                               
        
def use_mixed_berry(player_character):
    player_character.health = player_character.health + 70
    print("Mixed Berry used! you healed 70 hit points!")
    
def use_levelup_crystal(player_character):
    player_character.level = player_character.level + 1
    print(f"Level up crystal used! you leveled up to: {player_character.level}")

def use_expup_crystal(player_character):
    player_character.exp = player_character.exp + 350
    print(f"You used an EXP up crystal and gained 350 exp!")

def use_sword_of_doom(player_character):
    player_character.health = player_character.health - 30
    print("""
          You pick up the sword... your hands trembling at its immense power radiating from itself. You lay it across your shoulder admiring its expert craftsman ship.. 'wait... is that.. black paint?!'  
          
          It seems the infamous fraud mitler was the previous owner of this sword... useless.
          You throw the sword away as far as you can and accidently nick yourself on the finger as it flys away..
          [30 DAMAGE TAKEN.]""")
    pass

def use_healthup_crystal(player_character):
    player_character.health = player_character.health + 250
    print("You used a health up crystal! you healed 250 hit points")

def use_random_component_crystal(player_character):
    possible_componants = {
    "LegSweep": {"damage_mult": 1.03, "move_stun": 1},
    "SingleSlash": {"damage_mult": 1.07, "bleed_damage": 13},
    "DropKick": {"damage_mult": 1.095},
    "Warriors_Pride": {"damage_mult": 1.2, "self_stun_chance": 0.3},
    "Waterfoul": {"damage_mult": 0.80, "multi_hit": 3},
    "Stance": {"defence_mult": 1.2, "stun_reduc_chance": 0.7},
    "PerfectEyesight": {"dodge_chance_mult": 1.3, "stun_chance_reduc": 0.9}
}
    random_componant = random.choice(possible_componants)
    player_character.inventory.append(random_componant)
    print(f"You used a random componant crystal and found {random_componant}! Congrats")
    

def use_powerful_component_crystal(player_character):
    possible_componants = {
    "LegSweep": {"damage_mult": 1.03, "move_stun": 1},
    "SingleSlash": {"damage_mult": 1.07, "bleed_damage": 13},
    "DropKick": {"damage_mult": 1.095},
    "Warriors_Pride": {"damage_mult": 1.2, "self_stun_chance": 0.3},
    "Waterfoul": {"damage_mult": 0.80, "multi_hit": 3},
    "Stance": {"defence_mult": 1.2, "stun_reduc_chance": 0.7},
    "PerfectEyesight": {"dodge_chance_mult": 1.3, "stun_chance_reduc": 0.9}
}
    random_componant = random.choice(possible_componants)
    player_character.inventory.append(random_componant)

def use_item(player_character, item_used):
    possible_items = ["Mixed Berry", "LevelUp Crystal", "ExpUp Crystal","Sword of Doom","HealthUp Crystal", "RandomComponant Crystal","PowerfulComponant Crystal"]
    if item_used in possible_items:
        #use item logic
        item_actions = {
    "Mixed Berry": use_mixed_berry(player_character),
    "LevelUp Crystal": use_levelup_crystal(player_character),
    "ExpUp Crystal": use_expup_crystal(player_character),
    "Sword of Doom": use_sword_of_doom(player_character),
    "HealthUp Crystal": use_healthup_crystal(player_character),
    "RandomComponant Crystal": use_random_component_crystal(player_character),
    "PowerfulComponant Crystal": use_powerful_component_crystal(player_character)
    }

    action = item_actions.get(item_used)

    if action:
        action()
    else:
        print("This item can't be used.")
        pass
    

def check_character_apriciation(player_character):
# ask for a character to look at, show apriciation and some words on what that may mean
    if len(player_character.characters_met) == 0:
        print("You havent met any characters... how is that even possible??")
    character_to_find = input(f"Which of the characters you have met would you like to see..? [OPTIONS: {player_character.characters_met}]").lower()
    if character_to_find in player_character.characters_met:
        #character name -> apriciation chart
        character_to_apriciation_checker = [
        {"steve": player_character.steve_character_apriciation},
        {"syph": player_character.syph_character_apriciation},
        {"mitler": player_character.mitler_character_apriciation},
        {"smeg": player_character.smeg_character_apriciation},
        {"kade": player_character.kade_character_apriciation},
        {"luke": player_character.luke_player_apriciation},
        {"aurafarmer": player_character.aurafarmer_character_apriciation},
        {"weseethefit": player_character.weseethefit_character_apriciation},
        {"resident_homo": player_character.resident_homo_character_apriciation}]
        
        print(f"{character_to_find} apriciation meter for you is at {character_to_apriciation_checker[character_to_find]}")

def RoomOneIntro():
    print('''
    You wake up still groggy, your head is banging against your skull, coming towards you, slowly, rolling, someone approches..
    ''')
    #get players name + intro
    try:
        player_name = input("Hey! My names Steve! although you can call me  Sir if you want! whats your name?")
        if len(player_name) > 12 or len(player_name) < 3:
            raise ValueError
    except ValueError:
        print("Ensure your name is within 3 - 12 digits!") 

    #Get Player Stats
    player_information = {"Speed": 0, "Power": 0, "Perception": 0}
    player_stat_points = 7
    if player_stat_points != 0 :
        stat_points_unspent = True
    while stat_points_unspent == True:
        get_player_speed = int(input(f"So hey, tell me about yourself and your strengths- How fast are you? (0-10) : [YOU HAVE {player_stat_points} STAT POINTS TO SPEND.]: "))
        if get_player_speed > player_stat_points:
            print("Ensure you only spend stat points you have.")
            continue
        player_stat_points = player_stat_points - get_player_speed
        get_player_power = int(input(f"oooh, interesting! how about this- How POWERFUL are you? (0-10) : [YOU HAVE {player_stat_points} STAT POINTS TO SPEND.]: "))
        if get_player_power > player_stat_points:
            print("Ensure you only spend stat points you have.")
            continue
        get_player_perception = int(input(f"wow!, you surprise me.. one last thing.. How perceptive are you...? (0-10) : [YOU HAVE {player_stat_points} STAT POINTS TO SPEND.]: "))
        if get_player_perception > player_stat_points:
            print("Ensure you only spend stat points you have.")
            continue
        if player_stat_points == 0:
            stat_points_unspent = False

        #Initialise character
        player_character = Characters(player_name, get_player_speed, get_player_perception, get_player_power)

    try:
        player_reply = int(input(''' 
            Thanks for being so open! hey, ive gotta run im going on an adventure with some of my guildmates Luke and Muko! care to join us?
            [1] - Sure! i would love too Steve
            [2] - uhh, okay i suppose i could come-
            [3] - Yea fine i guess.
        
         ''' ))

        if player_reply == 1:
            print("Great! I'll see you there then! [Your response has been noted...]")
            player_character.steve_character_apriciation = 50
        elif player_reply == 2:
            print("Right, i suppose i will see you there then [Your response has been noted...]")  
            player_character.steve_character_apriciation = 30
        elif player_reply == 3:
            print("I mean you dont have too... but ok [Your response has been noted...]")
            player_character.steve_character_apriciation = 15      

        else:
            raise ValueError("Enter 1 2 or 3")
    except ValueError:
        print("Enter 1, 2 or 3")
    #characters met this scene:

    player_character.characters_met.append("steve")

    return player_character

def SceneTwo(player_character):
    print(f'''{player_character.name}... {player_character.name}!- Your eyes open, the suns glare temporarily blinds you 
          
          "Where am i..."
          {time.sleep(0.5)} Your eyes clear, growing accustom to the suns blinding glow.
          "You passed out just before you were about to enter the cave"
          "My names Syph, whats yours? ''')
    
    try:
        player_reply = int(input(f'''
        [1] - Call me {player_character.name} if you like. and thank you for helping me
        [2] - My name is {player_character.name} where did the others go..?
        '''))
        
        if player_reply == 1:
            print(f'''"No problem!, always happy to help a fellow traveller in need."
                "But hey, your friend steve left me with you to go and venture in the cave alone, how about we go down and support him? "''')
            player_character.syph_character_apriciation += 50
        elif player_character == 2:
            print(f'''"Oh, you mean steve?, he left me with you to go and venture in the cave alone, how about we go down and support him? "''')
    except:
        print("Invalid input.")

        #player continues into cave
        #set up combat system using the new move class
    pass 












#running program
player_character = RoomOneIntro()
SceneIntermission(player_character)
SceneTwo(player_character)
SceneIntermission(player_character)