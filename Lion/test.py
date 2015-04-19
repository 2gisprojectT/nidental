from unittest import TestCase
from Example import Lion
import unittest

class lionTest(TestCase):

    def testInitLion(self):
        # 0 - сытый, 1 - голодный
        # 0 - съесть, 1 - спать, 2 - бежать, 3 - смотреть
        # "antelope": 0, "hunter": 1, "tree": 2
        testTable = [[[1, 1], [2, 1], [3, 1]], [[0, 0], [2, 1], [1, 1]]]
        myLionTest = Lion(testTable,1)#голодный
        self.assertEqual(myLionTest.getCondition(),1,'Wrong condition!')
        self.assertEqual(myLionTest.getAction(),-1,'Wrong default action!')
        self.assertEqual(myLionTest.getTable(),testTable,'Wrong table!')

    def testEmptyInputTable(self):
         testTable={}
         self.assertRaises(Exception,Lion,testTable,0)

    def testChangeConditionAndAction(self):
        testTable = [[[1, 1], [2, 1], [3, 1]], [[0, 0], [2, 1], [1, 1]]]
        myLionTest = Lion(testTable,1)#голодный
        myLionTest.whoMet(0)#встретил антилопу
        self.assertEqual(myLionTest.getCondition(),0,'Wrong condition!')
        self.assertEqual(myLionTest.getAction(),0,'Wrong action!')

