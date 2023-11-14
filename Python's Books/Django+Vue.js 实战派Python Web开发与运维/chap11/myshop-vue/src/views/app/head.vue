<template>
  <div id="header" class="new_header">
    <div class="hd_bar">
      <div class="bd_bar_bd cle">
        <ul class="welcome">
          <li>
            <a id="favorite_wb" href="#" rel="nofollow">我的特产小店</a>
          </li>
          <li id="ECS_MEMBERZONE" v-if="userinfo">
            <router-link :to="'/profile'">{{ userinfo.username }}</router-link>
            <a @click="logout">退出</a>
          </li>
          <li id="ECS_MEMBERZONE" v-else>
            <router-link :to="'/login'">请登录</router-link>
            <s>|</s>
            <router-link :to="'/reg'">免费注册</router-link>
          </li>
        </ul>
        <ul id="userinfo-bar">
          <li class="more-menu">
            <router-link :to="'/profile'">会员中心</router-link>
            <router-link :to="'/myorder'">我的订单</router-link>
            <router-link :to="'/address'">修改收货地址</router-link>
          </li>
        </ul>
      </div>
    </div>

    <div class="hd_main cle">
      <div class="logo">
        <a href="./" class="lizi_logo">
          <img src="../../static/images/logo.jpg" alt="" />
        </a>
      </div>
      <div class="search_box">
        <form
          action="search.php"
          method="get"
          id="searchForm"
          name="searchForm"
          onSubmit="return checkSearchForm()"
        >
          <input
            class="sea_input"
            type="text"
            name="keywords"
            id="keyword"
            value=""
            autocomplete="off"
          />
          <input type="hidden" value="k1" name="dataBi" />
          <button type="submit" class="sea_submit">搜索</button>
        </form>
      </div>
    </div>
    <div class="hd_nav">
      <div class="hd_nav_bd cle">
        <div          class="main_nav main_nav_hover"
          id="main_nav"
          @mouseover="overAllmenu"
          @mouseout="outAllmenu"
        >
          <div class="main_nav_link">
            <a class="#">全部商品分类</a> <i class="iconfont"></i>
          </div>
          <div class="main_cata" id="J_mainCata" v-show="showmenu">
            <ul>
              <li
                :class="current === index ? 'current' : ''"
                v-for="(item, index) in allMenu"
                :key="index"
                @mouseover="oversubmenu(index)"
                @mouseout="outsubmenu(index)"
              >
                <h3
                  style="
                    background: url(../../static/images/1449088957941770398.png)
                      20px center no-repeat;
                  "
                >
                  <router-link :to="'/list/' + item.id">{{
                    item.name
                  }}</router-link>
                </h3>
                <div
                  class="J_subCata"
                  id="J_subCata"
                  v-show="showsubmenu === index"
                  style="left: 213px; top: 0px"
                >
                  <div class="J_subView" style="display: block">
                    <div v-for="iteminfo in item.sub_cat">
                      <dl>
                        <dt>
                          <router-link :to="'/list/' + iteminfo.id">{{
                            iteminfo.name
                          }}</router-link>
                        </dt>
                      </dl>
                      <div class="clear"></div>
                    </div>
                  </div>
                </div>
              </li>
            </ul>
          </div>
        </div>
        <ul class="sub_nav cle" id="sub_nav">
          <li>
            <router-link class="current" :to="'/index'">首页</router-link>
          </li>
          <template v-for="item in allMenu">
            <li v-if="item.is_nav">
              <router-link :to="'/list/' + item.id">{{
                item.name
              }}</router-link>
            </li>
          </template>
        </ul>
        <div
          class="hd_cart"
          :class="showCart ? 'hd_cart_hover' : ''"
          id="ECS_CARTINFO"
          @mouseover="overCart"
          @mouseout="outCart"
        >
          <router-link class="tit" :to="'/checkout'">
            <b class="iconfont">Ɲ</b>去购物车结算<span
              ><i class="iconfont"></i></span
            >
            <em class="num" id="hd_cartnum" style="visibility: visible">{{
              totalNum
            }}</em>
          </router-link>
          <div class="list" v-show="showCart">
            <div class="data">
              <dl v-for="item in cart_lists">
                <dt>
                  <a target="_blank" href="#"
                    ><img :src="item.goods.main_img"
                  /></a>
                </dt>
                <dd>
                  <h4>
                    <router-link
                      target="_blank"
                      :to="'detail' + item.goods.id"
                      >{{ item.goods.name }}</router-link
                    >
                  </h4>
                  <p>
                    <span class="red">{{ item.goods.price }}</span
                    >&nbsp;<i>X</i>&nbsp;{{ item.goods_num }}
                  </p>
                  <a
                    class="iconfont del"
                    title="删除"
                    href="javascript:deleteCartGoods(278);"
                    >Ť</a
                  >
                </dd>
              </dl>

              <div class="count">
                共<span class="red" id="hd_cart_count">{{ totalNum }}</span
                >件商品哦~
                <p>
                  总价:<span class="red"
                    ><em id="hd_cart_total">{{ totalPrice }}</em></span
                  >
                  <router-link class="btn" :to="'/checkout'"
                    >去结算</router-link
                  >
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="search_result"></div>
  </div>
</template>
<script>
import { mapGetters } from "vuex";
import { getGoodsCategory } from "@/api/goods";
export default {
  data() {
    return {
      showmenu: false,
      allMenu: [],
      showsubmenu: -1, //菜单显示控制
      first: false,
      current: false,
      showCart: false,
    };
  },
  methods: {
    overAllmenu() {
      this.showmenu = true;
    },
    outAllmenu() {
      this.showmenu = false;
    },
    oversubmenu(index) {
      this.current = index;
      this.showsubmenu = index;
    },
    outsubmenu() {
      this.current = false;
      this.showsubmenu = -1;
    },
    overCart() {
      this.showCart = true;
    },
    outCart() {
      this.showCart = false;
    },
    getAllMenu() {
      getGoodsCategory().then((response) => {
        //console.log(response.data.results);
        this.allMenu = response.data.data;
      });
    },
    logout() {
      this.$store.dispatch("delUser");
    },
  },
  computed: {
    ...mapGetters({
      userinfo: "userinfo",
      cart_lists: "cart_lists",
      totalNum: "totalNum",
      totalPrice: "totalPrice",
    }),
  },
  created() {
    this.getAllMenu();
    //console.log(this.cart_lists)
  },
};
</script>
