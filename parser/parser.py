from collections import defaultdict


class Parser:
    def __init__(self, text):
        self.__lines = text.split('\n')
        self.__it = 0

    def __get_level(self, line):
        stripped = line.lstrip(' ')
        return (len(line) - len(stripped)) // 4

    def __parse(self):
        def nested_dict(): return defaultdict(nested_dict)
        last_level = -1
        stack = []
        values = nested_dict()
        line = self.__lines[self.__it]

        while line != '':
            level = self.__get_level(line)
            if ' : ' in line:
                key, value = line.split(' : ')
                key, value = key.strip(), value.strip()
                values[key] = value
            else:
                while last_level > level:
                    values = stack.pop()
                    last_level -= 1

                key = line.strip()
                stack.append(values)
                values = values[key]

            last_level = level
            self.__it += 1
            if self.__it >= len(self.__lines):
                break
            line = self.__lines[self.__it]

        while len(stack) > 0:
            values = stack.pop()
        return values

    def __get_value(self):
        line = self.__lines[self.__it]
        value = line.split()[1]
        return value.strip()

    def parse(self):
        # Add offset
        values = {}
        while self.__it < len(self.__lines):
            line = self.__lines[self.__it]
            if line == '' or line[0] == '=':
                self.__it += 1
                continue
            values = {**values, **self.__parse()}
            self.__it += 1

        return values
