<template>
  <div class="pagenav" id="pagenav">
    <ul>
      <li>
        <a class="nextLink" @click="get_page(1)">首页</a>
        <a class="nextLink" @click="get_prev_page()">上一页</a>
        <a class="nextLink" v-for="num in total_page" @click="get_page(num)">{{
          num
        }}</a>
        <a class="nextLink" @click="get_next_page()">下一页</a>
        <a class="nextLink" @click="get_page(total_page)">尾页</a>
      </li>
    </ul>
    <div class="clear"></div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      curr_page: 1,
    };
  },
  name: "mypage",
  props: ["total_page"],
  methods: {
    get_page(num) {
      this.curr_page = num;
      let data = {
        curr_page: this.curr_page,
      };
      this.$emit("get_page", { curr_page: this.curr_page });
    },
    get_prev_page() {
      if (this.curr_page == 1) {
        return;
      }
      this.curr_page -= 1;
      this.$emit("get_page", { curr_page: this.curr_page });
    },
    get_next_page() {
      if (this.curr_page == this.total_page) {
        return;
      }
      this.curr_page += 1;
      this.$emit("get_page", { curr_page: this.curr_page });
    },
  },
};
</script>
