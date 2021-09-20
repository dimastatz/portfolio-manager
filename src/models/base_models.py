import random


class Model:
    def __init__(self, name: str):
        self.name = name

    def run(self, stock: str) -> str:
        raise Exception('Run is not implemented in Abstract Model')


class RandomModel(Model):
    def __init__(self, name: str):
        super().__init__(name)

    def run(self, stock: str) -> str:
        return 'Buy' if bool(random.getrandbits(1)) else 'Sell'
