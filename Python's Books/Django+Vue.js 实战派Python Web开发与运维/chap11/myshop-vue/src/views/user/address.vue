
<template>
  <div>
    <myhead></myhead>
    <link href="../../static/css/style.css" rel="stylesheet" type="text/css" />

    <div id="wrapper" class="cle">
      <div class="here cle"><a href="#">首页</a> <code>&gt;</code> 用户中心</div>

      <div class="my_nala_main">

        <left></left>

        <div class="my_nala_centre ilizi_centre">
          <div class="ilizi cle">
            <div class="box">
              <div class="box_1">
                <div class="userCenterBox boxCenterList clearfix" style="_height:1%;">

                  <h5><span>收货人信息</span></h5>
                  <div class="blank"></div>

                  <table v-for="(item,index) in address_lists" width="100%" height="150px;" border="0" cellpadding="5" cellspacing="1" bgcolor="#dddddd">
                    <tbody>
                      <tr>
                        <td align="right" bgcolor="#ffffff">省份：</td>
                        <td align="left" bgcolor="#ffffff">
                          <input name="province" type="text" class="inputBg" v-model="item.province">
                          (必填)
                        </td>
                        <td align="right" bgcolor="#ffffff">城市：</td>
                        <td align="left" bgcolor="#ffffff"><input name="city" type="text" class="inputBg" v-model="item.city">(必填)</td>

                      </tr>
                      <tr>
                        <td align="right" bgcolor="#ffffff">区域：</td>
                        <td align="left" bgcolor="#ffffff">
                          <input name="district" type="text" class="inputBg" v-model="item.district">
                          (必填)
                        </td>
                        <td align="right" bgcolor="#ffffff">详细地址：</td>
                        <td align="left" bgcolor="#ffffff"><input name="address" style="width:250px;" type="text" class="inputBg" v-model="item.address">(必填)</td>

                      </tr>
                      <tr>
                        <td align="right" bgcolor="#ffffff">联系人：</td>
                        <td align="left" bgcolor="#ffffff">
                          <input name="contact_name" type="text" class="inputBg" v-model="item.contact_name">
                          (必填)
                        </td>
                        <td align="right" bgcolor="#ffffff">联系电话：</td>
                        <td align="left" bgcolor="#ffffff">
                          <input name="contact_mobile" type="text" class="inputBg" v-model="item.contact_mobile">
                          (必填)
                        </td>
                      </tr>
                      <tr>
                        <td align="right" bgcolor="#ffffff">是否默认地址：</td>
                        <td align="left" bgcolor="#ffffff">
                          <input name="is_default" type="checkbox" class="inputBg"  v-model='item.is_default'>
                          (必填)
                        </td>
                        <td align="right" bgcolor="#ffffff"></td>
                        <td align="left" bgcolor="#ffffff"></td>
                      </tr>
                      <tr>
                        <td align="right" bgcolor="#ffffff">&nbsp;</td>
                        <td colspan="3" align="center" bgcolor="#ffffff">
                          <input type="button" name="submit" class="bnt_blue_2" @click=update(item.id,index) value="确认修改">
                          <input type="button" name="submit" class="bnt_blue_2" @click=del(item.id,index) value="删除">
                        </td>
                      </tr>
                    </tbody>
                  </table>

<hr>

                  <table width="100%" height="150px;" border="0" cellpadding="5" cellspacing="1" bgcolor="#dddddd">
                    <tbody>
                      <tr>
                        <td align="right" bgcolor="#ffffff">省份：</td>
                        <td align="left" bgcolor="#ffffff">
                          <input name="province" type="text" class="inputBg" id="province" v-model="addinfo.province">
                          (必填)
                        </td>
                        <td align="right" bgcolor="#ffffff">城市：</td>
                        <td align="left" bgcolor="#ffffff"><input name="city" type="text" class="inputBg" id="city" v-model="addinfo.city">(必填)</td>

                      </tr>
                      <tr>
                        <td align="right" bgcolor="#ffffff">区域：</td>
                        <td align="left" bgcolor="#ffffff">
                          <input name="district" type="text" class="inputBg" id="district" v-model="addinfo.district">
                          (必填)
                        </td>
                        <td align="right" bgcolor="#ffffff">详细地址：</td>
                        <td align="left" bgcolor="#ffffff"><input name="address" type="text" style="width:250px;" class="inputBg" v-model="addinfo.address" id="address">(必填)</td>

                      </tr>
                      <tr>
                        <td align="right" bgcolor="#ffffff">联系人：</td>
                        <td align="left" bgcolor="#ffffff">
                          <input name="contact_name" type="text" class="inputBg" id="contact_name" v-model="addinfo.contact_name">
                          (必填)
                        </td>
                        <td align="right" bgcolor="#ffffff">联系电话：</td>
                        <td align="left" bgcolor="#ffffff">
                          <input name="contact_phone" type="text" class="inputBg" id="contact_phone" v-model="addinfo.contact_mobile">
                          (必填)
                        </td>
                      </tr>
                      <tr>
                        <td align="right" bgcolor="#ffffff">是否默认地址：</td>
                        <td align="left" bgcolor="#ffffff">
                          <input name="is_default" type="checkbox" class="inputBg" v-model='addinfo.is_default'>
                          (必填)
                        </td>
                        <td align="right" bgcolor="#ffffff"></td>
                        <td align="left" bgcolor="#ffffff"></td>
                      </tr>
                      <tr>
                        <td align="right" bgcolor="#ffffff">&nbsp;</td>
                        <td colspan="3" align="center" bgcolor="#ffffff">
                          <input type="button" name="submit" @click="addAddr" class="bnt_blue_2" value="新增收货地址">
                          <input type="hidden" name="act" value="act_edit_address">
                          <input name="address_id" type="hidden" value="">
                        </td>
                      </tr>
                    </tbody>
                  </table>

                </div>
              </div>
            </div>
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
  import left from '@/views/user/left';
  import { addAddress, getAddress, updateAddress } from '@/api/basic'
  export default {
    data() {
      return {
        address_lists: [],
        addinfo: {
          province: '',
          city: '',
          district: '',
          address: '',
          contact_name: '',
          contact_mobile: '',
          is_default: false
        }
      };
    },
    components: {
      myhead,
      myfooter,
      left
    },
    methods: {
      getData() {
        getAddress({}).then((response) => {
          console.log(response.data);
          if (response.status === 200) {
            this.address_lists = response.data.data;
          }
        }).catch(function (error) {
          console.log(error);
        })
      },
      update(id, i) {
        this.address_lists[i].is_default=this.address_lists[i].is_default?1:0;
        updateAddress(id, this.address_lists[i]).then((response) => {
          console.log(response.data);
          this.getData();
        }).catch(function (error) {
          alert(error)
          console.log(error);
        })
      },
      addAddr() {
        this.addinfo.is_default=this.addinfo.is_default?1:0
        addAddress(this.addinfo).then((response) => {
          console.log(response.data);
          this.getData();
          this.addinfo=[];
        }).catch(function (error) {
          alert(error)
          console.log(error);
        })
      },
      del(id) {

      }
    },
    created() {
      this.getData();
    }
  };
</script>
<style scoped>
  @import "../../static/css/user.css";
</style>
