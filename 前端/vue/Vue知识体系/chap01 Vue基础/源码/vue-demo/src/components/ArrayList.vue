<template>
<h3>数组侦听</h3>
<button @click="addListHandle">添加数据</button>
<ul>
    <li v-for="(name,index) in names" :key="index">{{ name }}</li>
</ul>
</template>
<script>
export default{
    data(){
        return {
            names:['iwen','ime','frank']
        }
    },
    methods:{
        
        addListHandle(){
            //引起UI自动更新
            // this.names.push("sakura")
            //不会引起UI自动更新
            this.names.concat(['sakura'])

            console.log(this.names)
            this.names = this.names.concat(['sakura'])
        }
    }

}
</script>