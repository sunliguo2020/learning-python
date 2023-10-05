<template>
  <h3>模板语法</h3>
  <p>{{ msg }}</p>
  <p>{{ number + 1 }}</p>
  <p>{{ ok?"Yes":"No" }}</p>
  <p>{{ message.split("").reverse().join("") }}</p>
  <p v-html="rawHtml"></p>
</template>
<script >
export default {
  data() {
    return {
      msg: "神奇的语法",
      number: 10,
      ok:false,
      message: "大家好",
      rawHtml: "<a href='http://blog.sunliguo.com'>sunliguo</a>"
    };
  },
};
</script>
