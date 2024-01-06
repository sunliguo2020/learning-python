import axios from 'axios'

//var URL = 'http://192.168.77.102:8002/'
var URL = 'http://localhost:8000/'
// 创建 axios 实例
const service = axios.create({
  baseURL: URL,
  timeout: 6000 // 请求超时时间
})

// request拦截器
service.interceptors.request.use(
  config => {
    const { url } = config
    //指定页面访问需要JWT认证。
    if (url == '/cart/' || url == '/order/' || url == '/checkout/' || url == '/myorder/' || url.indexOf('address/') > 0 || url == 'profile/' || url.indexOf('users/')>0 ) {
      var jwt = localStorage.getItem('token');
      config.headers.Authorization = 'JWT  ' + jwt;
    }
    return config
  },
  error => {
    Promise.reject(error)
  }
)
// response拦截器
service.interceptors.response.use(
  response => {
    return response
  },
  error => {
    console.log(error.response)
    //授权验证失败
    if (error.response.status === 401) {
      alert('请先登录！');
    }
    return Promise.reject(error.response.data)
  }
)

export default service
