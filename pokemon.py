import random
import sys

class Pokemon:
    def __init__(self, name, types, moves, EVs, health='=========='):
        self.name=name
        self.types=types
        self.moves=moves
        self.attack= EVs['ATTACK']
        self.defense=EVs['DEFENSE']
        self.health=health
        self.bars=20 #amount of health bars

def fight(self, Pokemon2):
    #allow pokemon to fight each other
    print("----Pokemon Battle----")
    print(f"\n{self.name}")
    print("TYPE/", self.types)
    print("ATTACK/", self.attack)
    print("DEFENSE/", self.defense)
    
    print("\nVS")
    print("----Pokemon Battle----")
    print(f"\n{Pokemon2.name}")
    print("TYPE/", Pokemon2.types)
    print("ATTACK/", Pokemon2.attack)
    print("DEFENSE/", Pokemon2.defense)
    

    version=['Fire', 'Water', 'Grass']
    for i,k in enumerate(version):
        if self.type==k:
            if Pokemon2.type==k:
                string_1_attack= "It's not very effective..."
                string_2_attack= "It's not very effective..."

            if Pokemon2.types==version[(i+1)%3]:
                Pokemon2.attack*=2
                Pokemon2.defense*=2
                string_1_attack="It's not very effective..."
                string_2_attack= "It's super effective!"
            
            if Pokemon2.types==version[(i+2)%3]:
                self.attack*=2
                self.defense*=2
                Pokemon2.attack/=2
                Pokemon2.defense/=2
                string_1_attack="It's super effective!"
                string_2_attack="It's not very effective..."

#fight create continue while pokemon has health
    while (self.bars>0) and (Pokemon2.bars>0):
        #print health of each
        print(f"{self.name}\t\t\HLTH\t{self.health}")
        print(f"{Pokemon2.name}\t\t\HLTH\t{Pokemon2.health}\n")

        print(f"Go {self.name}!")
        for i, x in enumerate(self.moves):
            print(f"{i+1}.", x)
        index=int(input('Pick a move: '))
        print(f"{self.name} used {self.moves[index-1]}!")
        print(string_1_attack)

        #determine damage
        Pokemon2bars-=self.attack
        Pokemon2.health=""

        #add bars back from defense
        for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
            Pokemon2.health += "="

        print(f"{Pokemon2.name}\t\tHLTH\T{Pokemon2.health}\n")

        if Pokemon2.bars<=0:
            print("\n..."+Pokemon2.name+ 'has fainted!')
            break

        #Pokemon2

        print(f"Go {Pokemon2.name}!")
        for i, x in enumerate(Pokemon2.moves):
            print(f"{i+1}.", x)
        index=int(input('Pick a move: '))
        print(f"{Pokemon2.name} used {Pokemon2.moves[index-1]}!")
        print(string_2_attack)

        #determine damage
        self.bars-=Pokemon2.attack
        self.health=""

        #add bars back from defense
        for j in range(int(self.bars+.1*self.defense)):
            self.health += "="

        print(f"{self.name}\t\tHLTH\T{self.health}\n")

        if self.bars<=0:
            print("\n..."+self.name+ 'has fainted!')
            break

money=random.choice(range(10,5000))
print(f"Opponent paid you $"+str(money))

if __name__=='__main__':
    Charizard= Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK':12, 'DEFENSE':8})
    Blastoise=Pokemon('Blatiose', "Water", ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'], {'Attack':10, 'DEFENSE':10})

Charizard.fight(Blastoise)


        

