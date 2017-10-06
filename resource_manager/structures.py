class Definition:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def to_str(self, level):
        return f'{self.name.body} = {self.value.to_str(level)}'


class Resource:
    def __init__(self, name):
        self.name = name

    def to_str(self, level):
        return self.name.body


class Module:
    def __init__(self, module_type, module_name, params, init):
        self.module_type = module_type
        self.module_name = module_name
        self.params = params
        self.init = init

    def to_str(self, level):
        result = f'{self.module_type.body}.{self.module_name.body}(\n'

        if self.init is not None:
            result += '    ' * (level + 1) + f'@init = {self.init.to_str(level)}\n'

        for param in self.params:
            result += '    ' * (level + 1) + param.to_str(level + 1) + '\n'

        return result + '    ' * level + ')'


class Value:
    def __init__(self, value):
        self.value = value

    def to_str(self, level):
        return self.value.body


class Array:
    def __init__(self, values):
        self.values = values

    def to_str(self, level):
        result = '[\n'
        for value in self.values:
            result += '    ' * (level + 1) + value.to_str(level + 1) + '\n'
        return result + '    ' * level + ']'


class Dictionary:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def to_str(self, level):
        result = '{\n'
        for key, value in self.dictionary.items():
            result += '    ' * (level + 1) + f'{key.body}: {value.to_str(level+1)}\n'
        return result[:-1] + '    ' * level + '\n}'