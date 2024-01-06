import Vue from 'vue'
import Vuex from 'vuex'
import { getCart } from '@/api/order'
Vue.use(Vuex)
const state = {
  count: 10,
  userinfo: localStorage["userinfo"] ? JSON.parse(localStorage["userinfo"]) : [],
  cart_lists: localStorage["cart_lists"]? JSON.parse(localStorage["cart_lists"]) : {
    "goods_list": [],
    "total_price": 0,
    "total_num": 0
  }
}

const mutations = {
  saveUser(state, value) {
    state.userinfo = value,
      localStorage.setItem('userinfo', value)
  },
  delUser(state) {
    state.userinfo = null;
    localStorage['userinfo']=null;
    state.cart_lists=null;
    localStorage["cart_lists"]=JSON.stringify({
      "goods_list": [],
      "total_price": 0,
      "total_num": 0
    });
  },
  saveCart(state) {
    getCart().then((response) => {
      state.cart_lists.goods_list = response.data.data
      console.log("data " + JSON.stringify(response.data))
      var totalprice = 0;
      var totalnum = 0;
      console.log(state.cart_lists.goods_list)
      for (var i = 0; i < state.cart_lists.goods_list.length; i++) {
        var item = state.cart_lists.goods_list[i]
        console.log("item" + item)
        totalprice += item.goods_num * item.goods.price;
        totalnum += item.goods_num
      }
      state.cart_lists.total_price = totalprice
      state.cart_lists.total_num = totalnum
      localStorage.setItem('cart_lists', state.cart_lists)
    }).catch(function (error) {
      console.log(error)
    })
  },
  mutationAdd(state, n = 0) {
    return state.count += n
  },
  mutationReduce(state, n = 0) {
    return state.count -= n
  }
}

const actions = {
  saveUser(context, value) {
    return context.commit('saveUser', value)
  },
  delUser(context) {
    return context.commit('delUser')
  },
  saveCart(context) {
    return context.commit('saveCart')

  },
  actionsAdd(context, n = 0) {
    return context.commit('mutationAdd', n)
  },
  actionsReduce(context, n = 0) {
    return context.commit('mutationReduce', n)
  }
}
const getters = {
  getCount(state) {
    return state.count
  },
  userinfo(state) {
    localStorage.setItem("userinfo", JSON.stringify(state.userinfo));
    return state.userinfo;
  },
  cart_lists(state) {
    localStorage.setItem("cart_lists", JSON.stringify(state.cart_lists));
    return state.cart_lists;
  },
  getAllCount(state){
    var c=0;
    state.cart_lists.forEach(item=>{
        c+=item.count;
    })

  }
}

const store = new Vuex.Store({
  state,
  mutations,
  actions,
  getters
})
export default store
