

var t2 = '2.0'

var tr = {
    "zse93": "101_3_3.0",
    "dc0": "\"AGAS71rcFxWPTgKbwOWJ5lOixIy7shJ89DA=|1655158521\"",
    "xZst81": null
}


var tu = tr.dc0
var t4 = function (tt) {
    var te = new URL(tt, "https://www.zhihu.com");
    return "" + te.pathname + te.search
}

var t6 = function (tt) {
    return null == tt ? "" : "string" == typeof tt ? tt : "undefined" != typeof URLSearchParams && (0,
        tc._)(tt, URLSearchParams) ? tt.toString() : tm()(tt) ? JSON.stringify(tt) : t3(tt) ? String(tt) : ""
}

var t8 = function (tt, te) {
    return void 0 === te && (te = 4096),
    !!tt && t7(tt) <= te
}

var ta = '101_3_3.0'


const CryptoJS = require("crypto-js");


const ty = (aaa) => {
    return CryptoJS.MD5(aaa).toString();
}


/*
*
*
* ta = tr.zse93   #版本号
tu = tr.dc0     #d_c0这个cookie的值
tc = tr.xZst81  #null
tl = t5(tt)     #tl评论url
tf = t3(te)     #""
*
*
* */

//ed 函数的返回值 signature
function ed(tt, te, tr, ti) {
    var ta = tr.zse93
        , tu = tr.dc0
        , tc = tr.xZst81
        , tf = t4(tt)
        , td = t6(te)
        , tp = [ta, tf, tu, t8(td) && td, tc].filter(Boolean).join("+");
    return {
        source: tp,
        // (0,tJ(ti).encrypt)  ƒ (tt){return __g._encrypt(encodeURIComponent(tt))}
        // signature: (0,tJ(ti).encrypt)(ty(tp))
        signature: encrypt_b(ty(tp))
    }
}

// tC = td.xZst81 || tp.get("x-zst-81")

tC = null

// tf = {
//     "headers": {
//         "x-requested-with": "fetch",
//         "x-zst-81": "3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpTQ6nxERFZ8TY0-4Lm-h3_tufIwJS8gcxTgJS_AuPZNcXCTwxI78YxEM20s4PGDwN8gGcYAupMWufIeQuK7AFpS6O1vukyQ_R0rRnsyukMGvxBEqeCiRnxEL2ZZrxmDucmqhPXnXFMTAoTF6RhRuLPFHHmWgwyThwGOGFxrhLy-upLr0pqtBOBJwFM6hYKfGHKtqOpfUpMmwpCVwSTv4NsNGFLvCNOJcCm8vemnCH9JrO1rQoBb9OsoBXBsMXB-bpCOqSsUu2LlvXqivrMoMYm2G21E9NBgBOyOBHpB9CmqC2mtbeL9cn_wBx1GQOL_D9_fUF9CqfzwDOBJ6H0gDwp3bOCJCH8XU30AGSxAUS06h2GxUxMTCOYL9cLFJO8kH31_gFV1qoqXGwGeHw9HgC8oHtOAgHOVJC_c4SYy9wC87O9BJuYAqgKwhLCGBLC"
//     },
//     "credentials": "include"
// }


tf = tD(ti, ep)


let mycookie = {
    // cookie: 'SESSIONID=KWTqqpxR7cCzmRy2Rr1mOfC4Y1PpE9Bq07VtxH8YAnI; JOID=V1EWC0vVmb9XGhqeTtig4weUa4lQ-rCXfDw1t2bztpZ_MTyxZ0AdRT8THJ9NxGl1iVVnmmZMZEaZnAGRfGp8dTI=; osd=Ul8RA0PQl7hfEh-QSdCo5gmTY4FV9LefdDk7sG77s5h4OTS0aUcVTTodG5dFwWdygV1ilGFEbEOXmwmZeWR7fTo=; __snaker__id=dYwBey4J0WjOTTHJ; _zap=3ac25dde-c84d-4d65-bf3b-c9a16dadabfd; d_c0="AGAS71rcFxWPTgKbwOWJ5lOixIy7shJ89DA=|1655158521"; _xsrf=18c24249-a564-44c0-8f7c-591b1b5f8879; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1709559246,1710670146,1710772602,1710851457; gdxidpyhxdE=86GTGZPw2QP045cXHEhk9N%5CMXGtLsyqXlwhEDPHb4%2BBuCo0fcUBY0TwUzRQyIhZq%5CdUTzIuQxAyJUHrbRIv6ZM28TwK78nicsOvjutrLLXAsBpAEdLVhdnE7orepNxZge6Ike9oGNOBGxNNuKkcrReAI8wetxbxP01eDbfr%2FUG2RcHUh%3A1710854275482; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1710853391; KLBRSID=f48cb29c5180c5b0d91ded2e70103232|1710853407|1710851454'
    cookie: 'd_c0="AGAS71rcFxWPTgKbwOWJ5lOixIy7shJ89DA=|1655158521";'
}
t9 = RegExp("d_c0=([^;]+)")
er = function () {
    var tt = t9.exec(mycookie.cookie);
    return tt && tt[1]
}
var tA = undefined
var tE = er()
var tb = '101_3_3.0'
//te:url
// var te = '/api/v4/members/d53b74e344eed04badd1167d0fd5fe83?include=allow_message%2Cis_followed%2Cis_following%2Cis_org%2Cis_blocking%2Cemployments%2Canswer_count%2Cfollower_count%2Carticles_count%2Cgender%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics'

var te = 'http://www.zhihu.com/api/v4/comment_v5/questions/616391683/root_comment?order_by=score&limit=20&offset='

var tT = ed(te, tf.body, {
    zse93: tb,
    dc0: tE,
    xZst81: tC
}, tA)

var xzse = t2 + '_' + tO

console.log(xzse)