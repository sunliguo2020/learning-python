import unittest

from calc import Calc
from calc_testcase import TestCalcMethod

#创建测试套件
suit=unittest.TestSuite()
suit.addTest(unittest.TestLoader().loadTestsFromTestCase(TestCalcMethod))
