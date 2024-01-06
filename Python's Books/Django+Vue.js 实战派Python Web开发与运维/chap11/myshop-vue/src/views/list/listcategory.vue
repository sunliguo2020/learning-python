<template>
  <div class="sidebar">
    <div class="cate-menu" id="cate-menu">
      <h3>
        <a href="category.php?id=2">
          <strong>{{ categoryname }}</strong>
          <i id="total_count">商品共{{ sub_cat.length }}件</i>
        </a>
      </h3>
      <dl>
        <dt v-for="item in sub_cat">
          {{ item.name }}
        </dt>
      </dl>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {};
  },
  props: {
    sub_cat: {
      default: function () {
        return {};
      },
    },
    categoryname: "",
  },
};
</script>
