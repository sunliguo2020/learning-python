<template>
  <div class="slidebar">
    <ul class="slide_item">
      <li class="item">
        <div class="root_node">会员中心</div>
        <ul>
          <li>
            <router-link :to="'/profile'">用户信息</router-link>
          </li>
        </ul>
      </li>
      <li class="item">
        <div class="root_node">订单中心</div>
        <ul>
          <li>
            <router-link :to="'/myorder'">我的订单</router-link>
            <router-link :to="'/address'">收货地址</router-link>
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>
<style scoped>
.slidebar {
  float: left;
  width: 214px;
}

.slidebar .slide_item {
  zoom: 1;
  border: 1px solid #e7e7e7;
  border-bottom: 0;
  margin-bottom: 10px;
  background-color: #fff;
}

.slidebar .root_node {
  border-bottom: solid 1px #e7e7e7;
  padding: 14px 0 14px 14px;
  font-size: 14px;
}

.slidebar .root_node i {
  color: #ccc;
  margin-right: 8px;
  font-size: 12px;
}

.slidebar .item ul {
  border-bottom: solid 1px #e7e7e7;
}

.slidebar li {
  margin-bottom: 1px;
}

.slidebar li a {
  display: block;
  height: 20px;
  line-height: 20px;
  padding: 10px 0 10px 40px;
  color: #111;
}

.slidebar li a i {
  font-size: 18px;
  color: #999;
  margin-right: 6px;
}

.slidebar li a:hover,
.slidebar li a.on {
  background-color: #f1f1f1;
  color: #09c762;
  text-decoration: none;
}

.slidebar li a:hover i,
.slidebar li a.on i {
  color: #09c762;
  -webkit-animation: pop_ico 0.5s;
}

.slidebar .root_item {
  border-bottom: solid 1px #e7e7e7;
}

.slidebar .root_item a {
  font-size: 14px;
  padding: 14px 0 14px 15px;
}

.slidebar .root_item a i {
  font-size: 22px;
}
</style>
