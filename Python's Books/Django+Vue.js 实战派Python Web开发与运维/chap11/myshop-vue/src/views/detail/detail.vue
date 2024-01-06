<template>
  <div>
    <link href="../../static/css/style.css" rel="stylesheet" type="text/css">
    <link href="../../static/css/goods.css" rel="stylesheet" type="text/css">
    <myhead></myhead>
    <div id="wrapper">
      <div class="breadcrumbs cle">
        <div class="menus">您当前的位置：<a href="#">首页</a> <code>&gt;</code> <a href="#"></a> </div>
      </div>
      <div class="detail cle">

        <div class="detail_img" id="detail_img">
          <div class="pic_view"> 
        
            <img :alt="goods_lists.main_img" :src="goods_lists.main_img" style="opacity: 1;">
            
            </div>
          <div class="item-thumbs" id="item-thumbs">
            <a class="prev" href="javascript:void(0);"></a>
            <a class="next" href="javascript:void(0);"></a>
            <div class="bd">
              <ul class="cle">
                <li class="current"> 
                  <a> 
                <img :alt="goods_lists.main_img" :src=goods_lists.main_img> 
                </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <form method="post" name="ECS_FORMBUY" id="ECS_FORMBUY">
          <div class="item-info" id="item-info">
            <dl class="loaded">

              <dt class="product_name">
                <h1>{{goods_lists.name}}</h1>
                <p class="desc"> <span class="gray">{{goods_lists.goods_desc}}</span> </p>

                <div class="ewm">
                  <em></em>

                </div>
              </dt>

              <dd class="property">
                <ul>
                  <li> </li>

                  <li> <span class="lbl">市场价</span> <em class="cancel">￥{{goods_lists.market_price}}</em> </li>
                  <li>

                    <span class="lbl">销售价</span> <span class="unit"> <strong class="nala_price red" id="ECS_SHOPPRICE">￥{{goods_lists.price}}元</strong> </span>

                    <span><i class="iconfont">•</i><a href="javascript:;" id="membership" data-type="normal" class="membership"><i class="iconfont"></i></a></span>
                  </li>
                  <li><span class="lbl">销&nbsp;&nbsp;&nbsp;量</span><span>最近售出<em class="red">{{goods_lists.amount}}</em>件</span></li>
                </ul>
              </dd>

              <dd class="tobuy-box cle">
                <ul class="sku">
                  <li class="skunum_li cle">
                    <span class="lbl">数&nbsp;&nbsp;&nbsp;量</span>
                    <div class="skunum" id="skunum">
                      <span class="minus" title="减少1个数量" @click="reduce"><i class="iconfont">-</i></span>
                      <input id="number" name="number" type="text" min="1" v-model="buynum">
                      <span class="add" title="增加1个数量" @click="add"><i class="iconfont">+</i></span> <cite class="storage"> 件 </cite>
                    </div>
                    <div class="skunum" id="skunum">

                      <cite class="storage">(<font id="shows_number">{{goods_lists.stock_num}}件</font>)</cite>

                    </div>
                  </li>

                  <li class="add_cart_li">
                    <a @click="addcart" class="btn" id="buy_btn"><i class="iconfont">ŭ</i>加入购物车</a>
                  </li>
                </ul>
              </dd>
            </dl>
          </div>
        </form>

      </div>
      <div class="detail_bgcolor">
        <div class="z-detail-box cle">
          <div class="z-detail-left">

            <div class="tabs_bar_warp">
              <div class="tabs_bar" id="tabs_bar">
                <ul>
                  <li class="current_select"> <a class="spxqitem" rel="nofollow" href="javascript:void(0);">商品详情</a> </li>

                </ul>
              </div>
            </div>
            <div class="product_tabs">
              <div class="sectionbox z-box" id="spxqitem">
                <div class="spxq_main">
                  <div>
                    <div>
                      <table>
                        <tbody>
                          <tr>
                            <td width="20%" class="th"> 产品名称 :</td>
                            <td width="80%"> {{goods_lists.name}}</td>
                          </tr>

                        </tbody>
                      </table>
                    </div>
                    <p>&nbsp; </p>
                  </div>
                  <div class="spxq_dec">

                    <p v-html="goods_lists.goods_desc">

                    </p>
                  </div>
                </div>
              </div>
              <div class="z-box sectionbox">

                <div class="z-detail-com-box" id="ECS_COMMENT">
                  <div class="z-detail-point-box cle" style="border-width:0 0 1px 0">
                    <div class="z-detail-point-box-left">
                      <p><font>温馨提示：</font>购买前请与小二沟通！！！祝你购物愉快！！！</p>
                    </div>
                  </div>

                </div>

              </div>
            </div>
          </div>



        </div>
      </div>

      <div id="easyDialogBox" v-show="modelshow" style="margin: -118px 0px 0px -243px; padding: 0px; border: none; z-index: 10000; position: fixed; top: 50%; left: 50%; display: none;">
        <div class="add_ok" id="cart_show" style="display: block; margin: 0px;">
          <div class="tip">
            <i class="iconfont"></i>商品已成功加入购物车
          </div>
          <div class="go">
            <a @click="close" class="back">&lt;&lt;继续购物</a>
            <router-link class="btn" :to="'/cart'">去结算</router-link>
          </div>
        </div>
      </div>

    </div>
    <myfooter></myfooter>
  </div>

</template>
<script>
import myhead from '@/views/app/head';
import myfooter from '@/views/app/footer';
import { addCart } from "@/api/order"
import { getGoodsByID } from "@/api/goods"
export default{
  data(){
    return{
      goods_lists:{},
      buynum:1,
      modelshow:false

    };
  },
      components: {
      myhead,
      myfooter,
    },
  methods:{
      getDetail() {
        getGoodsByID(this.$route.params.id).then((response) => {
            //console.log(response.data);
            this.goods_lists = response.data
          })
      },
      add(){
        this.buynum=this.buynum+1;
      },
      reduce(){
        this.buynum=this.buynum-1
        if (this.buynum<=1){
          this.buynum=1
        }

      },
      addcart(){
        addCart({
          goods:this.goods_id,
          goods_num:this.buynum
         }).then((response) => {
            //console.log(response.data);
            if (response.status === 201) {
              this.modelshow=true;
              //这里对购物车进行vuex处理
              this.$store.dispatch('saveCart')
            }
          }).catch(function(error){
              console.log(error);
          })
      },
      close(){
        this.modelshow=false
      }
  },
  created(){
    this.goods_id=this.$route.params.id;
    this.getDetail();
  }
}

</script>
