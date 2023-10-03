<script >
export default {
  data() {
    return {
      msg: "active",
      dynamicID: "appid",
    };
  },
};
</script>

<template>
  <div class="{{msg}}">测试</div>
  <div v-bind:id="dynamicID" v-bind:class="msg">测试</div>
</template>

