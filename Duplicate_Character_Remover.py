# Delera, Aritz B.

# Create a CharacterRemovalProcess class
class CharacterRemovalProcess:
    def __init__(self, user_input):
        self.user_input = user_input

    # define the removal of duplicates
    def duplicates_removal(self):
        present = set()
        result = []

        # use for loop to add and append the characters
        for character in self.user_input:
            if character not in present:
                present.add(character)
                result.append(character)

        # use join method to return the result
        return ''.join(result)
