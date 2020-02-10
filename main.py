#Game
import time
print ("Invasion By Danyaal Kara")

def crater():
  print ("You pick up a card, it reads 'Welcome to my game! Press L to go Left and R to go right.' you put it back down. ")
  time.sleep(1)
  print("You are outside, and just woken up in a crater. You dont remember anything. The sky is a dark red and meteors are crashing down. There seems to be another card on the ground.")
  time.sleep(1)
  choice = input("Pick up card? y/n ")
  if choice == "y":
    print("You pickup the card, it reads 'if you are reading this, you have woken up. The world is ending, and ---- is taking over. You must help us please, we need assistance and with your power we can win.'")
    choicetravel1()
  else:
    print("You pick it up anyway, it seems you couldnt stop the urge to read it. I guess you were to curious. It reads 'if you are reading this, you have woken up. The world is ending, and ---- is taking over. You must help us please, we need assistance and with your power we can win.'")
    choicetravel1()



def Grassland():
  print ("You wonder aimlessly and you find a green grassy area. it seems that whatever is taking over has not destroyed this area. There is a sword on the ground. There is something in the distance charging at you!")
  time.sleep(1)
  choice = input("take the sword? ")
  if choice  == "take sword" or choice == "yes" or choice == "pickup sword" or choice == "take":
    print ("you picked up the sword, an unknown creature pulls out a sword too")
    Battle_1()
  else:
    die_first()


def choicetravel1():
  print ("Do you want to travel to the Grassland?")
  time.sleep(1)
  choice = input("Travel/Don't ")
  if choice == "Travel" or choice == "travel":
   Grassland()
  else:
    die_Joke()



def Battle_1():
  time.sleep(1)
  print("The alien is staring at you with hatred. he charges at you.")
  print("""                   ."-,.__
                 `.     `.  ,
              .--'  .._,'"-' `.
             .    .'         `'
             `.   /          ,'
               `  '--.   ,-"'
                `"`   |  \
                   -. \, |
                    `--Y.'      ___.
                         \     L._, \
               _.,        `.   <  <\                _
             ,' '           `, `.   | \            ( `
          ../, `.            `  |    .\`.           \ \_
         ,' ,..  .           _.,'    ||\l            )  '".
        , ,'   \           ,'.-.`-._,'  |           .  _._`.
      ,' /      \ \        `' ' `--/   | \          / /   ..\
    .'  /        \ .         |\__ - _ ,'` `        / /     `.`.
    |  '          ..         `-...-"  |  `-'      / /        . `.
    | /           |L__           |    |          / /          `. `.
   , /            .   .          |    |         / /             ` `
  / /          ,. ,`._ `-_       |    |  _   ,-' /               ` \
 / .           \"`_/. `-_ \_,.  ,'    +-' `-'  _,        ..,-.    \`.
.  '         .-f    ,'   `    '.       \__.---'     _   .'   '     \ \
' /          `.'    l     .' /          \..      ,_|/   `.  ,'`     L`
|'      _.-""` `.    \ _,'  `            \ `.___`.'"`-.  , |   |    | \
||    ,'      `. `.   '       _,...._        `  |    `/ '  |   '     .|
||  ,'          `. ;.,.---' ,'       `.   `.. `-'  .-' /_ .'    ;_   ||
|| '              V      / /           `   | `   ,'   ,' '.    !  `. ||
||/            _,-------7 '              . |  `-'    l         /    `||
. |          ,' .-   ,' ||               | .-.        `.      .'     ||
 `'        ,'    `".'    |               |    `.        '. -.'       `'
          /      ,'      |               |,'    \-.._,.'/'
          .     /        .               .       \    .''
        .`.    |         `.             /         :_,'.'
          \ `...\   _     ,'-.        .'         /_.-'
           `-.__ `,  `'   .  _.>----''.  _  __  /
                .'        /"'          |  "'   '_
               /_|.-'\ ,".             '.'`__'-( \
                 / ,"'"\,'               `/  `-.|"  """)
  choice = input("Charge at the alien too or Dodge and stab. C/D ")
  if choice == "d":
    time.sleep(1)
    print ("You dodge the attack, the alien was too slow, you stab him and the alien drops dead.")
    choicetravel2()


  elif choice == "c":
    print ("The alien stabs you and you stab him, you both drop dead.")
    exit()


def choicetravel2():
  time.sleep(1)
  print ("Do you want to travel to Right or Left?")
  choice = input("Right/Left ")
  time.sleep(1)
  if choice == "right" or choice == "Right" or choice == "r":
    Desert()
  elif choice == "left" or choice == "Left" or choice == "l": 
    die_3()
  else:
    die_Joke()

def Desert():
  choice = input("While travelling, you find a bright light pick up light?")
  if choice == "yes" or choice == "Yes" or choice == "take sword":
    print ("Nice.")
  else:
    print ("a meteor crashes down on you. lol.")
    die_first()

  print ("You walk to a Scorching hot desert,")
  time.sleep(1)
  print ("Its so hot, you start to feel drowsy. You havent had any water, and you have been travelling for a long time.")
  time.sleep(1)
  print ("there is something in the distance up north, it looks like its moving.")
  time.sleep(1)
  print ("there is bluey area to the right and a black area to the left.")
  time.sleep(1)
  choice = input("Where would you like to go? ")
  if choice == "north" or choice == "n" or choice == "North":
    battle_2()
  elif choice == "right" or choice == "blue area":
    print("You find an oasis")
    time.sleep(1)
    print ("there is food so you eat from it, and water so you drink it too.")
    time.sleep(1)
    print("you fall asleep and find yourself in hell.")
    quit()
  elif choice == "Left" or choice == "l" or choice == "left":
    die_3()
  else:
    dielol()



def battle_2():
  print("You walk north, the thing that was moving was an alien army!")
  time.sleep(1)
  print("your bright light shines! NEOOOOWOWOWOWO. -- sound of bright light.")
  time.sleep(1)
  choice = input("the army pulls out their guns. What do you do? ")
  if choice == "use light" or choice == "light":
    lightscene()
  elif choice == "use sword" or choice == "sword":
    Swordscene()
  else: die4()



def Swordscene():
  print ("You pull out your sword, and you are ready to battle.")
  time.sleep(1)
  print ("You charge at them and...")
  time.sleep(1)
  print ("you are dead.")





def lightscene():
  print ("The light shines brightly, the army is distracted.")
  time.sleep(1)
  print ("Suddenly the light bursts and sends you flying!")
  time.sleep(1)
  print(" the army is dead.")
  time.sleep(1)
  choice = input("there are guns on the floor, and there are strange looking capsules too. what do you want to pickup?")
  if choice == "pick up everything" or choice == "pickup all" or choice == "yes":
    print ("you picked up a key (type ¬¬ to use it at a door), you picked up a gun that has full ammo, you picked up some capsules too.")
    choice1()
  else: 
    die_Joke()

def choice1():
  while True:
    choice = input ("what would you like to do?")
    if choice == "Travel to Black Area" or choice == "go to black area" or choice == "travel to black area" or choice == "black area":
      void2()
    elif choice == "follow boltremixes and his friends Charzy6969 and xdstexin on twitch.":
      print ("You Win. btw follow them pls im desperate.")
    else:
      print ("you do not understand what you just said.")



def void2():
  print("You walk to a Jet black dark area, there is a castle there")
  time.sleep(1)
  print("Suddenly you get dragged into the massive castle!")
  time.sleep(1)
  print("its locked.")
  time.sleep(1)
  choice = input("What do you do?")
  if choice == "¬¬":
    void2con()
  elif choice == "``":
    print("hahahahahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
  else:
    time.sleep(1)
    print("Void's guard shoots your head off")
    exit()
  
def void2con():
  import time
  time.sleep(2)
  print ("you unlock the door")
  time.sleep(2)
  print ("you see him. Void aka Big Chungus.")
  print ("your light has gone, however you sword is shining brightly.")
  print ("""
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣧⠀⠀⠀⢰⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡟⡆⠀⠀⣿⡇⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⣿⠀⢰⣿⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡄⢸⠀⢸⣿⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡇⢸⡄⠸⣿⡇⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⢸⡅⠀⣿⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣥⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡿⡿⣿⣿⡿⡅⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠉⠀⠉⡙⢔⠛⣟⢋⠦⢵⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣄⠀⠀⠁⣿⣯⡥⠃⠀⢳⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡇⠀⠀⠀⠐⠠⠊⢀⠀⢸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⡿⠀⠀⠀⠀⠀⠈⠁⠀⠀⠘⣿⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣷⡀⠀⠀⠀
⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣧⠀⠀
⠀⠀⠀⡜⣭⠤⢍⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢛⢭⣗⠀
⠀⠀⠀⠁⠈⠀⠀⣀⠝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠠⠀⠀⠰⡅
⠀⠀⠀⢀⠀⠀⡀⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠔⠠⡕⠀
⠀⠀⠀⠀⣿⣷⣶⠒⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠊⠉⢆⠀⠀⠀⠀
⠀⢀⠤⠀⠀⢤⣤⣽⣿⣿⣦⣀⢀⡠⢤⡤⠄⠀⠒⠀⠁⠀⠀⠀⢘⠔⠀⠀⠀⠀
⠀⠀⠀⡐⠈⠁⠈⠛⣛⠿⠟⠑⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠉⠑⠒⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
  """)
  
  choice = input("what do you do?")
  if choice == "use sword" or choice == "sword":
    print("You pull out your sword.")
    swordscene2()
  elif choice == "use light" or choice == "light":
    print ("You dont have the light anymore.")
    dievoid2()
  else:
    print("You were too slow and Big chungus destroys your soul.")
    quit()

def dievoid2():
  print("you charge at him anyway without the light and you drop dead.")
  quit()


def swordscene2():
  time.sleep(2)
  print("You charge at him dodging all the attacks he throws at you.")
  time.sleep(2)
  print("You jump off from the ground and stab him in the head.")
  time.sleep(2)
  print("large letters appear in the air.")
  print ("""
  ______     ______     __    __     ______        ______     ______     __    __     ______   __         ______     ______   ______    
/\  ___\   /\  __ \   /\ "-./  \   /\  ___\      /\  ___\   /\  __ \   /\ "-./  \   /\  == \ /\ \       /\  ___\   /\__  _\ /\  ___\   
\ \ \__ \  \ \  __ \  \ \ \-./\ \  \ \  __\      \ \ \____  \ \ \/\ \  \ \ \-./\ \  \ \  _-/ \ \ \____  \ \  __\   \/_/\ \/ \ \  __\   
 \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\     \ \_____\  \ \_____\  \ \_\ \ \_\  \ \_\    \ \_____\  \ \_____\    \ \_\  \ \_____\ 
  \/_____/   \/_/\/_/   \/_/  \/_/   \/_____/      \/_____/   \/_____/   \/_/  \/_/   \/_/     \/_____/   \/_____/     \/_/   \/_____/ 
                                                                                                                                       
  """)
  end()


def end():
  print("You wake up in a headset, you slip it off and it turns out you are in a hospital.")
  time.sleep(1)
  print("It was just virtual reality.")
  print("THE END!")




def die4():
  print("the army shoots you to death")
  print("gg you got quite far!")
  quit()

def dielol():
  print ("okay then, a meteor kills you.")
  quit()


def die_3():
  print("You walk to a Jet black dark area, there is a castle there")
  print("Suddenly you get dragged into the massive castle!")
  print("You see him, Void the final Boss. He leaps at you knocking you out.")
  print("You were unprepared and now the human race is non exsistant!!!!!")
  print("You lose. Well done.")
  quit()

def die_Joke(): 
 print("you stay there forever and you starve to death.")
 print("lol")
 print("you died.. GG")
 quit()

def die_first(): 
 print("the unkown creature takes his sword out. he stabs you, you dont have a weapon.")
 print("you bleed alot, everything fades.")
 print("you died.. GG")
 quit()


crater()