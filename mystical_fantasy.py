import random 
import time
class Character:
    def __init__(self, name, hp, attack, magic, hp_effect):
        self.name=name
        self.hp= hp
        self.attack=attack
        self.magic=magic
        self.hp_effect=hp_effect

ssss=time.sleep(3)
aaaa=time.sleep(.5)


otter=Character("Sonja The Evil Otter Empress", 9999, 800, 600, 0)
mars=Character("Mars the Kitty Cat Witch", 2500, 300, 800, 300)
steffi=Character("Steffi the Tigress", 2500, 1000, 200, 500)
sam=Character("Sam the Sloth", 2500, 1200, 0, 1000)
#turn is set for the otter's major attack to only happen every 3 turns
print("\nOn a Supernatural Planet where the Mystical creatures of Gaia try to live, The Evil Otter Empress has begun ravaging the land and destroying Beautiful Gaia.")
print("Fueled by the 7 Deadly Sins and a hunger for destruction, The Evil Otter's Toxicity has spread throughout all of the land.") 
print("Manipulating the troubled animals into suffering through silence and non-action.")
print("It will take a group of Fearless Warrior Animals to have the Courage to fight back against a gluttonous wrath of a greedy, pride-filled Otter!")
print("Mars the Kitty Witch is seeking retribution from Sonja the Evil Otter Empress after a dark past. Steffi the Fearless Tigress companion will stop")
print("at nothing to help her close friend. And Sam the Sloth once cursed by the Otter Empress is seeking revenge! If only the curse won't stop him now!") 

while otter.hp>0 and mars.hp>0 or steffi.hp>0 or sam.hp>0:
    if otter.hp<=0:
        print("May your community live and grow in peace for eternity!<3")#Come back to
        break
    ssss
    print("\n"+otter.name, "has HP:", otter.hp)

#Otter Attacks
    o_attack=random.randint(1,10)
    if o_attack>=8 and o_attack<=10:
        ssss
        print("\nFoaming at the mouth", otter.name, "attacks with Rabies Spray!", otter.magic, "damage to the entire party!\n")
        mars.hp -= otter.magic
        steffi.hp-= otter.magic
        sam.hp-=otter.magic
        
        if mars.hp<=0 and steffi.hp<=0 and sam.hp<=0:
            ssss
            print("Oh No! You have been defeated...")
            break
        else:
            if mars.hp>0:
                print(mars.name, "HP:", mars.hp)
            if steffi.hp>0:
                print(steffi.name, "HP:", steffi.hp)
            if sam.hp>0:
                print(sam.name, "HP:", sam.hp)

    elif o_attack>=0 and o_attack<=7:
        attacked=random.randint(1,3)
        if attacked==1 and mars.hp>0:
            print(otter.name, "scratches", mars.name +'!', str(otter.attack), "damage!\n")
            mars.hp-=otter.attack
        elif attacked==2 and steffi.hp>0:
            print(otter.name, "scratches", steffi.name +'!', str(otter.attack), "damage!\n")
            steffi.hp-=otter.attack
        elif attacked==3 and sam.hp>0:
            print(otter.name, "scratches", sam.name +'!', str(otter.attack), "damage!\n")
            sam.hp-=otter.attack
        else:
            continue
        if mars.hp<=0:
            ssss
            print(mars.name, "has been defeated.")
        if steffi.hp<=0:
            ssss
            print(steffi.name, "has been defeated.")
        if sam.hp<=0:
            ssss
            print(sam.name, "has been defeated.")
        if mars.hp<=0 and steffi.hp<=0 and sam.hp<=0:
            ssss
            print("Oh No! You have been defeated...")
            break
        else:
            if mars.hp>0:
                print(mars.name, "HP:", mars.hp)
            if steffi.hp>0:
                print(steffi.name, "HP:", steffi.hp)
            if sam.hp>0:
                print(sam.name, "HP:", sam.hp)
#Mars Choices
    while True:
        if otter.hp<=0:
            break
        if mars.hp<=0:
            ssss
            print("\n"+mars.name, "is incapacitated")
            break
        else:
            ssss
            print("\n"+mars.name, "turn. HP:", mars.hp)
            ssss
            choice1=input("\n1. Scratch Back 2. Hex 3. Purrrification\nChoice:")
            if choice1=="1":
                aaaa
                print("*Hiss* *Hiss* Mars scratches back!", str(mars.attack), "Damage!")
                otter.hp-=mars.attack
                if otter.hp>0:
                    print(otter.name, "HP:",str(otter.hp))
                elif otter.hp<=0:
                    ssss
                    print("Congrats! You have defeated", otter.name+"!", "You have saved all of the mystical animals on Planet Gaia!")
                    break
                break#break to keep the fight going
            if choice1=="2":
                aaaa
                print("'When the wind howls, so forth comes the spirit of the owl!'\n"+mars.name, "casts a Hex on", otter.name+'.', "The Spirit of the Owl makes", otter.name, "pay for her sins!", str(mars.magic), 'Damage!')
                otter.hp-=mars.magic
                if otter.hp>0:
                    print(otter.name, "HP:",str(otter.hp))
                elif otter.hp<=0:
                    aaaa
                    print("Congrats! You have defeated", otter.name+"!", "You have saved all of the mystical animals on Planet Gaia!")
                    break
                break#break to keep the fight going
            if choice1=="3":
                aaaa
                print("\n*Meow* *Meow*\n"+mars.name, "casts a Purrrification! The entire party recovers", str(mars.hp_effect), "HP!")
                mars.hp+=mars.hp_effect
                if mars.hp>2500:
                    mars.hp=2500
                steffi.hp+=mars.hp_effect
                if steffi.hp>2500:
                    steffi.hp=2500
                if steffi.hp<0:
                    steffi.hp=0
                    steffi.hp+=mars.hp_effect
                sam.hp+=mars.hp_effect
                if sam.hp>2500:
                    sam.hp=2500
                if sam.hp<0:
                    sam.hp=0
                    sam.hp+=mars.hp_effect
                aaaa
                print(mars.name, "HP:", str(mars.hp), steffi.name, "HP:", str(steffi.hp), sam.name, "HP:", str(sam.hp))
                break
            else:
                print("Please enter valid option")
#steffi
    while True:
        if otter.hp<=0:
            break
        if steffi.hp<=0:
            aaaa
            print("\n"+steffi.name, "is incapacitated")
            break#break to keep the fight going
        else:
            ssss
            print("\n"+ steffi.name, "turn. HP:", steffi.hp)
            choice2=input("\n1. Pounce 2. Slap 3. Potion\nChoice:")
            if choice2=="1":
                aaaa
                print("*Channeling her Chi*\n"+steffi.name, "pounces", otter.name +"! She starts clawing", otter.name + "!", str(steffi.attack), "Damage!")
                otter.hp-=steffi.attack
                if otter.hp>0:
                    ssss
                    print(otter.name, "HP:",str(otter.hp))
                elif otter.hp<=0:
                    aaaa
                    print("Congrats! You have defeated", otter.name+"!", "You have saved all of the mystical animals on Planet Gaia!")
                    break#break to keep the fight going
                break
            if choice2=="2":
                aaaa
                print("'Your pettiness isn't worth my time, let me send you into next week!'\n"+ steffi.name, "slaps", otter.name+ "! Damage:", str(steffi.magic))
                otter.hp-=steffi.magic
                if otter.hp>0:
                    ssss    
                    print(otter.name, "HP:",str(otter.hp))
                elif otter.hp<=0:
                    aaaa
                    print("Congrats! You have defeated", otter.name+"!", "You have saved all of the mystical animals on Planet Gaia!")
                    break
                break#break to keep the fight going
            if choice2=="3":
                aaaa
                healing=input("Steffi pulls out a vial of silver liquid. Who would you like to heal 1. Mars 2. Steffi 3. Sam?\nChoice: ")
                if healing=="1":
                    aaaa
                    if mars.hp<=0:
                        print("You cannot heal an incapacitated team member.")
                        continue
                    if mars.hp>0:
                        print(steffi.name, 'uses a potion on', mars.name+'.', mars.name, "recovers", str(steffi.hp_effect), "HP!")
                        mars.hp+=steffi.hp_effect
                        if mars.hp>2500:
                            mars.hp=2500
                        print(mars.name+":",str(mars.hp))
                        break#break to keep the fight going
                if healing=="2":
                    aaaa
                    print(steffi.name, 'uses a potion on', steffi.name+'.', steffi.name, "recovers", str(steffi.hp_effect), "HP!")
                    steffi.hp+=steffi.hp_effect
                    if steffi.hp>2500:
                        steffi.hp=2500
                    print(steffi.name+":",str(steffi.hp))
                    break#break to keep the fight going
                if healing=="3":
                    aaaa
                    if sam.hp<0:
                        print("You cannot heal an incapacitated team member.")
                        continue
                    if sam.hp>0:
                        print(steffi.name, 'uses a potion on', sam.name+'.', sam.name, "recovers", str(steffi.hp_effect), "HP!")
                        sam.hp+=steffi.hp_effect
                    if sam.hp>2500:
                        sam.hp=2500
                    print(sam.name+":",str(sam.hp))
                    break#break to keep the fight going
                else:
                    aaaa
                    print("Please enter a valid option.")
            else:
                aaaa
                print("Please enter a valid option.")
#sam
    while True:
        if otter.hp<=0:
            break
        if sam.hp<=0:
            aaaa
            print("\n"+sam.name, "is incapacitated")
            break#break to keep the fight going
        else:
            ssss
            print("\n"+ sam.name, "turn. HP:", sam.hp)
            choice3=input("\n1. Snore 2. Take a Stand! 3. Hug Teammate\nChoice:")
            if choice3=="1":
                aaaa
                print("Opening his chomps, revealing sharp canines...",sam.name, "snores.\nThe lack of attention greatly damages", otter.name, "ego.", str(sam.attack), "Damage!")
                otter.hp-=sam.attack
                if otter.hp>0:
                    aaaa
                    print(otter.name, "HP:",str(otter.hp))
                elif otter.hp<=0:
                    aaaa
                    print("Congrats! You have defeated", otter.name+"!", "You have saved all of the mystical animals on Planet Gaia!")
                    break
                break#break to keep the fight going
            if choice3=="2":
                aaaa
                print("Taking a stand...",sam.name, "...rolls over.\nIt does nothing...")
                otter.hp-=sam.magic
                if otter.hp>0:
                    aaaa
                    print(otter.name, "HP:",str(otter.hp))
                elif otter.hp<=0:
                    aaaa
                    print("Congrats! You have defeated", otter.name+"!", "You have saved all of the mystical animals on Planet Gaia!")
                    break
                break#break to keep the fight going
            if choice3=="3":
                aaaa
                healing2=input("Who should Sam hug? 1. Mars 2. Steffi 3. Sam\nChoice:")
                if healing2=="1":
                    aaaa
                    print("Sam hugs", mars.name+ ". The hug is mystical! It recovers", str(sam.hp_effect), "HP!")
                    mars.hp+=sam.hp_effect
                    if mars.hp>2500:
                        mars.hp=2500
                    print(mars.name+ ":", str(mars.hp))
                    break
                if healing2=="2":
                    aaaa
                    print("Sam hugs", steffi.name+ ". The hug is mystical! It recovers", str(sam.hp_effect), "HP!")
                    steffi.hp+=sam.hp_effect
                    if steffi.hp>2500:
                        steffi.hp=2500
                    print(steffi.name+ ":",str(steffi.hp))  
                    break
                if healing2=="3":
                    aaaa
                    print("Sam hugs", sam.name+ ". The hug is mystical! It recovers", str(sam.hp_effect), "HP!")
                    sam.hp+=sam.hp_effect
                    if sam.hp>2500:
                        sam.hp=2500
                    print(sam.name+":",str(sam.hp))
                    break
                else:
                    aaaa
                    print("Please choose a valid option.")
            else:
                aaaa
                print("Please choose a valid option.")     
#if otter.hp<=0
    #print("Congrats! You have defeated", otter.name+"!", "You have saved all of the mystical animals on Planet Gaia!")
    #break