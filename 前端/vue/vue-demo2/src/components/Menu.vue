<template>
    <div>
        <p>来自父组件的数据：total= {{ htotal }}</p>
        <p>来自父组件的数据：title= {{ title }}</p>
        <br>
        <p>要发送给父组件的数据，num={{ num }}</p>
        <button @click="add">{{ num }}</button>
        <ul>
            <li><a href="">首页</a></li>
        </ul>
    </div>
</template>
<script>
export default {
    name: "Menu",
    //来自父组件的数据，全部通过props来接收，2种写法：json写法，数组写法
    // props:['htotal','title']
    props: {
        htotal: Number,   //来自父组件的数据
        title: String,
    },
    data() {
        return {
            num: 10,
            msg: "hello，我是子组件定义的属性。"
        }
    },
    methods: {
        add() {
            this.num ++;
            //传递数据给父组件,this.emit("自定义事件名",变量1，变量2---)
            this.$emit("add_num", this.num, this.msg)
        }
    }

}

</script>
<style scoped>
div {
    border: 1px solid red;
}

ul {
    list-style-type: none;
}

li {
    display: inline;
    margin-right: 10px;
}

li a {
    text-decoration: none;
}
</style>
