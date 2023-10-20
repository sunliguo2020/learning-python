<template>
  <div>
    <h1 v-text='msg' ref='title'></h1>
    <School ref='sch' />
    <button  ref='btn' @click="showDOM">点我显示DOM元素</button>
  </div>
</template>

<script>
import School from "./components/School.vue";
export default {
  name: "App",
  components: {
    School,
  },
  data(){
return {
    msg:'欢迎学习vue！'
}
  },
  methods: {
    showDOM() {
    //   console.log(this);
      console.log(this.$refs.btn);
      console.log(this.$refs.title);
      console.log(this.$refs.sch) //School组件的实例对象
    },
  },
};
</script>

<style>
</style>