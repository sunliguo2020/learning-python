<template>
    <!-- 第三步：显示组件 -->
    <MyComponent/>
</template>
<script>
//第一步：引入组件
import MyComponent from "./components/mycomponent.vue"

export default{
    //第二步：注入组件
    components:{
        MyComponent,
    }
}
</script>
