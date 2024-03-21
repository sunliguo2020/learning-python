import unittest
import HTMLTestRunnerNew
from calc import Calc
from calc_testcase import TestCalcMethod
import calc_testsuits as suit1

with open('report.html','wb')as fb:
    test_run = HTMLTestRunnerNew.HTMLTestRunner(stream=fb,
                              verbosity=2,
                              title = '测试报告',#定义测试报告的标题
                              description='...',
                              tester='yang')
    test_run.run(suit1.suit)