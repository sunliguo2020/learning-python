// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'

// 引入路由，会去寻找index.js配置文件
import router from './router'

// 关闭生产模式下的提示
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  // 在框架中使用路由功能
  router,
  components: { App },
  template: '<App/>'
})
