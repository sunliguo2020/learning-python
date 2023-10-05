<template>
    <h3>自定义事件传递数据</h3>
    <button @click="sendClickHandle">点击传递</button>
</template>
<script>
export default {
    name: "myComponent2",
    props: {

    },
    data(){
        return {
            message:'我是MyComponent数据',
        }
    },
    methods:{
        sendClickHandle(){
            //参数1：字符串
            //参数2：传递的数据
            this.$emit("onEvent",this.message)
        }
    },
    beforeCreate(){
        console.log('beforeCreate:组件创建前');
    },
    created(){
        console.log('Created:组件创建完成');
    },

}
</script>
<style scoped></style>