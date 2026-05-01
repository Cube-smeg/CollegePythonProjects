
#Text based adv game
#Characters - Mitler, Smeg, Kade, syphy, Luke, Muko, Steve, Aurafarmer, WeSeeTheFit, ResidentHomo

#Hours spent: 6.5
import time
import random

class Move:
    def __init__(self, name, requirement=0, stamina_cost=0,  **attributes):
        self.name = name
        self.requirement = requirement
        self.stamina_cost = stamina_cost

        self.damage_mult = 1.0
        self.move_stun = 0
        self.bleed_damage = 0
        self.self_stun_chance = 0.0
        self.multi_hit = 1
        self.defence_mult = 1.0
        self.stun_reduc_chance = 0.0
        self.dodge_chance_mult = 1.0
        self.stun_chance_reduc = 0.0 # 1 = 100%

        for key, value in attributes.items():
            setattr(self, key, value)

    def __str__(self):  
        return (f"{self.name} | DMG x{self.damage_mult} | "
                f"Stamina: {self.stamina_cost}")

class Characters:
    def __init__(self, Name, speed, perception, power, real):
        self.name = Name
        self.speed = speed
        self.perception = perception
        self.power = power
        self.real = real # used to check if character is a person of an npc
        self.moves = []
        #player inv
        self.inventory = []
        #stats
        self.stun_chance_reduc = 0 
        self.health = 100
        self.AttackBoost = 1
        self.Defence = 1
        self.CritBoost = 1.5
        self.Stamina = 100 
        self.lives = 3 #on each death deduct 1, add an item that rewards a life, once all lives are lost the character is deleted and they must restart
        self.stunned = 0
        #likeness
        self.characters_met = [] #AFTER EACH SCENE YOU MUST PLACE ALL NEW CHARACTERS INSIDE 
        self.syphy_character_appreciation = 0
        self.steve_character_appreciation = 0
        self.mitler_character_appreciation = 0
        self.smeg_character_appreciation = 0
        self.kade_character_appreciation = 0
        self.luke_character_appreciation = 0
        self.aurafarmer_character_appreciation = 0
        self.weseethefit_character_appreciation = 0
        self.resident_homo_character_appreciation = 0
        self.blacksmith_character_appreciation = 0
        #level handling
        self.level = 1
        self.BaseExp = 100
        self.Mult = 1.25
        self.ExpBoost = 1
        self.Exp = 0
        self.ExpReq = self.BaseExp * self.Mult * (self.level - 1) # works as 0 Exp for the first level to garuntee a level up
        #skill point stuff
        self.unspent = 0
        self.spent = 0

    def levelup(self):
        self.unspent = self.unspent + 2 #2 sp per level up
        self.level = self.level + 1
        self.Exp = 0
        print(f"You now have {player_character.unspent} unspent skillpoints.")
            
            
    def UpdateExpReq(self): 
        self.ExpReq = int(self.BaseExp * self.Mult * (self.level - 1))

    def ScaleCharacter(self):
        self.health = self.GetMaxhealth()
        self.AttackBoost = 1 * (1.05 ** (self.level - 1))
        self.Stamina = int(100 * (1.2 ** (self.level - 1)))
    
    def GetMaxhealth(self):
        return int(100 * (1.08 ** (self.level - 1)))
        
    def PlayerDied(self):
        #lose a life and empty your inventory
        self.lives -= 1
        self.inventory = []


def spend_skill_points(player_character):
    print(f''' 
    Current Skill Point Investments:
    speed: {player_character.speed}
    perception: {player_character.perception}
    power: {player_character.power}
    You have a total of {player_character.spent} skill points invested.

    You currently have {player_character.unspent} unspent skill points

    ''')
    if player_character.unspent == 0:
        print(f"You realise your skills have not been growing and so decide to train for a day..")
        score = mini_game()
        if score > 20:
            print(f"You trained diligently and gained 1 skill point!")
            player_character.unspent += 1
        elif score > 15:
            print(f"You trained diligently and gained 2 skill points!")
            player_character.unspent += 2
        else:
            print(f"Dispite your efforts, your training turned futile. Nothing was gained.")
        return
    else:
        while player_character.unspent > 0:
            invest_into = int(input('''
            Where would you like to invest into?
            [1] speed
            [2] perception
            [3] power '''))

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
            Move("power Slam", requirement=10, stamina_cost=20),
            Move("Gut Punch", requirement=5, stamina_cost=10)
        ],

        "speed": [
            Move("Quick Lunge", requirement=6, stamina_cost=12)
        ],

        "perception": [
            Move("Eagle Eye", requirement=10, stamina_cost=30, crit_chance_increase=25)
        ]
    }

    current_moves = len(player_character.moves)

    #this took like 9 years to figure out ngl
    for stat, moves in moves_by_stat.items():
        player_value = getattr(player_character, stat)

        for move in moves:
            if player_value >= move.requirement:
                if move.name not in [m.name for m in player_character.moves]:
                    player_character.moves.append(move)
                    print(f"Player has learned a new move! {str(move)}")
    
    if current_moves == len(player_character.moves):
        print("You try and train yourself.. yet nothing comes to fruition.")


    


def SceneIntermission(player_character):
    #intermission between scene switches, give options to check Exp, level, skill points, invest skillpoints, learn new moves
    print(f"The scene ends.. {player_character.name} closes their eyes and sees a vision...")
    menu_action = int(input(''' 
    ----------------------------------------------
                    Scene Ended.
    ----------------------------------------------
    | [1] Check skill points                     |                            
    | [2] Check inventory                        |
    | [3] Check character appreciation            |
    | [4] Learn new moves                        |
    | Beware... only 1 action is availible.      |
    |--------------------------------------------|
    '''))

    if menu_action == 1:
        spend_skill_points(player_character)
    if menu_action == 2:
        check_inventory(player_character)
    if menu_action == 3:
        check_character_appreciation(player_character)
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
            time_limit = 4
        elif difficulty == 2:
            difficulty = "Medium"
            time_limit = 5
        elif difficulty == 3:
            difficulty = "Easy"
            time_limit = 10
        else:
            print("invalid input detected. difficulty set to easy.")
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

There are 3 different types of components; 
              Burst: Used for damaging and outright killing opponants.
              Defence: Used for bulstering your own defences, granting damage reduction and slight dodge chance.
              Crit Chance: Used to increase player speed and critical hit chances aswell as damage.

There are infinate possibilities of moves you can create, 
              each move can have a maximum of 3 components,
              Using a single component will result in its full power
              Using 2 components means both will be slightly underpowered
              Using 3 components maximises varity however those effects can become dulled..

Each component will have its own unique properties, for example; LegSweep, this is a burst move, dealing low amounts of damage however stuns the opponant for a turn.

''')
    #Create component functionality:
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
        player_character.blacksmith_character_appreciation -= 10
        return

    components_used = []

    while len(components_used) < components_amount:
        print("Available components:")
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

    player_character.moves.append(final_move)

    print(f"New move created: {final_move.name}")
    


    #uses component system
    #16 components
    #8 for burst 4 for defence 4 for critchance
    #each has diff affects (multipliers)

def check_inventory(player_character):
# check player inventory [make a table inside class for it]
# if it is empty give an option to go foraging for health supplys (berrys) 2 berrys at most, make a minigame for it
    if len(player_character.inventory) == 0:
        print("My inventory seems empty... no matter ill go foraging for some supplys.")
        results = mini_game()
        print(f"results - {results}")
        possible_rewards = ["Mixed Berry", "LevelUp Crystal", "ExpUp Crystal","Sword of Doom","healthUp Crystal", "Randomcomponent Crystal","powerfulcomponent Crystal"]
        if results > 25:
            for x in range(1, 7):
                given_rewards = random.choice (possible_rewards)
                player_character.inventory.append(given_rewards)
                print(f"Item Found!: {given_rewards}")
        elif results > 15:
            for x in range(1,5):
                given_rewards = random.choice(possible_rewards)
                player_character.inventory.append(given_rewards)
                print(f"Item Found!: {given_rewards}")
        elif results > 10:
            for x in range(1,3): 
                given_rewards = random.choice(possible_rewards)
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
        use_item_from_inventory(player_character)

def use_item_from_inventory(player_character):
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
                    print(f"Using Item: {item}")
                    use_item(player_character, item)
                    player_character.inventory.pop(index)
                    print("")
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

def use_Expup_crystal(player_character):
    player_character.Exp = player_character.Exp + 350
    print(f"You used an Exp up crystal and gained 350 Exp!")

def use_sword_of_doom(player_character):
    player_character.health = player_character.health - 30
    print("""
          You pick up the sword... your hands trembling at its immense power radiating from itself. You lay it across your shoulder admiring its Expert craftsman ship.. 'wait... is that.. black paint?!'  
          
          It seems the infamous fraud mitler was the previous owner of this sword... useless.
          You throw the sword away as far as you can and accidently nick yourself on the finger as it flys away..
          [30 DAMAGE TAKEN.]""")
    pass

def use_healthup_crystal(player_character):
    player_character.health = player_character.health + 250
    print("You used a health up crystal! you healed 250 hit points")

def use_random_component_crystal(player_character):
    possible_components = {
    "LegSweep": {"damage_mult": 1.03, "move_stun": 1},
    "SingleSlash": {"damage_mult": 1.07, "bleed_damage": 13},
    "DropKick": {"damage_mult": 1.095},
    "Warriors_Pride": {"damage_mult": 1.2, "self_stun_chance": 0.3},
    "Waterfoul": {"damage_mult": 0.80, "multi_hit": 3},
    "Stance": {"defence_mult": 1.2, "stun_reduc_chance": 0.7},
    "PerfectEyesight": {"dodge_chance_mult": 1.3, "stun_chance_reduc": 0.9}
}
    component_name = random.choice(list(possible_components.keys()))
    component_data = possible_components[component_name]

    player_character.inventory.append({
    "name": component_name,
    "stats": component_data
    })
    print(f"You used a random component crystal and found {component_name}! Congrats")
    

def use_powerful_component_crystal(player_character):
    possible_components = {
    "LegSweep": {"damage_mult": 1.03, "move_stun": 1},
    "SingleSlash": {"damage_mult": 1.07, "bleed_damage": 13},
    "DropKick": {"damage_mult": 1.095},
    "Warriors_Pride": {"damage_mult": 1.2, "self_stun_chance": 0.3},
    "Waterfoul": {"damage_mult": 0.80, "multi_hit": 3},
    "Stance": {"defence_mult": 1.2, "stun_reduc_chance": 0.7},
    "PerfectEyesight": {"dodge_chance_mult": 1.3, "stun_chance_reduc": 0.9}
}
    component_name = random.choice(list(possible_components.keys()))
    component_data = possible_components[component_name]

    player_character.inventory.append({
    "name": component_name,
    "stats": component_data
    })
    
    print(f"You used a random component crystal and found {component_name}! Congrats")

def use_item(player_character, item_used):
    possible_items = ["Mixed Berry", "LevelUp Crystal", "ExpUp Crystal","Sword of Doom","healthUp Crystal", "Randomcomponent Crystal","powerfulcomponent Crystal"]
    if item_used in possible_items:
        print(f"item found: {item_used}")

        item_actions = {
            "Mixed Berry": use_mixed_berry,
            "LevelUp Crystal": use_levelup_crystal,
            "ExpUp Crystal": use_Expup_crystal,
            "Sword of Doom": use_sword_of_doom,
            "healthUp Crystal": use_healthup_crystal,
            "Randomcomponent Crystal": use_random_component_crystal,
            "powerfulcomponent Crystal": use_powerful_component_crystal
        }

        action = item_actions.get(item_used)

        if action:
            action(player_character)  
        else:
            print("This item can't be used.")
    

def check_character_appreciation(player_character):
# ask for a character to look at, show appreciation and some words on what that may mean
    if len(player_character.characters_met) == 0:
        print("You havent met any characters... how is that even possible??")
    character_to_find = input(f"Which of the characters you have met would you like to see..? [OPTIONS: {player_character.characters_met}]").lower()
    if character_to_find in player_character.characters_met:
        #character name -> appreciation chart
        character_to_appreciation_checker = {
        "steve": player_character.steve_character_appreciation,
        "syphy": player_character.syphy_character_appreciation,
        "mitler": player_character.mitler_character_appreciation,
        "smeg": player_character.smeg_character_appreciation,
        "kade": player_character.kade_character_appreciation,
        "luke": player_character.luke_character_appreciation,
        "aurafarmer": player_character.aurafarmer_character_appreciation,
        "weseethefit": player_character.weseethefit_character_appreciation,
        "resident_homo": player_character.resident_homo_character_appreciation
        }
        
        print(f"{character_to_find} appreciation meter for you is at {character_to_appreciation_checker[character_to_find]}")


#univeral battle creator
def BattleStart(enemy_character, player_character): #ENEMY CHARCTER MUST BE INITIALISED BEFORE ENTERING THE FUNCTION
    both_alive = True
    move_stun = 0
    unlockable_moves(enemy_character)
    if len(enemy_character.moves) < 1:
            enemy_character.moves.append(Move("Tackle", requirement=0, stamina_cost=1))
    #find who gets the first move (use speed, if one has more they got first, if its the same then  it will be a coin flip)
        
    who_goes_next = ["player", "enemy"]
    if player_character.speed > enemy_character.speed:
        goes_next = "player"
    elif player_character.speed == enemy_character.speed:
        goes_next = random.choice(who_goes_next)
    else:
        goes_next = "enemy"
    print("A Battle begins.")
    
    #find who gets the first move (use speed, if one has more they got first, if its the same then  it will be a coin flip)

    while both_alive == True: #loops until one character has reached 0 hp (maybe change?)
        
        
        #find who gets the first move (use speed, if one has more they got first, if its the same then  it will be a coin flip)
        

        #battle logic: 
        if goes_next == "enemy":
            enemy_turn(player_character, enemy_character)
            alive_or_dead = is_entity_alive(player_character)
            if alive_or_dead == False:
                print(f'''                                  -----YOU HAVE DIED!-----
                        {player_character.name} has been nobily defeated by the mighty {enemy_character.name}
                        as you fall you see something.. angelic, slowly decending towards you.. you hear a whisper, unsure as to
                        where it came from.. "One life down little one." - {player_character.lives} lives remain...''')
                battle_result = False
                return battle_result
            else:
                goes_next = "player"    
                
            
        #first player has been found, now we enter the damage dealing phase
        elif goes_next == "player":
            player_turn(player_character, enemy_character)
        #Check both hps, if one has reached 0 give the victor screen, if the player loses they lose a life (players have a max of 3 lives before they are wiped and data is deleted)
            alive_or_dead = is_entity_alive(enemy_character)
            if alive_or_dead == False:
                print(f'''                                  -----YOU HAVE WON!-----
                            {enemy_character.name} has been defeated by the mighty {player_character.name}
                            as he falls his body disintergrates and left just where it was treasures lay, waiting for the taking''')
                battle_result = True
                return battle_result
            else:
                goes_next = "enemy"
        #Finally, hand out rewards, Exp, potential item drops aswell as an option to invest skill points(maybeWW not)
def battle_lost(player_character, enemy_character):
    #reduce player Exp, take a life away, send them to the start of the scene:
    player_character.Exp = 0

def player_turn(player_character, enemy_character):
    #Get players Action;
    try:
        player_action = int(input('''Chose your action!
                                [1] - Attack!
                                [2] - Use an item!
                                [3] - Run away (pussy)'''))
        if player_action == 1:
            #ensure player has access to a move
            if len(player_character.moves) < 1:
                #create base move 
                player_character.moves.append(Move("Tackle", requirement=0, stamina_cost=1, damage_mult=1.0))
                    
            move_num = 1
            for x in player_character.moves:
                print(f"{move_num}: {x}")
                move_num += 1    
            move_selection = int(input(f''' Select your move! 
                                        Select from the position of your move:''' ))
            #check moves index position, use the input to find which move
            print(f"you have selected {player_character.moves[move_selection - 1]}")
            player_uses = player_character.moves[move_selection - 1]

            print("Your move.")
            untrue_damage = calculate_dmg_effects(player_character, enemy_character, player_uses, 1)
            true_damage = check_dmg_cap(enemy_character, untrue_damage)
            enemy_character.health -= true_damage
            print("--"*60)
            print(f"You used {player_uses} on {enemy_character.name}")
            print(f"{player_character.name} dealt {true_damage:.1f} damage!")
            print(f"{enemy_character.name} HP: {enemy_character.health}")
            print("--"*60)
        

        elif player_action == 2:
            use_item_from_inventory(player_character)
        elif player_action == 3:
            print("You attempt to run away, your legs kick as fast as they kick sprinting away-")
            if enemy_character.speed > player_character.speed or player_character.health < 0.5* player_character.GetMaxhealth():
                print("You tried.. and failed as you ran you tripped on a rock and fell face first [-5 HP], as you get up you turn to see your opponent waiting..")
                player_character.health -= 5
            else:
                print("somehow, someway, you escaped... you ran for so long and ultimately escaped. however it did not come without loss, you check your pockets to find an item missing")
                if len(player_character.inventory == 0 ):
                    print("nevermind your to broke to lose anything")
                random_item = random.choice(player_character.inventory)
                player_character.pop(random_item)
                print(f"You got to check... {random_item}.. its gone!")


    except:
        print("Invalid input")
        return
def enemy_turn(player_character, enemy_character):
    enemy_choses = random.choice(list(enemy_character.moves))
    print("The enemy attacks.")
    if enemy_character.stunned > 0:
        enemy_character.stunned -= 1
        print("The enemy is stunned! their move is skipped.")
        return
    #find enemys total damage

    untrue_damage = calculate_dmg_effects(player_character, enemy_character, enemy_choses, 0 )
    true_damage = check_dmg_cap(player_character, untrue_damage)
    player_character.health -= true_damage
    print("--"*60)
    print(f"Opponant used {enemy_choses} on {player_character.name}")
    print(f"{enemy_character.name} dealt {true_damage:.1f} damage!")
    print(f"{player_character.name} HP: {player_character.health}")
    print("--"*60)

def calculate_dmg_effects(player_character, enemy_character, move, player_npc):
    #find entitys total damage
    if player_npc == 1: # player:
        player_damage = player_character.power * 2
        damage_mult = move.damage_mult
        total_hit = move.multi_hit
        if enemy_character.stun_chance_reduc > 0:
            random_num = random.randint(0,1)
            if enemy_character.stun_chance_reduc < random_num:
                enemy_character.stunned += move.move_stun
            else:
                print(f"{enemy_character.name} has avoided your stun!")

        total_move_damage = player_damage * damage_mult + move.bleed_damage * total_hit
        return total_move_damage
    
    else: #npc:
        entity_damage = enemy_character.power * 2
        damage_mult = move.damage_mult  
        total_hit = move.multi_hit
        if player_character.stun_chance_reduc > 0:
            random_num = random.randint(0,1)
            if player_character.stun_chance_reduc < random_num:
                player_character.stunned += move.move_stun
            else:
                print(f"{player_character.name} has avoided the opponent stun!")
        
        total_move_damage = entity_damage * damage_mult + move.bleed_damage * total_hit
        return total_move_damage

def check_dmg_cap(entity, damage):
    entity_max_hp = entity.GetMaxhealth()
    if damage / entity_max_hp >= 0.25:
        new_dmg = entity_max_hp * 0.25 #25% of entitys max hp
        return new_dmg
    else:
        return damage
    
def is_entity_alive(entity):
    if entity.health <= 0 :  
        status = False
        print(f"{entity.name} has died.")
        if entity.real == True:
            entity.PlayerDied()
    else:
        status = True
    return status


def battle_won_rewards(rewards_amount, potential_rewards, enemy_character, player_character):
    for x in range(rewards_amount):
                item_found = random.choice(potential_rewards)
                take_item = str(input(f"Do you want to take {item_found}? Y/N ")).upper()
                if take_item == "Y":
                    player_character.inventory.append(item_found)
    Exp_to_award = 100 * enemy_character.level / 1.3
    if Exp_to_award > player_character.ExpReq:
        player_character.levelup()
        player_character.UpdateExpReq()
        player_character.ScaleCharacter()
    else:
        player_character.Exp += Exp_to_award

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
    player_information = {"speed": 0, "power": 0, "perception": 0}
    player_stat_points = 7
    if player_stat_points != 0 :
        stat_points_unspent = True
    while stat_points_unspent == True:
        get_player_speed = int(input(f"So hey, tell me about yourself and your strengths- How fast are you? (0-10) : [YOU HAVE {player_stat_points} STAT POINTS TO SPEND.]: "))
        if get_player_speed > player_stat_points:
            print("Ensure you only spend stat points you have.")
            continue
        player_stat_points = player_stat_points - get_player_speed
        get_player_power = int(input(f"oooh, interesting! how about this- How powerFUL are you? (0-10) : [YOU HAVE {player_stat_points} STAT POINTS TO SPEND.]: "))
        if get_player_power > player_stat_points:
            print("Ensure you only spend stat points you have.")
            player_stat_points = player_stat_points - get_player_speed
            continue
        player_stat_points = player_stat_points - get_player_power
        
        get_player_perception = int(input(f"wow!, you surprise me.. one last thing.. How perceptive are you...? (0-10) : [YOU HAVE {player_stat_points} STAT POINTS TO SPEND.]: "))
        if get_player_perception > player_stat_points:
            print("Ensure you only spend stat points you have.")#
            continue
        player_stat_points = player_stat_points - get_player_perception
        
        if player_stat_points == 0:
            stat_points_unspent = False

        #Initialise character
        player_character = Characters(player_name, get_player_speed, get_player_perception, get_player_power, 1)

    try:
        player_reply = int(input(''' 
            Thanks for being so open! hey, ive gotta run im going on an adventure with some of my guildmates Luke and Muko! care to join us?
            [1] - Sure! i would love too Steve
            [2] - uhh, okay i suppose i could come-
            [3] - Yea fine i guess.
        
         ''' ))

        if player_reply == 1:
            print("Great! I'll see you there then! [Your response has been noted...]")
            player_character.steve_character_appreciation = 50
        elif player_reply == 2:
            print("Right, i suppose i will see you there then [Your response has been noted...]")  
            player_character.steve_character_appreciation = 30
        elif player_reply == 3:
            print("I mean you dont have too... but ok [Your response has been noted...]")
            player_character.steve_character_appreciation = 15      

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
          "My names syphy, whats yours? ''')
    
    try:
        player_reply = int(input(f'''
        [1] - Call me {player_character.name} if you like. and thank you for helping me
        [2] - My name is {player_character.name} where did the others go..?
        '''))
        
        if player_reply == 1:
            print(f'''"No problem!, always happy to help a fellow traveller in need."
                "But hey, your friend steve left me with you to go and venture in the cave alone, how about we go down and support him? "''')
            player_character.syphy_character_appreciation += 50
        elif player_reply == 2:
            print(f'''"Oh, you mean steve?, he left me with you to go and venture in the cave alone, how about we go down and support him? "''')
    except:
        print("Invalid input.")

    print(f''' 
          *Slowly, you walk down the dimly lit carved out path through the cave,
           "How deep does this place go...." 
           syphy turns to reply to you- "I dont know.. this feels much deeper then usual."
         
           You turn a corner and see two ajacent paths, what do you do.. ''')

    route = None
    try:
        player_action = int(input(''' 
            [1] - Go left, and split up with syphy
            [2] - Go right, and split up with syhpy
            [3] - Let syphy chose for the both of you.'''))

        if player_action == 1:
            route = "left"
            player_character.syphy_character_appreciation -= 10
        elif player_action == 2:
            route = "right"
            player_character.syphy_character_appreciation -= 10
        elif player_action == 3:
            choices = ["right", "left"]
            route = random.choice(choices)
            print(f"syphy has decided, you will both go {route}.")
            print("syphy thanks you for allowing him to choose. [Action will be remembered.]")
            player_character.syphy_character_appreciation += 15
    except:
        print("invalid input")

    if route == "right":
        SceneTwoRight(player_character)
    elif route == "left":
        SceneTwoLeft(player_character) 

        #player continues into cave
        #set up combat system using the new move class

        #set up 2 different scenes one for going right, one for going left
        #Left side = very easy fight with minimal rewards
        #Right side = kinda hard fight with large rewards

    pass 


def SceneTwoRight(player_character):
        print(''' Its decided, you enter on the right side and continue walking down the dark cave,
            You hear a sound...   something approches you, something powerful.''')
        time.sleep(.5)
        print(f''' Prepare yourself {player_character.name} its time to fight.''')
        #Create enemy character to use for the battle
        enemy_character = Characters("powerful Slime", 1, 1, 3, 0)
        #enter battle
        battle_result = BattleStart(enemy_character, player_character)
        if battle_result == True:
            #battle won
            battle_won_rewards(3, ["Mixed Berry", "LevelUp Crystal", "ExpUp Crystal", "healthUp Crystal"], enemy_character, player_character)
        else:
            #battle lost
            print("you lose")   


def SceneTwoLeft(player_character):
        print(''' Its decided, you enter on the left side and continue walking down the dark cave,
            You hear a sound...   something approches you, something rather weak..''')
        time.sleep(.5)
        print(f''' Prepare yourself {player_character.name} its time to fight.''')
        #Create enemy character to use for the battle
        enemy_character = Characters("Weak Slime", 2, 1, 1, 0)
        #enter battle
        battle_result = BattleStart(enemy_character, player_character)
        if battle_result == True:
            #battle won
            print("GoodJob! your rewards await you.")
            battle_won_rewards(1, ["Mixed Berry", "ExpUp Crystal", "healthUp Crystal"], enemy_character, player_character)
        else:
            #battle lost
            print("you lose")
            battle_lost(player_character, enemy_character)
    

#CURRENTLY WORKING ON new scenes

#running program
player_character = RoomOneIntro()
SceneIntermission(player_character)
SceneTwo(player_character)
SceneIntermission(player_character)
