characters = {
    'Jesse': 1,
    'Jaden': 2,
    'Michael': 3,
    'Marcus': 4
}
choosing = True
def character_selecting(characters, choosing):
    for character in characters.keys():
        print(character)
    character1 = input("Player 1, select a player: ")
    while choosing:
        if character1 in characters.keys():
            character2 = input("Player 2, select a player: ")
            if character2 != character1 and character2 in characters.keys():
                choosing = False
            else:
                print("Please select a character that has not been chosen")
        else:
            print("Please select a valid chacter: ")
            print(characters.keys)

character_selecting(characters, choosing)
