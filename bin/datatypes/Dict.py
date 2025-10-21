from .Value import *
from .String import *
from .List import *

class Dict(Value):
    def __init__(self, elements):
        super().__init__()
        self.elements = elements

    def added_to(self, other):
        new_dict = self.copy()
        if isinstance(other, Dict):
            new_dict.elements.update(other.elements)
            return new_dict, None
        else:
            return None, Value.illegal_operation(self, other)

    def subbed_by(self, other):
        if isinstance(other, Dict):
            common_keys = list(set(self.elements.keys()) & set(other.elements.keys()))
            new_dict = {key: self.elements[key] for key in common_keys}
            return Dict(new_dict), None
        else:
            return None, Value.illegal_operation(self, other)

    def multed_by(self, other):
        if isinstance(other, Dict):
            common_keys = list(set(self.elements.keys()) & set(other.elements.keys()))
            new_dict = {key: [self.elements[key], other.elements[key]] for key in common_keys}
            return Dict(new_dict), None
        else:
            return None, Value.illegal_operation(self, other)

    def dived_by(self, other):
        if isinstance(other, String) or isinstance(other, Number):
            if isinstance(self.elements[other.value], List) or isinstance(self.elements[other.value], Dict) :
                value = self.elements[other.value]
                if isinstance(self.elements[other.value], List) : return List(value.elements), None
                else: return Dict(value.elements), None
            elif isinstance(self.elements[other.value], String) or isinstance(self.elements[other.value], Number):
                value = self.elements[other.value]
                return String(str(value)), None
        else:
            return None, Value.illegal_operation(self, other)

    def copy(self):
        copy = Dict(self.elements)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def __str__(self):
        elements_str = [f"'{key}': {str(value)}" for key, value in self.elements.items()]
        return "{" + ", ".join(elements_str) + "}"

    def __repr__(self):
        return self.__str__()