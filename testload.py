from varsave import load_from_file


class GameWorld:
    class Player:
        def __init__(self, name="", level=0):
            self.name = name
            self.level = level
            self.inventory = []
            self.stats = {}

    class Enemy:
        def __init__(self, species="", strength=0):
            self.species = species
            self.strength = strength

    def __init__(self):
        self.players = []
        self.enemies = []


def create_dynamic_class():
    class DynamicObject:
        def __init__(self, value=0):
            self.value = value
            self.tags = []
    return DynamicObject


DynamicClass = create_dynamic_class()

load_from_file("snapshot.pkl")

print("=== RESTORED STATE ===")

print("World players:", [p.name for p in world.players])
print("World enemies:", [e.species for e in world.enemies])

print("Player 1 inventory:", world.players[0].inventory)
print("Player 2 inventory:", world.players[1].inventory)

print("Player 1 rival:", world.players[0].rival.species)
print("Enemy 1 target:", world.enemies[0].target.name)

print("Dynamic object 1 value:", dyn1.value)
print("Dynamic object 1 owner:", dyn1.owner.name)

print("Score:", score)
print("Settings:", settings)
