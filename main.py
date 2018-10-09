from parser import Parser
from pprint import pprint

with open('node1665') as i:
    text = i.read()

p = Parser(text)
d = p.parse()
pprint(d)
