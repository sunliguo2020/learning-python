<template>
<!--  <p>{{ Chengpin.title }}</p>-->
  <div>
    <ul v-for="item of chengpin_list">
      <li>{{item.title}}</li>
      <li>{{item.content}}</li>
      <li><img v-for="img of item.img" :src="img"></li>
    </ul>
  </div>
</template>
<script>
import axios from "axios"
import querystring from "querystring"

export default {
  data() {
    return {
      Chengpin: {},
      chengpin_list :[]
    }
  },
  mounted() {
    //get 请求
    axios({
      method: "get",
      url: 'http://iwenwiki.com/api/blueberrypai/getChengpinDetails.php'
    }).then(res => {
      console.log(res.data)
      this.Chengpin = res.data.chengpinDetails[0];
      this.chengpin_list = res.data.chengpinDetails;
    }),
        //post
        axios({
          method: 'post',
          url: 'http://iwenwiki.com/api/blueberrypai/login.php',
          data: querystring.stringify({
            user_id: 'iwen@qq.com',
            password: "iwen123",
            verification_code: "crfvw"
          }),
        }).then(res => {
          console.log(res.data)
        })
  }
}
</script>