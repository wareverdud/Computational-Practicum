class SolutionException(Exception):
    def __init__(self, x):
        super().__init__()
        self.x = x


class ConstantException(Exception):
    def __init__(self):
        super().__init__()


class DerivativeException(Exception):
    def __init__(self):
        super().__init__()


class StepException(Exception):
    def __init__(self):
        super().__init__()
