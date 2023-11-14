import request from '@/utils/request'
// 封装请求的方式
export function login(data) {
  return request({
    url: '/login/',
    method: 'post',
    data
  })
}

export function reg(data) {
  return request({
    url: '/users/',
    method: 'post',
    data
  })
}

export function getUsersByID() {
  return request({
    url: '/users/1/',
    method: 'get',
  })
}

export function updateUsers(data) {
  return request({
    url: '/users/1/',
    method: 'patch',
    data
  })
}

export function updatePwd(data) {
  return request({
    url: '/users/1/',
    method: 'patch',
    data
  })
}
