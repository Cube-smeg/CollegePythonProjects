from random import randint
from random import choice
from time import sleep

PlayersTurn = True # Gives player first turn

class Pokemon:
    def __init__(self, Name, Type, CritChance, Moves):
        self.Name = Name
        self.Type = Type
        self.CritChance = CritChance
        self.Moves = Moves
        self.Move1 = Moves[0]
        self.Move2 = Moves[1]
        self.Health = 100
        self.AttackBoost = 1
        self.Defence = 1
        self.CritBoost = 1.5

        self.Level = 1
        self.BaseExp = 100
        self.Mult = 1.25
        self.ExpBoost = 1
        self.Exp = 0
        self.ExpReq = self.BaseExp * self.Mult * (self.Level - 1) # works as 0 exp for the first level to garuntee a level up 

        self.GymBadge1 = 0
        self.GymBadge2 = 0
        self.GymBadge3 = 0

    def UpdateExpReq(self): 
        self.ExpReq = int(self.BaseExp * self.Mult * (self.Level - 1))

    def GymBadgeRewards(self):
        self.Defence = self.Defence - 0.05 # + 5% defence
        self.AttackBoost = self.AttackBoost + 0.05 # + 5% attack
        self.Health = self.Health * 0.05 # 5% health boost
    def ResetStats(self):
        self.Health = 100
        self.AttackBoost = 1
        self.Defence = 1
        self.CritBoost = 1.5

        self.Level = 1
        self.BaseExp = 100
        self.Mult = 1.25
        self.ExpBoost = 1
        self.Exp = 0
        
        self.GymBadge1 = 0
        self.GymBadge2 = 0
        self.GymBadge3 = 0
    def ResetBuffs(self):
        self.AttackBoost = 1
        self.CritBoost = 1.5
        self.ExpBoost = 1
        #not touching defence since it can only be obtained thru gym badges which wouldnt be reset
    def ScaleCharacter(self): #mainly for the opponants character
        self.Health = 100
        if self.Level > 1: # if this isnt here it sets both of them to 0 from the calculation
            self.Health = self.Health * 1.08 * (self.Level - 1)
            self.AttackBoost = self.AttackBoost * 1.05 * (self.Level - 1)
#Create Character Moves

#Syphy 
SyphStab = {"Name": "Syph Stab", "Damage": 30}
SyphNeedle = {"Name": "Syph Needle Eye", "Damage": 25}
SyphyMoves = [SyphStab, SyphNeedle]

#Verdantail 
TailWhip = {"Name": "TailWhip", "Damage": 25}
FlowerStorm = {"Name": "Flower Storm", "Damage": 35}
VerdantailMoves = [TailWhip, FlowerStorm]

#Milert
MitlerAbsorbtion = {"Name": "Absorbtion", "DamageBoost": 1.25} # add later AttackBoost = AttackBoost + 1.25
MitlerLightningWar = {"Name": "Lightning War", "Damage": 45}
MitlerMoves = [MitlerAbsorbtion, MitlerLightningWar]

#Select Character
print("""
PokemonDescriptions:
Spyhy: Spyhy, a dark hound, she prances around the battlefield gracefully erasing her foes with unholy efficancy- each attack leaves them scorched beyond recognition. An excellent choice however you may need to spend time dampening her temper.
Verdantail : A fox-like Beast with a long, leafy tail that blooms with flowers in spring. Its said to bring good fortune to forests it inhabits.
Mitler : Mitler, an electric type pokemon. Her stature is rather small, but she is very influenncial. if around other pokemon, it is possible she will take control and lead them. if they dont oblige, she will use a thunder attack, which is super effective towards posion type pokemon, especially if the pokemon is weak to gas attacks.
"""
      )
def PlayerPokemonSelector():
    CharacterFound = False
    while CharacterFound == False:
        try:
            CharacterSelected = int(input("""Select your pokemon! 
1.) Mitler
2.) Syphy
3.) Verdantail: """))

            if CharacterSelected == 1:
                CharacterSelected = Pokemon("Mitler", "Electric", 12, MitlerMoves)
            elif CharacterSelected == 2:
                CharacterSelected = Pokemon("Syphy", "Fire", 8, SyphyMoves)
            elif CharacterSelected == 3:
                CharacterSelected = Pokemon("Verdantail", "Grass", 5, VerdantailMoves)
            else:
                raise(ValueError)
            CharacterFound = True
            return (CharacterSelected)
        except ValueError:
            print("Enter within 1-3 only")
        except Exception as e:
            print(f"an error has occured: {e}")
            

    

def LevelScaling(CharacterSelected):
    #needs flushing out when i fully understand how to edit character instances
    CharacterSelected.Level = CharacterSelected.Level + 1
    CharacterSelected.Health = 100 #re setting the max hp to 100 after the fight ends
    CharacterSelected.Health = CharacterSelected.Health * 1.08 * (CharacterSelected.Level - 1)
    CharacterSelected.AttackBoost = CharacterSelected.AttackBoost * 1.05 * (CharacterSelected.Level - 1)
    print(f"[ Your pokemon leveled up! {CharacterSelected.Name}s level is now {CharacterSelected.Level} ]")
    print(f"[ Your new max HP is {CharacterSelected.Health} and you damage is boosted by {CharacterSelected.AttackBoost}! 1]")

def YourAttack(CharacterSelected):
    MoveSelection = CharacterSelected.Moves
    if CharacterSelected.Name == "Mitler": #So it doesnt break when it cant find the damage key in mitlers first move)
        print(f"[  {CharacterSelected.Move1["Name"]} Which buffs your attack power by {CharacterSelected.Move1["DamageBoost"]} or {CharacterSelected.Move2["Name"]} which deals {CharacterSelected.Move2["Damage"]} damage  ] ")
    else:
        print(f"[  {CharacterSelected.Move1["Name"]} which deals {CharacterSelected.Move1["Damage"]}, or {CharacterSelected.Move2["Name"]} Which deals {CharacterSelected.Move2["Damage"]} Damage  ] ")
    MoveFound = False
    while MoveFound == False:
        try:
            PlayerChoice = int(input(f"Select your attack (0 or 1): "))
            if PlayerChoice != 0 and PlayerChoice != 1:
                raise(ValueError)
            MoveFound = True
            return MoveSelection[PlayerChoice]
        except ValueError:
            print("Enter within the given boundary")
        except Exception as e:
            print(f"An error has occured {e}")


def OpponantCharacterSelector(CharacterSelected):
    OpponantCharacterChoice = randint(1,3)

    if OpponantCharacterChoice == 1:
        OpponantCharacter = Pokemon("Mitler", "Electric", 12, MitlerMoves)
    elif OpponantCharacterChoice == 2:
        OpponantCharacter = Pokemon("Syphy", "Fire", 8, SyphyMoves)
        
    elif OpponantCharacterChoice == 3:
        OpponantCharacter = Pokemon("Verdantail", "Grass", 5, VerdantailMoves)
    #Create a level for the opponant based on the players level
    if CharacterSelected.Level > 3:
        OpponantCharacter.Level = CharacterSelected.Level - randint(1,3)
    else:
        OpponantCharacter.Level = CharacterSelected.Level
    return(OpponantCharacter)

def OpponantAttack(OpponantCharacter):  #using randint to let the program select a random move for its character and makes the opponent level in a range around your own level (within 1 - 3 levels cant be under level 1)
    MovePicked = choice(OpponantCharacter.Moves)
    return MovePicked
    
def DealingDamage(PlayerMovePicked, OpponantCharacter, CharacterSelected):       # Remember to check for crit, mult by crit boost if true, add attack boost on the start before crit check check for enemy defence and reduce by *0.xx
    PlayersTurn = True
    while PlayersTurn == True:
        #Calculating damage/buffs
        #Player
        if PlayerMovePicked["Name"] == "Absorbtion":
            DamageBoost = PlayerMovePicked["DamageBoost"]
        else:
            Damage = PlayerMovePicked["Damage"] 
            Damage = Damage * CharacterSelected.AttackBoost
            #Check critical hit with appropiate chances for each character
            if randint(1, 100) <= CharacterSelected.CritChance:
                Damage = Damage * CharacterSelected.CritBoost
                print(f"[ Your {CharacterSelected.Name} hit a critical!, there attack will deal 50% more damage! ]")
                
    #Time to deal the damage and give buffs for the players turn
    # PLAYER DEALING DAMAGE TO OPPONANT
        if PlayerMovePicked["Name"] == "Absorbtion":
            CharacterSelected.AttackBoost = CharacterSelected.AttackBoost + DamageBoost # Made it +25 instead of 25% so players cant inf stack it later on
            print(f"[ {CharacterSelected.Name} Has used Absorbtion! Their attack power has increased by 25% ]")
            OpponantHealth = OpponantCharacter.Health
            PlayersTurn = False
        else:
            OpponantHealth = OpponantCharacter.Health
            OpponantHealth = OpponantHealth - Damage
        if OpponantHealth <= 0:
            print(f"[ Opponant has fallen! your attack delt {Damage} and took them out! Well done ]")
            PokemonBattleWon(OpponantCharacter, CharacterSelected)
            BattleWon = True
            return True, BattleWon
        elif PlayerMovePicked["Name"] != "Absorbtion":
            print(f"[ {CharacterSelected.Name} delt {Damage} to the opponants {OpponantCharacter.Name}, The opponant has {OpponantHealth} health remaining! ]")
            OpponantCharacter.Health = OpponantHealth
            PlayersTurn = False

    #checking for crit, applying and checking for absorbtion
    while PlayersTurn == False: #opponants turn 
        MovePicked = OpponantAttack(OpponantCharacter)
        if  MovePicked["Name"] == "Absorbtion":
            DamageBoost = MovePicked["DamageBoost"] 
        else:
            Damage = MovePicked["Damage"] 
            Damage = Damage * OpponantCharacter.AttackBoost
            if randint(1, 100) <= OpponantCharacter.CritChance:
                Damage = Damage * OpponantCharacter.CritBoost
                print(f"[ The opponants {OpponantCharacter.Name} landed a critical! their attack deals 50% more damage! ]")
    #Time to deal the damage for the opponants attack and display buffs
    # OPPONANT DEALING DAMAGE TO PLAYER

        if MovePicked["Name"] == "Absorbtion":
            OpponantCharacter.AttackBoost = OpponantCharacter.AttackBoost + DamageBoost
            print(f"[ {OpponantCharacter.Name} Has used Absorbtion! Their attack power has increased by 25% ]")
            PlayerHealth = CharacterSelected.Health
            PlayersTurn = True
        else:
            PlayerHealth = CharacterSelected.Health
            PlayerHealth = PlayerHealth - (Damage * CharacterSelected.Defence) # Damage taken is damage multiplied by defence (which is normally 1) defence needs to be <1 to lower damage
        if PlayerHealth <= 0:
            print(f"[ Your pokemon has fallen! their attack delt {Damage} and took you out! Unfortunate ]")
            PokemonBattleLost(OpponantCharacter, CharacterSelected)
            BattleLost = True
            return True, BattleLost
        elif MovePicked["Name"] != "Absorbtion":
            print(f"[ {OpponantCharacter.Name} delt {Damage} to your pokemon! {CharacterSelected.Name}, has {PlayerHealth} health remaining! ]")
            CharacterSelected.Health = PlayerHealth
            PlayersTurn = True
            return False
            
            

def PokemonBattleLost(OpponantCharacter, CharacterSelected):    # Deal with pokemon feinting, a slight loss of exp and a lil death screen
    print("Your pokemon feinted in battle!")
    
    #Reset All Player and opponant buffs 
    CharacterSelected.ResetBuffs()
    OpponantCharacter.ResetBuffs()
    exit


def PokemonBattleWon(OpponantCharacter, CharacterSelected):          # Deals with exp giving, checking for a level up and giving a win screen to move on to the next fight
    ExpRewarded = 30 * OpponantCharacter.Level 
    ExpRewarded = ExpRewarded * CharacterSelected.ExpBoost
    print(f"Your pokemon gained {ExpRewarded} exp!")
    CharacterSelected.Exp = CharacterSelected.Exp + ExpRewarded 
    #Reset All Player and opponant buffs 
    CharacterSelected.ResetBuffs()
    OpponantCharacter.ResetBuffs()
    #player gains a 5% exp boost for each game won in a row to make leveling slightly easier 
    CharacterSelected.ExpBoost = CharacterSelected.ExpBoost * 1.05
    #Check for level up and award if needed
    if CharacterSelected.Exp > CharacterSelected.ExpReq:
        LevelScaling(CharacterSelected)
        #exp overflow add
        CharacterSelected.Exp = ExpRewarded - CharacterSelected.ExpReq
        if CharacterSelected.Exp < 0:
            CharacterSelected.Exp = 0 #if final exp is less then 0  set it to 0  (i dont know how this would occur but it might)
        CharacterSelected.UpdateExpReq()
    else:
        print(f"Your pokemon has {CharacterSelected.Exp} exp, you need {CharacterSelected.ExpReq} to move on to the next level: {CharacterSelected.Level + 1}" )


#Deals with type advantage : Fire > Grass, Water > Fire, Grass > NA, Electric > Grass (idk), 35% dmg boost if this is true
def TypeADV(OpponantCharacter, CharacterSelected):
    PlayerTypeAdvantage = False
    OpponantTypeAdvantage = False
    if CharacterSelected.Type == "Fire" and  OpponantCharacter.Type == "Grass":
        PlayerTypeAdvantage = True
        OpponantTypeAdvantage = False
    elif CharacterSelected.Type == "Fire" and OpponantCharacter.Type == "Electric" or OpponantCharacter.Type == "Water":
        PlayerTypeAdvantage = False
        if OpponantCharacter.Type == "Water":
            OpponantTypeAdvantage = "True"
        else:
            OpponantTypeAdvantage = "False"
    elif CharacterSelected.Type == "Electric" and OpponantCharacter.Type == "Grass":
        PlayerTypeAdvantage = True
        OpponantTypeAdvantage = False
    
    if PlayerTypeAdvantage == True:
        CharacterSelected.AttackBoost = CharacterSelected.AttackBoost * 1.35 #35% dmg boost for element adv
    elif OpponantTypeAdvantage == True:
        OpponantCharacter.AttackBoost = OpponantCharacter.AttackBoost * 1.35 

def GymFight(CharacterSelected, Element):
    if Element == 1:
        OpponantCharacter = Pokemon("Mitler", "Electric", 15, MitlerMoves)
    elif Element == 2:
        OpponantCharacter = Pokemon("Syphy", "Fire", 11, SyphyMoves)
    elif Element == 3:
        OpponantCharacter = Pokemon("Verdantail", "Grass", 9, VerdantailMoves) 
        #all pokemon have increased crit chances for being boss
    #Above was copied from old character selector im js gonna tweak its level and stats
    BossEntity = OpponantCharacter
    BossEntity.Level = CharacterSelected.Level + 3 # always 3 levels above the player
    BossEntity.AttackBoost = 1.15 #15% dmg boost
    BossEntity.Defence = 0.90 #10% dmg reduction
    BattleEnded = False
    while BattleEnded == False:
        PlayerUses = YourAttack(CharacterSelected)
        BattleEnded, BattleResult = DealingDamage(PlayerUses, BossEntity, CharacterSelected) 
        #Copied from battle loop) 
    if BattleResult == True:
        if Element == 1:
            CharacterSelected.GymBadge1 = CharacterSelected.GymBadge1 + 1
            CharacterSelected.GymBadgeRewards()
        elif Element == 2:
            CharacterSelected.GymBadge2 = CharacterSelected.GymBadge2 + 1
            CharacterSelected.GymBadgeRewards()
        elif Element == 3:
            CharacterSelected.GymBadge3 = CharacterSelected.GymBadge3 + 1
            CharacterSelected.GymBadgeRewards()
        print(f"[ You now have {CharacterSelected.GymBadge1 + CharacterSelected.GymBadge2 + CharacterSelected.GymBadge3} gym badge(s) in total! ]")
    else:
        print(f"[ Unlucky! the gym was too strong for you this time, go and train some more and im sure you will come out victorious! ]")

#List of things needed:
#
#Battle System
#Story Type?, possible gyms

BattleEnded = False
#Made this a function so i can add other game functions later on (ie. Shops, pokemon captures?, gyms, and other stuff)
def GameLoop(CharacterSelected):
        BattleLoopActive = True
        while BattleLoopActive: 
            print(f"Opponant is being created...")
            sleep(0.3)
            #Create Opponant
            OpponantCharacter = OpponantCharacterSelector(CharacterSelected)
            OpponantCharacter.ScaleCharacter() # Give the opponant their buffs from levels
            print(f"Opponant Created, you will be facing a level {OpponantCharacter.Level} {OpponantCharacter.Name}! Goodluck")
            sleep(0.3)
            #Find type advantage at the START of a battle only (resets at the end maybe?)
            TypeADV(OpponantCharacter, CharacterSelected)
            #Opponants attack
            #Players Attack
            #Deal Damage from attacks
            BattleEnded = False
            while BattleEnded == False:
                PlayerUses = YourAttack(CharacterSelected)
                BattleEnded = DealingDamage(PlayerUses, OpponantCharacter, CharacterSelected)
            print("Battle has ended!")
            sleep(0.5)
            NextActionUnchosen = True
            while NextActionUnchosen == True: # i dont think 2 whiles in the same loop is a great idea but its fine 
                NextAction = int(input("""What would you like to do next?: 
[1] Enter another battle
[2] Restart your progress with a new pokemon
[3] Enter a boss battle (Level 5+)"""))

                if NextAction == 1:
                    print("[ Good luck on your next battle! ]")
                    sleep(0.5)
                    BattleLoopActive = True # not needed but helps show what this is
                    CharacterSelected.ResetBuffs() 
                    OpponantCharacter.ResetBuffs()
                    NextActionUnchosen = False
                
                elif NextAction == 2:
                    print(f"You chose {CharacterSelected.Name} this time, i wonder what you will go for next..")
                    CharacterSelected.ResetStats() # added to re set stats since it somehow wasnt before?
                    PlayerPokemonSelector() # re selects character 
                    NextActionUnchosen = False
                    BattleLoopActive = True
                elif NextAction == 3 and CharacterSelected.Level >= 5:
                    GymSelector = int(input("""Which gym do you want to face up against?
                    [1] Electric 
                    [2] Fire
                    [3] Grass"""))
                    print(f"This is going to be a hard match up for you and your {CharacterSelected.Name}... I wish you luck.")
                    GymFight(CharacterSelected, GymSelector)
                    NextActionUnchosen = True
                    BattleLoopActive = False

                    
CharacterSelected = PlayerPokemonSelector()
GameLoop(CharacterSelected)



#Current Issues
#NextActionLoop not ending on option #1 (HP) - fixed
#AttackBoost potentially giving more then previously thought (45 + 25% shouldnt equal 101 but it does and i have no idea) (MP)
#Some potential errors involving wrong inputs (LP) - fixed all of them(?)
#players hp isnt getting correctly set sometimes during the first turn of a battle?




