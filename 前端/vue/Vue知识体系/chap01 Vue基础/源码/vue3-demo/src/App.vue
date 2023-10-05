<template>
  <img alt="Vue logo" src="./assets/logo.png">

  <!-- <myComponent :title="title" :age="age" />
  <p>{{ message }}</p>
  <myComponent2 @onEvent="getDataHandle" /> -->
  <axiosDemo/>
</template>

<script>
import myComponent from "./components/myComponents.vue"
import myComponent2 from "./components/myComponents2.vue"
import axiosDemo from "./components/axiosDemo.vue"

export default {
  name: 'App',
  data() {
    return {
      title: '我是一个标题',
      age: 20,
      message:""
    }
  },

  methods:
  {
    getDataHandle(data) {
      console.log(data);
      this.message = data;
    }
  },
  components: {
    // myComponent,
    // myComponent2,
    axiosDemo,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
