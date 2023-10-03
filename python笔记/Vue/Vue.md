```
npm init vue@latest
```

### 5 Vue项目目录结构

### 6 模板语法

### 7 属性绑定

### 8 条件渲染

### 9 列表渲染	v-for

利用v-for 指令，可以基于一个数组渲染一个列表。

v-for = "item in items"

### 10 通过key管理状态





### 11 事件处理

Vue.js的事件绑定格式是"v-on:"或者”@“。事件处理方法需要在methods中定义。

### 12 事件传参



### 13事件修饰符

### 14 数组变化侦测

### 15 计算属性

```vue
<template>
    <h3>{{itbaizhan.name}}</h3>
    <p>{{itbaizhan.content.length > 0 ?"Yes":"No"}}</p>
    <p>{{itbaizhanContent}}</p>
</template>
<script>
export default {
    data(){
        return {
            itbaizhan:{
                name:"百战程序员",
                content:['前端',"Java",'Python']
            }
        }
    },
    //计算属性
    computed:{
        itbaizhanContent(){
            return this.itbaizhan.content.length > 0 ?"Yes":"No"
        }
    }
}
</script>
```

### 16 Class 绑定

```vue
<template>
  <p :class="myClass">Class样式</p>
  <p v-bind:class="myClass">Class样式</p>
  <p :class="{ active: isActive, 'text-danger': hasError }">Class样式</p>
  <p :class="classObject">Class样式绑定2</p>
  <p :class="[arrActive, arrHasError]">Class样式绑定3</p>
</template>
<script>
export default {
  data() {
    return {
      myClass: "demo",
      isActive: false,
      hasError: true,
      classObject: {
        active: true,
        "text-danger": true,
      },
      arrActive: "active",
      arrHasError: "text-danger",
    };
  },
};
</script>
<style >
.active {
  font-size: 30px;
}
.text-danger {
  color: red;
}
</style>
```



### 18 侦听器

```vue
<template>
  <h3>侦听器</h3>
  <p>{{ message }}</p>
  <button @click="updateHandle">修改数据</button>
</template>
<script>
export default {
  data() {
    return {
      message: "Hello",
    };
  },
  methods: {
    updateHandle() {
      this.message = "world";
    },
  },
  watch: {
    //newValue 改变之后的数据
    //oldValue 改变之前的数据
    //函数名必须与侦听的数据对象保持一致
    message(newValue, oldValue) {
      console.log(newValue);
      console.log(oldValue);
    },
  },
};
</script>
```

### 19表单输入绑定

```vue
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

```

### 20 模板引用

```vue
<template>
  <div ref="container" class="container">{{ content }}</div>
  <input type="text" ref="username">
  <button @click="getElementHandle">获取元素</button>

</template>
<script>
/**
 *内容改变：{{模板语法}}
属性改变：v-bind: 指令
事件： v-on:click
如果没有特别的需求，不要操作DOM
 */
export default {
  data() {
    return {
      content: "内容",
    };
  },
  methods:{
    getElementHandle(){
        //innerHTML:原生js的属性
        //console.log(this.$refs.container.innerHTML='哈哈哈')
        console.log(this.$refs.username.value)
    }
  }
};
</script>
```

### 21组件组成

### 22 组件嵌套关系

### 23 组件传递数据_Props

组件与组件之间不是完全独立的。

传递数据的解决方案是Props。

>
>
>## 注意事项 ##
>
>`props`传递数据，只能从父级传递到子级，不能反其道而行。

