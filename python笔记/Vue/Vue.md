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

vuejs的使用官方提供了2中方式：

1、基于脚本导入使用，下载vue.js文件，通过script标签引入到html网页。

2、基于项目构建工具来使用，需要安装项目构建工具，自动构建程一个独立的项目。

目前官方推荐的项目构建项目：vue-CLI,vite

# el唯一根标签

```vue
 <!-- 定义唯一根元素div -->
    <div id="app">{{name}}</div>
    <script>
        var vm = new Vue({
            el: "#app", //通过el与div元素绑定
            data: {
                name: "Vue 实例创建成功!"
            }
        })
    </script>
```



```vue
    <!-- 定义唯一根元素div -->
    <div id="app">{{name}}</div>
    <script>
        var vm = new Vue({
            // el: "#app", //通过el与div元素绑定
            data: {
                name: "Vue 实例创建成功!"
            }
        })
        vm.$mount("#app")
    </script>
```



## data与el的2种写法

1、el有2种写法：

- new Vue时候配置el属性
- 先创建Vue实例，随后再通过vm.$mount('#app')指定el的值。

2、data有2种写法

- 对象式
- 函数式

以后学习组件时，data必须使用函数式

3、一个重要的原则：

由Vue管理的函数，一定不要写箭头函数，一旦写了箭头函数，this就不再式Vue实例了。

Vue中数据代理：通过vm对象来代理data对象中属性的操作（读/写）

Vue中数据代理的好处：更加方便的操作data中的数据

基本原理：通过Object.defineProperty()把data对象中所有属性添加到vm上。

为每一个添加到vm上的属性，都指定一个getter/setter。

在getter/setter内部去操作（读/写）data中对应的属性。

### 事件的基本使用：

- 使用v-on:xxx 或@xxx绑定事件，其中xxx是事件名
- 事件的回调需要配置在methods对象中，最终会在vm上
- methods中配置的函数，不要用箭头函数！否则this就不是vm了。
- methods中配置的函数，都是被Vue所管理的函数，this的指向是vm或组件实例对象；
- @click="demo" 和 @click=“demo($event)"效果一致，单后者可以传参数。

### Vue中的事件修饰符：

- prevent：阻止默认事件
- stop：阻止事件冒泡
- once：事件只触发一次
- capture：使用是哪的捕获模式
- self：只有event.target是当前操作的元素时才触发事件
- passive：事件的默认行为立即执行，无需等待事件回调执行完毕

## Vue中常用的按键别名：

- 回车=>enter
- 删除-》delete
- 退出-》esc
- 空格-》space
- 换行-》tab（特殊，必须配合keydown去使用）
- 上-》up
- 下-》down
- 左-》left
- 右-》right

Vue未提供别名的按键，可以使用按键原始的key值去绑定，但注意要转为kebab-case（短横线命名）

3、系统修饰键：ctrl、alt、shift、meta

- 配合keyup使用：按下修饰键的同时，再按下其他键，随后释放其他键，事件才被触发。
- 配合keydown使用：正常触发事件。

4、也可以使用keyCode去指定具体的按键（不推荐）

5、Vue.config.keyCodes.自定义键名 = 键码 可以去定制按键别名。

### 创建项目

#### 第一种：使用 vue cli Vue脚手架

第一步（仅第一次执行）：全局安装@vue/cli

```
npm install -g @vue/cli
```

 The recommended way to start a Vite-powered Vue project

第二步：切换到你要创建项目的目录，然后使用命令创建项目。

```
npm create vue@latest
```

第三步：启动项目

```
  cd vue-demo12
  npm install
  npm run serve
```

备注：

- 如果出现下载缓慢配置npm淘宝镜像：

  ```
  npm config set registry https://registry.npm.taobao.org
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

### Vue.js的M-V-VM思想

MVVM是Model-View-ViewModel的缩写，它是一种基于前端开发的架构模式，是一种代码分工思想来的 。

Model指代的是vue对象的data属性里面的数据。这里的数据要显示到页面中。

View指代的是vue中数据要显示的HTML页面，在vue中，也称之为“视图模板”。

ViewModel指代的是我们编写代码的vm对象了，他是vue.js的核心，负责连接View和Model，保证视图和数据的一致性，所以前面代码中，data里面的数据被显示中p标签中就是vm对象自动完成的。vm对象会时刻的监控View和Model的变化，并保持双方数据一致性！！！



## 5 Vue项目目录结构

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

## 6 模板语法

“插值”是指，使用{{变量}}的方法讲数据插入到HTML文档中。

插值分为文本插值、HTML插值等。

- 文本插值 {{变量}} v-text
- HTML插值 v-html

双花括号仅拥用输出文本内容，如果要输出html代码，则要使用v-html来输出。

v-html必须在html标签里面作为属性写出来，而且只能写在普通双标签中，单标签元素或者表单都不行。

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



# 2、常用指令

|         |                          |                       | 简写              |                      |
| ------- | ------------------------ | --------------------- | ----------------- | -------------------- |
| v-bind  | 单向绑定解析表达式       | v-bind:id="data"      | :id="data"        | 绑定id属性，值为data |
| v-model | 双向数据绑定             |                       |                   |                      |
| v-on    | 绑定事件监听             | v-on:click="showInfo" | @click="showInfo" | 事件监听             |
| v-for   | 遍历数组/对象/字符串     |                       |                   |                      |
| v-if    | 条件渲染                 |                       |                   |                      |
| v-else  | 条件渲染                 |                       |                   |                      |
| v-show  | 动态控制节点是否展示     |                       |                   |                      |
| v-text  | 向其所在节点渲染文本内容 |                       |                   |                      |
| v-html  |                          |                       |                   |                      |
| v-cloak |                          |                       |                   |                      |
| v-once  |                          |                       |                   |                      |



## 7 属性绑定 v-bind

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

## 10 通过key管理状态

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

## 11 事件处理

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

## 12 事件传参

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

## 13事件修饰符

Vue为v-on提供了事件修饰符，常用的有以下几个：

- .stop

- .prevent

- .once       # 限制事件绑定次数为1次

- .enter

- .number    #限制表单输入为数字

- .trim

  

#### 阻止默认事件 .prevent

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

# 18 侦听器 watch

监视属性watch:

1、当被监视的属性变化时，回调函数自动调用，进行相关操作

2、监视的属性必须存在，才能进行监视

3、监视的两种写法：

- new Vue时传入watch配置
- 通过vm.$watch监视

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

### computed和watch之间的区别

1、computed能完成的功能，watch都可以完成。

2、watch能完成的功能，computed不一定能完成。例如：watch可以进行异步操作。

两个重要的小原则：

1、所被Vue管理的函数，最好写成普通函数，这样this的指向才是vm或组件实例对象。

2、所有不被Vue所管理的函数（定时器的回调函数、ajax的回调函数等），最好写成箭头函数，这样this的指向才是vm或组件实例对象。



# 19表单输入绑定v-model

```vue
<input type="text" v-model="message">
```



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

# 20 模板引用 $ref

虽然Vue的声明性渲染模型为你抽象了大部分对DOM的直接操作，但在某些情况下，我们仍然需要直接访问的底层DOM元素。要实现这一点，我们可以使用特殊的ref attribute。

 模板引用也就是指向模板中一个 DOM 元素的 ref。 我们需要通过这个特殊的 ref attribute来实现模板引用：

```vue
<p ref="pElementRef" >
    hello
</p>
```

此元素将作为this.$refs.pElementRef暴露在 this.$refs上。然而，你只能在组件挂载之后访问它。

要在挂载之后执行代码，我们可以使用mouted选项：

```vue
export default{
	mounted(){
	//此时组件已经挂载
	}
}
```

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

### ref属性

- 被用来给元素或子组件注册引用信息（id的替代者）
- 应用在html标签上获取的是真实DOM元素，应用在组件标签上是组件实例对象（vc）
- 使用方式：
  - 打标识<h1 ref="xxx">....</h1> 或<school ref="xxx"></school>
  - 获取：this.$refs.xxx



# 21组件组成

关于组件名：

- 一个单词组成：

  - 首字母小写：school
  - 首字母大写：School

- 多个单词组成：

  - kebab-case命名：my-school
  - CamelCase命名：MySchool（需要Vue脚手架支持）

  备注：

  1、组件名尽可能回避HTML中已有的元素名称。

  2、可以使用name配置项值当嘴贱在开发者工具中呈现的名字。

  一个简写方式：

  const shcool = Vue.extend(options) 可简写为：const school = options

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

## 组件声明

```vue
    <script>
        //组件声明
        Vue.component("组件名",{
            data(){ //组件内部的数据

            },
            methods:{  //组件内部的操作方法

            },
            temlate:"", //组件的HTML代码
        });
    </script>
```



# 22 组件嵌套关系

通常一个应用会以一棵嵌套的组件树的形式来组织。

真正的Vue应用往往是有嵌套组件创建的。

父组件可以在模板中渲染另一个组件作为子组件。要使用子组件间，我们需要先导入它：

```vue
import ChildComp from './ChildComp.vue'

export default {
  components: {
    ChildComp
  }
}
```

我们还需要使用components选项注册组件。这里我们使用对象属性的简写形式在ChildComp键下中注册ChildComp组件。

然后我们就可以在模板中使用组件

```
<ChildComp/>
```

# 23 组件传递数据_Props

组件与组件之间不是完全独立的。

传递数据的解决方案是Props。 一个组件需要显式声明它所接受的 props，这样 Vue 才能知道外部传入的哪些是 props 。

子组件可以通过props从父组件接收动态数据。

首先，子组件中需要声明它所接收的props：

```vue
//在子组件中
export default{
//简单声明接收
props:['name','age','sex'],
//接收的同时对数据进行类型限制
props:{
name:String,
age:Number,
sex:String,
},
props:{
name:{
type:String,
required:true,
},
age:{
type:Number,
default:99,
},
sex:{
type:String,
require:true,
}
}

}
```

一旦声明，msg prop 就会暴露在this上，并可以在子组件的模板中使用。

父组件可以像声明HTML attributes一样传递props。若要传递动态值，也可以使用v-bind 语法：

```vue
<ChildComp :msg="greeting"/>
```

父组件：

```vue
<template>
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

子组件：

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

例二：

父组件

```vue
<template>
    <h1>Home页面</h1>
    <!--父组件要发送数据给子组件，通过组件的属性传递。属性名就是将来的变量名，
    传递数据如果时一个变量，则需要在左边加上冒号
    -->
    <Menu :htotal="total" title="来自父组件的数据"> </Menu>
    <button @click="total++">{{total}}</button>
</template>
<script>
import Menu from '../components/Menu.vue'

export default {
    name: "home",
    data(){
        return {
            total:0
        }
    },
    components: {
        Menu,
    }
}
</script>
<style scoped>
list-style-type:none;
</style>
```

子组件：

```vue
<template>
    <div>
        <p>来自父组件的数据：total= {{ htotal }}</p>
        <p>来自父组件的数据：title= {{ title }}</p>
        <ul>
            <li><a href="">首页</a></li>
            <li><a href="">商品</a></li>
            <li><a href="">论坛</a></li>
            <li><a href="">注册</a></li>
        </ul>
    </div>
</template>
<script>
export default {
    name: "Menu",
    //来自父组件的数据，全部通过props来接收，2种写法：json写法，数组写法
    // props:['htotal','title']
    props: {
        htotal: Number,   //来自父组件的数据
        title: String,
    }
}

</script>
<style scoped>
div {
    border: 1px solid red;
}

ul {
    list-style-type: none;
}

li {
    display: inline;
    margin-right: 10px;
}

li a {
    text-decoration: none;
}
</style>

```



>## 注意事项 ##
>
>`props`传递数据，只能从父级传递到子级，不能反其道而行。

>功能：让组件接收外部传过来的数据
>
>- 传递数据：<Demo name="xxx"/>
>- 接收数据：
>  - props:['name']
>  - props:{ name:Number}
>  - props:{name:{type:String,required:true}}
>
>备注：props是只读的，Vue底层会检测你对props的修改，如果进行了修改，就会发出警告，若业务需求确实需要修改，那么请复制props的内容到data中一份，然后去修改data中的数据。
>
>温馨提示：
>
>数据类型为数组或对象的时候，默认值需要返回工厂模式

# 自定义事件组件交互 $emit

子组件还可以向父组件触发事件：

```vue
export default{
// 声明触发的事件
emits:['response'],
created(){
//带参数触发
this.$emit("resonse","hello from child")
}
}
```

this.$emit()的第一个参数是事件的名称。其他所有参数都将传递给事件监听器。

父组件：

```vue
<template>
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

子组件：

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

# 局部注册组件

```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="js/vue-2.7.14.js"></script>
</head>
<body>
    <div id="app">
        父组件
{{name}}
        <Demo></Demo>
    </div>
    <script>
        //创建子组件
        const Demo = {
            template: `
            <div>
                <h1>{{msg}}</h1>
                <input type="text" v-model="msg"/>
                <input type="button" @click="showMsg" value="点我呀">
            </div>
                `,
            methods: {
                showMsg() {
                    alert(this.msg)
                }
            },
            data: function () {
                return {
                    msg: "哈哈哈哈"
                }
            }
        }
        var vm = new Vue({
            el: "#app",
            data: {
                name:'武沛齐'
            },
            components: {
                Demo,
            }
        })
    </script>
</body>

</html>
```

# 全局注册组件

```vue
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="js/vue-2.7.14.js"></script>

</head>

<body>
    <div id="app">
        父组件{{name}}
        <Demo></Demo>
    </div>
    <script>
        //创建子组件
        Vue.component('Demo',
            {
                template: `
<div>
    <h1>{{msg}}</h1>
    <input type="text" v-model="msg"/>
    <input type="button" @click="showMsg" value="点我呀">
</div>
    `,
                methods: {
                    showMsg() {
                        alert(this.msg)
                    }
                },
                data: function () {
                    return {
                        msg: "哈哈哈哈"
                    }
                }
            })

        var vm = new Vue({
            el: "#app",
            data: {
                name: '武沛齐'
            },
            components:{
            }
        })
    </script>
</body>

</html>
```



## 组件生命周期

创建时：beforeCreate,created

渲染时：beforeMount,mounted

更新时：beforeUpdate，updated

卸载时：beforeUnmount，unmounted



# Axios网络请求

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

