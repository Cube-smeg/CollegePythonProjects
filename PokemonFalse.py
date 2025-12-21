from random import randint


PlayersTurn = True # Gives player first turn

PokemonDescriptions = { 
    "Spyhy": "Spyhy, a dark hound, she prances around the battlefield gracefully erasing her foes with unholy efficancy-   each attack leaves them scorched beyond recognition. An excellent choice however you may need to spend time dampening her temper...",
    " Verdantail" : "A fox-like Beast with a long, leafy tail that blooms with flowers in spring. Its said to bring good fortune to forests it inhabits.",
    "Mitler" :  "Mitler, an electric type pokemon. Her stature is rather small, but she is very influenncial. if around other pokemon, it is possible she will take control and lead them. if they dont oblige, she will use a thunder attack, which is super effective towards posion type pokemon, especially if the pokemon is weak to gas attacks."
}


class Pokemon:
    def __init__(self, Name, Type, CritChance, Moves):
        self.Name = Name
        self.Type = Type
        self.CritChance = CritChance
        self.Moves = Moves
        self.Health = 100
        self.AttackBoost = 1
        self.Defence = 1
        self.CritBoost = 1.5

        self.Level = 1
        self.BaseExp = 100
        self.Mult = 1.25
        self.ExpBoost = 1
        self.Exp = 0
        self.ExpReq = self.BaseExp * self.Mult * (self.Level - 1)

    
#Create Character Moves

#Syphy 
SyphStab = {"Name": "Syph Stab", "Damage": 30}
SyphNeedle = {"Name": "Syph Needle Eye", "Damage": 25}
SyphyMoves = [SyphStab, SyphNeedle]

#Verdantail 
TailWhip = {"Name": "TailWhip", "Damage": 25}
FlowerStorm = {"Name": "Flower Storm", "Damage": 35}
VerdantailMoves = [TailWhip, FlowerStorm]

#
MitlerAbsorbtion = {"Name": "Absorbtion", "DamageBoost": 1.25} # add later AttackBoost = AttackBoost + 1.25
MitlerLightningWar = {"Name": "Lightning War", "Damage": 45}
MitlerMoves = [MitlerAbsorbtion, MitlerLightningWar]

#Select Character
print(PokemonDescriptions)
try:
    CharacterSelected = int(input("Select your pokemon! 1.) Mitler, 2.) Syphy, 3.) Verdantail: "))

    if CharacterSelected == 1:
        CharacterSelected = Pokemon("Mitler", "Electric", 12, MitlerMoves)
    elif CharacterSelected == 2:
        CharacterSelected = Pokemon("Syphy", "Fire", 8, SyphyMoves)
    elif CharacterSelected == 3:
        CharacterSelected = Pokemon("Verdantail", "Grass", 5, VerdantailMoves)
    else:
        print("Enter between 1 - 3.")
except ValueError:
    print("Enter within 1-3 only")

    

def LevelScaling():
    #needs flushing out when i fully understand how to edit character instances
    CharacterSelected.Level = CharacterSelected.Level + 1
    CharacterSelected.Health = CharacterSelected.Health * 1.08 * (CharacterSelected.Level - 1)
    CharacterSelected.AttackBoost = CharacterSelected.AttackBoost * 1.05 * (CharacterSelected.Level - 1)

def YourAttack(CharacterSelected):
    MoveSelection = CharacterSelected.Moves

    PlayerChoice = int(input(f"Select your attack (0 or 1): "))
    return MoveSelection[PlayerChoice]


def OpponantCharacterSelector():
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
    MoveSelection = OpponantCharacter.Moves
    MovePicked = MoveSelection[randint(0, len(MoveSelection) - 1)]
    return MovePicked
    
def DealingDamage(PlayerMovePicked, MovePicked, OpponantCharacter):       # Remember to check for crit, mult by crit boost if true, add attack boost on the start before crit check check for enemy defence and reduce by *0.xx
    PlayersTurn = True
    while PlayersTurn == True:
        #Calculating damage/buffs
        Damage = PlayerMovePicked["Damage"] 
        Damage = Damage * CharacterSelected.AttackBoost
        #Check critical hit with appropiate chances for each character
        if randint(1, 100) > CharacterSelected.CritChance:
            Damage * CharacterSelected.CritBoost
    #Time to deal the damage and give buffs for the players turn
        if MovePicked == "Absorbtion":
            CharacterSelected.AttackBoost = CharacterSelected.AttackBoost * 1.25
            print(f"{CharacterSelected.Name} Has used Absorbtion! Their attack power has increased by 25%")
        else:
            OpponantHealth = OpponantCharacter.Health
            OpponantHealth = OpponantHealth - Damage
        if OpponantHealth <= 0:
            print(f"Opponant has fallen! your attack delt {Damage} and took them out! Well done")
            PokemonBattleWon()
            BattleEnded = True
            return(BattleEnded)
        else:
            print(f"{CharacterSelected.Name} delt {Damage} to the opponants {OpponantCharacter.Name}, The opponant has {OpponantHealth} health remaining!")
            OpponantCharacter.Health = OpponantHealth
            PlayersTurn = False

    while PlayersTurn == False: #opponants turn#
        print(MovePicked["Damage"])        
        Damage = MovePicked["Damage"] 
        Damage = Damage * CharacterSelected.AttackBoost
        if randint(1, 100) > OpponantCharacter.CritChance:
            Damage = Damage * OpponantCharacter.CritBoost
    #Time to deal the damage for the opponants attack and display buffs
        if MovePicked == "Absorbtion":
            OpponantCharacter.AttackBoost = CharacterSelected.AttackBoost * 1.25
            print(f"{OpponantCharacter.Name} Has used Absorbtion! Their attack power has increased by 25%")
        else:
            PlayerHealth = CharacterSelected.Health
            PlayerHealth = PlayerHealth - (Damage * CharacterSelected.Defence) # Damage taken is damage multiplied by defence (which is normally 1) defence needs to be <1 to lower damage
        if PlayerHealth <= 0:
            print(f"Your pokemon has fallen! their attack delt {Damage} and took you out! Unfortunate")
            PokemonBattleLost()
            BattleEnded = True
            return(BattleEnded)
        else:
            print(f"{OpponantCharacter.Name} delt {Damage} to the opponants {CharacterSelected.Name}, The opponant has {PlayerHealth} health remaining!")
            CharacterSelected.Health = PlayerHealth
            PlayersTurn = True
            

def PokemonBattleLost(OpponantCharacter):    # Deal with pokemon feinting, a slight loss of exp and a lil death screen
    print("Your pokemon feinted in battle!")
    #Reset All Player and opponant buffs 
    CharacterSelected.AttackBoost = 1
    OpponantCharacter.AttackBoost = 1
    CharacterSelected.Defence = 1
    OpponantCharacter.Defence = 1
    #reset exp boost for losing 
    CharacterSelected.ExpBoost = 1


def PokemonBattleWon(OpponantCharacter):          # Deals with exp giving, checking for a level up and giving a win screen to move on to the next fight
    ExpRewarded = 60 * OpponantCharacter.Level 
    ExpRewarded = ExpRewarded * CharacterSelected.ExpBoost
    print(f"Your pokemon gained {ExpRewarded} exp!")
    CharacterSelected.Exp = CharacterSelected.Exp + ExpRewarded 
    #Reset All Player and opponant buffs 
    CharacterSelected.AttackBoost = 1
    OpponantCharacter.AttackBoost = 1
    CharacterSelected.Defence = 1
    OpponantCharacter.Defence = 1
    #player gains a 5% exp boost for each game won in a row to make leveling slightly easier 
    CharacterSelected.ExpBoost = CharacterSelected.ExpBoost * 1.05
    #Check for level up and award if needed
    if CharacterSelected.Exp > CharacterSelected.ExpReq:
        LevelScaling(CharacterSelected)
    else:
        print(f"Your pokemon has {CharacterSelected.Exp} exp, you need {CharacterSelected.ExpReq} to move on to the next level: {CharacterSelected.Level + 1}" )


#Deals with type advantage : Fire > Grass, Water > Fire, Grass > NA, Electric > Grass (idk), 35% dmg boost if this is true
def TypeADV(OpponantCharacter):
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



#List of things needed:
#
#Battle System
#Story Type?, possible gyms

BattleEnded = True
#Made this a function so i can add other game functions later on (ie. Shops, pokemon captures?, gyms, and other stuff)
def BattleLoop():
    if BattleEnded == True:
        print(f"Opponant is being created...")
        #Create Opponant
        OpponantCharacter = OpponantCharacterSelector()
        print(f"Opponant Created, you will be facing {OpponantCharacter.Name}! Goodluck")
        #Find type advantage at the START of a battle only (resets at the end maybe?)
        TypeADV(OpponantCharacter)
        #Opponants attack
        OpponantUses = OpponantAttack(OpponantCharacter)
        #Players Attack
        PlayerUses = YourAttack(CharacterSelected)
        #Deal Damage from attacks
        DealingDamage(PlayerUses, OpponantUses, OpponantCharacter)

BattleLoop()




    





