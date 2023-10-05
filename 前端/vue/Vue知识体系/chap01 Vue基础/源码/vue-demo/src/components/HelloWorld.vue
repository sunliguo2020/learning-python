<template>
  <div class="{{msg}}">测试</div>
  <div v-bind:id="dynamicID" v-bind:class="msg">测试</div>
  <div>{{ rawHtml }}</div>
  <div v-html="rawHtml"></div>
  <div v-bind:id="dynamicID">测试</div>
</template>

<script >
export default {
  data() {
    return {
      msg: "active",
      dynamicID: "appid",
      rawHtml:"<a href='http://www.itbaizhan.com'>百战</a>",
      
    };
  },
};
</script>

