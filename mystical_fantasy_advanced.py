import random, time
class Character:
    def __init__(self, name, hp, attack, magic, hp_effect):
        self.name=name
        self.hp= hp
        self.attack=attack
        self.magic=magic
        self.hp_effect=hp_effect
otter=Character("Sonja The Evil Otter Empress", 9999, 1500, 1000, 2000)
mars=Character("Mars the Kitty Cat Witch", 2500, 300, 1300, 300)
steffi=Character("Steffi the Tigress", 2500, 1000, 500, 300)
sam=Character("Sam the Sloth", 2500, 1200, 0, 1000)
def defeated(Character): #Character from Party Defeated after attack
        print(Character.name, "has been defeated.")
def party_defeat(): #Party is defeated
    ssss()
    print("Oh No! You have been defeated...")
def otter_dead():#otter is dead
        aaaa()
        print("Congrats! You have defeated", otter.name+"!", "You have saved all of the mystical animals on Planet Gaia!")
def party_health():#prints party health if they're alive
        if mars.hp>0:
            print(mars.name, "HP:", mars.hp)
        if steffi.hp>0:
            print(steffi.name, "HP:", steffi.hp)
        if sam.hp>0:
            print(sam.name, "HP:", sam.hp)
def print_otter():#print otter hp
    aaaa()
    print("\n"+otter.name, "has HP:", otter.hp)
def turn_hp(Character): #print character hp
    ssss()
    print("\n"+ Character.name, "turn. HP:", Character.hp)
def party_attack(Character): #party member attack on their turn
    aaaa()
    otter.hp-=Character.attack
def otter_attack(Character): #otter's attack
    print("\n"+otter.name, "scratches", Character.name +'!', str(otter.attack), "damage!\n")
    Character.hp-=otter.attack
def incapacitated(Character): #prints character incapacitated on their turn
    aaaa()
    print("\n"+Character.name, "is incapacitated")
def party_magic(Character): #basic party's magic attack
    aaaa()
    otter.hp-=Character.magic
def potion(Character):
    ssss()
    print(steffi.name, 'uses a potion on', Character.name+'.', Character.name, "recovers", str(steffi.hp_effect), "HP!")
    Character.hp+=steffi.hp_effect
def hug(Character):
    ssss()
    print("Sam hugs", Character.name+ ". The hug is mystical! They recover", str(sam.hp_effect), "HP!")
    if Character.hp<0:
        Character.hp=0
    Character.hp+=sam.hp_effect
    if Character.hp>2500:
        Character.hp=2500
    ssss()
    print(Character.name+ ":", str(Character.hp))
def invalid_option():
    aaaa()
    print("Please choose a valid option.")
def cannot_heal():
    print("You cannot heal an incapacited team member.")
def ssss():
    time.sleep(3)
def aaaa():
    time.sleep(.5)

#GAME START!!!
print("\nOn a Supernatural Planet where the Mystical creatures of Gaia try to live, The Evil Otter Empress has begun ravaging the land and destroying Beautiful Gaia.")
print("Fueled by the 7 Deadly Sins and a hunger for destruction, The Evil Otter's Toxicity has spread throughout all of the land.") 
print("Manipulating the troubled animals into suffering through silence and non-action.")
print("It will take a group of Fearless Warrior Animals to have the Courage to fight back against a gluttonous wrath of a greedy, pride-filled Otter!")
print("Mars the Kitty Witch is seeking retribution from Sonja the Evil Otter Empress after a dark past. Steffi the Fearless Tigress companion will stop")
print("at nothing to help her close friend. And Sam the Sloth once cursed by the Otter Empress is seeking revenge! If only the curse won't stop him now!") 
time.sleep(10)
while otter.hp>0 and mars.hp>0 or steffi.hp>0 or sam.hp>0:
    if otter.hp<=0:
        print("May your community live and grow in peace for eternity!<3")
        break
    ssss()

#Otter Attacks
    o_attack=random.randint(1,10)
    if o_attack>=8 and o_attack<=10: #magic attack
        ssss()
        print("\nFoaming at the mouth", otter.name, "attacks with Rabies Spray!", otter.magic, "damage to the entire party!\n")
        mars.hp-= otter.magic
        steffi.hp-=otter.magic
        sam.hp-=otter.magic  
        if mars.hp<=0 and steffi.hp<=0 and sam.hp<=0:
            party_defeat()
            break
        else:
            party_health()

    elif o_attack>=1 and o_attack<=7:#basic attack
        attacked=random.randint(1,3)
        if attacked==1 and mars.hp>0:
            otter_attack(mars)
        elif attacked==2 and steffi.hp>0:
            otter_attack(steffi)
        elif attacked==3 and sam.hp>0:
            otter_attack(sam)
        else:
            continue
        if mars.hp<=0:
            defeated(mars)
        if steffi.hp<=0:
            defeated(steffi)
        if sam.hp<=0:
            defeated(sam)
        if mars.hp<=0 and steffi.hp<=0 and sam.hp<=0:
            party_defeat()
            break
        else:
            party_health()
    #elif o_attack==1:
        # print(otter.name+"feeds off of the attention and drama of battle and regains", str(otter.hp_effect), "hp!")
        # otter.hp+=otter.hp_effect
#Mars Choices
    while True:
        if mars.hp<=0:
            incapacitated(mars)
            break
        else:
            turn_hp(mars)
            choice1=input("\n1. Scratch Back 2. Hex 3. Purrrification\nChoice:")
            if choice1=="1":
                party_attack(mars)
                print("*Hiss* *Hiss* Mars scratches back!", str(mars.attack), "Damage!")
                if otter.hp>0:
                    print_otter()
                elif otter.hp<=0:
                    otter_dead()
                    break
                break#break to keep the fight going
            if choice1=="2":
                aaaa()
                m_attack=random.randint(1,10)
                if m_attack>=8:
                    print("'When the wind howls, so forth comes the spirit of the owl!'\n"+mars.name, "casts a Hex on", otter.name+'.', "The Spirit of the Owl makes", otter.name, "pay for her sins!", str(mars.magic), 'Damage!')
                    otter.hp-=mars.magic
                if m_attack<8:
                    print("'While the Birds work to plant the seeds, one destroys Gaia out of Greed!'\n" +mars.name, "casts a spell to summon the spirits of wild birds! The bird's spirits rise up from behind", otter.name, "and they all swarm in pecking at her! 800 Damage!")
                    otter.hp-=800    
                if otter.hp>0:
                    ssss()
                    print_otter()
                elif otter.hp<=0:
                    otter_dead()
                    break
                break#break to keep the fight going
            if choice1=="3":
                ssss()
                print("\n*Meow* *Meow*\n"+mars.name, "casts a Purrrification! The entire party recovers", str(mars.hp_effect), "HP!")
                mars.hp+=mars.hp_effect
                if mars.hp>2500:
                    mars.hp=2500
                if steffi.hp<0:
                    steffi.hp=0
                steffi.hp+=mars.hp_effect
                if steffi.hp>2500:
                    steffi.hp=2500
                if sam.hp<0:
                    sam.hp=0
                sam.hp+=mars.hp_effect
                if sam.hp>2500:
                    sam.hp=2500
                party_health()
                break
            else:
                invalid_option()
#steffi
    while True:
        if otter.hp<=0:
            break
        if steffi.hp<=0:
            incapacitated(steffi)
            break#break to keep the fight going
        else:
            turn_hp(steffi)
            choice2=input("\n1. Pounce 2. Slap 3. Potion\nChoice:")
            if choice2=="1":
                party_attack(steffi)
                print("*Channeling her Chi*\n"+steffi.name, "pounces", otter.name +"! She starts clawing", otter.name + "!", str(steffi.attack), "Damage!")
                if otter.hp>0:
                    print_otter()
                elif otter.hp<=0:
                    otter_dead()
                    break
                break#break to keep the fight going
            if choice2=="2":
                party_magic(steffi)
                print("'Your pettiness isn't worth my time, let me send you into next week!'\n"+ steffi.name, "slaps", otter.name+ "! Damage:", str(steffi.magic))
                if otter.hp>0:
                    ssss()    
                    print_otter()
                elif otter.hp<=0:
                    otter_dead()
                    break
                break#break to keep the fight going
            if choice2=="3":
                aaaa()
                healing=input("Steffi pulls out a vial of silver liquid. Who would you like to heal 1. Mars 2. Steffi 3. Sam?\nChoice: ")
                if healing=="1":
                    if mars.hp<=0:
                        cannot_heal()
                        continue
                    if mars.hp>0:
                        potion(mars)
                        if mars.hp>2500:
                            mars.hp=2500
                        ssss()
                        print(mars.name+":",str(mars.hp))
                        break#break to keep the fight going
                if healing=="2":
                    ssss()
                    potion(steffi)
                    if steffi.hp>2500:
                        steffi.hp=2500
                    ssss()
                    print(steffi.name+":",str(steffi.hp))
                    break#break to keep the fight going
                if healing=="3":
                    if sam.hp<0:
                        cannot_heal()
                        continue
                    if sam.hp>0:
                        potion(sam)
                    if sam.hp>2500:
                        sam.hp=2500
                    ssss()
                    print(sam.name+":",str(sam.hp))
                    break#break to keep the fight going
                else:
                    invalid_option()
            else:
                invalid_option()
#sam
    while True:
        if otter.hp<=0:
            break
        if sam.hp<=0:
            incapacitated(sam)
            break#break to keep the fight going
        else:
            turn_hp(sam)
            choice3=input("\n1. Snore 2. Take a Stand! 3. Hug Teammate\nChoice:")
            if choice3=="1":
                party_attack(sam)
                print("Opening his chomps, revealing sharp canines...",sam.name, "snores.\nThe lack of attention greatly damages", otter.name, "ego.", str(sam.attack), "Damage!")
                if otter.hp>0:
                    print_otter()
                elif otter.hp<=0:
                    otter_dead()
                    break
                break#break to keep the fight going
            if choice3=="2":
                party_magic(sam)
                print("Taking a stand...",sam.name, "...rolls over.\nIt does nothing...")
                if otter.hp>0:
                    print_otter()
                elif otter.hp<=0:
                    otter_dead()
                    break
                break#break to keep the fight going
            if choice3=="3":
                aaaa()
                healing2=input("Who should Sam hug? 1. Mars 2. Steffi 3. Sam\nChoice:")
                if healing2=="1":
                    hug(mars)
                    break
                if healing2=="2":
                    hug(steffi) 
                    break
                if healing2=="3":
                    hug(sam)
                    break
                else:
                    invalid_option()
            else:
                invalid_option()