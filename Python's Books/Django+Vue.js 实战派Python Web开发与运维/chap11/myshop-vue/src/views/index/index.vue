<template>
  <div id="i1">
    <link href="../../static/css/style.css" rel="stylesheet" type="text/css" />
    <link href="../../static/css/index.css" rel="stylesheet" type="text/css" />
    <myhead></myhead>
    <slide></slide>
    <recommend></recommend>
    <categorygoods></categorygoods>
    <myfooter></myfooter>
  </div>
</template>
<script>
import myhead from "./../app/head";
import myfooter from "./../app/footer";
import slide from "./slide";
import recommend from "./recommend";
import categorygoods from "./categorygoods";
export default {
  data() {
    return {};
  },
  components: {
    myhead,
    slide,
    recommend,
    categorygoods,
    myfooter,
  },
};
</script>
