#!/usr/bin/env python3
"""
annotated original code
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return element length"""
    return [(i, len(i)) for i in lst]
