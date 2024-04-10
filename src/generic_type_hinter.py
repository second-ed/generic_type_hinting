from src.constants import DUNDER_METHODS, TYPING_DUNDERS


def get_single_generic_type(obj):
    has_methods = []

    for method in DUNDER_METHODS:
        if hasattr(obj, method):
            has_methods.append(method)

    for dunders, type_hint in TYPING_DUNDERS:
        if dunders.issubset(has_methods):
            return type_hint
    return None


def get_generic_type(objs):
    type_hints = []
    for obj in objs:
        type_hints.append(get_single_generic_type(obj))

    return type_hints
