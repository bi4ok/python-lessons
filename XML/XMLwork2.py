import xml.etree.ElementTree as ETree
import unittest

data = ETree.Element('data')

itm_name = ETree.SubElement(data, 'name')
itm_sex = ETree.SubElement(data, 'sex')
itm_age = ETree.SubElement(data, 'age')
itm_langs = ETree.SubElement(data, 'languages')
itm_pc = ETree.SubElement(data, 'pc')

itm_name.text = 'Petya'
itm_sex.text = 'true'
itm_age.text = '23'

itm_l1 = ETree.SubElement(itm_langs, 'language')
itm_l1.text = '9'
itm_l1.set('name', 'Python')
itm_l1 = ETree.SubElement(itm_langs, 'language')
itm_l1.text = '7'
itm_l1.set('name', 'Java')
itm_l1 = ETree.SubElement(itm_langs, 'language')
itm_l1.text = '8'
itm_l1.set('name', 'C#')

itm_pc1 = ETree.SubElement(itm_pc, 'pc_item')
itm_pc1.text = 'Linux'
itm_pc1.set('name', 'os')
itm_pc1 = ETree.SubElement(itm_pc, 'pc_item')
itm_pc1.text = '64'
itm_pc1.set('name', 'ram')
itm_pc1 = ETree.SubElement(itm_pc, 'pc_item')
itm_pc1.text = '5000'
itm_pc1.set('name', 'hard')

serialze = ETree.tostring(data, encoding='utf8', method='xml').decode()
fil = open("items.xml", "w")
fil.write(serialze)

#for lng in itm_langs.findall('language'):
 #   print(lng.attrib, lng.text)

item = data.find('pc')
#for subitem in item.findall('pc_item'):
 #   print(subitem.attrib, subitem.text)

#for item in data.iter():
 #   print(item.tag, item.text, item.attrib)


def poisknaglubine(d, tag):
    x = []
    for i in d.iter():
        if i.tag == tag:
            x.append(i)
    if len(x) == 0:
        return None
    else:
        return x


def bambi(d, tag):
    for i in d.iter():
        if i.find(tag) is not None:
            return i
    return None


def udalenie(d, tag):
    bambi(d, tag).clear()


class TestMethods(unittest.TestCase):

    def initialize(self):
        self.data = ETree.Element('data')

        self.itm_name = ETree.SubElement(self.data, 'name')
        self.itm_sex = ETree.SubElement(self.data, 'sex')
        self.itm_age = ETree.SubElement(self.data, 'age')
        self.itm_stats = ETree.SubElement(self.data, 'stats')
        self.itm_skills = ETree.SubElement(self.data, 'skills')

        self.itm_name.text = 'Max'
        self.itm_sex.text = 'M'
        self.itm_age.text = '25'

        self.itm_s1 = ETree.SubElement(self.itm_stats, 'hp')
        self.itm_s1.text = 100
        self.itm_s2 = ETree.SubElement(self.itm_skills, 'magic')
        self.itm_s2.text = 20
        self.itm_s2.set('name', 'fire ball')
        self.itm_s2 = ETree.SubElement(self.itm_skills, 'abilities')
        self.itm_s2.text = 11
        self.itm_s2.set('name', 'hard punch')

    def test_poiskglubina(self):
        self.initialize()
        self.assertTrue(len(poisknaglubine(self.data, 'magic')) == 1)
        self.data.clear()

    def test_bambi(self):
        self.initialize()
        self.assertTrue(bambi(self.data, 'hp').tag == 'stats')
        self.data.clear()

    def test_udalenie(self):
        self.initialize()
        self.assertTrue(len(poisknaglubine(self.data, 'magic')) == 1)
        udalenie(self.data, 'magic')
        self.assertTrue(poisknaglubine(self.data, 'magic') is None)
        self.data.clear()


if __name__ == '__main__':
    unittest.main()