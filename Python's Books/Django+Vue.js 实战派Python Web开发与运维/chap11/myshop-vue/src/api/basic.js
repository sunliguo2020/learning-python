import request from '@/utils/request'
// 封装请求的方式
export function addAddress(data) {
  return request({
    url: '/address/',
    method: 'post',
    data
  })
}

export function getAddress(data) {
  return request({
    url: '/address/',
    method: 'get',
    data
  })
}

export function updateAddress(id, data) {
  return request({
    url: '/address/' + id + '/',
    method: 'patch',
    data
  })
}
