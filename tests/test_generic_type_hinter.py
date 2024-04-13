import collections
import typing

import pytest
from generic_type_hinting.generic_type_hinter import GenericTypeHinter


@pytest.fixture
def get_instance() -> GenericTypeHinter:
    return GenericTypeHinter()


def test_init(get_instance: GenericTypeHinter) -> None:
    assert isinstance(get_instance, GenericTypeHinter)


@pytest.mark.parametrize(
    "objs, expected_result",
    [
        (
            [{}],
            [
                collections.abc.Mapping,
                collections.abc.Collection,
                collections.abc.Sized,
                collections.abc.Iterable,
                collections.abc.Container,
                object,
            ],
        ),
        (
            [set()],
            [
                collections.abc.Collection,
                collections.abc.Sized,
                collections.abc.Iterable,
                collections.abc.Container,
                object,
            ],
        ),
        (
            [[]],
            [
                collections.abc.Sequence,
                collections.abc.Reversible,
                collections.abc.Collection,
                collections.abc.Sized,
                collections.abc.Iterable,
                collections.abc.Container,
                object,
            ],
        ),
        (
            [{}, []],
            [
                collections.abc.Collection,
                collections.abc.Sized,
                collections.abc.Iterable,
                collections.abc.Container,
                object,
            ],
        ),
        (
            [set(), {}],
            [
                collections.abc.Collection,
                collections.abc.Sized,
                collections.abc.Iterable,
                collections.abc.Container,
                object,
            ],
        ),
        (
            [[], set()],
            [
                collections.abc.Collection,  # type: ignore
                collections.abc.Sized,
                collections.abc.Iterable,
                collections.abc.Container,
                object,
            ],
        ),
    ],
)
def test_values_analyse_group(
    get_instance: GenericTypeHinter, objs, expected_result
) -> None:
    get_instance.analyse_group(objs) == expected_result


@pytest.mark.parametrize(
    "objs",
    [
        ({"test": "case"}),
        ({"test", "case"}),
    ],
)
def test_types_analyse_group(get_instance: GenericTypeHinter, objs) -> None:
    with pytest.raises(TypeError):
        get_instance.analyse_group(objs)


@pytest.mark.parametrize(
    "objs, expected_result",
    [
        ([{}, []], [typing.Mapping, typing.Sequence]),
        ([set(), {}], [typing.Collection, typing.Mapping]),
        ([[], set()], [typing.Sequence, typing.Collection]),
    ],
)
def test_values_get_generic_types(
    get_instance: GenericTypeHinter, objs, expected_result
) -> None:
    get_instance.get_generic_types(objs) == expected_result


@pytest.mark.parametrize(
    "objs",
    [
        ({"test": "case"}),
        ({"test", "case"}),
    ],
)
def test_types_get_generic_types(
    get_instance: GenericTypeHinter, objs
) -> None:
    with pytest.raises(TypeError):
        get_instance.get_generic_types(objs)


@pytest.mark.parametrize(
    "obj, expected_result",
    [
        ([], typing.Sequence),
        (set(), typing.Collection),
        ({}, typing.Mapping),
        (1, None),
        (0.0, None),
        (" ", None),
    ],
)
def test_values_get_single_generic_type(
    get_instance: GenericTypeHinter, obj, expected_result
) -> None:
    get_instance.get_single_generic_type(obj) is None
