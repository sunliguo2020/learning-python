
import request from '@/utils/request'
// 封装请求的方式
export function addCart(data) {
  return request({
    url: '/cart/',
    method: 'post',
    data
  })
}

export function getCart(data) {
  return request({
    url: '/cart/',
    method: 'get',
    data
  })
}

export function updateCart(id,data) {
  return request({
    url: '/cart/'+id+'/',
    method: 'patch',
    data
  })
}

export function addOrder(data) {
  return request({
    url: '/order/',
    method: 'post',
    data
  })
}

export function getOrder(data) {
  return request({
    url: '/order/',
    method: 'get',
    data
  })
}


