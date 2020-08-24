from base.Unit import Unit


class Decorator(Unit):
    def __init__(self, components: list):
        super().__init__(components)
