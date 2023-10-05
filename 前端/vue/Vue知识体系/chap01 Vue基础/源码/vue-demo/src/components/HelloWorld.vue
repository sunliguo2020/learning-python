<template>
  <div class="{{msg}}">测试</div>
  <div v-bind:id="dynamicID" v-bind:class="msg" :title="dynamicTitle">测试</div>
  <div>{{ rawHtml }}</div>
  <div v-html="rawHtml"></div>
  <p v-text="rawHtml"></p>
  <div v-bind:id="dynamicID" v-bind:title="dynamicTitle">测试</div>
</template>

<script >
export default {
  data() {
    return {
      msg: "active",
      dynamicID: "appid",
      dynamicTitle:"undefined",
      rawHtml:"<a href='http://www.itbaizhan.com'>百战</a>",
    };
  },
};
</script>

