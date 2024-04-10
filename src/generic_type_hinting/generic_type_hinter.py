import attr
from generic_type_hinting.constants import DUNDER_METHODS, TYPING_DUNDERS


@attr.define
class GenericTypeHinter:
    def get_single_generic_type(self, obj):
        has_methods = []

        for method in DUNDER_METHODS:
            if hasattr(obj, method):
                has_methods.append(method)

        for dunders, type_hint in TYPING_DUNDERS:
            if dunders.issubset(has_methods):
                return type_hint
        return None

    def get_generic_types(self, objs):
        type_hints = []
        for obj in objs:
            type_hints.append(self.get_single_generic_type(obj))

        return type_hints

    def get_group_type(self, objs):
        types = self.get_generic_types(objs)
        type_dict = {t: len(t.mro()) for t in types if t is not None}
        return min(type_dict, key=type_dict.get)
