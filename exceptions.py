class Solution(Exception):
    def __init__(self, x):
        super().__init__()
        self.x = x


class Constant(Exception):
    def __init__(self):
        super().__init__()


class Derivative(Exception):
    def __init__(self):
        super().__init__()


class Step(Exception):
    def __init__(self):
        super().__init__()
