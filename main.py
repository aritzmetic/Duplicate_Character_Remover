# Delera, Aritz B.

# in seperate file, call the CharacterRemovalProcess class by importing the other file
from Duplicate_Character_Remover import CharacterRemovalProcess

import pyfiglet
import time

opening = pyfiglet.figlet_format("= D.S.A =", font = "starwars")
print(opening)


# Create an introduction
print("=" * 51)
print("\033[32m Welcome to AritzMetic's Duplicate Remover! \033[0m".center(60, "+"))
print("=" * 51)

# Ask the name of the user to create a greeting
name = input("\033[34mHi Smart Pipol! what is your name?\033[0m")

time.sleep(1)
print()

print(f"\033[34mHello, {name}!\033[0m")

time.sleep(1)

answer = input("\033[34mAre you ready to remove duplicate characters from strings? (yes/no):  \033[0m").lower()

time.sleep(1)
print()

if answer == "yes":
    print("\033[45mAYOOOO! Let's get started.🔰\033[0m")
elif answer == "no":
    print("\033[45mOKIIIII! No problem. Whenever you're ready, just run the program again.😉\033[0m")
else:
    print("\033[45mBalakadiyan🥹, but let's continue.\033[0m")

time.sleep(1)
print("=" * 51)
print("\033[32m Loading... \033[0m".center(60))
print("=" * 51)
time.sleep(1)


# interact with the user by asking the number of strings
if __name__ == "__main__":
    N = int(input("\033[32mEnter the number of strings: \033[0m"))

    # declare the results to store the list
    results = []

    # use for loop and call the method from the another file
    for s in range(N):
        user_input = input("\033[31mEnter a string: \033[0m")
        remover = CharacterRemovalProcess(user_input)
        duplicate_removed = remover.duplicates_removal()
        results.append(duplicate_removed)

# display the results
    print()
    print("\033[44mResults: \033[0m")
    for result in results:
        time.sleep(1)
        print("=" * 51)
        print("\033[33m Processing Your Duplicated-Free Word/s!...\033[0m".center(60))
        print("=" * 51)
        time.sleep(1)
        print()
        print(result)
    
    time.sleep(1)
    closing = pyfiglet.figlet_format("Thank you for using AritzMetic's Duplicate Remover. Have a nice day!", font="bubble")
    print(closing)
