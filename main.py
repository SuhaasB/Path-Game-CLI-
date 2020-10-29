print("Welcome to my first game!")
name = input("What is your name? \n")
age = int(input("What is your age? \n"))
health = 5

if age >=13 and age <= 80:
  print("Welcome", name, ", you start with 10 health. Make sure to choose wisely!")

  cont = input("Do you want to continue(y/N)? \n").lower()
  if cont == "y":
    print("\n...Entering Dungeon...\n")

    ch1 = input("Do you want to go left(a) or right(b)?\n")
    if ch1 == 'a':
      ch2 = input("You followed a clear path and found the gatekeeper to the City of Holkn. Do you wish to talk(a) or sneak in(b)?\n")

      if ch2 == 'a':
        print("The gatekeeper's allow you in, but warns you not to wander after 11:00 PM.")
        q1 = input("You enter and find a crowd gathered around in the distance, Do you want to investigate(y/N)?")

      elif ch2 == 'b':
        health -= 5
        ch2 = input("You found a back alley door to the City of Holkn. You sneak in and you accidently step on a glass bottle. You lose 5 health.")

        if health<=0:
          print("\nYou lost all your health, you have chosen death.")

    elif ch1 ==  'b':
      ch3 = input("You find a dingy back alley, and follow it. There's a old Tavern on one side of the road. Do you go inside(a) or continue walking(b)?\n")

      if ch3 == 'a':
        ch4 = input("You enter the tavern. A strong scent of alcohol overpowers you. There's people gambling, drinking away and arguing. Do you buy a drink(a) or find a table(b)?\n")

        if ch4 == 'a':
          ch5 = input("You sit down on a bar stool and beckoned the bartender. He asks you: 'What will you be having?' Do you choose a Sunset Rum or just water?\n")

          if ch5 == 'a':
            health -= 2
            ch6 = input("He gives you your drink. You take a sip and it tastes like you remember it. But you're starving. You start feeling weak. (You lost 2 health)\n")
          
          elif ch5 == 'b':
            ch7 = input("Just water. You don't want to relapse again. Amara would be dissapointed if she knew.\n")

        elif ch4 == 'b':
          ch8 = input("You don't feel like drinking. You sit down at table instead. There's a lot you have on your mind. You can feel a pair of eyes staring at you from across the room. Do you ignore it(a) or look up(b)?\n")
      elif ch3 == 'b':
        ch9 = input("The alley leads to a crowded main street. You try to make your way through the chaos and find a man staring at you at the corner of the street. Will you approach him(a) or look away(b)?\n")

        if ch9 == 'a':
          ch10 = input("You're curious. You try to aproach him but you lose him amid the crowd. You turn back to see a guard glaring at you\n")
        
        elif ch9 == 'b':
          ch11 = input("You couldn't care less. You walk away from the crowd right in time to avoid the guard that passed by. Did he know who you were? You hoped not.")
    
    else :
      print("You have chosen death.")

else:
  print("Oops you need to be 13 or older.")

print("\nGame still in development, Thank you for playing!")


