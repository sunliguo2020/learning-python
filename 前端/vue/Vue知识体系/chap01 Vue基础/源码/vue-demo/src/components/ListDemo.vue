<template>
  <h3>列表渲染</h3>
  <p v-for="(item,index) in names" :key="index">{{ item }}</p>
  <div v-for="item in result">
    <p>{{ item.title }}</p>
    <img :src="item.avator" />
  </div>
</template>
<script>
export default {
  data() {
    return {
      names: ["百战程序员", "尚学堂", "IT"],
      result: [
        {
          id: 2261677,
          title: "鄂尔多斯|",
          avator: "http://www",
        },
        {
          id: 2261566,
          title: "成都|",
          avator: "http://www",
        },
        {
          id: 2261662,
          title: "川西|",
          avator: "http://www",
        },
      ],
    };
  },
};
</script>