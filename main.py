print("Welcome to my first game!")
name = input("What is your name? \n")
print("Hello,", name)
age = int(input("What is your age? \n"))

if age >=13 and age <= 80:
  print("Great!")

  cont = input("Do you want to continue(y/N)? \n").lower()
  if cont == "y":
    print("\n...Entering Dungeon...\n")

    ch1 = input("Do you want to go left(a) or right(b)?\n")
    if ch1 == 'a':
      ch2 = input("You followed a clear path and found the gatekeeper to the City of Holkn. Do you wish to talk(a) or sneak in(b)?\n")

    elif ch == 'b':
      ch2 = input("You found a back alley door to the City of Holkn. You sneak in and you find a drunk watching you. Do you ignore(a) or talk(b)?\n")

    else :
      print("You have chosen death.")

else:
  print("Oops you need to be 13 or older.")

print("\n\nGame still in development, Thank you for playing!")


