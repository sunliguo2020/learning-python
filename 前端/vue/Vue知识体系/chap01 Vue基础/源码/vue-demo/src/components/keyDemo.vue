<template>
  <h3>key属性添加到v-for中</h3>
  <p v-for="(name, index) of names" v-bind:key="index">{{ name }}</p>
</template>
<script>
export default {
  data() {
    return { names: ["百战程序员", "尚学堂", "IT"] };
  },
};
</script>