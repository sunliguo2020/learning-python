# chap01 jQuery基础

## 1.1 使用jQuery

```html
<!doctype html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport"
        content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script src="./jquery/jquery-3.7.1.min.js"></script>
    <script>
    //在这里用户就可以使用jQuery编程了。

    </script>
</head>

<body>

</body>

</html>
```

在jQuery代码中，$是jQuery的别名，如$()等效于jQuery()。jQuery()函数是jQuery库文件的接口函数，所有jQuery操作都必须从该接口函数切入。jQuery()函数相当于页面初始化事件处理函数，当页面加载完成，会执行jQuery()函数包含的函数。

如果使用jQuery操作DOM文档，则必须确保在DOM载入完毕后开始执行。

```javascript
$(document).ready(funciton(){
//javascript代码或者jQuery代码
});
```

进一步简化，直接使用$()方法来表示$(document).ready()方法

```javascript

$(function(){
    //javascript代码或者jQuery代码
});
```

# chap02 使用选择器

## 2.1jQuey选择器基础

jQuery选择器返回值是一个伪数组对象，如果没有匹配，则会返回一个空的伪数组对象。

jQuery选择器分为基本选择器、结构选择器、过滤选择器、属性选择器以及表单选择器。

## 2.2基本选择器

基本选择器主要包括5种类型：ID选择器，类型选择器，类选择器，通配选择器，分组选择器。

jQuery的选择器有三种类型

1. ID选择器 $.("#id") ，意思就是根据HTML标签的ID来寻找，id代表标签id
2. 类选择器 $(".class") ,意思就是根据类名来寻找，class代表类名
3. 标签选择器 $("tagname") ，意思就是根据标签名来寻找，tag那么代表标签名，如input、select等

寻找到你想要的标签后(如果你用的是id选择器)，jQuery会提供一系列操作的方法，如$("#id").text("要更改的值") 代表修改标签文本，$("#id").val("要更改的值") 代表修改标签value值，如果括号内不带参数的话，便是获取该值。

## 2.3结构选择器

#### 2.3.1层级选择器

层级选择器能够根据元素之间的结构关系进行匹配操作，主要包含选择器、子选择器、相邻选择器和兄弟选择器。

| 选择器              | 说明 |
| ------------------- | ---- |
| ancestor descendant |      |
| parent>child        |      |
| prev+next           |      |
| prev~siblings       |      |





# chap03 使用过滤器

# chap04 操作DOM

## 4.1 创建节点

### 4.1.1 创建元素



#### jQuery语法

基本语法：

```jquery
$(selector).action()

```

实例：

```javascript
$(this).hide()
$('p').hide()
$('p.test').hide()
$('#test').hide()
```

#### 文档就绪事件

 在 DOM 加载完成后才可以对 DOM 进行操作 

```javascript
$(document).ready(function(){
    //开始写jQuery代码
});
```

简洁写法：

```javascript
$(function(){
    
});
```

#### jQuery选择器

jQuery中所有的选择器都是以美元符号开头：$().

##### 元素选择器

```javascript
$('p')
```

##### #id选择器

```javascript
$("#test")
```

##### .class选择器

```javascript
$('.test')
```

类型选择器

```
$("div")
```

结构选择器

过滤选择器

属性选择器

表单选择器

## 更多实例

| 语法                     | 描述                                                    |
| :----------------------- | :------------------------------------------------------ |
| $("*")                   | 选取所有元素                                            |
| $(this)                  | 选取当前 HTML 元素                                      |
| $("p.intro")             | 选取 class 为 intro 的 <p> 元素                         |
| $("p:first")             | 选取第一个 <p> 元素                                     |
| $("ul li:first")         | 选取第一个 <ul> 元素的第一个 <li> 元素                  |
| $("ul li:first-child")   | 选取每个 <ul> 元素的第一个 <li> 元素                    |
| $("[href]")              | 选取带有 href 属性的元素                                |
| $("a[target='_blank']")  | 选取所有 target 属性值等于 "_blank" 的 <a> 元素         |
| $("a[target!='_blank']") | 选取所有 target 属性值不等于 "_blank" 的 <a> 元素       |
| $(":button")             | 选取所有 type="button" 的 <input> 元素 和 <button> 元素 |
| $("tr:even")             | 选取偶数位置的 <tr> 元素                                |
| $("tr:odd")              | 选取奇数位置的 <tr> 元素                                |

```javascript

$("#id", ".class")  复合选择器
$("div p span")       层级选择器 //div下的p元素中的span元素
$("div>p")            父子选择器 //div下的所有p元素
$("div+p")            相邻元素选择器 //div后面的p元素(仅一个p)
$("div~p")            兄弟选择器  //div后面的所有p元素(同级别)
$(".p:last")          类选择器 加 过滤选择器  第一个和最后一个（first 或者 last）
$("#mytable td:odd")      层级选择 加 过滤选择器 奇偶（odd 或者 even）
$("div p:eq(2)")    索引选择器 div下的第三个p元素（索引是从0开始）
$("a[href='www.baidu.com']")  属性选择器
$("p:contains(test)")        // 内容过滤选择器，包含text内容的p元素
$(":emtyp")        //内容过滤选择器，所有空标签（不包含子标签和内容的标签）parent 相反
$(":hidden")       //所有隐藏元素 visible 
$("input:enabled") //选取所有启用的表单元素
$(":disabled")     //所有不可用的元素
$("input:checked") //获取所有选中的复选框单选按钮等
$("select option:selected") //获取选中的选项元素
```

# chap05 事件处理

## 5.1 jQuery事件基础

jQuery提供了四种事件绑定方式：bind(),live(),delegate(),on()。

### 1、bind() 为匹配元素添加一个或多个事件处理器。

```javascript
bind(event,data,function)
//event 添加到元素的一个或者多个事件
//data,可选，设计需要传递的参数
//function：必须，当绑定事件发生时，需要执行的函数
```

```javascript
  <script>
        $(function () {
            /*添加单个事件处理*/
            $(".btn-test").bind("click", function () {
                console.log('bind')
                $(".container").slideToggle(); //显示隐藏div
            });
        });

    </script>
```

```html

<!doctype html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport"
        content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script src="./jquery/jquery-3.7.1.min.js"></script>
    <script>
        $(function () {
            /*添加单个事件处理*/
            $(".btn-test").bind("click", function () {
                console.log('bind')
                $(".container").slideToggle(); //显示隐藏div
            });
            /*添加多个事件处理*/
            $(".btn-test").bind("mouseout click",function(){ //空格相隔方式
                $(".container").slideToggle(); // 显示隐藏div
            });
            $(".btn-test").bind({   //大括号替代方式
                "mouseout":function(){
                    alert("这是mouseout事件！")
                },
                "click":function(){
                    $(".countainer").slideToggle();
                }
            });
            /*删除事件处理*/
            $(".btn-test").unbind("click");

        });

    </script>
</head>

<body>
    <input type="button" value="按钮" class="btn-test">
    <div class="container">
        <img src="images/1.jpg" height="200" alt="">
    </div>
</body>

</html> 
```

2.live()为当前或未来的匹配元素添加一个或多个事件处理程序。

```
live(event,data,function)
```

3、delegate()为指定的元素，以及被选元素的子元素，添加一个或多个事件处理程序，并规定当这些事件发生时运行的函数。

```
delegate(childSelector,event,data,function)
```

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="jquery/jquery-3.7.1.min.js"></script>
    <title>Document</title>
    <script>
        $(function () {

            $("ul").delegate("li", "click", function () {
                alert(this.innerHTML);
            });

            var i = 4;
            $("#btn").click(function () {
                $("ul").append("<li>列表项目" + i++ + "</li>");
            })

        });
    </script>
</head>

<body>
    <button id="btn">添加列表项目</button>
    <ul id="list">
        
        <li>列表项目1</li>
        <li>列表项目2</li>
        <li>列表项目3</li>
    </ul>
</body>

</html>
```



常见 DOM 事件：

| 鼠标事件                                                     | 键盘事件                                                     | 表单事件                                                  | 文档/窗口事件                                             |
| :----------------------------------------------------------- | :----------------------------------------------------------- | :-------------------------------------------------------- | :-------------------------------------------------------- |
| [click](https://www.runoob.com/jquery/event-click.html)      | [keypress](https://www.runoob.com/jquery/event-keypress.html) | [submit](https://www.runoob.com/jquery/event-submit.html) | [load](https://www.runoob.com/jquery/event-load.html)     |
| [dblclick](https://www.runoob.com/jquery/event-dblclick.html) | [keydown](https://www.runoob.com/jquery/event-keydown.html)  | [change](https://www.runoob.com/jquery/event-change.html) | [resize](https://www.runoob.com/jquery/event-resize.html) |
| [mouseenter](https://www.runoob.com/jquery/event-mouseenter.html) | [keyup](https://www.runoob.com/jquery/event-keyup.html)      | [focus](https://www.runoob.com/jquery/event-focus.html)   | [scroll](https://www.runoob.com/jquery/event-scroll.html) |
| [mouseleave](https://www.runoob.com/jquery/event-mouseleave.html) |                                                              | [blur](https://www.runoob.com/jquery/event-blur.html)     | [unload](https://www.runoob.com/jquery/event-unload.html) |
| [hover](https://www.runoob.com/jquery/event-hover.html)      |                                                              |                                                           |                                                           |

jQuery事件方法语法

页面中的一个点击事件

```javascript
$('p').click();
```

定义了点击后触发事件

```javasc
$("p").click(function(){
//动作触发后执行的代码!!
});
```

### 5.1.6 触发事件

```
tigger(type,[data])
```

[示例10]

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="jquery/jquery-3.7.1.min.js"></script>
    <script>
        $(function(){
            $("li").click(function(){
                alert($(this).text());
            });
            $("li").mouseover(function(){
                $(this).trigger("click"); //调用tigger方法直接触发click操作
            });
        })
    </script>
</head>
<body>
    <ul id="list">
        <li>空山新雨后，天气晚来秋。</li>
        <li>明月松间照，清泉石上流。</li>
        <li>竹暄归浣女，莲动下鱼舟。</li>
        <li>随意春芳歇，王孙自可留。</li>
    </ul>
</body>
</html>

```

## 5.2 实战案例

#### 5.2.1 切换事件

【示例12】

```html
<script>
        $(function(){
            $("button").click(mySlow               
            );
        })
        function mySlow(){
            $("ul#list").toggle("slow")
        }
    </script>
    <button>控制</button>
    <ul id="list">
        <li>空山新雨后，天气晚来秋。</li>
        <li>明月松间照，清泉石上流。</li>
        <li>竹暄归浣女，莲动下鱼舟。</li>
        <li>随意春芳歇，王孙自可留。</li>
    </ul>
```

#### 5.2.2 使用悬停事件

【示例13】

```javascript
<script>
        $(function(){
            $("input").hover(
                function(){
                    this.value = "鼠标经过";
                },
                function(){
                    this.value = "鼠标已经移出";
                }
            );
        })
    </script>
    <input type="button" value="鼠标切换实践">
```



【示例14】



jQuery获取内容和属性

## 获得内容 - text()、html() 以及 val()

三个简单实用的用于 DOM 操作的 jQuery 方法：

- **text()** - 设置或返回所选元素的文本内容
- **html()** - 设置或返回所选元素的内容（包括 HTML 标签）
- **val()** - 设置或返回表单字段的值

## 获取属性 - attr()



# jQuery - 设置内容和属性

------

## 设置内容 - text()、html() 以及 val()

我们将使用前一章中的三个相同的方法来设置内容：

- text() - 设置或返回所选元素的文本内容
- html() - 设置或返回所选元素的内容（包括 HTML 标记）
- val() - 设置或返回表单字段的值

# chap06 使用Ajax

## 6.1jQuery Ajax基础

### 6.1.1 认识Ajax

## 6.2 实战案例

### 6.2.1 使用GET请求

```javascript
jQuery.get(url,[data],[callback],[type])
```

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="jquery/jquery-3.7.1.min.js"></script>
    <script>
        $(function () {
            $('input').click(function () {
                //请求当前url
                $.get('', {
                    name: 'css8',
                    password: '12345',
                    age: 1
                }, function (data) {
                    alert(data);
                });
            });
        });
    </script>
</head>

<body>
<input type="button" value="jQuery 实现异步请求">
</body>

</html>
```



### 6.2.2 使用POST请求

```
jQuery.post(url,[data],[callback],[type])
```

### 6.2.3 使用ajax()请求

```javascript
$.ajax({name:value, name:value, ... })
```

