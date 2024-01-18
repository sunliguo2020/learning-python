//寻找sliderInfo
sliderInfo = {
    openTime: Date.now() - Math.random()*1999,
    //鼠标开始点击
    startTime: Date.now() - 20,
    //鼠标抬起
    endTime: Date.now(),
    // userAgent: window.navigator.userAgent,
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    // uid: h("QN1"),
    uid:"0000ea80306c5af20058a1eb",
    track: [],
    acc: [],
    ori: [],
    deviceMotion: []
}

// 组成track
n = 1;
//开始点击时，x的坐标
clientX = 91

//开始点击时，y的坐标
clientY = 100

//时间戳随机数
i = Date.now() % 1e5
o = clientX.toFixed(2)
u = clientY.toFixed(2)
//滑动的距离
a = n.toFixed(2)
f = "".concat(i, ";").concat(o, ";").concat(u, ";").concat(a);
sliderInfo.track.push(f)
console.log(sliderInfo)

const CryptoJs = require("crypto-js")
d= CryptoJs
// 加密data d 为标准的js加密库
function encryption(sliderInfo) {
    var e = JSON.stringify(sliderInfo);
    return d.AES.encrypt(d.enc.Utf8.parse(e), d.enc.Utf8.parse("227V2xYeHTARSh1R"), {
        mode: d.mode.ECB,
        padding: d.pad.Pkcs7
    }).toString()
}


//查找cookie的值
function h(e) {
    if (u[e])
        return u[e];
    for (var t = e + "=", n = document.cookie.split(";"), r = 0; r < n.length; r++) {
        var i = n[r].trim();
        if (0 == i.indexOf(t)) {
            var s = i.substring(t.length, i.length);
            return u[e] = s,
                s
        }
    }
    return ""
}

// var e = JSON.stringify(sliderInfo);
// console.log(encryption(sliderInfo))

function func(){
    return encryption(sliderInfo)
}
