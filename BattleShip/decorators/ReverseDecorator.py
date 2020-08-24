from decorators.Decorator import Decorator
import copy


class ReverseDecorator(Decorator):
    def __init__(self, unit: Decorator):
        contents = copy.copy(unit.components)
        contents[0] = contents[0].split('.')[0] + '_rev.png'
        contents[1] = contents[1].split('.')[0] + '_rev.png'
        super().__init__(contents)
