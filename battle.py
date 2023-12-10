import random

from pokemon import create_default
from person import Person
from pokemon import Pokemon
from data_handling import table_print

# Battle Class
class Battle:

    # Class attributes
    __all_battles_list = []
    __num_battles = 0

    # A static method to print all battles
    @staticmethod
    def print_all_battles():
        # List of data from each battle
        battle_list = []

        # Check to see if there are no battles
        if len(Battle.__all_battles_list) == 0:
            print("No battles to present.")
            return 0

        # Loop through each battle in the list of all battles
        for battle in Battle.__all_battles_list:
            # Get the pokemon in each battle
            pokemon1 = battle.get_combatant(0)
            pokemon2 = battle.get_combatant(1)

            # To the battle list, add the battle number, the name, owner, and kind of the two pokemon, and the battle's result
            battle_list.append((battle.get_battle_num(), pokemon1.get_name(), pokemon1.get_owner(), 
                                pokemon1.get_kind(), pokemon2.get_name(), pokemon2.get_owner(), 
                                pokemon2.get_kind(), battle.get_result()))


        # Table print the list of data (headers, data, widths)
        table_print(("Battle #", "Pokemon1", "Owner", "Kind", "Pokemon2", "Owner", "Kind", "Result"),
                    battle_list,
                    (10, 10, 10, 10, 10, 10, 10, 10))

    # Initialize a battle object that takes in 2 pokemon objects
    def __init__(self, pokemon1, pokemon2):
        self.__fighters = [pokemon1, pokemon2] # Tracks both pokemon
        
        self.__battle_result = "Battle hasn't started yet." # Holds the result of the battle
        
        self.__battle_number = self.__num_battles # Battle number

        # Update the class attribute integer and list
        Battle.__all_battles_list.append(self)
        Battle.__num_battles += 1

    # To-string method
    # Includes the battle's number, names, and result
    def __str__(self):
        reply = "---Battle---\n"
        reply += "Number: " + str(self.get_battle_num()) + "\n"
        reply += "Pokemon 1 Name: " + self.get_combatant(0).get_name() + "\n"
        reply += "Pokemon 2 Name: " + self.get_combatant(1).get_name() + "\n"
        reply += "Result: " + self.get_result() + "\n"

        return reply

    # Starts the battle   
    def start_battle(self):

        # Convenience variables for the two combatants
        pokemon0 = self.get_combatant(0)
        pokemon1 = self.get_combatant(1)

        # Let the user know that two pokemon have appeared and their names
        print(pokemon0.get_name() + " has appeared.")
        print(pokemon1.get_name() + " has appeared.")

        # If both pokemon are owned, say the name of each pokemon's owner and let the user know that the pokemon are battling.
        if pokemon0.get_owner() != "None" and pokemon1.get_owner() != "None":
            print(f"{pokemon0.get_owner()}'s and {pokemon1.get_owner()}'s pokemon are battling!")

        # If only one pokemon is owned let the user know that the owned pokemon was attacked by a 'wild' pokemon.
        elif pokemon0.get_owner() != "None" and pokemon1.get_owner() == "None":
            print(f"{pokemon0.get_owner()}'s pokemon was attacked by a wild pokemon!")
        elif pokemon0.get_owner() == "None" and pokemon1.get_owner() != "None":
            print(f"{pokemon1.get_owner()}'s pokemon was attacked by a wild pokemon!")
        
        # If neither pokemon are owned say two 'wild' pokemon are battling
        else:
            print("Two wild pokemon are battling!")

        # Start the battle with round 0
        round_number = 0

        # Have the pokemon battle!
        # This continues as long as both pokemon have more than 0 hp    
        while pokemon0.get_hp() > 0 and pokemon1.get_hp() > 0:

            # Show the Round number
            print("-" * 50)
            print("Round: " + str(round_number))

            # Show name, kind, and HP of each pokemon
            print(f"{pokemon0.get_name()} ({pokemon0.get_kind()})'s HP: {pokemon0.get_hp()}")
            print(f"{pokemon1.get_name()} ({pokemon1.get_kind()})'s HP: {pokemon1.get_hp()}")
            print()

            # Pokemon 1 attacks first
            pokemon1_attack = random.randint(1, 3)

            # Subtract pokemon1's random value from pokemon0's hp   
            pokemon0.set_hp(pokemon0.get_hp() - pokemon1_attack)

            # Output status of pokemon0
            print(f"{pokemon1.get_name()} ({pokemon1.get_kind()}) is attacking and did {pokemon1_attack} damage!")
            print(f"{pokemon0.get_name()} ({pokemon0.get_kind()})'s new HP is {pokemon0.get_hp()}")
            print()

            # Pokemon0 attacks next
            pokemon0_attack = random.randint(1, 3)

            # Subtract pokemon0's random value from pokemon1's hp
            pokemon1.set_hp(pokemon1.get_hp() - pokemon0_attack)

            # Output status of pokemon1
            print(f"{pokemon0.get_name()} ({pokemon0.get_kind()}) is attacking and did {pokemon0_attack} damage!")
            print(f"{pokemon1.get_name()} ({pokemon1.get_kind()})'s new HP is {pokemon1.get_hp()}")

            # Increment round number for start of next round
            round_number += 1 

            
        # Display results from battle
        print("-" * 50)

        # If battle ended with both pokemon at or below 0 HP, it was a tie
        if pokemon0.get_hp() <= 0 and pokemon1.get_hp() <= 0:
            # Display both pokemon's names and say it was a tie
            print(f"{pokemon0.get_name()} ({pokemon0.get_kind()}) and {pokemon1.get_name()} ({pokemon1.get_kind()}) tied")
            self.update_result("There has been a tie!") # Update result variable
        
        # If pokemon0 has 0 or less HP, but pokemon1 has more than 0 HP, pokemon1 wins
        elif pokemon0.get_hp() <= 0:
            # Display names and say pokemon1 won
            print(f"{pokemon1.get_name()} ({pokemon1.get_kind()}) has beaten {pokemon0.get_name()} ({pokemon0.get_kind()})")
            self.update_result(f"{pokemon1.get_name()} has won") # Update result variable
        
        # Otherwise, pokemon0 wins
        else:
            # Display names and say pokemon 0 won
            print(f"{pokemon0.get_name()} ({pokemon0.get_kind()}) has beaten {pokemon1.get_name()} ({pokemon1.get_kind()})")
            self.update_result(f"{pokemon0.get_name()} has won") # Update result variable
        
        # Heal both pokemon back to their starting values
        pokemon0.set_hp(4)
        pokemon1.set_hp(4)


    # Getters and Setters for the Battle class

    # Update the pokemon battling
    def update_pokemon(self, pokemon1, pokemon2):
        self.__fighters = [pokemon1, pokemon2]

    # Update result of battle
    def update_result(self, result):
        self.__battle_result = result

    # Get battle result
    def get_result(self):
        return self.__battle_result

    # Get battle number
    def get_battle_num(self):
        return self.__battle_number

    # Get one of the pokemon objects
    def get_combatant(self, number):
        if number >= 0 and number < 2:
            return self.__fighters[number]
   
# This function is used to print all of the people in our system
def print_people_list(person_list):
    # Initialize local variables
    people_data = []
    number = 0

    # Check to see if there are no people
    if len(person_list) == 0:
        print("No people to list.")
        return

    # Add all the people to our list
    for person in person_list:
        people_data.append((number, person.get_name(), person.get_email()))
        number += 1

    # Table print the list
    table_print( ("Number", "Name", "Email"), people_data, (10,10,10) )
 
    
# DO NOT DELETE - creates starting pokemon/people
# and adds people to a list to keep track of people
person_list = create_default()

# Create a user menu
if __name__ == "__main__":

    while True:
        # Output a user menu with 8 Menu options
        print("\nWelcome to the Pokemon Battle Program!")
        print("Your options are:")
        print("1 - Add a Pokemon\n2 - See all Pokemon\n3 - Add a Person\n4 - See all People \
              \n5 - Adopt a Pokemon\n6 - Create a Battle\n7 - See all Battles\n8 - Quit")
        user_input = input("Choose an option: ")
        
        # Add a pokemon
        if user_input == "1":
            print("\nAdd a Pokemon\n")
            name = input("What is the pokemon's name? ")
            kind = input("What is the pokemon's kind? ")
            pokemon_type = input("What is the pokemon's type? ")

            # Create a pokemon with the above attributes
            Pokemon(name, kind, pokemon_type)
            

        # See all pokemon
        elif user_input == "2":
            print("\nSee all Pokemon\n")
            Pokemon.print_all_pokemon()

        # Add a person
        elif user_input == "3":
            print("\nAdd a Person\n")

            # Get person's name/email
            name = input("What is the person's name? ")
            email = input("What is the person's email? ")

            # Create person object and add to person list
            person_list.append(Person(name, email))

            # Let user know person has been added
            print("Added " + name)

        # See all people
        elif user_input == "4":
            print("\nSee all People\n")
            print_people_list(person_list)

            
        #Adopt a pokemon
        elif user_input == "5":
            print("\nAdopt a Pokemon\n")

            # Show the available people to adopt
            print_people_list(person_list)

            # Get user input for the number of the person adopting, check that input is valid
            try:
                person_num = int(input("Enter the number of the Person adopting: "))
            except:
                print("Input must be an integer.")
                continue # If input is not an integer, return to start of while loop
            
            # Check if input is in range of list of people. If not, return to start of loop
            if not (person_num >= 0 and person_num < len(person_list)):
                print("No person with that number exists. Input must be between 0-" + str(len(person_list) - 1))
                continue

            # Print list of pokemon without owners
            Pokemon.print_non_owned_pokemon()

            # Get user input for the number of the pokemon to adopt, check if valid input
            try:
                pokemon_num = int(input("Choose a pokemon's number: "))
            except:
                print("Input must be an integer.")
                continue # If input is not an integer, return to start of loop
            
            # Find pokemon with user's number
            user_pokemon = Pokemon.find_pokemon(pokemon_num)
            
            # If no pokemon has that number, print error message
            if user_pokemon == -1:
                print("No pokemon with that number.")
            
            # If that pokemon is already owned, print error message
            elif user_pokemon.get_owner() != "None":
                print("That pokemon already has an owner.")
            
            # Otherwise, set chosen person to the owner of chosen pokemon and print success message
            else:
                user_pokemon.adopt(person_list[person_num])
                print(person_list[person_num].get_name() + " adopted " + user_pokemon.get_name())

        # Create a battle
        elif user_input == "6":
            print("\nCreate a Battle\n")
            
            # List all pokemon
            Pokemon.print_all_pokemon()

            # Get user input of first pokemon to battle, check that input is valid
            try:
                pokemon1_num = int(input("Enter the number of the first pokemon: "))
            except:
                print("Input must be an integer.")
                continue
            
            # Find pokemon with inputted integer
            pokemon1 = Pokemon.find_pokemon(pokemon1_num)

            # If no pokemon with that number exist, print error message and return to start of loop
            if pokemon1 == -1:
                print("No pokemon by that number exists.")
                continue

            # Get user input of second pokemon to battle, check that input is valid
            try:
                pokemon2_num = int(input("Enter the number of the second pokemon: "))
            except:
                print("Input must be an integer.")
                continue
            
            # Find pokemon with inputted integer
            pokemon2 = Pokemon.find_pokemon(pokemon2_num)

            # If no pokemon with that number exist, print error message and return to start of loop
            if pokemon2 == -1:
                print("No pokemon by that number exists.")
                continue
            
            # Create the battle
            battle = Battle(pokemon1, pokemon2)

            # Display battle number, names of pokemon battling, and initial result
            print(f"Battle Number: {battle.get_battle_num()}")
            print(pokemon1.get_name() + " vs " + pokemon2.get_name())
            print(f"Result: {battle.get_result()}")
            
            # When the user hits Enter, start the battle
            input("\nPress Enter to Start the Battle!")
            
            # Start the battle
            battle.start_battle() 

        # See all battles, print out battle data
        elif user_input == "7":
            print("\nSee all Battles\n")
            Battle.print_all_battles()
            
        # End Program
        elif user_input == "8":
            print("\nGoodbye!\n")
            break

        # Error handling for bad input
        elif user_input != "":
            print("\nPlease enter a valid menu option\n")