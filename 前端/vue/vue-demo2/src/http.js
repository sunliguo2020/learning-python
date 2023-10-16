import axios from "axios" //要导入安装的包，则直接填写包名即可。不需要使用路径。

//实例化 
const httptool = axios.create({
    baseURL: 'http://wthrcdn.etouch.cn/',           //请求的公共路径
    timeout: 1000,                              //最大请求超时事件
    headers: { 'X-Custom-Header': "foobar" }    //预定义请求头

});
export default httptool