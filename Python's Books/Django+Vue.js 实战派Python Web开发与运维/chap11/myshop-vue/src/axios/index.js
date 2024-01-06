import axios from 'axios';//引入axios
//import store from '@/vuex';
 //环境的切换 开发环境(development)使用的是测试接口  和   生产环境(production)使用的是上线接口
if(process.env.NODE_ENV=='dev'){
    //设置默认路径
     //axios.defaults.baseURL='http://localhost:8000/'
 }
if(process.env.NODE_ENV=='prod'){
     //axios.defaults.baseURL='https://192.168.77.103:85/'
}
axios.defaults.timeout=5000;//加载不出来5秒之后就是加载失败
//定义一个请求的拦截器。
axios.interceptors.request.use(
    config=>{
         //增加jwt
        //需要验证的地方比如部分页面，或者post提交增加
        //if (store.getters.username){
            var jwt=localStorage.getItem('token');
            config.headers.Authorization='JWT  '+jwt;
        //}
            
        return config;
    },
    err=>{
        return Promise.reject(err);
    }
);
// axios.interceptors.response.use(
//      response=>{
//        return response;
//      },
//      error=>{
//          if(error.response.status){

//          }
//          console.log(error)
//          return Promise.reject(error.response.data)
//      }
//  )
 
 // 使用promise返回axios请求的结果
export function get(url, params) {
         return new Promise((resolve, reject) => {
             axios.get(url, {
                params:params
             }).then(res => {
                 resolve(res)
             }).catch(err => {
                reject(err)
             })
         })
     };
     
     export function post(url,params){
         return new Promise((resolve,reject)=>{
             axios.post(url,params).then(res=>{
                 resolve(res.data)
             }).catch(err=>{
                 reject(err.data)
             })
     
         })
     }  