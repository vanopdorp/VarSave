from varsave import save_to_file, save_everything

class GameWorld:
    class Player:
        def __init__(self, name, level):
            self.name = name
            self.level = level
            self.inventory = []
            self.stats = {"hp": 100, "mana": 50}

    class Enemy:
        def __init__(self, species, strength):
            self.species = species
            self.strength = strength

    def __init__(self):
        self.players = []
        self.enemies = []


def create_dynamic_class():
    class DynamicObject:
        def __init__(self, value):
            self.value = value
            self.tags = ["dynamic", "runtime"]

    return DynamicObject


DynamicClass = create_dynamic_class()


world = GameWorld()

p1 = GameWorld.Player("Alice", 12)
p1.inventory.append("Sword")
p1.inventory.append("Health Potion")

p2 = GameWorld.Player("Bob", 7)
p2.inventory.append("Bow")

world.players.extend([p1, p2])

e1 = GameWorld.Enemy("Orc", 30)
e2 = GameWorld.Enemy("Dragon", 200)

world.enemies.extend([e1, e2])

dyn1 = DynamicClass(999)
dyn2 = DynamicClass(123)

p1.rival = e1
e1.target = p1

p2.partner = dyn1
dyn1.owner = p2

score = 42
settings = {"difficulty": "hard", "sound": True}

print("=== SNAPSHOT CONTENT ===")
print(save_everything())

save_to_file("snapshot.pkl")
