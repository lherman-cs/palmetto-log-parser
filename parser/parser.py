from .specs import tok_regex
import re


class Parser:
    def __init__(self, text):
        self.__it = re.finditer(tok_regex, text)

    def __get_value(self):
        mo = next(self.__it)
        kind = mo.lastgroup
        value = mo.group(kind)
        if kind == 'SKIP':
            mo = next(self.__it)
            kind = mo.lastgroup
            value = mo.group(kind)

        # print(kind, value)
        if kind == 'INT':
            return int(value)
        if kind == 'FLOAT':
            return float(value)
        if kind == 'BOOLEAN':
            if value == 'Enabled' or value == 'Yes':
                return True
            return False
        if kind == 'DATE':
            # TODO! Parse date to date object
            return value
        if kind == 'NA':
            return None

        raise RuntimeError("Unknown Data Type, {}".format(value))

    def parse(self):
        values = {}
        for mo in self.__it:
            kind = mo.lastgroup
            value = mo.group(kind)
            # print(kind, value)
            if kind == 'COMMENT' or kind == 'SKIP':
                continue
            elif kind == 'UNKNOWN':
                raise RuntimeError("Unknown Token, {}".format(value))
            elif kind == 'KEY':
                values[value] = self.parse()
            elif kind == 'COLON':
                return self.__get_value()
            else:
                return RuntimeError("Uknown Error, {}".format(value))
        return values
