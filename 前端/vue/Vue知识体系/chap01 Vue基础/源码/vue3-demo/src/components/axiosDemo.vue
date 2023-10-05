<template>
    <p>{{ chengpin.title }}</p>
</template>
<script>
import axios from "axios"
import querystring from "querystring"

export default {
    data() {
        return {
            chengpin: {}
        }
    },
    mounted() {
        //get 请求
        axios({
            method: "get",
            url: 'http://iwenwiki.com/api/blueberrypai/getChengpinDetails.php'
        }).then(res => {
            console.log(res.data)
            this.chengpin = res.data.chengpinDetails[0]
        }),
        //post
        axios({
            method:'post',
            url:'http://iwenwiki.com/api/blueberrypai/login.php',
            data:querystring.stringify({
                user_id:'iwen@qq.com',
                password:"iwen123",
                verification_code:"crfvw"
            }),
        }).then(res=>{
            console.log(res.data)
        })
    }
}
</script>