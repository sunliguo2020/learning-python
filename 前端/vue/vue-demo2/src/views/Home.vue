<template>
    <h1>Home页面</h1>
    <!--父组件要发送数据给子组件，通过组件的属性传递。属性名就是将来的变量名，
    传递数据如果时一个变量，则需要在左边加上冒号
    -->
    <Menu :htotal="total" title="来自父组件的数据" @add_num="get_data"> </Menu>
    <button @click="total++">{{ total }}</button>

    <br>
    <Register></Register>
</template>
<script>
import Menu from '../components/Menu.vue'
import Register from './Register.vue'
export default {
    name: "home",
    data() {
        return {
            total: 0
        }
    },
    components: {
        Menu,
        Register,
    },
    methods: {
        get_data(a1, a2) {
            console.log('子组件传递数据过来了！')
            console.log(a1, a2)
        }
    }
}
</script>
<style scoped>

</style>