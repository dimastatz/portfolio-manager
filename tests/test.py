from typing import NamedTuple

class Sample(NamedTuple):
    name: str
    average: float 
  

x = Sample('test', 1.0)
print(x)
