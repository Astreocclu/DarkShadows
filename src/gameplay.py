import random
from grid import grid_width, grid_height, random_starting_positions
from units import Archer, Mage, Warrior

def autoplay_turn(army, enemy_army):
    for unit in army:
        if unit.is_dead():
            continue

        # Find an enemy in attack range
        target = None
        for enemy in enemy_army:
            if unit.in_attack_range(enemy):
                target = enemy
                break

        if target:
            # Attack the enemy
            unit.attack(target)
            if target.is_dead():
                enemy_army.remove(target)
        else:
            # Check if there are any enemies left
            if enemy_army:
                # Move the unit towards the closest enemy
                closest_enemy = min(enemy_army, key=lambda enemy: unit.distance_to(enemy))
                dx, dy = unit.direction_to(closest_enemy)
                unit.move(dx, dy)
            else:
                # All enemies have been defeated
                print("All enemies have been defeated!")
                return

def all_units_dead(army):
    return all(unit.is_dead() for unit in army)


def play_again():
    while True:
        play_again_input = input("Would you like to play again? (y/n): ")
        if play_again_input.lower() == 'y':
            return True
        elif play_again_input.lower() == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def generate_army(num_units, starting_positions):
    unit_classes = [Archer, Mage, Warrior]
    army = []
    for position in starting_positions:
        unit_class = random.choice(unit_classes)
        x, y = position
        army.append(unit_class(x, y))
    return army
