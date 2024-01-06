const u = "fanyideskweb"
    , d = "webfanyi"
    , m = "client,mysticTime,product"
    , p = "1.0.0"
    , g = "web"
    , b = "fanyi.web"
    , A = 1
    , h = 1
    , f = 1
    , v = "wifi"
    , O = 0;

var crypto = require('crypto');
var md5 = crypto.createHash('md5');

// var result = md5.update('a').digest('hex');

function j(e) {
    // return c.a.createHash("md5").update(e.toString()).digest("hex")
    return md5.update(e.toString()).digest("hex")
}


function k(e, t) {
    return j(`client=${u}&mysticTime=${e}&product=${d}&key=${t}`)
}


// e 时间戳
const e = (new Date).getTime();
// sign = k(e, 'fsdsogkndfokasodnaso')

function fn(ee){
    return k(ee,'fsdsogkndfokasodnaso')
}

// console.log(fn('1704295619456'))