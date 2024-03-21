import pytest
class Calc:
   
    def add(self,a,b):
        c=a+b
        return c
    
    def sub(self,a,b):
        c=a-b
        return c

class TestCalc():#类名需要以test开头，否则找不到

    def setup_class(self):
        print("每个类之前执行一次"+'\n')
    
    def teardown_class(self):
        print("每个类之后执行一次"+'\n')
    
    def setup_method(self):
        print("在每个方法之前执行")
    
    def teardown_method(self):
        print("在每个方法之后执行")
    
    #测试函数必须以test开头
    def test_add(self):
        c=Calc()
        result=c.add(2,3)
        assert result==5

    #测试函数必须以test开头
    def test_sub(self):
        c=Calc()
        result=c.sub(2,3)
        assert result==-1



if __name__=='__main__':
    pytest.main(["-s","-v","--html=pytest_test/report_1.html","pytest_test/calc_test.py"])