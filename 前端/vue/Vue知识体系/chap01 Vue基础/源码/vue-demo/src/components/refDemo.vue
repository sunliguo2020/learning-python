<template>
  <div ref="container" class="container">{{ content }}</div>
  <input type="text" ref="username">
  <br>
  <button v-on:click="counter += 1">点击：counter={{ counter }}</button>
  <button @click="getElementHandle">获取元素</button>
  <button @click="clickHandle">按钮</button>
  <p>{{ message }}</p>

  <br>
  <button @click="say('hi')">say</button>
  <button @click="say('what')">say what</button>
  <ul>
    <li @click="clickHandle2(item)" v-for="(item, idnex) in names" :key="index">{{ item }}</li>
  </ul>
</template>
<script>
/**
    *内容改变：{{模板语法}}
    *属性改变：v-bind: 指令
    *事件： v-on:click
    *如果没有特别的需求，不要操作DOM
 */
export default {
  data() {
    return {
      content: "内容",
      counter: 1,
      message: '消息通知',
      names: ['iwen', 'ime', 'frank']
    };
  },
  methods: {
    getElementHandle() {
      //innerHTML:原生js的属性
      //console.log(this.$refs.container.innerHTML='哈哈哈')
      console.log(this.$refs.username.value)
    },
    clickHandle(event) {
      // 在事件中，读取data中的属性，是需要通过this.属性
      this.message = '消息撤回了';
      //event 是原生的DOM event
      console.log(event);
      event.target.innerHTML = '点击之后';
    },
    say(data) {
      console.log(data)
    },
    clickHandle2(data) {
      console.log(data)
    }
  }
};
</script>