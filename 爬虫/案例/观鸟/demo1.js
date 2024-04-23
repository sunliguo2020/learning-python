var JSEncrypt = require('node-jsencrypt')
// import JSEncrypt from 'node-jsencrypt';
// import MD5 from "./MD5.js"
// var MD5 = require('MD5')
const MD5 = require('./md5'); // 注意路径前的 './' 表示当前目录


function getUuid() {
    var s = [];
    var a = "0123456789abcdef";
    for (var i = 0; i < 32; i++) {
        s[i] = a.substr(Math.floor(Math.random() * 0x10), 1)
    }
    s[14] = "4";
    s[19] = a.substr((s[19] & 0x3) | 0x8, 1);
    s[8] = s[13] = s[18] = s[23];
    var b = s.join("");
    return b
}

function sort_ASCII(a) {
    var b = new Array();
    var c = 0;
    for (var i in a) {
        b[c] = i;
        c++
    }
    var d = b.sort();
    var e = {};
    for (var i in d) {
        e[d[i]] = a[d[i]]
    }
    return e
}

function url2json(a) {
    var b = /^[^\?]+\?([\w\W]+)$/, reg_para = /([^&=]+)=([\w\W]*?)(&|$|#)/g, arr_url = b.exec(a), ret = {};
    if (arr_url && arr_url[1]) {
        var c = arr_url[1], result;
        while ((result = reg_para.exec(c)) != null) {
            ret[result[1]] = result[2]
        }
    }
    return ret
}

function dataTojson(a) {
    var b = [];
    var c = {};
    b = a.split('&');
    for (var i = 0; i < b.length; i++) {
        if (b[i].indexOf('=') != -1) {
            var d = b[i].split('=');
            if (d.length == 2) {
                c[d[0]] = d[1]
            } else {
                c[d[0]] = ""
            }
        } else {
            c[b[i]] = ''
        }
    }
    return c
}


const serialize = function (a) {
    var b = [];
    for (var p in a) if (a.hasOwnProperty(p) && a[p]) {
        b.push(encodeURIComponent(p) + '=' + encodeURIComponent(a[p]))
    }
    return b.join('&')
};
var paramPublicKey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCvxXa98E1uWXnBzXkS2yHUfnBM6n3PCwLdfIox03T91joBvjtoDqiQ5x3tTOfpHs3LtiqMMEafls6b0YWtgB1dse1W5m+FpeusVkCOkQxB4SZDH6tuerIknnmB/Hsq5wgEkIvO5Pff9biig6AyoAkdWpSek/1/B7zYIepYY0lxKQIDAQAB";
var encrypt = new JSEncrypt();
encrypt.setPublicKey(paramPublicKey);

function get_headers( b) {
    console.log(typeof b)
    //时间戳后三位为0
    var c = Date.parse(new Date());
    //生成UUID
    var d = getUuid();
    var e = JSON.stringify(sort_ASCII(dataTojson(b || '{}')));
    b = encrypt.encryptUnicodeLong(e);
    var f = MD5(e + d + c);
    // a.setRequestHeader("timestamp", c);
    // a.setRequestHeader('requestId', d);
    // a.setRequestHeader('sign', f)
    // console.log('c:', c)
    // console.log('d:', d)
    // console.log('e:', e)
    // console.log(e + d + c)
    // console.log(b)
    return {
        "header": {
            timestamp: c+'',
            requestId: d,
            sign: f
        },
        "data": b
    }

}

// console.log(get_headers( {'data': '123=2&dsf=232'}))
console.log(get_headers( '123=2&dsf=232'))