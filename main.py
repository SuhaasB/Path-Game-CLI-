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
        q1 = print("You enter and find a crowd gathered around in the distance, Do you want to investigate(y/N)?")

      elif ch2 == 'b':
        health -= 5
        ch2 = input("You found a back alley door to the City of Holkn. You sneak in and you accidently step on a glass bottle. You lose 5 health.")

        if health<=0:
          print("\nYou lost all your health, you have chosen death.")
          
    else :
      print("You have chosen death.")

else:
  print("Oops you need to be 13 or older.")

print("\nGame still in development, Thank you for playing!")


