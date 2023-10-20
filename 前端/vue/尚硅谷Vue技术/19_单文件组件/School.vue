<template>
  <!-- 组件的结构 -->
  <div>
    <h2>学校名称：{{ name }}</h2>
    <h2>学校地址：{{ address }}</h2>
  </div>
</template>

<script>
//组件交互相关的代码
export default {
  name: "School",
  data() {
    return {
      name: "尚硅谷",
      address: "北京昌平",
    };
  },
  methods: {},
};
</script>
<style>
/* 组件的样式 */
</style>
