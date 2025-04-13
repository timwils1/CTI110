# Your Name: Timothy Wilson
# Date: April 13, 2025
# Assignment Name: P5HW_WilsonTimothy
# character creation game 

import random

def create_character():
    """
    Creates a character dictionary with attributes: name, health, and attack points.
    The function takes no parameters and returns a dictionary for a single character.
    """
    name = input("Enter character's name: ")
    health = random.randint(50, 100)
    attack_points = random.randint(10, 30)
    
    character = {
        "name": name,
        "health": health,
        "attack_points": attack_points
    }
    
    return character

def display_character(character):
    """
    Displays the character's details such as name, health, and attack points.
    This function takes the character dictionary as input and has no return value.
    """
    print(f"Character Name: {character['name']}")
    print(f"Health: {character['health']}")
    print(f"Attack Points: {character['attack_points']}")
    print()

def attack(attacker, defender):
    """
    Simulates an attack where the attacker's attack points reduce the defender's health.
    This function does not return any value.
    """
    defender['health'] -= attacker['attack_points']
    print(f"{attacker['name']} attacks {defender['name']}!")
    print(f"{defender['name']}'s new health: {defender['health']}")
    print()

def main():
    # Character creation and display
    print("Welcome to the Character Creation Game!\n")
    
    character1 = create_character()  # Create first character
    character2 = create_character()  # Create second character

    print("\nDisplaying Character 1's Info:")
    display_character(character1)

    print("Displaying Character 2's Info:")
    display_character(character2)
    
    # Battle simulation
    while character1['health'] > 0 and character2['health'] > 0:
        print("Character 1's Turn to Attack!")
        attack(character1, character2)
        
        if character2['health'] <= 0:
            print(f"{character2['name']} has been defeated!")
            break
        
        print("Character 2's Turn to Attack!")
        attack(character2, character1)
        
        if character1['health'] <= 0:
            print(f"{character1['name']} has been defeated!")
            break

    # Exit game message
    print("Game Over!")
    
if __name__ == "__main__":
    main()
