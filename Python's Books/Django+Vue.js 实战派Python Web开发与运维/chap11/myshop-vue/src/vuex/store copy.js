import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)
const state = {
    count: 10,
    username:''||localStorage.getItem('username'),
}

const mutations = {
    saveUser(state,username){
        state.username=username,
        localStorage.setItem('username',username)
    },
    delUser(state){
        state.user=null;
    },
    mutationAdd(state,n=0){
        return state.count+=n
    },
    mutationReduce(state,n=0){
        return state.count-=n
    }
}

const actions={
    saveUser(context,value){
        return context.commit('saveUser',value)
    },
    delUser(context){
        return context.commit('delUser')
    },
    actionsAdd(context,n=0){
        return context.commit('mutationAdd',n)
    },
    actionsReduce(context,n=0){
        return context.commit('mutationReduce',n)
    }
}
const getters={
    getCount(state){
        return state.count
    },
    username(state){
        return state.username
    }
}

const store =new Vuex.Store({
    state,
    mutations,
    actions,
    getters
})
export default store
