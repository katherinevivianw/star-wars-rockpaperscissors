import random
import time

# initialize choices for player (republic) and computer (separatists)
republic_choices = ["clone army", "jedi knight", "jedi master"]
separatists_choices = ["droid army", "sith apprentice", "sith lord"]

# helper function - player chooses an option
def choose_deployment():
    republic = input("Choose a force to deploy into battle. Clone army, Jedi Knight, or Jedi Master? ").lower()
    if republic not in republic_choices:
        print("Deployment choice not valid. Please try again.")
        choose_deployment()
    return republic

# helper function - computer chooses a random option
def separatists_option():
    separatists = random.choice(separatists_choices)
    return separatists

# main program

# introduction blurb
time.sleep(2)
print("Greetings, General! Welcome to a galaxy far, far away.")
time.sleep(2)
print("The year is 21 BBY, and the Clone Wars continues to rage across the galaxy with no end in sight.")
time.sleep(2)
print("You have been newly appointed to lead the 202nd Legion and are in charge of war decisions for your battalion from here on out.")
time.sleep(2)
print("You and your squad are descending onto the elegant, beachy planet of Murkhana after hearing an anonymous tip about a Separatist base.")
time.sleep(2)
print("It’s your job to find this alliance and crush them before they can bring any further malice into the galaxy.")
time.sleep(2)
print("The rules are simple. You have three options when choosing who to deploy into battle: a clone army, a Jedi Knight, or a Jedi Master.")
time.sleep(2)
print("In order to win this battle, you must win the majority in three rounds of deployment (not counting ties). "
      "However, beware of the Dark Side and suspicious forces…")
time.sleep(2)

while True:
    round_count = 0
    win_count = 0
    while round_count <= 3:
        republic = choose_deployment()
        separatists = separatists_option()

        # account for all possible outcomes
        if republic == "clone army":
            if separatists == "droid army":
                print("You have deployed a clone army into battle. The Separatists have sent their infamous droid army against your troopers. "
                      "Let's see how this plays out...")
                time.sleep(2)
                print("Pew! Pew!")
                time.sleep(2)
                print("Pew! Pew!")
                time.sleep(2)
                print("Tie! There appears to be no clear winner in this round of deployment.")
            elif separatists == "sith apprentice":
                print("You have deployed a clone army into battle. The Separatists have sent a young Sith apprentice against your troopers. "
                    "Let's see how this plays out...")
                time.sleep(2)
                print("Pew! Pew!")
                time.sleep(2)
                print("Ksh! Ksh!")
                time.sleep(2)
                print("Tie! There appears to be no clear winner in this round of deployment.")
            elif separatists == "sith lord": # order 66 - game ends immediately
                round_count += 1
                print("You have deployed a clone army into battle. The Separatists have sent a mysterious, hooded figure against your troopers. "
                    "Let's see how this plays out...")
                time.sleep(2)
                print("Ksh! Ksh! Pew! Pew!")
                time.sleep(2)
                print("It's Darth Sidious! The Sith Master we have been searching for! We must alert the Jedi temple--")
                time.sleep(3)
                print("'Execute Order 66.'")
                time.sleep(3)
                print("Something unexpected has happened...it appears that your clone troopers have turned against the Republic!")
                time.sleep(2)
                win_count = 0
                break
        elif republic == "jedi knight":
            if separatists == "droid army":
                round_count += 1
                print("You have deployed a Jedi Knight into battle. The Separatists have sent their infamous droid army against your young apprentice. "
                      "Let's see how this plays out...")
                time.sleep(2)
                print("Ksh! Ksh!")
                time.sleep(2)
                print("Pew! Pew!")
                time.sleep(2)
                win_count += 1
                print("Congratulations! With the help of the young Jedi, the Republic has won this round of deployment.")
            elif separatists == "sith apprentice":
                print("You have deployed a Jedi Knight into battle. The Separatists have sent a young Sith apprentice against the young apprentice. "
                    "Let's see how this plays out...")
                time.sleep(2)
                print("Ksh! Ksh!")
                time.sleep(2)
                print("Ksh! Ksh!")
                time.sleep(2)
                print("Tie! There appears to be no clear winner in this round of deployment.")
            elif separatists == "sith lord":
                round_count += 1
                print("You have deployed a Jedi Knight into battle. The Separatists have sent a mysterious, hooded figure against the young apprentice. "
                    "Let's see how this plays out...")
                time.sleep(2)
                print("Ksh! Ksh!")
                time.sleep(2)
                print("It's Darth Sidious! The powerful Sith Lord we have been searching for! We must alert the Jedi temple--")
                time.sleep(2)
                print("Unfortunately, the young Jedi Knight has perished in battle. You have lost this round of deployment.")
        elif republic == "jedi master":
            if separatists == "droid army":
                round_count += 1
                print("You have deployed a Jedi Master into battle. The Separatists have sent their infamous droid army against the experienced soldier. "
                      "Let's see how this plays out...")
                time.sleep(2)
                print("Ksh! Ksh!")
                time.sleep(2)
                print("Pew! Pew!")
                time.sleep(2)
                win_count += 1
                print("Congratulations! With the help of the Jedi Master, the Republic has won this round of deployment. ")
            elif separatists == "sith apprentice":
                round_count += 1
                print("You have deployed a Jedi Master into battle. The Separatists have sent a young Sith apprentice against the experienced soldier. "
                    "Let's see how this plays out...")
                time.sleep(2)
                print("Ksh! Ksh!")
                time.sleep(2)
                print("Ksh! Ksh!")
                time.sleep(2)
                win_count += 1
                print("Congratulations! With the help of the Jedi Master, the Republic has won this round of deployment.")
            elif separatists == "sith lord":
                print("You have deployed a Jedi Master into battle. The Separatists have sent a mysterious, hooded figure against the young apprentice. "
                    "Let's see how this plays out...")
                time.sleep(2)
                print("Ksh! Ksh!")
                time.sleep(2)
                print("It's Darth Sidious! The powerful Sith Lord we have been searching for! We must alert the Jedi temple--")
                time.sleep(2)
                print("Tie! There appears to be no clear winner in this round of deployment.")

    if win_count >= 2: # majority, aka republic wins
        print("Congratulations! With the help of your bravery and leadership, the Republic has won this battle.")
        time.sleep(2)
        print("Your service will be recognized by all and has brought the galaxy a step forward in the war for peace.")
        time.sleep(2)
        print("May the Force be with you, General!")
    elif win_count <= 1: # minority, aka separatists win
        print("This battle has come to an end, and it appears the Separatists have won this time around.")
        time.sleep(2)
        print("Do not fear, General! The Force is with us, always.")
        time.sleep(2)
        print("For now, we shall bring our soldiers back to Coruscant and wish them a speedy recovery...")

    # allow players the choice to replay
    republic = input("This game has concluded. Would you like to play again? (type YES or NO). ")
    if republic == "YES":
        pass
    elif republic == "NO":
        break
    else:
        break