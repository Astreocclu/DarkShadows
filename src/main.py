import pygame
import random
from grid import draw_grid, grid_width, grid_height, random_starting_positions
from constants import tile_size
from units import Archer, Mage, Warrior
from gameplay import autoplay_turn, generate_army, all_units_dead, play_again
# import the gameplay module from the gameplay.py file


pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("My 2D Auto-Chess Game")

player_color = (0, 255, 0)  # Green
enemy_color = (255, 0, 0)   # Red

running = True

clock = pygame.time.Clock()

player_starting_positions, enemy_starting_positions = random_starting_positions(4, grid_width, grid_height)

player_army = generate_army(4, player_starting_positions)
enemy_army = generate_army(4, enemy_starting_positions)


# Inside your game loop:
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Fill the screen with black

    # Draw the grid
    draw_grid(screen, grid_width, grid_height, tile_size)

    # Draw the units
    for unit in player_army:
        unit.draw(screen, player_color)
    for unit in enemy_army:
        unit.draw(screen, enemy_color)

    # Play one turn for each army
    autoplay_turn(player_army, enemy_army)
    autoplay_turn(enemy_army, player_army)

    # Check if all units in either army are dead
    if all_units_dead(player_army):
        print("All player units are dead! Game over.")
        running = play_again()
        if running:
            player_starting_positions, enemy_starting_positions = random_starting_positions(4, grid_width, grid_height)
            player_army = generate_army(4, player_starting_positions)
            enemy_army = generate_army(4, enemy_starting_positions)
    elif all_units_dead(enemy_army):
        print("All enemy units are dead! You win!")
        running = play_again()
        if running:
            player_starting_positions, enemy_starting_positions = random_starting_positions(4, grid_width, grid_height)
            player_army = generate_army(4, player_starting_positions)
            enemy_army = generate_army(4, enemy_starting_positions)

    pygame.display.update()

    # Wait for a bit between frames
    clock.tick(1)  # Wait for one second between frames


pygame.quit()