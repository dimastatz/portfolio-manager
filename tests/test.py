import sys
from typing import NamedTuple


class Point:
    def __init__(self, val: float):
        self.val = val


print(Point(1) == Point(1))

def f(node: dict) -> float:
    if node is None:
        return sys.float_info.max
    else:
        return min(node['value'], f(node['left']), node.get('right')) 