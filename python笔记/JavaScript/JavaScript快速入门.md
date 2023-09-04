JavaScript 组成

ECMScript DOM BOM

##### JavaScript书写位置

- 行内

```html
  <input type="button" value="按钮" onclick="alert('hello world!')">
```

- html script 标签内
- 外部js文件 src = ""

##### 注释

### DOM

1、获取元素

- 根据id

  ```js
  var para = document.getElementById('para');
  ```

  

- 根据标签名

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      <script>
          var divs = document.getElementsByTagName('div');
          console.log(divs)
      </script>
  </head>
  <body>
      <p>text1</p>
      <p>text2</p>
      <p>text3</p>
      <p>text4</p>
      <div>div1</div>
      <div>div2</div>
      <div>div3</div>
      <div>div4</div>
      <script>
          console.log(divs)
          var ps = document.getElementsByTagName('p');
          console.log(ps)
          //HTMLCollection html 元素组成的集合 伪数组
          //操作时需要按照操作数组的方法进行
          //遍历数组
          for(var i =0;i<=ps.length;i++){
              //输出每一项
              console.log(ps[i])
          }
          ps[0].style.backgroundColor='pink'
      </script>
  </body>
  </html>
  ```

  

  -元素对象内部获取元素

###常用事件监听方法

- 方法1：绑定HTML元素属性。
- 方法2：绑定DOM对象属性。

#### this

```javascript
        // 在事件函数内部有一个this，指向事件源。
        //区分一下不同函数内部 this的指向
        //普通函数  ->window对象
        //构造函数 ->生成的实例对象
        //对象的方法 ->对象本身
        //事件函数 ->事件源
```

