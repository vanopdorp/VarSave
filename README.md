# VarSave  
A lightweight, flexible system for capturing and restoring Python runtime state.

VarSave gives you something Python normally doesn’t:  
the ability to **save the entire state of a running program** and restore it later — objects, globals, nested structures, cross‑references, and more.

It works like a “save game” system for Python scripts.

VarSave is built on top of `dill`, which allows it to serialize far more than the standard `pickle` module. This includes nested classes, closures, dynamically created objects, and complex object graphs.

---

## Features

- **Snapshot the full runtime state**  
  Globals, objects, attributes, lists, dicts — everything that matters.

- **Restore state automatically**  
  After loading, your variables and objects reappear exactly as they were.

- **Supports advanced Python constructs**  
  Thanks to `dill`, VarSave can serialize:
  - nested classes  
  - classes defined inside functions  
  - closures  
  - lambdas  
  - dynamically created objects  

- **Cross‑reference safe**  
  Objects that reference each other restore correctly.

## Simple API

VarSave keeps its interface intentionally small and easy to understand.  
There are four core functions you will use:

### `save_to_file(path)`
Save the current runtime state directly to a file.

- **Arguments:**  
  `path` — the filename to write the snapshot to (e.g. `"snapshot.pkl"`)

- **Returns:**  
  Nothing

---

### `load_from_file(path)`
Load a previously saved snapshot and restore all globals and objects into the current module.

- **Arguments:**  
  `path` — the filename containing the saved snapshot

- **Returns:**  
  Nothing

---

### `save_everything()`
Capture the entire runtime state and return it as a Python object (a dill‑serializable dictionary).

- **Arguments:**  
  None

- **Returns:**  
  A Python dictionary containing:
  - all globals  
  - all locals  
  - all object attributes  
  - all nested structures  

This is useful if you want to manipulate or store the snapshot yourself instead of writing it to a file.

---

### `load_everything(data)`
Restore a previously captured snapshot into the current module.

- **Arguments:**  
  `data` — the snapshot object returned by `save_everything()` or loaded from a dill file

- **Returns:**  
  Nothing

This function injects variables back into the caller’s global namespace and restores object attributes exactly as they were.


---

## Installation

Install VarSave from PyPI:

```bash
pip install varsave
```

VarSave automatically installs `dill` as a dependency.

---

## Quick Start

### Saving a snapshot

```python
from varsave import save_to_file

x = 42

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = ["sword", "potion"]

p = Player("Alice")

save_to_file("snapshot.pkl")
```

### Restoring a snapshot

```python
from varsave import load_from_file

class Player:
    def __init__(self, name=""):
        self.name = name
        self.inventory = []

load_from_file("snapshot.pkl")

print(x)          # 42
print(p.name)     # Alice
print(p.inventory)  # ['sword', 'potion']
```

---

## How It Works

VarSave inspects the caller’s execution frame and collects:

- all global variables  
- all local variables  
- all object attributes  
- all nested structures  

It then serializes this data using `dill` and writes it to a file.

When restoring, VarSave injects the saved variables back into the caller’s global namespace and reconstructs object attributes.

This makes it possible to pause and resume complex programs without manually managing state.

---

## Advanced Example

VarSave can handle nested classes, dynamic objects, and cross‑references:

```python
from varsave import save_to_file

class Game:
    class Player:
        def __init__(self, name):
            self.name = name
            self.hp = 100

    class Enemy:
        def __init__(self, species):
            self.species = species

game = Game()
player = Game.Player("Alice")
enemy = Game.Enemy("Orc")

# Cross‑references
player.target = enemy
enemy.target = player

save_to_file("snapshot.pkl")
```

Restoring:

```python
from varsave import load_from_file

class Game:
    class Player:
        def __init__(self, name=""):
            self.name = name
            self.hp = 0

    class Enemy:
        def __init__(self, species=""):
            self.species = species

load_from_file("snapshot.pkl")

print(player.name)       # Alice
print(enemy.species)     # Orc
print(player.target)     # <Enemy object>
print(enemy.target)      # <Player object>
```

---

## Important Notes

- Classes must be re‑defined before calling `load_from_file()`.  
  VarSave restores **instances**, not class definitions.

- Open file handles, sockets, and active threads cannot be serialized.

- Snapshot files created with older versions of VarSave may not be compatible with future versions.

---

## License

VarSave is released under the **GPL‑3.0** license.  
See the `LICENSE` file for details.

---

## Contributing

Contributions are welcome!  
If you have ideas, improvements, or bug reports, feel free to open an issue or submit a pull request on GitHub:

**https://github.com/vanopdorp/VarSave**

---

## Why VarSave?

Because sometimes you just want to stop your program, walk away, and come back later — without losing anything.

VarSave makes that possible.
