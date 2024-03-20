!function (e) {
    var t = {};

    //加载器，所有的模块都是从这个函数加载执行
    function n(r) {
        if (t[r])
            return tr[r].exports;
        var o = t[r] = {
            i: r,
            l: !1,
            exports: {}
        };

        return e[r].call(o.exports, o, o.exports, n),
            o.l = !0,
            o.exports
    }

    n(0)
}([
    function () {
        console.log('12345');
    },
    function () {
        console.log('模块2')
    }
])