<template>
  <div>
    <myhead></myhead>
    <link href="../../static/css/style.css" rel="stylesheet" type="text/css" />
    <div class="cle cart_main">
      <div class="flowBox_cart">
        <h6><span style="padding-left: 0px">确认订单信息页面</span></h6>
        <div class="flowBox_in">
          <div class="flowBox">
            <h6>
              <span>商品列表</span><a href="#" class="f16">返回修改购物车</a>
            </h6>
            <table
              width="99%"
              align="center"
              border="0"
              cellpadding="5"
              cellspacing="1"
              bgcolor="#dddddd"
            >
              <tbody>
                <tr style="text-align: center">
                  <th bgcolor="#f5f5f5">商品名称</th>
                  <th bgcolor="#f5f5f5">原价</th>
                  <th bgcolor="#f5f5f5">本店价</th>
                  <th bgcolor="#f5f5f5">购买数量</th>
                  <th bgcolor="#f5f5f5">小计</th>
                </tr>
                <tr align="center" v-for="item in cart_lists">
                  <td bgcolor="#ffffff">
                    <router-link
                      :to="'detail/' + item.goods.id"
                      target="_blank"
                      class="f6"
                      >{{ item.goods.name }}</router-link
                    >
                  </td>
                  <td bgcolor="#ffffff">￥{{ item.goods.market_price }}元</td>
                  <td bgcolor="#ffffff">￥{{ item.goods.price }}元</td>
                  <td bgcolor="#ffffff">{{ item.goods_num }}</td>
                  <td bgcolor="#ffffff">
                    ￥{{ item.goods.price * item.goods_num }}元
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="blank"></div>
          <div class="flowBox">
            <h6>
              <span>收货人信息</span
              ><a href="#" class="f16">返回修改收货地址</a>
            </h6>
            <table
              width="99%"
              align="center"
              border="0"
              cellpadding="5"
              cellspacing="1"
              bgcolor="#dddddd"
            >
              <tbody>
                <tr>
                  <td bgcolor="#f5f5f5">收货人姓名:</td>
                  <td bgcolor="#ffffff">{{ contact_name }}</td>
                  <td bgcolor="#f5f5f5">详细地址:</td>
                  <td bgcolor="#ffffff">{{ address }}</td>
                </tr>
                <tr>
                  <td bgcolor="#f5f5f5">手机:</td>
                  <td bgcolor="#ffffff">{{ contact_mobile }}</td>
                  <td bgcolor="#f5f5f5">备用电话:</td>
                  <td bgcolor="#ffffff"></td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="blank"></div>
          <div class="flowBox">
            <h6><span>配送方式</span></h6>
            <table
              width="99%"
              align="center"
              border="0"
              cellpadding="5"
              cellspacing="1"
              bgcolor="#dddddd"
              id="shippingTable"
            >
              <tbody>
                <tr style="text-align: center">
                  <th bgcolor="#f5f5f5" width="5%">&nbsp;</th>
                  <th bgcolor="#f5f5f5" width="25%">名称</th>
                </tr>
                <tr>
                  <td bgcolor="#ffffff" align="center">
                    <input
                      name="shipping"
                      type="radio"
                      value="3"
                      supportcod="0"
                      insure="0"
                      checked
                    />
                  </td>
                  <td bgcolor="#ffffff"><strong>全场包邮</strong></td>
                </tr>
                <tr>
                  <td bgcolor="#ffffff" align="center">
                    <input
                      name="shipping"
                      type="radio"
                      value="3"
                      supportcod="0"
                      insure="0"
                      disabled
                    />
                  </td>
                  <td bgcolor="#ffffff"><strong>顺丰速运</strong></td>
                </tr>
                <tr>
                  <td bgcolor="#ffffff" align="center">
                    <input
                      name="shipping"
                      type="radio"
                      value="4"
                      supportcod="1"
                      insure="0"
                      disabled
                    />
                  </td>
                  <td bgcolor="#ffffff"><strong>圆通速递</strong></td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="blank"></div>

          <div class="flowBox">
            <h6><span>支付方式</span></h6>
            <table
              width="99%"
              align="center"
              border="0"
              cellpadding="5"
              cellspacing="1"
              bgcolor="#dddddd"
              id="paymentTable"
            >
              <tbody>
                <tr>
                  <th width="5%" bgcolor="#ffff99">&nbsp;</th>
                  <th width="20%" bgcolor="#ffff99">名称</th>
                </tr>

                <tr>
                  <td bgcolor="#ffffff">
                    <input
                      type="radio"
                      name="payment"
                      value="1"
                      id="pay_check_value_1"
                      checked=""
                      iscod="0"
                    />
                  </td>
                  <td bgcolor="#ffffff">
                    <label class="pay_label" for="pay_check_value_1"
                      >支付宝</label
                    >
                  </td>
                </tr>

                <tr>
                  <td bgcolor="#ffffff">
                    <input
                      type="radio"
                      name="payment"
                      value="2"
                      id="pay_check_value_2"
                      iscod="0"
                    />
                  </td>
                  <td bgcolor="#ffffff">
                    <label class="pay_label" for="pay_check_value_2"
                      >微信支付</label
                    >
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="blank"></div>

          <div class="flowBox">
            <h6><span>其它信息</span></h6>
            <table
              width="99%"
              align="center"
              border="0"
              cellpadding="5"
              cellspacing="1"
              bgcolor="#dddddd"
            >
              <tbody>
                <tr>
                  <td valign="top" bgcolor="#f5f5f5">
                    <strong>订单附言:</strong>
                  </td>
                  <td bgcolor="#ffffff">
                    <textarea
                      name="postscript"
                      cols="80"
                      rows="3"
                      id="postscript"
                      v-model="memo"
                      style="border: 1px solid #ccc"
                    ></textarea>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="blank"></div>
          <div class="flowBox">
            <h6><span>费用总计</span></h6>
            <div id="ECS_ORDERTOTAL">
              <table
                width="99%"
                align="center"
                border="0"
                cellpadding="5"
                cellspacing="1"
                bgcolor="#dddddd"
              >
                <tbody>
                  <tr>
                    <td align="right" bgcolor="#f5f5f5"></td>
                  </tr>
                  <tr>
                    <td align="right" bgcolor="#f5f5f5" style="color: #666666">
                      商品总价: <font class="f4_b">￥{{ totalPrice }}元</font>
                    </td>
                  </tr>
                  <tr>
                    <td align="right" bgcolor="#ffffff">
                      应付款金额: <font class="f4_b">￥{{ totalPrice }}元</font>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div align="center" style="margin: 8px auto">
              <img
                src="../../static/images/bnt_subOrder.jpg"
                @click="submit_order"
              />
            </div>
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
import { mapGetters } from "vuex";
import { addOrder } from "@/api/order";
import { getAddress } from "@/api/basic";
export default {
  data() {
    return {
      address_lists: {},
      address: "2222",
      contact_name: "张三",
      contact_mobile: "111111",
      memo: "",
      pay_method: "1",
    };
  },
  methods: {
    submit_order() {
      addOrder({
        contact_name: this.contact_name,
        contact_mobile: this.contact_mobile,
        memo: this.memo,
        address: this.address,
        pay_method: this.pay_method,
      })
        .then((response) => {
          console.log(response.data);
          if (response.data.code == "200") {
            alert(response.data.msg);
            //这里对购物车进行vuex处理
            this.$store.dispatch("saveCart");
            this.$router.push({ name: "/myorder" });
          } else {
            alert(response.data.msg);
            return;
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    getAddressData() {
      getAddress()
        .then((response) => {
          console.log(response.data);
          if (response.status === 200) {
            this.address_lists = response.data.data;
            this.address =
              this.address_lists[0].province +
              this.address_lists[0].city +
              this.address_lists[0].district +
              this.address_lists[0].address;
            this.contact_name = this.address_lists[0].contact_name;
            this.contact_mobile = this.address_lists[0].contact_mobile;
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
  components: {
    myhead,
    myfooter,
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
    this.getAddressData();
  },
};
</script>
<style scoped>
@import "../../static/css/cart4.css";
</style>
