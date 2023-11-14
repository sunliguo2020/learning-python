<template>
<div>
<myhead></myhead>

  <div id="wrapper" class="cle">
    <link href="../../static/css/style.css" rel="stylesheet" type="text/css" />
    <div class="here cle"><a href="#">首页</a> <code>&gt;</code> 用户中心</div>

    <div class="my_nala_main">

      <left></left>

      <div class="my_nala_centre ilizi_centre">
        <div class="ilizi cle">
          <div class="box">
            <div class="box_1">
              <div class="userCenterBox boxCenterList clearfix" style="_height:1%;">
                <h5><span>个人资料</span></h5>
                <div class="blank"></div>
                <form name="formEdit" action="#" method="post">
                  <table width="100%" height="200px" border="1" cellpadding="5" cellspacing="1" bgcolor="#dddddd">
                    <tbody>
                      <tr>
                        <td width="28%" align="right" bgcolor="#FFFFFF">姓名： </td>
                        <td width="72%" align="left" bgcolor="#FFFFFF"> <input name="truename" type="text" v-model="userinfo.truename" size="25" class="inputBg" /> </td>
                      </tr>
                      <tr>
                        <td width="28%" align="right" bgcolor="#FFFFFF">性　别： </td>
                        <td width="72%" align="left" bgcolor="#FFFFFF">
                          <input type="radio" name="sex" value="1" v-model="userinfo.sex" />
                          男&nbsp;&nbsp;
                          <input type="radio" name="sex" value="0"  v-model="userinfo.sex" />
                          女&nbsp;&nbsp;
                        </td>
                      </tr>
                      <tr>
                        <td width="28%" align="right" bgcolor="#FFFFFF">电子邮件地址： </td>
                        <td width="72%" align="left" bgcolor="#FFFFFF"><input name="email" type="text" v-model="userinfo.email" size="25" class="inputBg" /><span style="color:#FF0000"> *</span></td>
                      </tr>
                      <tr>
                        <td width="28%" align="right" bgcolor="#FFFFFF" id="extend_field5i">手机：</td>
                        <td width="72%" align="left" bgcolor="#FFFFFF">
                          <input name="extend_field5" type="text" class="inputBg" v-model="userinfo.mobile" /><span style="color:#FF0000"> *</span>
                        </td>
                      </tr>
                      <tr>
                        <td colspan="2" align="center" bgcolor="#FFFFFF">
                          
                          <input name="submit" type="button" @click="updateUserinfo" value="确认修改" class="btn-primary" style="border:none;" />
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </form>
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
import { getUsersByID, updateUsers } from '@/api/users'
export default {
  data() {
    return {
      userinfo:{
        birthday:'',
        sex:'0',
        email:'',
        mobile:''
      }
    };
  },
      components: {
      myhead,
      myfooter,
      left,
    },
  methods:{
      getData(){
        getUsersByID().then((response)=>{
          this.userinfo=response.data.data;
        }).catch(function(error){
          console.log(error);
        })
      },
      updateUserinfo(){
        updateUsers(this.userinfo).then((response)=>{
          alert('修改成功')
        }).catch(function(error){
          console.log(error);
          alert(JSON.stringify(error));
        })
      },
  },
  created(){
    this.getData();
  }
};
</script>
<style scoped>
  @import "../../static/css/user.css";
</style>
