CryptoJS = require('crypto-js')
var D = parseInt((new Date).getTime() / 1e3);
var d = function () {
    var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : 5;
    return Math.random().toString(36).substring(3, 3 + e)
}
var U = {
    "App-Ver": "",
    "Os-Ver": "",
    "Device-Ver": "",
    "Imei": "",
    "Access-Token": "",
    "Timestemp": D,
    "NonceStr": "".concat(D).concat(Object(d)()),
    "App-Id": "4ac490420ac63db4",
    "Device-Os": "web"
};
// console.log(U);


var f = function (t) {
    var e = "";
    return Object.keys(t).sort().forEach((function (n) {
            e += n + ("object" === typeof t[n] ? JSON.stringify(t[n], (function (t, e) {
                    return "number" == typeof e && (e = String(e)),
                        e
                }
            )).replace(/\//g, "\\/") : t[n])
        }
    )),
        e
}

var d = function (data) {
    // return o.a.MD5(data).toString()
    return CryptoJS.MD5(data).toString()
}

l = {
    key: CryptoJS.enc.Utf8.parse("fX@VyCQVvpdj8RCa"),
    iv: CryptoJS.enc.Utf8.parse(function (t) {
        for (var e = "", i = 0; i < t.length - 1; i += 2) {
            var n = parseInt(t[i] + "" + t[i + 1], 16);
            e += String.fromCharCode(n)
        }
        return e
    }("00000000000000000000000000000000"))
}
var v = function (data) {
    return function (data) {
        return CryptoJS.AES.encrypt(data, l.key, {
            iv: l.iv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        }).toString()
    }(data)
}
var f_a = function (t) {
    var data = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {};

    var e = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : "a75846eb4ac490420ac63db46d2a03bf"
    var n = e + f(data) + f(t) + e;
    return n = d(n),
        n = v(n)
}

//汉字助手
function fn(username, password) {
    var M = {
        username: username,
        password: password,
        code: '',
        hdn_refer: 'https://zt.epwk.com/'
    }
    var third = "a75846eb4ac490420ac63db46d2a03bf"
//U.Signature = Object(f.a)(U, M, l.j ? l.g : l.c);
    U.Signature = f_a(U, M, third);

    return U

}
