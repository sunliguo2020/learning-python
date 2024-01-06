import Vue from 'vue' // 引入vue框架
import Router from 'vue-router' // 引入vue-router组件
import HelloWorld from '@/components/HelloWorld' // 引入@路径下的名称为HelloWorld的页面组件
// import { head } from 'shelljs'
Vue.use(Router) // Vue全局使用Router
// 路由配置的定义，只有export后，其他地方才能import进来
export default new Router({
  routes: [
    // 当访问跟路径时，会链接到HelloWorld.vue组件
    {
      path: '/hello',
      name: 'HelloWorld', // 路由名称
      component: HelloWorld // 对应的组件模板
    },
    {
      name: 'index',
      path: '/index',
      component: () => import('@/views/index/index'),
      meta: {
        title: '商城首页'
      }
    },
    {
      name: 'list',
      path: '/list/:id',
      component: () => import('@/views/list/list'),
      meta: {
        title: '商品列表'
      }
    },
    {
      name: 'detail',
      path: '/detail/:id',
      component: () => import('@/views/detail/detail'),
      meta: {
        title: '明细页'
      }
    },
    {
      name: 'cart',
      path: '/cart',
      component: () => import('@/views/cart/cart'),
      meta: {
        title: '购物车'
      }
    },
    {
      name: 'reg',
      path: '/reg',
      component: () => import('@/views/user/reg'),
      meta: {
        title: '用户注册'
      }
    },
    {
      name: 'login',
      path: '/login',
      component: () => import('@/views/user/login'),
      meta: {
        title: '用户登录'
      }
    },
    {
      name: 'checkout',
      path: '/checkout',
      component: () => import('@/views/cart/checkout'),
      meta: {
        title: '结算'
      }
    },
    {
      name: 'address',
      path: '/address',
      component: () => import('@/views/user/address'),
      meta: {
        title: '我的配送地址'
      }
    },
    {
      name: 'profile',
      path: '/profile',
      component: () => import('@/views/user/profile'),
      meta: {
        title: '个人中心'
      }
    },
    {
      name: '/myorder',
      path: '/myorder',
      component: () => import('@/views/user/myorder'),
      meta: {
        title: '我的订单'
      }
    }
  ]
})
