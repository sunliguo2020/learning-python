import request from '@/utils/request'
// 封装请求的方式
//get方式请求商品分类
export function getGoodsCategory() {
  return request({
    url: '/goodscategory/',
    method: 'get',
  })
}
//获取某个商品分类
export function getGoodsCategoryByID(id) {
  return request({
    url: '/goodscategory/' + id + '/',
    method: 'get',
  })
}
//获取分类下的商品
export function getCategoryGoods() {
  return request({
    url: '/indexgoods/',
    method: 'get',
  })
}

//post方式获取商品。并传递参数
export function getGoods(data) {
  return request({
    url: '/goods/',
    method: 'get',
    params: data
  })
}
//获取某个商品
export function getGoodsByID(id) {
  return request({
    url: '/goods/' + id + '/',
    method: 'get',
  })
}
//获取商品轮播
export function getSlide() {
  return request({
    url: '/slide/',
    method: 'get',
  })
}
