day01 微信小程序

### 问题

- 什么是微信小程序？
  - 移动互联时代 手机
  - 手机软件在手机上中安装很多软件
  - 腾讯 微信+N小程序
  - 阿里 支付宝+N小程序
- 为什么要做小程序？
- 如何开发小程序？
  - 小程序  学习微信开发的语言（前端 html css js vue.js)
    - 微信开发者工具
  - API：restful接口（python+Django+drf框架）
    - pycharm

### 环境的搭建

python环境：

​	虚拟环境

			-	django
			-	drf

微信小程序

## 3、开发小程序

#### 全局配置：

app.json

```python

{
  "pages": [
    "pages/index/index",
    "pages/logs/index"
  ],
  "window": {
    "navigationBarTitleText": "Demo"
  },
  "tabBar": {
    "list": [{
      "pagePath": "pages/index/index",
      "text": "首页"
    }, {
      "pagePath": "pages/logs/index",
      "text": "日志"
    }]
  },
    "tabBar": {
    "selectedColor": "#CDSCSC",
    "list": [
      {
        "pagePath": "pages/index/index",
        "text": "首页",
        "iconPath": "",
        "selectedIconPath": "static/bg.jpg"
      },
      {
        "pagePath": "pages/logs/logs",
        "text": "日志"
      },
      {
        "pagePath": "pages/bind/bind",
        "text": "获取信息"
      },
      {
        "pagePath": "pages/login/login",
        "text": "登录"
      }
    ]
  }
}
```



### 3.2 组件

##### 3.2.1 text 文本信息  

类似于span

##### 3.2.2 view

类似于div 标签

##### 3.2.3 image

图片



## 4、flex布局

一种非常方便的布局方向

在容器中4个样式：

```css
display:flex;   使用flex布局
flex-direction:row;   主轴方向 row/column
justify-content:space-around;  元素在主轴方向上的排列方式  flex-start/flex-end/space-around/space-between
align-items:center;				元素在副轴方向上的排列方式
        
```

6、获取图片

```python
<text>pages/publish/publish.wxml</text>
<view bindtap="uploadImage">请上传图片</view>
<view class="container">

<image wx:for="{{imageList}}" wx:key="item" src="{{item}}"></image>

</view>

```





js

```javascript
data: {
    imageList: ['/static/bg.jpg', '/static/default.png']
  },
  uploadImage: function () {
    var that = this
    wx.chooseImage(
      {
        count: 9,
        sizeType: ['original', 'compressed'],
        sourceType: ['album', 'camera'],
        success: function (res) {
          console.log(res)
          //设置imageList，页面上图片自动修改
          // that.setData({
          //   imageList: res.tempFilePaths
          // });
          //默认图片+选择图片
          that.setData(
            {
              imageList:that.data.imageList.concat(res.tempFilePaths)
            }
          )

        },
        fail: function (res) { },
        complete: function () {

        }

      }

    );
  },
```

## 总结

- 标签（组件）

  - text
  - view
  - image
  - navigator  跳转到其他页面（默认只能跳转到非tabbar页面）
  - button   按钮  （特殊：建议在获取用户信息时）

- 事件

  - bindtap 

    - ```python
      <view bindtap='func'></view>
      
      <view bindtap="func" data-xx='123'></view>
      
      func:function(e){
          e.currentTarget.dataset
      }
      ```

    - 

  api

  - navigateTo
  - openSetting
  - getUserinfo
  - wx.chooseLocation
  - wx.chooseImage

  

- 数据绑定

- for指令

  注意：setData+that

- 

#### 1、数据绑定

- 基本绑定
- for循环

双向绑定

