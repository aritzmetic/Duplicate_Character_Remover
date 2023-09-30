# Delera, Aritz B.

# in seperate file, call the CharacterRemovalProcess class by importing the other file
from Duplicate_Character_Remover import CharacterRemovalProcess

# interact with the user by asking the number of strings
if __name__ == "__main__":
    N = int(input("Enter the number of strings: "))

    # declare the results to store the list
    results = []

    # use for loop and call the method from the another file
    for s in range(N):
        user_input = input("Enter a string: ")
        remover = CharacterRemovalProcess(user_input)
        duplicate_removed = remover.duplicates_removal()
        results.append(duplicate_removed)

# display the results
    print("\nResults:")
    for result in results:
        print(result)
