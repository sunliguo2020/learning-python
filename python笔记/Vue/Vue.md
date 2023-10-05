# Vue是什么

Vue是前端优秀框架，是一套用于构建用户界面的**渐进式框架**。

# Vue API风格

Vue的组件可以按两种不同的风格书写：***选项式API***和**组合式API**

# Vue开发前端的准备



> 前提条件：
>
> 命令行
>
> nodejs 15.0或更高版本

### 创建项目

#### 第一种：使用 vue cli

```
npm install -g @vue/cli
```

 The recommended way to start a Vite-powered Vue project

```
npm create vue@latest
```

使用

```
  cd vue-demo12
  npm install
  npm run dev
```

#### 第二种：

```
npm init vue@latest
```

这一条指令将会安装并执行create-vue,它是Vue官方的项目脚手架工具。你将会看到一些诸如TypeScript和测试支持之类的可选项功能提示。

```
Vue.js - The Progressive JavaScript Framework

√ Project name: ... vue-demo
√ Add TypeScript? ... No / Yes
√ Add JSX Support? ... No / Yes
√ Add Vue Router for Single Page Application development? ... No / Yes
√ Add Pinia for state management? ... No / Yes
√ Add Vitest for Unit Testing? ... No / Yes
√ Add an End-to-End Testing Solution? » No
√ Add ESLint for code quality? ... No / Yes

Scaffolding project in C:\Users\sunliguo\vue-test\vue-demo...

Done. Now run:

  cd vue-demo
  npm install
  npm run dev
```

#### 开发环境

vscode + volar

# 5 Vue项目目录结构

```
.vscode			--vscode工具的配置文件
node_modules 	---Vue项目的运行依赖文件夹
public 			--- 资源文件夹（浏览器图标）
src				---	源码文件夹
.gitignore		---git忽略文件
index.html		--- html文件
package.json	---	信息描述文件
README.md		---	注释文件
vite.config.js	---	Vue配置文件
```

# 6 模板语法

“插值”是指，使用{{变量}}的方法讲数据插入到HTML文档中。

插值分为文本插值、HTML插值等。

- 文本插值 {{变量}} v-text
- HTML插值 v-html

```vue
<script >
export default {
  data() {
    return {
      msg: "神奇的语法",
      number:10,
      message:"大家好",
      rawHtml :"<a href='http://blog.sunliguo.com'>sunliguo</a>"
    };
  },
};
</script>

<template>
  <h3>模板语法</h3>
  <p>{{ msg }}</p>
  <p>{{number+1}}</p>
  <p>{{message.split("").reverse().join("")}}</p>
  <p v-html="rawHtml"></p>
</template>

```



```html
 <div id="app">
        <p>{{title}}</p>
        <p v-text="title"></p>
        <p>{{content}}</p>
        <p>{{ htmlContent}}</p>
        <p v-text="htmlContent"></p>
        <p v-html="htmlContent"></p>
 
    </div>
    <script>
        const vm = new Vue({
            el: '#app',
            data() {
                return {
                    title: '这是标题内容',
                    content: "这是内容文本",
                    htmlContent:'这是一个<span>span</span>标签'
                }
            },
        }
        )
    </script>
</body>
```

### 使用JavaScript表达式





# 7 属性绑定 v-bind

 双大括号不能在 HTML attributes 中使用。想要响应式地绑定一个 attribute，应该使用 [`v-bind` 指令](https://cn.vuejs.org/api/built-in-directives.html#v-bind)： 

```html
<div v-bind:id="dynamicId"></div>
```

```vue
<script >
export default {
  data() {
    return {
      msg: "active",
      dynamicID: "appid",      
    };
  },
};
</script>

<template>
  <div v-bind:id="dynamicID">测试</div>
</template>

```

v-bind指令只是将元素的id attribute与组件的dynamicld属性保持一致。如果绑定的值是null或者undefined，那么该attribute将会从渲染的元素上移除。

> 温习提示：
>
> v-bind: 可以简写为：

## 8 条件渲染 v-if

```vue
<template>
    <h3>条件渲染</h3>
    <div v-if="flag">你能看见我吗？</div>
    <div v-else>那你还是看看我吧</div>
</template>
<script>
export default{
    data(){
        return {
            flag:false,
        }
    }
}
</script>

```

v-show 

## 9 列表渲染	v-for

利用v-for 指令，可以基于一个数组渲染一个列表。

v-for = "item in items"

```vue
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
```

# 10 通过key管理状态

### 维护状态

当Vue正在更新使用v-for渲染的元素列表时，它默认使用“就地更新”的策略。如果数据项的**顺序**改变，Vue就不会移动DOM元素来匹配数据项的顺序，而是就地更新每个元素，并确保他们在原本指定的索引位置上渲染。

为了给Vue一个提示，以便它能耿总每个节点的身份，从而重用和重新排序现有元素，你需要为每项提供一个唯一的key attribute：

```vue
<template>
  <h3>key属性添加到v-for中</h3>
  <p v-for="(name, index) of names" v-bind:key="index">{{ name }}</p>
</template>
<script>
export default {
  data() {
    return { names: ["百战程序员", "尚学堂", "IT"] };
  },
};
</script>
```

# 11 事件处理

Vue.js的事件绑定格式是"v-on:"或者”@“。事件处理方法需要在methods中定义。

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

```vue
<template>
  <div ref="container" class="container">{{ content }}</div>
  <input type="text" ref="username">
  <br>
  <button v-on:click="counter += 1">点击：counter={{ counter }}</button>
  <button @click="getElementHandle">获取元素</button>
  <button @click="clickHandle">按钮</button>
  <p>{{ message }}</p>
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
      counter: 1,
      message: '消息通知'
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
    }
  }
};
</script>
```

# 12 事件传参

内联处理器中的参数

```
<template>
  <button @click="say('hi')">say</button>
  <button @click="say('what')">say what</button>
  <ul>
    <li @click="clickHandle2(item)" v-for="(item,idnex) in names" :key="index">{{item}}</li>
  </ul>
  
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
      counter: 1,
      message: '消息通知',
      names:['iwen','ime','frank']
    };
  },
  methods: {

    say(data){
      console.log(data)
    },
    clickHandle2(data){
      console.log(data)
    }
  }
};
</script>
```

# 13事件修饰符

Vue为v-on提供了事件修饰符，常用的有一下几个：

- .stop

- .prevent

- .once

- .enter

  

#### 阻止默认事件

```vue
<template>
<h3>事件修饰符</h3>
<a @click.prevent="clcikHandle" href="https://itbaizhan.com">百战程序员</a>
</template>
<script>

export default{
    data(){

        return {

        }
    },
    methods:{
        clcikHandle(e){
            //阻止默认事件
            // e.preventDefault();
            console.log('点击了');
        }
    }
}
</script>
```

#### 阻止冒泡事件

```vue
<template>
<h3>事件修饰符</h3>

<div @click="clickDiv">
    <p @click.stop="clickP">测试冒泡</p>
</div>
</template>
<script>

export default{
    data(){

        return {

        }
    },
    methods:{
   
        clickDiv(){
            console.log('点击了div')
        },
        clickP(e){
            //阻止冒泡
            // e.stopPropagation();
            console.log('点击了p')
        }
    }
}
</script>
```

# 14 数组变化侦测

#### 变更方法

变更方法，顾名思义，就是会对调用他们的原数组进行变更。

Vue能够侦听响应式数组的变更方法，并在它们被调用时触发相关的更新。这些变更方法包括：

- push()
- pop()
- shift()
- unshift()
- splice()
- sort()
- reverse()  

```vue
<template>
<h3>数组侦听</h3>
<button @click="addListHandle">添加数据</button>
<ul>
    <li v-for="(name,index) in names" :key="index">{{ name }}</li>
</ul>
</template>
<script>
export default{
    data(){
        return {
            names:['iwen','ime','frank']
        }
    },
    methods:{
        //引起UI自动更新
        addListHandle(){
            this.names.push("sakura")
        }
    }

}
</script>
```



#### 替换一个数组

filter(),concat()和slice()，不会更改原数组，而总是返回一个新数组。当遇到的是非变更方法时，我门需要将就的数组替换为新的。

```vue
<template>
<h3>数组侦听</h3>
<button @click="addListHandle">添加数据</button>
<ul>
    <li v-for="(name,index) in names" :key="index">{{ name }}</li>
</ul>
</template>
<script>
export default{
    data(){
        return {
            names:['iwen','ime','frank']
        }
    },
    methods:{
        
        addListHandle(){
            //引起UI自动更新
            // this.names.push("sakura")
            //不会引起UI自动更新
            this.names.concat(['sakura'])

            console.log(this.names)
            this.names = this.names.concat(['sakura'])
        }
    }

}
</script>
```

# 15 计算属性

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

# 16 Class 绑定

数据绑定的一个常见需求场景是操纵元素的CSS class列表。

Vue专门为class的v-bind用法提供了特殊的功能增强。处理字符串外，表达式的值也可以是对象或数组。



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

# 17 style绑定

```vue
<template>
    <p :style="{class:'red'}">style绑定1</p>
    <p :style="{class:activeColor}">style绑定2</p>
    <p :style="styleObject">style绑定3</p>

    
</template>
<script>
export default {
    data(){
        return {
            activeColor:'green',
            fontSize:30,
            styleObject:{
                color:'red',
                fontSize:'30px'
            }

        }
    }
}
</script>
```

# 18 侦听器

我们使用wach选项在每次响应式属性发生变化时触发一个函数。

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

# 19表单输入绑定v-model



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

# 20 模板引用

虽然Vue的声明性渲染模型为你抽象了大部分对DOM的直接操作，但在某些情况下，我们仍然需要直接访问的底层DOM元素。要实现这一点，我们可以使用特殊的ref attribute。

挂载结束后引用都会被暴露在<font color=red>this.$refs</font>之上。

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

# 21组件组成

组件最大的优势就是可复用性。

当使用构建步骤时，我们一般会将Vue组件定义在一个.vue文件中，这被叫做单文件组件（简称SFC）

#### 组件组成结构

```vue
<template>
	<div>承载标签</div>
</template>
<script>
export default {

}
</script>
<style scoped>
</style>
```

#### mycomponent

```vue
<template>
  <div class="container">组件基础组成</div>
</template>
<script >
export default {
  data() {
    return "";
  },
};
</script>

<!--scoped 让当前样式只在当前组件生效-->
<style scoped>
.container {
  font-size: 20px;
}
</style>

```

App.vue

```vue
<template>
    <!-- 第三步：显示组件 -->
    <MyComponent/>
</template>
<script>
//第一步：引入组件
import MyComponent from "./components/mycomponent.vue"

export default{
    //第二步：注入组件
    components:{
        MyComponent,
    }
}
</script>

```



# 22 组件嵌套关系

通常一个应用会以一棵嵌套的组件树的形式来组织。



### 23 组件传递数据_Props

组件与组件之间不是完全独立的。

传递数据的解决方案是Props。

```vue
<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <p>
    {{ title }}
  </p>
  <myComponent :title="title" :age="age"/>
</template>

<script>
import myComponent from "./components/myComponents.vue"

export default {
  name: 'App',
  data() {
    return {
      title: '我是一个标题',
      age:20,
    }

  },

  components: {
    myComponent,
  }
}
</script>
```



```vue
<template>
    <h3>prop传递数据</h3>
    <p>{{ title }}</p>
    <p>{{ age }}</p>
</template>
<script>
export default {
    name: "myComponent",
    props: {
        title: {
            type: String,
            default: ''
        },
        age: {
            type: Number,
            default: 2
        }

    }
}
</script>
<style scoped></style>
```



>
>
>## 注意事项 ##
>
>`props`传递数据，只能从父级传递到子级，不能反其道而行。

>
>
>温馨提示：
>
>数据类型为数组或对象的时候，默认值需要返回工厂模式

## 自定义事件组件交互

```vue
template>
  <img alt="Vue logo" src="./assets/logo.png">

  <myComponent :title="title" :age="age" />
  <p>{{ message }}</p>
  <myComponent2 @onEvent="getDataHandle" />
</template>

<script>
import myComponent from "./components/myComponents.vue"
import myComponent2 from "./components/myComponents2.vue"

export default {
  name: 'App',
  data() {
    return {
      title: '我是一个标题',
      age: 20,
      message:""
    }
  },

  methods:
  {
    getDataHandle(data) {
      console.log(data);
      this.message = data;
    }
  },
  components: {
    // myComponent,
    myComponent2,
  }
}
</script>
```

```vue
<template>
    <h3>自定义事件传递数据</h3>
    <button @click="sendClickHandle">点击传递</button>
</template>
<script>
export default {
    name: "myComponent2",
    props: {

    },
    data(){
        return {
            message:'我是MyComponent数据',
        }
    },
    methods:{
        sendClickHandle(){
            //参数1：字符串
            //参数2：传递的数据
            this.$emit("onEvent",this.message)
        }
    }
}
</script>
```



## 组件生命周期

创建时：beforeCreate,created

渲染时：beforeMount,mounted

更新时：beforeUpdate，updated

卸载时：beforeUnmount，unmounted



## Axios网络请求

### 安装

```
npm install --save axios
```

### 引入

组件中引入：import axios from "axios"

post请求

>
>
>post请求的参数需要额外的处理
>
>安装依赖：npm install --save querystring
>
>转换格式：qs.stringify({})