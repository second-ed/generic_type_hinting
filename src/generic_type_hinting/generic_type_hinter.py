from typing import Optional

import attr
from attr.validators import instance_of
from generic_type_hinting.constants import DUNDER_METHODS, TYPING_DUNDERS


@attr.define
class GenericTypeHinter:
    type_dict: dict = attr.ib(init=False, validator=[instance_of(dict)])
    common_elems_ordered: list = attr.ib(
        init=False, validator=[instance_of(list)]
    )

    def get_single_generic_type(self, obj: object) -> Optional[object]:
        has_methods = []

        for method in DUNDER_METHODS:
            if hasattr(obj, method):
                has_methods.append(method)

        for dunders, type_hint in TYPING_DUNDERS:
            if dunders.issubset(has_methods):
                return type_hint
        return None

    def get_generic_types(self, objs: list) -> list:
        if not isinstance(objs, list):
            raise TypeError(f"objs must be a list. Received {type(objs)}")
        type_hints = []
        for obj in objs:
            type_hints.append(self.get_single_generic_type(obj))
        return type_hints

    def analyse_group(self, objs: list) -> list:
        if not isinstance(objs, list):
            raise TypeError(f"objs must be a list. Received {type(objs)}")

        types = self.get_generic_types(objs)
        self.type_dict = {t: t.mro() for t in types if t is not None}

        common_elements = set(self.type_dict[next(iter(self.type_dict))])
        for lst in self.type_dict.values():
            common_elements.intersection_update(lst)

        self.common_elems_ordered = [
            elem
            for elem in self.type_dict[next(iter(self.type_dict))]
            if elem in common_elements
        ]
        return self.common_elems_ordered
