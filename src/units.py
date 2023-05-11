import pygame
from constants import tile_size
class Unit:

    def __init__(self, x, y, max_hp, attack_damage, attack_range, symbol):
        self.x = x
        self.y = y
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.attack_damage = attack_damage
        self.attack_range = attack_range
        self.symbol = symbol
        self.font = pygame.font.Font(None, 24)  # Initialize the font here

    def __str__(self):
        return f"{self.__class__.__name__} at ({self.x}, {self.y})"

    def is_dead(self):
        return self.current_hp <= 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def attack(self, target):
        if self.in_attack_range(target):
            print(f"{self} is attacking {target}")
            target.current_hp -= self.attack_damage
            if target.is_dead():
                print(f"{target} has been defeated!")
            return True
        return False

    def in_attack_range(self, target):
        distance = abs(self.x - target.x) + abs(self.y - target.y)
        return distance <= self.attack_range

    def distance_to(self, target):
        return abs(self.x - target.x) + abs(self.y - target.y)

    def direction_to(self, target):
        dx = target.x - self.x
        dy = target.y - self.y

        if abs(dx) > abs(dy):
            return (1 if dx > 0 else -1, 0)
        else:
            return (0, 1 if dy > 0 else -1)

    def draw(self, screen, color):
        text = self.font.render(self.symbol, True, color)
        screen.blit(text, (self.x * tile_size + tile_size // 2, self.y * tile_size + tile_size // 2))
class Archer(Unit):
    def __init__(self, x, y):
        super().__init__(x, y, max_hp=100, attack_damage=30, attack_range=3, symbol='A')

class Mage(Unit):
    def __init__(self, x, y):
        super().__init__(x, y, max_hp=150, attack_damage=40, attack_range=2, symbol='M')

class Warrior(Unit):
    def __init__(self, x, y):
        super().__init__(x, y, max_hp=200, attack_damage=30, attack_range=1, symbol='W')
