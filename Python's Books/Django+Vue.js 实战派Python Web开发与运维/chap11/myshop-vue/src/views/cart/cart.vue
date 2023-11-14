<template>
  <div>
    <link href="../../static/css/style.css" rel="stylesheet" type="text/css" />
    <link href="../../static/css/cart.css" rel="stylesheet" type="text/css" />
    <myhead></myhead>
    <div id="main">
      <div class="top-next cle">
        <div class="fr">
          <a href="./" class="graybtn">继续购物</a>
          <a href="flow.php?step=checkout" class="btn" id="checkout-top"
            >&nbsp;去结算&nbsp;</a
          >
        </div>
      </div>
      <div class="cart-box" id="cart-box">
        <div class="hd">
          <span class="no2" id="itemsnum-top">2件商品</span>
          <span class="no4">单价</span> <span>数量</span> <span>小计</span>
        </div>
        <div class="goods-list">
          <ul>
            <li
              class="cle hover"
              v-for="(item, index) in cart_lists"
              style="border-bottom-style: none"
            >
              <div class="pic">
                <a href="goods.php?id=2" target="_blank">
                  <img :alt="item.goods.name" :src="item.goods.main_img" />
                </a>
              </div>
              <div class="name">
                <router-link :to="'/detail' + item.goods.id"
                  ><span style="color: #ff0000">{{
                    item.goods.name
                  }}</span></router-link
                >
                <p></p>
              </div>

              <div class="price-xj">
                <p>
                  <em>￥{{ item.goods.price }}元</em>
                </p>
              </div>
              <div class="nums">
                <span
                  class="minus"
                  title="减少1个数量"
                  @click="reduce(item.goods.id, item.goods_num)"
                  >-</span
                >
                <input
                  type="text"
                  id="goods_number_270"
                  v-model="item.goods_num"
                />
                <span
                  class="add"
                  title="增加1个数量"
                  @click="add(item.goods.id, item.goods_num)"
                  >+</span
                >
              </div>
              <div class="price-xj">
                <span></span>
                <em id="total_items_270"
                  >￥{{ item.goods.price * item.goods_num }}元</em
                >
              </div>
              <div class="del"><a class="btn-del">删除</a></div>
            </li>
          </ul>
        </div>

        <div class="fd cle">
          <div class="fl">
            <p class="no1"><a id="del-all" href="#">清空购物车</a></p>
            <p><a class="graybtn" href="#">继续购物</a></p>
          </div>
          <div class="fr" id="price-total">
            <p>
              <span id="selectedCount">{{ cart_lists.length }}</span
              >件商品，总价：<span class="red"
                ><strong id="totalSkuPrice"
                  >￥{{ this.allprice }}元</strong
                ></span
              >
            </p>
            <p>
              <router-link :to="'checkout'" class="btn">去结算</router-link>
            </p>
          </div>
        </div>
      </div>
    </div>
    <myfooter></myfooter>
  </div>
</template>
<script>
import myhead from "@/views/app/head";
import myfooter from "@/views/app/footer";
import { getCart, updateCart } from "@/api/order";
export default {
  data() {
    return {
      cart_lists: {},
      buynum: 1,
      modelshow: false,
      allprice: 0,
    };
  },
  components: {
    myhead,
    myfooter,
  },
  methods: {
    getCart() {
      getCart().then((response) => {
        console.log("2dsfds" + response.data);
        this.cart_lists = response.data.data;
        //console.log("cart"+JSON.stringify(this.cart_lists[0]));
        var totalprice = 0;
        for (var i = 0; i < this.cart_lists.length; i++) {
          var item = this.cart_lists[i];
          console.log("item" + item);
          totalprice += item.goods_num * item.goods.price;
        }
        console.log("okoko" + this.cart_lists[0]);
        //console.log("okoko"+this.cart_lists[0].goods_num);
        console.log("okoko" + this.cart_lists[0].goods.price);
        this.allprice = totalprice;
      });
    },
    add(id, nums) {
      updateCart(id, { goods_num: nums + 1 }).then((response) => {
        console.log(response.data);
        this.getCart();
        //这里对购物车进行vuex处理
        this.$store.dispatch("saveCart");
      });
    },
    reduce(id, nums) {
      updateCart(id, { goods_num: nums - 1 }).then((response) => {
        console.log(response.data);
        this.getCart();
        //这里对购物车进行vuex处理
        this.$store.dispatch("saveCart");
      });
    },
  },
  created() {
    this.getCart();
  },
};
</script>

<style scoped>
@import "../../static/css/style.css";
@import "../../static/css/cart.css";
</style>
