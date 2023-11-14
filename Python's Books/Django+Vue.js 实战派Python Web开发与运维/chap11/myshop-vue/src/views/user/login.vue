<template>
  <div class="login">
    <myhead></myhead>
    <link href="../../static/css/style.css" rel="stylesheet" type="text/css" />
    <div class="reg_warp">
      <div class="reg_header_top clearfix">
        <div class="reg_header center clearfix">
          <p class="reg_login_link fr f14">
            <a
              class="fr t_c login_link"
              href="http://ecshop.numberone.ink:10003/user.php?act=register"
              >注册</a
            >如未注册， 点此
          </p>
        </div>
      </div>
      <div class="reg_main center">
        <ul class="reg_nav f18 t_c clearfix">
          <li class="user_reg on login_user">
            <font class="iconfont"></font><font id="login_cat">用户登录</font>
          </li>
        </ul>
        <div class="reg_cont reg_cont1 relative" style="">
          <form name="formLogin" action="" method="post">
            <div class="register_infor">
              <ul>
                <li class="input_box">
                  <input
                    type="text"
                    name="username"
                    id="username"
                    v-model="username"
                    placeholder="用户名、手机、邮箱"
                  />
                  <span class="error_icon"></span>
                </li>
                <li class="error_box" id="username_notice">
                  <em>{{ err_username }}</em>
                </li>
                <li class="input_box">
                  <input
                    type="password"
                    name="password"
                    id="password"
                    v-model="password"
                    placeholder="请输入你的密码"
                  />
                  <span class="error_icon"></span>
                </li>
                <li class="error_box" id="password_notice">
                  <em>{{ err_password }}</em>
                </li>
                <li class="go2register">
                  <input
                    type="hidden"
                    name="login_type"
                    value="0"
                    id="login_type"
                  />
                  <input type="hidden" name="act" value="act_login" />
                  <input type="hidden" name="back_act" value="./index.php" />
                  <input
                    type="button"
                    name="submit"
                    class="btn submit_btn"
                    @click="login"
                    value="登 录"
                  />
                </li>
              </ul>
            </div>
          </form>
        </div>
      </div>
    </div>
    <myfooter></myfooter>
  </div>
</template>
<style scoped>
@import "../../static/css/login.css";
</style>
<script>
import myhead from "@/views/app/head";
import myfooter from "@/views/app/footer";
import { mapMutations, mapActions, mapGetters } from "vuex";
import { login } from "@/api/index";
export default {
  data() {
    return {
      username: "",
      password: "",
      message: "",
      err_username: "",
      err_password: "",
    };
  },
  components: {
    myhead,
    myfooter,
  },
  methods: {
    login() {
      var that = this;
      this.message = "";
      login({
        username: this.username,
        password: this.password,
      })
        .then((Response) => {
          console.log(Response);
          if (Response.status === 200) {
            //保存数据到本地存储
            console.log(Response.data.token);
            //同时保存到vuex
            //this.saveUser(Response.data);
            //localStorage.setItem('user',{'token':Response.data.token,'id':Response.data.id,'username':Response.data.username});
            localStorage.setItem("token", Response.data.token),
              this.$store.dispatch("saveUser", Response.data);
            //console.log(this.$store.user.id);
            this.username = "";
            this.password = "";
            this.$router.push("/index"); //跳转到首页
            //alert('登陆成功');
          }
        })
        .catch(function (error) {
          if ("username" in error) {
            that.err_username = error.username[0];
          } else if ("password" in error) {
            that.err_password = error.password[0];
          } else {
            alert("登录失败");
          }
        });
    },
  },
};
</script>
