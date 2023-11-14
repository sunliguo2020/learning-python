<template>
  <div>
    <myhead></myhead>
    <div class="reg_warp">
      <link
        href="../../static/css/style.css"
        rel="stylesheet"
        type="text/css"
      />
      <div class="reg_header_top clearfix">
        <div class="reg_header center clearfix">
          <p class="reg_login_link fr f14">
            <a class="fr t_c login_link" href="#">登录</a>如已注册， 点此
          </p>
        </div>
      </div>
      <div class="reg_main center">
        <ul class="reg_nav f18 t_c clearfix">
          <li class="user_reg on">新用户注册</li>
        </ul>
        <div class="reg_cont reg_cont1">
          <form name="formUser">
            <div class="register_infor">
              <ul>
                <li class="input_box">
                  <span class="t_text">用户名</span>
                  <input
                    type="text"
                    name="username"
                    v-model="username"
                    id="username"
                  />
                  <span class="error_icon"></span>
                </li>
                <li class="error_box" id="username_notice">
                  <em>{{ err_username }}</em>
                </li>

                <li class="input_box">
                  <span class="t_text">密码</span>
                  <input
                    type="password"
                    name="password"
                    v-model="password"
                    id="password1"
                  />
                  <span class="error_icon"></span>
                </li>
                <li class="error_box" id="password_notice">
                  <em>{{ err_password }}</em>
                </li>

                <li class="input_box">
                  <span class="t_text" id="extend_field5i">手机</span>
                  <input
                    id="mobile"
                    name="mobile"
                    v-model="mobile"
                    type="text"
                  />
                  <span class="error_icon"></span>
                </li>
                <li class="error_box">
                  <em>{{ err_mobile }}</em>
                </li>

                <li class="lizi_law">
                  <label>
                    <input
                      name="agreement"
                      type="checkbox"
                      value="1"
                      checked="checked"
                      tabindex="5"
                      class="remember-me"
                    />
                    我已看过并接受《<a
                      href="#"
                      style="color: blue"
                      target="_blank"
                      >用户协议</a
                    >》
                  </label>
                </li>
                <li class="error_box"><em></em></li>
                <li class="go2register">
                  <input
                    name="Submit"
                    @click="register"
                    type="button"
                    value="同意协议并注册登录"
                    class="btn submit_btn"
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
<script>
import myhead from "@/views/app/head";
import myfooter from "@/views/app/footer";
import { reg } from "@/api/users";
export default {
  data() {
    return {
      username: "",
      password: "",
      mobile: "",
      err_username: "",
      err_password: "",
      err_mobile: "",
    };
  },
  components: {
    myhead,
    myfooter,
  },
  methods: {
    register() {
      var that = this;
      that.err_username = "";
      that.err_password = "";
      that.err_mobile = "";
      reg({
        username: this.username,
        password: this.password,
        mobile: this.mobile,
      })
        .then((response) => {
          console.log(response.data);
          if (response.data.code === 201) {
            //跳转到登陆页面进行登陆
            this.$router.push({ name: "login" });
          }
        })
        .catch(function (error) {
          console.log("reg" + error);
          if ("non_field_errors" in error) {
            that.error = error.non_field_errors[0];
          }
          if ("username" in error) {
            that.err_username = error.username[0];
          }
          if ("password" in error) {
            that.err_password = error.password[0];
          }
          if ("mobile" in error) {
            that.err_mobile = error.mobile[0];
          }
        });
    },
  },
};
</script>

<style scoped>
@import "../../static/css/login.css";
</style>
