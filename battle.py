import random

from pokemon import create_default
from person import Person
from pokemon import Pokemon
from data_handling import table_print

# Battle Class
class Battle:

    # Create two class attributes
    # 1. A list to track all battles
    # 2. An integer of the amount of battles


    # A static method to print all battles
    @staticmethod
    def print_all_battles():
        # Check to see if there are no battles
        
        # Create a list of the data from each battle:       
        # The battle number, and the name, owner, and kind of the two pokemon
        
        # Table print it (headers, data, widths)
        pass

    # Initialize a battle object that takes in 2 pokemon objects
    def __init__(self, pokemon1, pokemon2):
        # Track both pokemon in a list
        
        # Create a variable that holds the result of the battle (initially set to say battle has not happened yet) 
        
        # Create a variable to get battle number (using class attribute for total amount of battles)
        
        # Update the class attribute integer and list
        pass
       

    # Create to-string method (use this when you do print(battle_object)
    # Includes the battle's number, names, and result
    def __str__(self):
        pass

    # Starts the battle   
    def start_battle(self):

        # Create convenience variables for the two combatants

        # Let the user know that two pokemon have appeared and their names
        # If both pokemon are owned, say the name of each pokemon's owner and let the user know that the pokemon are battling.
        # If only one pokemon is owned let the user know that the owned pokemon was attacked by a 'wild' pokemon.
        # If neither pokemon are owned say two 'wild' pokemon are battling

        # Start the battle with round 0
        
        # Have the pokemon battle!
        # This continues as long as both pokemon have more than 0 hp    
                   
            # Have each pokemon randomly choose a value between 1-3 to represent their attack
            
            # ORIGINAL Solution
            # Both pokemon do random damage between 1-3

            # BONUS Solution
            # Try to change damage based on the type of pokemon.
            # Divide the 18 types of pokemon in 4 different groups that do different amounts of random damage
            
            # Show the Round number and the name, kind, and HP of each pokemon
            
            # Pokemon 1 attacks first
            # Subtract pokemon1's random value from pokemon0's hp            
            # Output status of pokemon0
                        
            # Pokemon0 attacks next
            # Subtract pokemon0's random value from pokemon1's hp
            # Output status of pokemon1
            
            # This round is now over, return to the top of the loop
                       
        # The loop is over - time to find out why!
        # We'll return the winning pokemon or a list of both pokemon if there is a tie
        # We'll also heal both pokemon back to their starting values
                
        # Was it a tie?
        
        # Did pokemon0 win?
        
        # Did pokemon1 win?

        pass

                

    # Getters and Setters for the Battle class
    # These will be very useful for print_all_battles and start_battle

    # Update the pokemon battling
    def update_pokemon(self, pokemon1, pokemon2):
        pass

    # Update result of battle
    def update_result(self, result):
        pass

    # Get battle result
    def get_result(self):
        pass

    # Get battle number
    def get_battle_num(self):
        pass

    # Get one of the pokemon objects
    def get_combatant(self, number):
        pass
   
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
# Make sure you work through the user menu and complete all the missing code
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
            #Add a pokemon with the above attributes
            

        # See all pokemon
        elif user_input == "2":
            print("\nSee all Pokemon\n")
            #print all pokemon

        # Add a person
        elif user_input == "3":
            print("\nAdd a Person\n")

            # Get person's name/email
            

            # Create person object and add to person list
            

            # Let user know person has been added
            

        # See all people
        elif user_input == "4":
            print("\nSee all People\n")
            #print all the people

            
        #Adopt a pokemon
        elif user_input == "5":
            print("\nAdopt a Pokemon\n")

            # Show the available people to adopt
            print_people_list(person_list)
            person_num = input("Enter the number of the Person adopting: ")
            

            # Is the person number valid?
            

            # Are there pokemon to be adopted?    
            

            # Is the pokemon number a number?

            # Check to see if the number is valid.
            # Check to see if the pokemon is un-owned
            # If these are true, adopt!
            


        #Create a battle (list all pokemon, ask them to choose 2 pokemon battling)
        elif user_input == "6":
            print("\nCreate a Battle\n")

            # Check to see if there are pokemon
            

            # Try to get two pokemon by name and look them up, then create a Battle
            

            # When the user hits Enter, start the battle
            input("Press Enter to Start the Battle!")
            

        # See all battles, print out battle data
        elif user_input == "7":
            print("\nSee all Battles\n")

            
            
        # End Program
        elif user_input == "8":
            print("\nGoodbye!\n")
            break

        # Error handling for bad input
        elif user_input != "":
            print("\nPlease enter a valid menu option\n")
        
                    
        
       
        
     

