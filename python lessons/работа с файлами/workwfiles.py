import os.path
import unittest


def vernutvse(path):
    s1 = []
    s2 = []
    for root, dirs, files in os.walk(str(path)):
        s1.append(dirs)
        s2.append(files)
    return s1, s2


def udalitnevse(path):
    if len(vernutvse(path)[1]) > 0:
        if len(vernutvse(path)[0]) > 1:
            return None
        for i in vernutvse(path)[1][0]:
            os.remove(path + '/' + str(i))
        os.rmdir(path)
    return None


class TestMethods(unittest.TestCase):

    def initialize(self):
        if not os.path.isdir('test_dir'):
            os.makedirs('test_dir')
        if not os.path.isdir('test_dir/test_dir2'):
            os.makedirs('test_dir/test_dir2')
        open('test_dir/test', 'w')

    def test_vozvrat(self):
        self.initialize()
        self.assertTrue(len(vernutvse('test_dir')[1]) == 2)

    def test_del(self):
        self.initialize()
        self.assertTrue(len(vernutvse('test_dir')[1]) == 2)
        self.assertTrue(len(vernutvse('test_dir')[0]) == 2)
        self.assertTrue(udalitnevse('test_dir') is None)
        udalitnevse('test_dir/test_dir2')
        udalitnevse('test_dir')
        self.assertTrue(len(vernutvse('test_dir')[1]) == 0)
        self.assertTrue(len(vernutvse('test_dir')[0]) == 0)


if __name__ == '__main__':
    unittest.main()