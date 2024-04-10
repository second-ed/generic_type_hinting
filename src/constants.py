from typing import (
    Collection,
    Container,
    Iterable,
    Mapping,
    Reversible,
    Sequence,
    Set,
    Sized,
)

DUNDER_METHODS = {
    "__and__",
    "__contains__",
    "__eq__",
    "__ge__",
    "__getitem__",
    "__gt__",
    "__iter__",
    "__le__",
    "__len__",
    "__lt__",
    "__ne__",
    "__or__",
    "__reversed__",
    "__sub__",
    "__xor__",
    "count",
    "get",
    "index",
    "items",
    "keys",
    "values",
}

ITERABLE = {"__iter__"}

SIZED = {"__len__"}

CONTAINER = {"__contains__"}

COLLECTION = ITERABLE | SIZED | CONTAINER

REVERSIBLE = ITERABLE | {"__reversed__"}

SEQUENCE = COLLECTION | REVERSIBLE | {"__getitem__", "index", "count"}

MAPPING = COLLECTION | {
    "__getitem__",
    "__eq__",
    "__ne__",
    "get",
    "items",
    "keys",
    "values",
}

SET = COLLECTION | {
    "isdisjoint",
    "__le__",
    "__lt__",
    "__gt__",
    "__ge__",
    "__eq__",
    "__ne__",
    "__and__",
    "__or__",
    "__sub__",
    "__xor__",
}


TYPING_DUNDERS = (
    (SET, Set),
    (MAPPING, Mapping),
    (SEQUENCE, Sequence),
    (REVERSIBLE, Reversible),
    (COLLECTION, Collection),
    (CONTAINER, Container),
    (SIZED, Sized),
    (ITERABLE, Iterable),
)
