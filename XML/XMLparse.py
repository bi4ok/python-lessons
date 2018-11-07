import xml.etree.ElementTree as ETree
import unittest


xml12 = ETree.parse("demo.xml")
root1 = xml1.getroot()


print(len(root))
print(root[0].tag, root[0].text, len(root[0]))


for i in range(len(root[3])):
    print(root[3][i].attrib["name"], root[3][i].text)


for i in range(len(root[3])):
    print(root[3][i].get("name"), root[3][i].text)


for i in range(len(root[4])):
    print(root[4][i].tag, root[4][i].attrib, root[4][i].text)
for i in range(len(root[3])):
    print(root[3][i].tag, root[3][i].attrib, root[3][i].text)


def formtag(itemxml, tag):
    spisok = []
    for j in range(len(itemxml)):
        if len(itemxml[j]) > 0:
            for i in range(len(itemxml[j])):
                if root[j][i].tag == tag:
                    spisok.append(itemxml[j][i].text)
        else:
            if itemxml[j].tag == tag:
                spisok.append(itemxml[j].text)
    return spisok


def schettag(itemxml, tag):
    z = 0
    for j in range(len(itemxml)):
        if len(itemxml[j]) > 0:
            for i in range(len(itemxml[j])):
                if root[j][i].get(tag) is not None:
                    z += 1
        else:
            if root[j].get(tag) is not None:
                z += 1
    return z


print("_________________________________")


class TestMethods(unittest.TestCase):

    def initialize(self):
        xml1 = ETree.parse("demo.xml")
        root = xml1.getroot()

    def test_formtag(self):
        self.initialize()
        self.assertTrue(len(formtag(root, "sex")) == 1)
        self.assertTrue(formtag(root, "sex")[0] == "true")
        self.assertTrue(len(formtag(root, "pc_item")) == 4)

    def test_schet(self):
        self.initialize()
        self.assertTrue(schettag(root, "name") == 7)


if __name__ == '__main__':
    unittest.main()
