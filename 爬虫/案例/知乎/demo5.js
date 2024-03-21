// 基本逻辑 md5(tp),然后再使用加密函数加密
//构造tp
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
    console.log("tf", tf)
    tp = [ta, tf, tu, false, null].filter(Boolean).join("+");

    return tp
}

//md5
const CryptoJS = require("crypto-js");


const md5 = (aaa) => {
    return CryptoJS.MD5(aaa).toString();
}


// 加密函数
const entcrypt_v3 = require('./加载器')

// console.log(entcrypt_v3(md5(tp)))

function x93(tt, tu) {
    return '2.0_' + entcrypt_v3(md5(get_tp(tt, tu)))
}

tt = 'https://www.zhihu.com/api/v4/comment_v5/questions/616391683/root_comment?limit=10&offset=457158625_10644363034_0&order_by=score'
console.log(x93(tt, 'ADDSD-j4lRePTsK721fRFrWpxQLGjfijbjo=|1697981461'))
