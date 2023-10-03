<template>
  <h3>表单数据绑定</h3>
  <form>
    <input type="text " v-model="message" />
    <p>{{ message }}</p>
    <input type="checkbox" id="checkbox" v-model="checked" />
    <label for="checkbox">{{ checked }}</label>
  </form>
</template>
<script>
export default {
  data() {
    return {
      message: "",
      checked: true,
    };
  },
};
</script>
