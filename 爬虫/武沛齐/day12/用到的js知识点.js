//concat()用法
i = 'i';
o = '0';
u = 'u';
a = 'a'
// 合并数组
// 数组的concat()方法是用来合并2个或更多个数组的。
//这个方法不会改变原数组，而是返回一个新数组。

f = "".concat(i, ";").concat(o, ";").concat(u, ";").concat(a);
console.log(f)

//三元表达式

"GET" == e.type ? (r = o(e.data),
    t.open("GET", e.url + "?" + r, !0),
    t.withCredentials = !0,
    t.send(null)) : "POST" === e.type && (t.open("POST", e.url, !0),
    t.withCredentials = !0,
    t.send(JSON.stringify(r))),
e.time && (n = setTimeout(function () {
    t.abort(),
    e.error && e.err({
        message: "超时"
    })
}, e.time))