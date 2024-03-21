import requests
import pytest
host = "http://localhost:8000"
class IndexTestCase():

    def testIndexCategoryList(self):
        """
        首页分类列表
        """
        url = host + "/goods/goodscategory"
        response = requests.get(url)
        assert response.status_code==200, "分类接口状态正常"
        assert len(response.content) > 0, "分类列表不为空"
        cates = response.json().get('results')
        for cate in cates:
            assert len(cate['name']) > 0, "分类 id=" + str(cate['id'])

    def testIndexGoods(self):
        """
        首页商品
        """
        url = host + "/goods/goods"
        response = requests.get(url)
        assert response.status_code==200, "商品接口状态正常"
        assert len(response.content) > 0, "商品列表不为空"
        cates = response.json().get('results')
        for cate in cates:
            assert len(cate['name']) > 0, "商品 id=" + str(cate['id'])

if __name__ == '__main__':
    pytest.main(["-s","-v","pytest_test/test_api.py"])