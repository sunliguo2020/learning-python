from django.test import TestCase

from django.test import TestCase
from app8.models import Goods

class TestGoodModel(TestCase):
    def setUp(self):
        objid=Goods.objects.create(name='大枣',market_price=99,price=89,category_id=1)

    def test_goodmodel(self):
        #good=Goods.objects.get(name='大枣')
        good=Goods.objects.get(id=objid)
        self.assertEqual(good.price,89) 

