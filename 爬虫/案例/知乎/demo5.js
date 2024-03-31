// 基本逻辑 md5(tp),然后再使用加密函数加密
// function ed(tt,te,tr,ti)
//tt url
//te : undefined
//tr:{
//     "zse93": "101_3_3.0",
//     "dc0": "\"AGAS71rcFxWPTgKbwOWJ5lOixIy7shJ89DA=|1655158521\"",
//     "xZst81": null
// }
//ti: undefined
//构造tp
// ta :tr.zse93 固定
//tf=t4(tt) ->可能是清理或格式化URL，或者从给定的URL片段中提取出相对于特定基础URL的路径和查询字符串
//tu tr.dc0 cookie中d_c0
//
// tp = [ta,tf,tu,t8(td)&&td,tc]
//[ta, tf, tu, t8(td) && td, tc].filter(Boolean) =>
// [
//     "101_3_3.0",
//     "/api/v4/answers/3157488975/relationship?desktop=true",
//     "\"AGAS71rcFxWPTgKbwOWJ5lOixIy7shJ89DA=|1655158521\""
// ]
function get_tp(tt, tu) {

    var ta = "101_3_3.0";

// tt 为url
//     var tt = '/api/v4/search/preset_words'
//tu 为cookie中的d_c0的值
//     var tu = 'ADDSD-j4lRePTsK721fRFrWpxQLGjfijbjo=|1697981461'

    function t4(tt) {
        var te = new URL(tt, "https://www.zhihu.com");
        return "" + te.pathname + te.search
    }

    var tf = t4(tt);
    console.log("tf:URL", tf)
    // tp = [ta, tf, tu, false, null].filter(Boolean).join("+");
    // console.log('[ta,tf,tu]',[ta,tf,tu])
    let tp = [ta, tf, tu].filter(Boolean).join("+");
    // console.log('tp.length',tp.length)
    return tp
}

//md5
const CryptoJS = require("crypto-js");

const md5 = (aaa) => {
    return CryptoJS.MD5(aaa).toString();
}
// console.log(md5('1'))

// 加密函数
const entcrypt_v3 = require('./load')

// console.log(entcrypt_v3(md5(tp)))

function x96(tt, tu) {
    return '2.0_' + entcrypt_v3(md5(get_tp(tt, tu)))
}

tt = 'https://www.zhihu.com/api/v4/comment_v5/questions/616391683/root_comment?order_by=score&limit=20&offset=457158625_10644363034_0'
tu = 'ADDSD-j4lRePTsK721fRFrWpxQLGjfijbjo=|1697981461'

tp = get_tp(tt, tu)
console.log('tp\n', tp, tp.length)
console.log("md5(tp)",md5(tp))


console.log('x96', x96(tt, tu))

