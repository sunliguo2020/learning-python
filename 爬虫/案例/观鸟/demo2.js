const CryptoJS = require('crypto-js')


const key = '3583ec0257e2f4c8195eec7410ff1619';
const iv = 'd93c0d5ec6352f20'
var BIRDREPORT_APIJS_decode = function (a) {
    var b = CryptoJS.enc.Utf8.parse(key);
    var c = CryptoJS.enc.Utf8.parse(iv);
    var d = CryptoJS.AES.decrypt(a, b, {
        iv: c,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    return d.toString(CryptoJS.enc.Utf8)
}

var parseData = function (res) {
    var decode_str = BIRDREPORT_APIJS_decode(res.data);
    var results = JSON.parse(decode_str);
    return {
        "code": res.code,
        "count": res.count,
        "data": results
    };
}

res = {
    data: 'Ak6JdWsSxM8kH0rpmVhCfQ=='
}

console.log(parseData(res))