import Vue from 'vue'  // 引入Vue.js框架
import Router from 'vue-router'  //引入vue-router组件
//引入@路径下名称为HelloWorld的页面组件
import HelloWorld from '@/components/HelloWorld'

//Vue 全局使用Router
Vue.use(Router)

//定义路由，只有在导出后在其他地方才可以使用
export default new Router({
  routes: [
    // 在访问根路径时会链接到HelloWorld.vue组件
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    }
  ]
})
