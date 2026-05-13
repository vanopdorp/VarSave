import dill as pickle
import inspect
import types

def is_instance(obj):
    return (
        hasattr(obj, "__dict__") and
        not isinstance(obj, type) and
        not isinstance(obj, types.ModuleType) and
        not inspect.isfunction(obj) and
        not inspect.ismethod(obj)
    )

def get_real_caller():
    frame = inspect.currentframe().f_back
    while frame:
        module = inspect.getmodule(frame)
        if module and not module.__name__.startswith("varsave"):
            return frame
        frame = frame.f_back
    raise RuntimeError("Can't find caller outside varsave")

def save_everything():
    data = {}

    frame = get_real_caller()
    caller_globals = frame.f_globals
    caller_locals = frame.f_locals

    globals_copy = {}
    for k, v in caller_globals.items():
        if not k.startswith("__"):
            globals_copy[k] = v
    data["globals"] = globals_copy

    locals_copy = {}
    for k, v in caller_locals.items():
        if not k.startswith("__"):
            locals_copy[k] = v
    data["locals"] = locals_copy

    objects = {}
    for name, value in {**globals_copy, **locals_copy}.items():
        if is_instance(value):
            objects[name] = value.__dict__.copy()

    data["objects"] = objects
    return data

def load_everything(data):
    frame = get_real_caller()
    caller_globals = frame.f_globals

    for k, v in data.get("globals", {}).items():
        caller_globals[k] = v

    for name, attrs in data.get("objects", {}).items():
        if name in caller_globals:
            obj = caller_globals[name]
            for ak, av in attrs.items():
                setattr(obj, ak, av)

def save_to_file(filename="snapshot.pkl"):
    data = save_everything()
    with open(filename, "wb") as f:
        pickle.dump(data, f)

def load_from_file(filename="snapshot.pkl"):
    with open(filename, "rb") as f:
        data = pickle.load(f)
    load_everything(data)
