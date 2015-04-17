from unittest import TestCase
from Example import Lion
import unittest

class lionTest(TestCase):

    def test_init(self):
        # 0 - сытый, 1 - голодный
        # 0 - съесть, 1 - спать, 2 - бежать, 3 - смотреть
        # "antelope": 0, "hunter": 1, "tree": 2
        myLionTest = Lion(1)#голодный
        self.assertEqual(myLionTest.getCondition(),1,'Wrong condition!')
        myLionTest = Lion(0)#сытый
        self.assertEqual(myLionTest.getCondition(),0,'Wrong condition!')
        myLionTest.whoMet(0)#сытый встретил антилопу
        self.assertEqual(myLionTest.getCondition(),1,'Wrong condition!')
        self.assertEqual(myLionTest.getAction(),1,'Wrong action!')
        myLionTest.whoMet(0)#голодный встретил антилопу
        self.assertEqual(myLionTest.getCondition(),0,'Wrong condition!')
        self.assertEqual(myLionTest.getAction(),0,'Wrong action!')
        myLionTest.whoMet(1)#сытый встретил охотника
        self.assertEqual(myLionTest.getCondition(),1,'Wrong condition!')
        self.assertEqual(myLionTest.getAction(),2,'Wrong action!')
        myLionTest.whoMet(1)#голодный встретил охотника
        self.assertEqual(myLionTest.getCondition(),1,'Wrong condition!')
        self.assertEqual(myLionTest.getAction(),2,'Wrong action!')
        myLionTest = Lion(0)
        myLionTest.whoMet(2)#сытый встретил дерево
        self.assertEqual(myLionTest.getCondition(),1,'Wrong condition!')
        self.assertEqual(myLionTest.getAction(),3,'Wrong action!')
        myLionTest.whoMet(2)#голодный встретил дерево
        self.assertEqual(myLionTest.getCondition(),1,'Wrong condition!')
        self.assertEqual(myLionTest.getAction(),1,'Wrong action!')