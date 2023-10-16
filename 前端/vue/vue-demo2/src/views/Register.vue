<template>
    <h1>注册页面</h1>
    <button @click="send">点击发送请求</button>
</template>
<script>

import httptool from '@/http';

export default {
    name: 'Register',
    components: {

    },
    methods: {
        // send() {
        //     console.log('开始发送请求')
        //     httptool.get({
        //         url:'weather_mini', 
        //         config: {
        //             params: {
        //                 city:'潍坊'
        //             },
        //             headers:{
        //                 "company":"vue company"
        //             }
        //         }
        //     }).then(response=>{
        //         console.log(response);
        //         console.log(response.data);
        //     }).catch(error=>{
                
        //     });
        // }
        send(){
            httptool.get('http://httpbin.org/get/').then(response=>{
                console.log(response.data);
            })
        }
    }
}
</script>

<style></style>