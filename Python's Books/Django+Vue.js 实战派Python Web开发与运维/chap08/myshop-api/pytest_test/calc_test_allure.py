import pytest
import allure
import os
from calc import Calc

class TestCalc():#类名需要以test开头，否则找不到
    @allure.feature("数字加减测试")#功能名称
    def setup_class(self):
        print("每个类之前执行一次"+'\n')
    
    def teardown_class(self):
        print("每个类之后执行一次"+'\n')
    
    def setup_method(self):
        print("在每个方法之前执行")
    
    def teardown_method(self):
        print("在每个方法之后执行")
    
    @allure.story("数字相加")#子功能名称
    def test_add(self):
        c=Calc()
        result=c.add(2,3)
        assert result==5

    @allure.story("数字相减")
    def test_sub(self):
        c=Calc()
        result=c.sub(2,3)
        assert result==-2



if __name__=='__main__':
    pytest.main(["--alluredir","pytest_test/report","pytest_test/calc_test.py"])
    #执行allure命令
    cmd="allure generate"+ r"F:\python_project\myshop-test\pytest_test\report"+ "-o"+ r"F:\python_project\myshop-test\pytest_test\report\html"+ " --clean"
    os.system(cmd)
