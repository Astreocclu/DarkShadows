import pygame
from constants import tile_size

player_turrets = []
enemy_turrets = []


class Unit:
    def __init__(self, x, y, team, max_hp, attack_damage, attack_range, symbol, move_range=1, area_effect=1):
        self.x = x
        self.y = y
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.attack_damage = attack_damage
        self.attack_range = attack_range
        self.move_range = move_range
        self.area_effect = area_effect
        self.symbol = symbol
        self.font = pygame.font.Font(None, 24)  # Initialize the font here
        self.team = team

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
    def __init__(self, x, y, team):
        super().__init__(x, y, team=team, max_hp=100, attack_damage=30, attack_range=3, symbol='A', move_range=2, area_effect=1)

class Mage(Unit):
    def __init__(self, x, y, team):
        super().__init__(x, y, team=team, max_hp=150, attack_damage=40, attack_range=2, symbol='M', move_range=1, area_effect=2)

class Warrior(Unit):
    def __init__(self, x, y, team):
        super().__init__(x, y, team=team, max_hp=200, attack_damage=50, attack_range=1, symbol='W', move_range=1, area_effect=1)
        
class Thief(Unit):
    def __init__(self, x, y, team):
        super().__init__(x, y, max_hp=150, attack_damage=40, attack_range=2, symbol='T', move_range=1, area_effect=1) 
      
class ArcherThief(Unit):
    def __init__(self, x, y, team):
        super().__init__(x, y, max_hp=200, attack_damage=50, attack_range=1, symbol='AT', move_range=1, area_effect=1)

class Priest(Unit):
    def __init__(self, x, y, team):
        super().__init__(x, y, max_hp=120, attack_damage=20, attack_range=1, symbol='P', team=team, move_range=1, area_effect=1)

    def heal(self, target):
        if self.distance_to(target) <= self.area_effect:
            print(f"{self} is healing {target}")
            target.current_hp += 75  # Heal amount
            if target.current_hp > target.max_hp:
                target.current_hp = target.max_hp
            return True
        return False


class Engineer(Unit):
    def __init__(self, x, y, team):
        super().__init__(x, y, team, max_hp=100, attack_damage=10, attack_range=2, symbol='E', move_range=2, area_effect=2)
        self.turret = None

    def deploy_turret(self, enemy_army):
        # Find an enemy within attack range
        for enemy in enemy_army:
            if self.in_attack_range(enemy):
                # If an enemy is found, deploy the turret at current position
                new_turret = Turret(self.x, self.y)
                if self.team == 'player':
                    player_turrets.append(new_turret)
                else:
                    enemy_turrets.append(new_turret)
                break  # Stop searching after deploying turret


class Turret:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.attack_damage = 10
        self.attack_range = 2
        self.symbol = 'T'
        self.font = pygame.font.Font(None, 24)  # Initialize the font here

    def __str__(self):
        return f"{self.__class__.__name__} at ({self.x}, {self.y})"

    def in_attack_range(self, target):
        distance = abs(self.x - target.x) + abs(self.y - target.y)
        return distance <= self.attack_range

    def attack(self, target):
        if self.in_attack_range(target):
            print(f"{self} is attacking {target}")
            target.current_hp -= self.attack_damage
            if target.is_dead():
                print(f"{target} has been defeated!")
            return True
        return False

    def draw(self, screen, color):
        text = self.font.render(self.symbol, True, color)
        screen.blit(text, (self.x * tile_size + tile_size // 2, self.y * tile_size + tile_size // 2))
