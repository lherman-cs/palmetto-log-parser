import unittest
from parser import Parser
from os.path import join, expanduser
from os import walk

HOME = expanduser('~')
DATASET_DIR = join(HOME, 'Documents', 'hpc', 'ecc-gpu-reports')


class ParserTestCase(unittest.TestCase):
    def numkeys_without_parsing(self, text):
        keys = 0
        for line in text.split('\n'):
            line = line.strip()
            if line == '' or line.startswith('='):
                continue
            keys += 1
        return keys

    def numkeys_with_parsing(self, text):
        p = Parser(text)
        m = p.parse()
        stack = [m]
        keys = 0

        while len(stack) > 0:
            m = stack.pop()
            if not isinstance(m, dict):
                continue

            stack.extend(m.values())
            keys += len(m.keys())
        return keys

    def test_numkeys(self):
        for (dirpath, _, filenames) in walk(DATASET_DIR):
            if len(filenames) == 0:
                continue

            for filename in filenames:
                filepath = join(dirpath, filename)
                print("Testing {}".format(filepath))
                with open(filepath) as i:
                    text = i.read()

                wo_parsing = self.numkeys_without_parsing(text)
                w_parsing = self.numkeys_with_parsing(text)
                self.assertEqual(wo_parsing, w_parsing)


if __name__ == '__main__':
    unittest.main()
