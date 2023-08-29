#!/usr/bin/env python3
"""
Takes a string k and an int OR float v as arguments and returns a tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, v**2)
