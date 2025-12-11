from random import randint
import json as jason
import time


PokemonDescriptions{ 
Spyhy: "Spyhy, a dark hound, she prances around the battlefield gracefully erasing her foes with unholy efficancy-   each attack leaves them scorched beyond recognition. An excellent choice however you may need to spend time dampening her temper...",
Verdantail: "A fox-like Beast with a long, leafy tail that blooms with flowers in spring. Its said to bring good fortune to forests it inhabits.",
Mitler: "Mitler, an electric type pokemon. Her stature is rather small, but she is very influenncial. if around other pokemon, it is possible she will take control and lead them. if they dont oblige, she will use a thunder attack, which is super effective towards posion type pokemon, especially if the pokemon is weak to gas attacks."
}


class Pokemon:
    Pokemon.ExpReq = (BaseExp * Mult * (level - 1))
    Pokemon.BaseExp = 100 # base exp for level
    Pokemon. Mult = 1.25 # Multiplier for exp

    def __init__(self, Name, ElementType, CritChance, ElementADV )
    self.Name = Name
    Pokemon.Health = 100
    Pokemon.AttackBoost = 1
    Pokemon.Defence = 0 #percentage defence
    self.ElementADV = ElementADV
    self.ElementType = ElementType
    self.CritChance = CritChance #percentage
    Pokemon.CritBoost = 1.5
    Pokemon.Level = 1
    Pokemon.ExpReq = (BaseExp * Mult * (level - 1))
    Pokemon.Exp = 0 # current exp

#Create Character Moves

#Syphy 
SyphStab = {Name: "Syph Stab", Damage: 30}
SyphNeedle = {Name: "Syph Needle Eye", Damage: 25}
SyphyMoves = [SyphStab, SyphNeedle]

#Verdantail 
TailWhip = {Name: "TailWhip", Damage: 25}
FlowerStorm = {Name: "Flower Storm", Damage: 35}
VerdantailMoves = [TailWhip, FlowerStorm]

#
Absorbtion = {Name: "Absorbtion"} # add later AttackBoost = AttackBoost + 1.25
LightningWar = {Name: "Lightning War", Damage: 45}
MaeMoves = [MaeAbsorbtion, MaeLightningWar]

#Create Characters
Mitler = Pokemon("Miter", Health, AttackBoost, Defence, ElementType="Electric", CritChance=12, CritBoost, Level, Exp)
Spyhy = Pokemon("Syphy", Health, AttackBoost, Defence, ElementType="Fire", CritChance=8, CritBoost, Level, Exp)
Verdantail = Pokemon("Verndantail", Health, AttackBoost, Defence, ElementType="Grass", CritChance=5, CritBoost, Level, Exp)

#Select Characters
print(PokemonDescriptions)
try:
    CharacterSelected = int(input(f"Select your pokemon!, 1.) Mae, 2.) Syphy, 3.) Verdantail"))
    if CharacterSelected = "1":
        CharacterSelected = "Mae"
    elif CharacterSelected = "2":
        CharacterSelected = "Syphy"
    elif CharacterSelected = "3":
        CharacterSelected = "Verdantail"
    else:
        print("Enter between 1 - 3.")
except ValueError:
    print("enter within 1-3 only")
    

def LevelScaling(PokemonName, Level):
    #needs flushing out when i fully understand how to edit character instances
    Level = Level + 1
    Heath = Health * 1.08 * (Level - 1)
    AttackBoost = AttackBoost * 1.05 * (Level - 1)

def YourAttack(CharacterSelected):
    if CharaterSelected = Mitler:
        MoveSelection = MitlerMoves
        PlayerMovePicked = int(input(f"Select your attack! {MoveSelection}"))
    elif Syphy:
        MoveSelection = SyphyMoves
        PlayerMovePicked = int(input(f"Select your attack! {MoveSelection}"))
    elif Verdantail:
        MoveSelection = VerdantailMoves
        PlayerMovePicked = int(input(f"Select your attack! {MoveSelection}"))
    else:
        print("Move Selection Failed - Character not found")
    
    return PlayerMovePicked


def OpponantAttack:  #using randint to let the program select a random move for its character and makes the opponent level in a range around your own level (within 1 - 3 levels cant be under level 1)
    OpponantCharacter = randint(1,3)
    if OpponantCharacter = "1":
        OpponantCharacter = "Mitler"
    elif OpponantCharacter = "2":
        OpponantCharacter = "Syphy"
    elif OpponantCharacter = "3":
        OpponantCharacter = "Verdantail"
    else:
        print("Enter between 1 - 3.")
    
    OpponantAttackNum = randint(1,2)
    MoveSelection = [OpponantCharacter + "Moves"]
    MovePicked = MoveSelection[OpponantAttackNum]

    return OpponantCharacter, MovePicked
    
def DealingDamage(PlayerMovePicked, MovePicked):       # Remember to check for crit, mult by crit boost if true, add attack boost on the start before crit check check for enemy defence and reduce by *0.xx
    MovePicked[Damage] = MovePicked * CharacterSelected.AttackBoost * ElementADV


def PokemonBattleLost           # Deal with pokemon feinting, a slight loss of exp and a lil death screen
    
def PokemonBattleWon            # Deals with exp giving, checking for a level up and giving a win screen to move on to the next fight

def TypeADV
    if C
        CharacterSelected.ElementADV = 1.75 # damageboost



