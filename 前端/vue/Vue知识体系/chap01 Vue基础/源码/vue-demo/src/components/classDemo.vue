<template>
  <p :class="myClass">Class样式绑定</p>
  <p v-bind:class="myClass">Class样式</p>
  <p :class="{ 'active': isActive, 'text-danger': hasError }">Class样式</p>
  <p :class="classObject">Class样式绑定2</p>
  <p :class="[arrActive, arrHasError]">Class样式绑定3</p>
</template>
<script>
export default {
  data() {
    return {
      myClass: "demo",
      isActive: false,
      hasError: true,
      classObject: {
        active: true,
        "text-danger": true,
      },
      arrActive: "active",
      arrHasError: "text-danger",
    };
  },
};
</script>
<style >
.active {
  font-size: 30px;
}
.text-danger {
  color: red;
}
</style>