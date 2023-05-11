# grid.py

import pygame
import random

grid_width = 15
grid_height = 15


def draw_grid(screen, grid_width, grid_height, tile_size):
    for row in range(grid_height):
        for col in range(grid_width):
            tile_color = (255, 255, 255)  # White
            pygame.draw.rect(screen, tile_color, (col * tile_size, row * tile_size, tile_size, tile_size), 1)


def random_starting_positions(n, grid_width, grid_height):
    positions = []

    # Create a list of all possible positions in the grid
    all_positions = [(x, y) for x in range(grid_width) for y in range(grid_height)]

    # Divide the grid into two halves
    half = grid_width // 2
    player_positions = [pos for pos in all_positions if pos[0] < half]
    enemy_positions = [pos for pos in all_positions if pos[0] >= half]

    # Randomly choose starting positions for player and enemy
    player_starting_positions = random.sample(player_positions, n)
    enemy_starting_positions = random.sample(enemy_positions, n)

    return player_starting_positions, enemy_starting_positions
