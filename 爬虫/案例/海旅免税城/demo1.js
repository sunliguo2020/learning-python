const jsdom = require("jsdom");
const {JSDOM} = jsdom;
const $ = require("jquery")(new JSDOM(`<!DOCTYPE html><p>Hello world</p>`).window);
window = global;

/*! For license information please see LICENSES */
(window.webpackJsonp = window.webpackJsonp || []).push([
    [67],
    {
    0: function(e, t, n) {
        "use strict";
        n.d(t, "k", (function() {
            return y
        }
        )),
        n.d(t, "m", (function() {
            return w
        }
        )),
        n.d(t, "l", (function() {
            return k
        }
        )),
        n.d(t, "e", (function() {
            return _
        }
        )),
        n.d(t, "b", (function() {
            return O
        }
        )),
        n.d(t, "s", (function() {
            return j
        }
        )),
        n.d(t, "g", (function() {
            return P
        }
        )),
        n.d(t, "h", (function() {
            return z
        }
        )),
        n.d(t, "d", (function() {
            return S
        }
        )),
        n.d(t, "r", (function() {
            return T
        }
        )),
        n.d(t, "j", (function() {
            return E
        }
        )),
        n.d(t, "t", (function() {
            return C
        }
        )),
        n.d(t, "o", (function() {
            return I
        }
        )),
        n.d(t, "q", (function() {
            return A
        }
        )),
        n.d(t, "f", (function() {
            return U
        }
        )),
        n.d(t, "c", (function() {
            return D
        }
        )),
        n.d(t, "i", (function() {
            return N
        }
        )),
        n.d(t, "p", (function() {
            return L
        }
        )),
        n.d(t, "a", (function() {
            return J
        }
        )),
        n.d(t, "v", (function() {
            return X
        }
        )),
        n.d(t, "n", (function() {
            return W
        }
        )),
        n.d(t, "u", (function() {
            return Y
        }
        ));
        n(75),
        n(65),
        n(37),
        n(66),
        n(76),
        n(88),
        n(267);
        var o = n(27)
          , r = (n(38),
        n(39),
        n(97),
        n(111),
        n(175),
        n(52),
        n(21),
        n(4))
          , l = (n(67),
        n(53),
        n(36),
        n(32))
          , c = n(25)
          , d = (n(31),
        n(16),
        n(270),
        n(2))
          , f = n(40);
        function m(object, e) {
            var t = Object.keys(object);
            if (Object.getOwnPropertySymbols) {
                var n = Object.getOwnPropertySymbols(object);
                e && (n = n.filter((function(e) {
                    return Object.getOwnPropertyDescriptor(object, e).enumerable
                }
                ))),
                t.push.apply(t, n)
            }
            return t
        }
        function h(e) {
            for (var i = 1; i < arguments.length; i++) {
                var source = null != arguments[i] ? arguments[i] : {};
                i % 2 ? m(Object(source), !0).forEach((function(t) {
                    Object(l.a)(e, t, source[t])
                }
                )) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(source)) : m(Object(source)).forEach((function(t) {
                    Object.defineProperty(e, t, Object.getOwnPropertyDescriptor(source, t))
                }
                ))
            }
            return e
        }
        function v(e, t) {
            var n;
            if ("undefined" == typeof Symbol || null == e[Symbol.iterator]) {
                if (Array.isArray(e) || (n = function(e, t) {
                    if (!e)
                        return;
                    if ("string" == typeof e)
                        return x(e, t);
                    var n = Object.prototype.toString.call(e).slice(8, -1);
                    "Object" === n && e.constructor && (n = e.constructor.name);
                    if ("Map" === n || "Set" === n)
                        return Array.from(e);
                    if ("Arguments" === n || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n))
                        return x(e, t)
                }(e)) || t && e && "number" == typeof e.length) {
                    n && (e = n);
                    var i = 0
                      , o = function() {};
                    return {
                        s: o,
                        n: function() {
                            return i >= e.length ? {
                                done: !0
                            } : {
                                done: !1,
                                value: e[i++]
                            }
                        },
                        e: function(e) {
                            throw e
                        },
                        f: o
                    }
                }
                throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
            }
            var r, l = !0, c = !1;
            return {
                s: function() {
                    n = e[Symbol.iterator]()
                },
                n: function() {
                    var e = n.next();
                    return l = e.done,
                    e
                },
                e: function(e) {
                    c = !0,
                    r = e
                },
                f: function() {
                    try {
                        l || null == n.return || n.return()
                    } finally {
                        if (c)
                            throw r
                    }
                }
            }
        }
        function x(e, t) {
            (null == t || t > e.length) && (t = e.length);
            for (var i = 0, n = new Array(t); i < t; i++)
                n[i] = e[i];
            return n
        }
        function y(e) {
            d.default.config.errorHandler && d.default.config.errorHandler(e)
        }
        function w(e) {
            return e.then((function(e) {
                return e.default || e
            }
            ))
        }
        function k(e) {
            return e.$options && "function" == typeof e.$options.fetch && !e.$options.fetch.length
        }
        function _(e) {
            var t, n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : [], o = e.$children || [], r = v(o);
            try {
                for (r.s(); !(t = r.n()).done; ) {
                    var l = t.value;
                    l.$fetch ? n.push(l) : l.$children && _(l, n)
                }
            } catch (e) {
                r.e(e)
            } finally {
                r.f()
            }
            return n
        }
        function O(e, t) {
            if (t || !e.options.__hasNuxtData) {
                var n = e.options._originDataFn || e.options.data || function() {
                    return {}
                }
                ;
                e.options._originDataFn = n,
                e.options.data = function() {
                    var data = n.call(this, this);
                    return this.$ssrContext && (t = this.$ssrContext.asyncData[e.cid]),
                    h(h({}, data), t)
                }
                ,
                e.options.__hasNuxtData = !0,
                e._Ctor && e._Ctor.options && (e._Ctor.options.data = e.options.data)
            }
        }
        function j(e) {
            return e.options && e._Ctor === e || (e.options ? (e._Ctor = e,
            e.extendOptions = e.options) : (e = d.default.extend(e))._Ctor = e,
            !e.options.name && e.options.__file && (e.options.name = e.options.__file)),
            e
        }
        function P(e) {
            var t = arguments.length > 1 && void 0 !== arguments[1] && arguments[1]
              , n = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : "components";
            return Array.prototype.concat.apply([], e.matched.map((function(e, o) {
                return Object.keys(e[n]).map((function(r) {
                    return t && t.push(o),
                    e[n][r]
                }
                ))
            }
            )))
        }
        function z(e) {
            var t = arguments.length > 1 && void 0 !== arguments[1] && arguments[1];
            return P(e, t, "instances")
        }
        function S(e, t) {
            return Array.prototype.concat.apply([], e.matched.map((function(e, n) {
                return Object.keys(e.components).reduce((function(o, r) {
                    return e.components[r] ? o.push(t(e.components[r], e.instances[r], e, r, n)) : delete e.components[r],
                    o
                }
                ), [])
            }
            )))
        }
        function T(e, t) {
            return Promise.all(S(e, function() {
                var e = Object(r.a)(regeneratorRuntime.mark((function e(n, o, r, l) {
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                if ("function" != typeof n || n.options) {
                                    e.next = 4;
                                    break
                                }
                                return e.next = 3,
                                n();
                            case 3:
                                n = e.sent;
                            case 4:
                                return r.components[l] = n = j(n),
                                e.abrupt("return", "function" == typeof t ? t(n, o, r, l) : n);
                            case 6:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                )));
                return function(t, n, o, r) {
                    return e.apply(this, arguments)
                }
            }()))
        }
        function E(e) {
            return $.apply(this, arguments)
        }
        function $() {
            return ($ = Object(r.a)(regeneratorRuntime.mark((function e(t) {
                return regeneratorRuntime.wrap((function(e) {
                    for (; ; )
                        switch (e.prev = e.next) {
                        case 0:
                            if (t) {
                                e.next = 2;
                                break
                            }
                            return e.abrupt("return");
                        case 2:
                            return e.next = 4,
                            T(t);
                        case 4:
                            return e.abrupt("return", h(h({}, t), {}, {
                                meta: P(t).map((function(e, n) {
                                    return h(h({}, e.options.meta), (t.matched[n] || {}).meta)
                                }
                                ))
                            }));
                        case 5:
                        case "end":
                            return e.stop()
                        }
                }
                ), e)
            }
            )))).apply(this, arguments)
        }
        function C(e, t) {
            return R.apply(this, arguments)
        }
        function R() {
            return (R = Object(r.a)(regeneratorRuntime.mark((function e(t, n) {
                var r, l, d, m;
                return regeneratorRuntime.wrap((function(e) {
                    for (; ; )
                        switch (e.prev = e.next) {
                        case 0:
                            return t.context || (t.context = {
                                isStatic: !1,
                                isDev: !1,
                                isHMR: !1,
                                app: t,
                                store: t.store,
                                payload: n.payload,
                                error: n.error,
                                base: t.router.options.base,
                                env: {}
                            },
                            n.req && (t.context.req = n.req),
                            n.res && (t.context.res = n.res),
                            n.ssrContext && (t.context.ssrContext = n.ssrContext),
                            t.context.redirect = function(e, path, n) {
                                if (e) {
                                    t.context._redirected = !0;
                                    var r = Object(o.a)(path);
                                    if ("number" == typeof e || "undefined" !== r && "object" !== r || (n = path || {},
                                    path = e,
                                    r = Object(o.a)(path),
                                    e = 302),
                                    "object" === r && (path = t.router.resolve(path).route.fullPath),
                                    !/(^[.]{1,2}\/)|(^\/(?!\/))/.test(path))
                                        throw path = Object(f.d)(path, n),
                                        window.location.replace(path),
                                        new Error("ERR_REDIRECT");
                                    t.context.next({
                                        path: path,
                                        query: n,
                                        status: e
                                    })
                                }
                            }
                            ,
                            t.context.nuxtState = window.__NUXT__),
                            e.next = 3,
                            Promise.all([E(n.route), E(n.from)]);
                        case 3:
                            r = e.sent,
                            l = Object(c.a)(r, 2),
                            d = l[0],
                            m = l[1],
                            n.route && (t.context.route = d),
                            n.from && (t.context.from = m),
                            t.context.next = n.next,
                            t.context._redirected = !1,
                            t.context._errored = !1,
                            t.context.isHMR = !1,
                            t.context.params = t.context.route.params || {},
                            t.context.query = t.context.route.query || {};
                        case 15:
                        case "end":
                            return e.stop()
                        }
                }
                ), e)
            }
            )))).apply(this, arguments)
        }
        function I(e, t) {
            return !e.length || t._redirected || t._errored ? Promise.resolve() : A(e[0], t).then((function() {
                return I(e.slice(1), t)
            }
            ))
        }
        function A(e, t) {
            var n;
            return (n = 2 === e.length ? new Promise((function(n) {
                e(t, (function(e, data) {
                    e && t.error(e),
                    n(data = data || {})
                }
                ))
            }
            )) : e(t)) && n instanceof Promise && "function" == typeof n.then ? n : Promise.resolve(n)
        }
        function U(base, e) {
            if ("hash" === e)
                return window.location.hash.replace(/^#\//, "");
            base = decodeURI(base).slice(0, -1);
            var path = decodeURI(window.location.pathname);
            base && path.startsWith(base) && (path = path.slice(base.length));
            var t = (path || "/") + window.location.search + window.location.hash;
            return Object(f.c)(t)
        }
        function D(e, t) {
            return function(e, t) {
                for (var n = new Array(e.length), i = 0; i < e.length; i++)
                    "object" === Object(o.a)(e[i]) && (n[i] = new RegExp("^(?:" + e[i].pattern + ")$",G(t)));
                return function(t, o) {
                    for (var path = "", data = t || {}, r = (o || {}).pretty ? B : encodeURIComponent, l = 0; l < e.length; l++) {
                        var c = e[l];
                        if ("string" != typeof c) {
                            var d = data[c.name || "pathMatch"]
                              , f = void 0;
                            if (null == d) {
                                if (c.optional) {
                                    c.partial && (path += c.prefix);
                                    continue
                                }
                                throw new TypeError('Expected "' + c.name + '" to be defined')
                            }
                            if (Array.isArray(d)) {
                                if (!c.repeat)
                                    throw new TypeError('Expected "' + c.name + '" to not repeat, but received `' + JSON.stringify(d) + "`");
                                if (0 === d.length) {
                                    if (c.optional)
                                        continue;
                                    throw new TypeError('Expected "' + c.name + '" to not be empty')
                                }
                                for (var m = 0; m < d.length; m++) {
                                    if (f = r(d[m]),
                                    !n[l].test(f))
                                        throw new TypeError('Expected all "' + c.name + '" to match "' + c.pattern + '", but received `' + JSON.stringify(f) + "`");
                                    path += (0 === m ? c.prefix : c.delimiter) + f
                                }
                            } else {
                                if (f = c.asterisk ? F(d) : r(d),
                                !n[l].test(f))
                                    throw new TypeError('Expected "' + c.name + '" to match "' + c.pattern + '", but received "' + f + '"');
                                path += c.prefix + f
                            }
                        } else
                            path += c
                    }
                    return path
                }
            }(function(e, t) {
                var n, o = [], r = 0, l = 0, path = "", c = t && t.delimiter || "/";
                for (; null != (n = M.exec(e)); ) {
                    var d = n[0]
                      , f = n[1]
                      , m = n.index;
                    if (path += e.slice(l, m),
                    l = m + d.length,
                    f)
                        path += f[1];
                    else {
                        var h = e[l]
                          , v = n[2]
                          , x = n[3]
                          , y = n[4]
                          , w = n[5]
                          , k = n[6]
                          , _ = n[7];
                        path && (o.push(path),
                        path = "");
                        var O = null != v && null != h && h !== v
                          , j = "+" === k || "*" === k
                          , P = "?" === k || "*" === k
                          , z = n[2] || c
                          , pattern = y || w;
                        o.push({
                            name: x || r++,
                            prefix: v || "",
                            delimiter: z,
                            optional: P,
                            repeat: j,
                            partial: O,
                            asterisk: Boolean(_),
                            pattern: pattern ? V(pattern) : _ ? ".*" : "[^" + H(z) + "]+?"
                        })
                    }
                }
                l < e.length && (path += e.substr(l));
                path && o.push(path);
                return o
            }(e, t), t)
        }
        function N(e, t) {
            var n = {}
              , o = h(h({}, e), t);
            for (var r in o)
                String(e[r]) !== String(t[r]) && (n[r] = !0);
            return n
        }
        function L(e) {
            var t;
            if (e.message || "string" == typeof e)
                t = e.message || e;
            else
                try {
                    t = JSON.stringify(e, null, 2)
                } catch (n) {
                    t = "[".concat(e.constructor.name, "]")
                }
            return h(h({}, e), {}, {
                message: t,
                statusCode: e.statusCode || e.status || e.response && e.response.status || 500
            })
        }
        window.onNuxtReadyCbs = [],
        window.onNuxtReady = function(e) {
            window.onNuxtReadyCbs.push(e)
        }
        ;
        var M = new RegExp(["(\\\\.)", "([\\/.])?(?:(?:\\:(\\w+)(?:\\(((?:\\\\.|[^\\\\()])+)\\))?|\\(((?:\\\\.|[^\\\\()])+)\\))([+*?])?|(\\*))"].join("|"),"g");
        function B(e, t) {
            var n = t ? /[?#]/g : /[/?#]/g;
            return encodeURI(e).replace(n, (function(e) {
                return "%" + e.charCodeAt(0).toString(16).toUpperCase()
            }
            ))
        }
        function F(e) {
            return B(e, !0)
        }
        function H(e) {
            return e.replace(/([.+*?=^!:${}()[\]|/\\])/g, "\\$1")
        }
        function V(e) {
            return e.replace(/([=!:$/()])/g, "\\$1")
        }
        function G(e) {
            return e && e.sensitive ? "" : "i"
        }
        function J(e, t, n) {
            e.$options[t] || (e.$options[t] = []),
            e.$options[t].includes(n) || e.$options[t].push(n)
        }
        var X = f.b
          , W = (f.e,
        f.a);
        function Y(e) {
            try {
                window.history.scrollRestoration = e
            } catch (e) {}
        }
    },
    1: function(e, t, n) {
        "use strict";
        n(21);
        var o = n(4)
          , r = (n(97),
        n(34))
          , l = n.n(r)
          , c = n(185)
          , d = n.n(c)
          , f = n(6)
          , m = n(12)
          , h = (n(81),
        n(174),
        n(3))
          , v = navigator.userAgent.indexOf("Opera") > -1
          , x = navigator.userAgent.indexOf("compatible") > -1 && navigator.userAgent.indexOf("MSIE") > -1 && !v
          , y = !1;
        x && (new RegExp("MSIE (\\d+\\.\\d+);").test(navigator.userAgent),
        9 === parseFloat(RegExp.$1) && (y = !0));
        var w = "production" === document.getElementById("ipt_env_api").value;
        l.a.defaults.baseURL = w ? f.a.defaultService.baseURL : f.a.defaultService.baseURL_TEST,
        l.a.defaults.timeout = f.a.defaultService.timeout,
        l.a.defaults.headers = f.a.defaultService.headers;
        var k = document.getElementById("ipt_env_mid").value || null
          , _ = document.getElementById("ipt_env_sid").value || null
          , O = document.getElementById("ipt_env_pid").value || null
          , j = document.getElementById("ipt_env_plid").value || null
          , P = document.getElementById("sflsource").value || null;
        l.a.interceptors.request.use((function(e) {
            return e.silent || window.__EVENT_BUS__.$emit(m.b, !0),
            e
        }
        ), (function(e) {
            return window.__EVENT_BUS__.$emit(m.b, !1),
            window.__EVENT_BUS__.$emit("globalMessage", "网络异常……"),
            e
        }
        )),
        l.a.interceptors.response.use((function(e) {
            var t = e.config && e.config.silent || !1;
            return t || window.__EVENT_BUS__.$emit(m.b, !1),
            40300 === e.data.code ? window.__EVENT_BUS__.$emit(m.e, !t) : 1e4 === e.data.code ? window.__EVENT_BUS__.$emit(m.c, e.data.data.message) : t || 200 !== e.data.code && e.data.message && (100005 == e.data.code || window.__EVENT_BUS__.$emit("globalMessage", e.data.message)),
            {
                status: 200,
                data: e.data
            }
        }
        ), (function(e) {
            if (console.error(e),
            !e.config.silent) {
                var t = "服务器错误……";
                "Network Error" === e.message ? t = "网络异常……" : e.message.indexOf("timeout") > -1 && (t = "请求超时……"),
                window.__EVENT_BUS__.$emit(m.b, !1),
                window.__EVENT_BUS__.$emit("globalMessage", t)
            }
            return e
        }
        )),
        t.a = {
            post: function(e, data, t, n) {
                return Object(o.a)(regeneratorRuntime.mark((function o() {
                    var r, c;
                    return regeneratorRuntime.wrap((function(o) {
                        for (; ; )
                            switch (o.prev = o.next) {
                            case 0:
                                return (data = data || {}).platformId = f.a.platFormId,
                                data.shop_id = f.a.shopId,
                                null !== k && (data.mid = k),
                                null !== _ && (data.sid = _),
                                null !== O && (data.pid = O),
                                null !== P && (data.sflsource = P),
                                null !== j && (data.platformId = j),
                                data.token || (data.token = h.a.fetchFromCookie("UserToken")),
                                data.ident = (new Date).getTime(),
                                window.$nuxt && window.$nuxt.$store && window.$nuxt.$store.state.User.ident && (data.ident = window.$nuxt.$store.state.User.ident),
                                data = f.a.setSignData(data),
                                r = {
                                    method: "post",
                                    url: e,
                                    data: d.a.stringify(data),
                                    headers: {}
                                },
                                !n || "application/json;charset=UTF-8" !== n.headers["Content-Type"] && "multipart/form-data" !== n.headers["Content-Type"] || (r.data = data),
                                n && (n.baseURL && n.baseURL_TEST && (r.baseURL = w ? n.baseURL : n.baseURL_TEST),
                                n.timeout && (r.timeout = n.timeout),
                                n.headers && (r.headers = n.headers)),
                                y && (r.baseURL = ""),
                                t && (r.silent = !0),
                                o.next = 19,
                                l()(r);
                            case 19:
                                return 200 == (c = o.sent).status && 40010 == c.data.code && window.__EVENT_BUS__.$emit(m.g),
                                o.abrupt("return", c);
                            case 22:
                            case "end":
                                return o.stop()
                            }
                    }
                    ), o)
                }
                )))()
            },
            get: function(e, t, n, r) {
                return Object(o.a)(regeneratorRuntime.mark((function o() {
                    var c, d;
                    return regeneratorRuntime.wrap((function(o) {
                        for (; ; )
                            switch (o.prev = o.next) {
                            case 0:
                                return (t = t || {}).platformId = f.a.platFormId,
                                t.shop_id = f.a.shopId,
                                t.t = (new Date).getTime(),
                                null !== k && (t.mid = k),
                                null !== _ && (t.sid = _),
                                null !== O && (t.pid = O),
                                null !== P && (t.sflsource = P),
                                null !== j && (t.platformId = j),
                                t.token || (t.token = h.a.fetchFromCookie("UserToken")),
                                t.ident = (new Date).getTime(),
                                window.$nuxt && window.$nuxt.$store && window.$nuxt.$store.state.User.ident && (t.ident = window.$nuxt.$store.state.User.ident),
                                t = f.a.setSignData(t),
                                c = {
                                    method: "get",
                                    url: e,
                                    params: t,
                                    headers: {}
                                },
                                n && (c.silent = !0),
                                r && (c.baseURL = w ? r.baseURL : r.baseURL_TEST,
                                c.timeout = r.timeout,
                                c.headers = r.headers),
                                o.next = 18,
                                l()(c);
                            case 18:
                                return 200 == (d = o.sent).status && 40010 == d.data.code && window.__EVENT_BUS__.$emit(m.g),
                                o.abrupt("return", d);
                            case 21:
                            case "end":
                                return o.stop()
                            }
                    }
                    ), o)
                }
                )))()
            }
        }
    },
    100: function(e, t, n) {
        "use strict";
        n(31),
        n(65),
        n(37),
        n(67),
        n(66),
        n(36),
        n(38),
        n(39),
        n(16),
        n(76),
        n(88);
        var o = n(2);
        function r(e, t) {
            var n;
            if ("undefined" == typeof Symbol || null == e[Symbol.iterator]) {
                if (Array.isArray(e) || (n = function(e, t) {
                    if (!e)
                        return;
                    if ("string" == typeof e)
                        return l(e, t);
                    var n = Object.prototype.toString.call(e).slice(8, -1);
                    "Object" === n && e.constructor && (n = e.constructor.name);
                    if ("Map" === n || "Set" === n)
                        return Array.from(e);
                    if ("Arguments" === n || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n))
                        return l(e, t)
                }(e)) || t && e && "number" == typeof e.length) {
                    n && (e = n);
                    var i = 0
                      , o = function() {};
                    return {
                        s: o,
                        n: function() {
                            return i >= e.length ? {
                                done: !0
                            } : {
                                done: !1,
                                value: e[i++]
                            }
                        },
                        e: function(e) {
                            throw e
                        },
                        f: o
                    }
                }
                throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
            }
            var r, c = !0, d = !1;
            return {
                s: function() {
                    n = e[Symbol.iterator]()
                },
                n: function() {
                    var e = n.next();
                    return c = e.done,
                    e
                },
                e: function(e) {
                    d = !0,
                    r = e
                },
                f: function() {
                    try {
                        c || null == n.return || n.return()
                    } finally {
                        if (d)
                            throw r
                    }
                }
            }
        }
        function l(e, t) {
            (null == t || t > e.length) && (t = e.length);
            for (var i = 0, n = new Array(t); i < t; i++)
                n[i] = e[i];
            return n
        }
        var c = window.requestIdleCallback || function(e) {
            var t = Date.now();
            return setTimeout((function() {
                e({
                    didTimeout: !1,
                    timeRemaining: function() {
                        return Math.max(0, 50 - (Date.now() - t))
                    }
                })
            }
            ), 1)
        }
          , d = window.cancelIdleCallback || function(e) {
            clearTimeout(e)
        }
          , f = window.IntersectionObserver && new window.IntersectionObserver((function(e) {
            e.forEach((function(e) {
                var t = e.intersectionRatio
                  , link = e.target;
                t <= 0 || !link.__prefetch || link.__prefetch()
            }
            ))
        }
        ));
        t.a = {
            name: "NuxtLink",
            extends: o.default.component("RouterLink"),
            props: {
                prefetch: {
                    type: Boolean,
                    default: !0
                },
                noPrefetch: {
                    type: Boolean,
                    default: !1
                }
            },
            mounted: function() {
                this.prefetch && !this.noPrefetch && (this.handleId = c(this.observe, {
                    timeout: 2e3
                }))
            },
            beforeDestroy: function() {
                d(this.handleId),
                this.__observed && (f.unobserve(this.$el),
                delete this.$el.__prefetch)
            },
            methods: {
                observe: function() {
                    f && this.shouldPrefetch() && (this.$el.__prefetch = this.prefetchLink.bind(this),
                    f.observe(this.$el),
                    this.__observed = !0)
                },
                shouldPrefetch: function() {
                    return this.getPrefetchComponents().length > 0
                },
                canPrefetch: function() {
                    var e = navigator.connection;
                    return !(this.$nuxt.isOffline || e && ((e.effectiveType || "").includes("2g") || e.saveData))
                },
                getPrefetchComponents: function() {
                    return this.$router.resolve(this.to, this.$route, this.append).resolved.matched.map((function(e) {
                        return e.components.default
                    }
                    )).filter((function(e) {
                        return "function" == typeof e && !e.options && !e.__prefetched
                    }
                    ))
                },
                prefetchLink: function() {
                    if (this.canPrefetch()) {
                        f.unobserve(this.$el);
                        var e, t = r(this.getPrefetchComponents());
                        try {
                            for (t.s(); !(e = t.n()).done; ) {
                                var n = e.value
                                  , o = n();
                                o instanceof Promise && o.catch((function() {}
                                )),
                                n.__prefetched = !0
                            }
                        } catch (e) {
                            t.e(e)
                        } finally {
                            t.f()
                        }
                    }
                }
            }
        }
    },
    12: function(e, t, n) {
        "use strict";
        n.d(t, "b", (function() {
            return o
        }
        )),
        n.d(t, "e", (function() {
            return r
        }
        )),
        n.d(t, "f", (function() {
            return l
        }
        )),
        n.d(t, "d", (function() {
            return c
        }
        )),
        n.d(t, "c", (function() {
            return d
        }
        )),
        n.d(t, "a", (function() {
            return f
        }
        )),
        n.d(t, "g", (function() {
            return m
        }
        ));
        var o = "loadingSet"
          , r = "tokenError"
          , l = "userReady"
          , c = "switchGolbalTabBar"
          , d = "EVENT_STOP_SERVICE"
          , f = 16
          , m = "EVENT_VERIFY_JUMP"
    },
    132: function(e, t, n) {
        "use strict";
        var o = {};
        o.checkLogin = n(235),
        o.checkLogin = o.checkLogin.default || o.checkLogin,
        o.isagent = n(358),
        o.isagent = o.isagent.default || o.isagent,
        o.stat = n(265),
        o.stat = o.stat.default || o.stat,
        t.a = o
    },
    135: function(e, t, n) {
        "use strict";
        n.d(t, "c", (function() {
            return o
        }
        )),
        n.d(t, "d", (function() {
            return r
        }
        )),
        n.d(t, "e", (function() {
            return l
        }
        )),
        n.d(t, "a", (function() {
            return c
        }
        )),
        n.d(t, "b", (function() {
            return d
        }
        ));
        n(52),
        n(68),
        n(87),
        n(3);
        function o(e) {
            e = e || encodeURIComponent(window.location.href),
            window.location.href = "/passport/login?backURL=".concat(e)
        }
        function r(e, t) {
            e.$store.state.env.mpJd ? jd.miniProgram.navigateTo({
                url: "/pages/login/login?url=".concat(encodeURIComponent(window.location.href))
            }) : e.$store.state.env.mpBd ? swan.webView.navigateTo({
                url: "/pages/login/login?url=".concat(encodeURIComponent(window.location.href))
            }) : e.$store.state.env.mpAlipay ? my.navigateTo({
                url: "/pages/login/login?url=".concat(encodeURIComponent(window.location.href))
            }) : e.$store.state.env.app ? uni.navigateTo({
                url: "/pages/login/applogin"
            }) : e.$store.state.env.mpWechat ? uni.navigateTo({
                url: "/pages/login/login?url=".concat(encodeURIComponent(window.location.href))
            }) : o(t)
        }
        function l(e, t) {
            if (t && !(t.length < 1))
                if ("/" != t) {
                    var n = t.match(/\/specialcomplex\/([0-9A-Za-z]+)$/);
                    if (n)
                        e.$store.state.env.mpAlipay ? my.navigateTo({
                            url: "/pages/web/web?url=".concat(n[0])
                        }) : e.$store.state.env.mpJd ? jd.miniProgram.navigateTo({
                            url: "/pages/web/web?url=".concat(n[0])
                        }) : e.$store.state.env.mpBd ? swan.webView.navigateTo({
                            url: "/pages/web/web?url=".concat(n[0])
                        }) : e.$store.state.env.mpWechat ? uni.navigateTo({
                            url: "/pages/web/web?url=".concat(n[0])
                        }) : uni.getEnv((function(o) {
                            o.plus && 1 == o.plus ? uni.navigateTo({
                                url: "/pages/web/web?url=".concat(n[0])
                            }) : e.$router.push(t)
                        }
                        ));
                    else if (n = t.match(/\/special\?id=([0-9A-Za-z]+)$/))
                        e.$store.state.env.mpAlipay ? my.navigateTo({
                            url: "/pages/marketing/special/index?code=".concat(n[1])
                        }) : e.$store.state.env.mpJd ? jd.miniProgram.navigateTo({
                            url: "/pages/marketing/special/special?code=".concat(n[1])
                        }) : e.$store.state.env.mpBd ? swan.webView.navigateTo({
                            url: "/pages/marketing/special/special?code=".concat(n[1])
                        }) : e.$store.state.env.mpWechat ? uni.navigateTo({
                            url: "/pages/marketing/special/index?code=".concat(n[1])
                        }) : uni.getEnv((function(o) {
                            o.plus && 1 == o.plus ? uni.navigateTo({
                                url: "/pages/marketing/special/index?code=".concat(n[1])
                            }) : e.$router.push(t)
                        }
                        ));
                    else if (n = t.match(/\/brandhall(.+)$/)) {
                        var o = encodeURIComponent(t);
                        e.$store.state.env.mpAlipay ? my.navigateTo({
                            url: "/pages/web/web?url=".concat(o)
                        }) : e.$store.state.env.mpJd ? jd.miniProgram.navigateTo({
                            url: "/pages/web/web?url=".concat(o)
                        }) : e.$store.state.env.mpBd ? swan.webView.navigateTo({
                            url: "/pages/web/web?url=".concat(o)
                        }) : e.$store.state.env.mpWechat ? uni.navigateTo({
                            url: "/pages/web/web?url=".concat(o)
                        }) : uni.getEnv((function(n) {
                            n.plus && 1 == n.plus ? uni.navigateTo({
                                url: "/pages/web/web?url=".concat(o)
                            }) : e.$router.push(t)
                        }
                        ))
                    } else if (n = t.match(/\/getcoupon\?(.+)$/)) {
                        var r = decodeURI(n[1]);
                        e.$store.state.env.mpAlipay ? my.navigateTo({
                            url: "/pages/marketing/getcoupon/index?".concat(r)
                        }) : e.$store.state.env.mpJd ? jd.miniProgram.navigateTo({
                            url: "/pages/marketing/getcoupon/getcoupon?".concat(r)
                        }) : e.$store.state.env.mpBd ? swan.webView.navigateTo({
                            url: "/pages/marketing/getcoupon/getcoupon?".concat(r)
                        }) : e.$store.state.env.mpWechat ? uni.navigateTo({
                            url: "/pages/marketing/getcoupon/index?".concat(r)
                        }) : uni.getEnv((function(n) {
                            n.plus && 1 == n.plus ? uni.navigateTo({
                                url: "/pages/marketing/getcoupon/index?".concat(r)
                            }) : e.$router.push(t)
                        }
                        ))
                    } else if (n = t.match(/\/activity(.+)$/)) {
                        var l = encodeURIComponent(t);
                        e.$store.state.env.mpAlipay ? my.navigateTo({
                            url: "/pages/web/web?url=".concat(l)
                        }) : e.$store.state.env.mpJd ? jd.miniProgram.navigateTo({
                            url: "pages/web/web?url=".concat(l)
                        }) : e.$store.state.env.mpBd ? swan.webView.navigateTo({
                            url: "pages/web/web?url=".concat(l)
                        }) : e.$store.state.env.mpWechat ? uni.navigateTo({
                            url: "/pages/web/web?url=".concat(l)
                        }) : uni.getEnv((function(n) {
                            n.plus && 1 == n.plus ? uni.navigateTo({
                                url: "/pages/web/web?url=".concat(l)
                            }) : e.$router.push(t)
                        }
                        ))
                    } else if (n = t.match(/\/help(.+)$/)) {
                        var c = encodeURIComponent(t);
                        e.$store.state.env.mpAlipay ? my.navigateTo({
                            url: "/pages/web/web?url=".concat(c)
                        }) : e.$store.state.env.mpJd ? jd.miniProgram.navigateTo({
                            url: "pages/web/web?url=".concat(c)
                        }) : e.$store.state.env.mpBd ? swan.webView.navigateTo({
                            url: "pages/web/web?url=".concat(c)
                        }) : e.$store.state.env.mpWechat ? uni.navigateTo({
                            url: "/pages/web/web?url=".concat(c)
                        }) : uni.getEnv((function(n) {
                            n.plus && 1 == n.plus ? uni.navigateTo({
                                url: "/pages/web/web?url=".concat(c)
                            }) : e.$router.push(t)
                        }
                        ))
                    } else if (n = t.match(/\/cate(.+)$/))
                        e.$store.state.env.mpAlipay ? my.navigateTo({
                            url: "/pages/cate/cate".concat(n[1])
                        }) : e.$store.state.env.mpJd ? jd.miniProgram.navigateTo({
                            url: "/pages/tabs/cate/cate".concat(n[1])
                        }) : e.$store.state.env.mpBd ? swan.webView.navigateTo({
                            url: "/pages/tabs/cate/cate".concat(n[1])
                        }) : e.$store.state.env.mpWechat ? uni.navigateTo({
                            url: "/pages/cate/cate".concat(n[1])
                        }) : uni.getEnv((function(o) {
                            o.plus && 1 == o.plus ? uni.navigateTo({
                                url: "/pages/cate/cate".concat(n[1])
                            }) : e.$router.push(t)
                        }
                        ));
                    else if (n = t.match(/\/goods\?(.+)$/)) {
                        var d = decodeURI(n[1]);
                        e.$store.state.env.mpAlipay ? my.navigateTo({
                            url: "/pages/goods/goods?".concat(d)
                        }) : e.$store.state.env.mpJd ? jd.miniProgram.navigateTo({
                            url: "/pages/goods/goods?".concat(d)
                        }) : e.$store.state.env.mpBd ? swan.webView.navigateTo({
                            url: "/pages/goods/goods?".concat(d)
                        }) : e.$store.state.env.mpWechat ? uni.navigateTo({
                            url: "/pages/goods/goods?".concat(d)
                        }) : uni.getEnv((function(n) {
                            if (n.plus && 1 == n.plus)
                                uni.navigateTo({
                                    url: "/pages/goods/goods?".concat(d)
                                });
                            else {
                                var o = "".concat(t);
                                e.$router.push(o)
                            }
                        }
                        ))
                    } else if (n = t.match(/\/list\?(.+)$/)) {
                        var f = decodeURI(n[1]);
                        e.$store.state.env.mpAlipay ? my.navigateTo({
                            url: "/pages/list/list?".concat(f)
                        }) : e.$store.state.env.mpJd ? jd.miniProgram.navigateTo({
                            url: "/pages/list/list?".concat(f)
                        }) : e.$store.state.env.mpBd ? swan.webView.navigateTo({
                            url: "/pages/list/list?".concat(f)
                        }) : e.$store.state.env.mpWechat ? uni.navigateTo({
                            url: "/pages/list/list?".concat(f)
                        }) : uni.getEnv((function(n) {
                            n.plus && 1 == n.plus ? uni.navigateTo({
                                url: "/pages/list/list?".concat(f)
                            }) : e.$router.push(t)
                        }
                        ))
                    } else if (n = t.match(/\/cart(\?)?(.+)$/)) {
                        var m = decodeURI(n[1]);
                        e.$store.state.env.mpAlipay ? my.switchTab({
                            url: "/pages/cart/cart?".concat(m)
                        }) : e.$store.state.env.mpJd ? jd.miniProgram.switchTab({
                            url: "/pages/tabs/cate/cate?".concat(m)
                        }) : e.$store.state.env.mpBd ? swan.webView.switchTab({
                            url: "/pages/tabs/cate/cate?".concat(m)
                        }) : e.$store.state.env.mpWechat ? uni.switchTab({
                            url: "/pages/cart/cart?${temp}"
                        }) : uni.getEnv((function(n) {
                            n.plus && 1 == n.plus ? uni.navigateTo({
                                url: "/pages/cart/cart?".concat(m)
                            }) : e.$router.push(t)
                        }
                        ))
                    } else if ("/member/bind" != t)
                        if (n = t.match(/\/pay-result\?(.+)$/)) {
                            var h = decodeURI(n[1]);
                            e.$store.state.env.mpAlipay ? my.redirectTo({
                                url: "/pages/order/pay-result/success/index?".concat(h)
                            }) : e.$store.state.env.mpJd ? jd.miniProgram.redirectTo({
                                url: "/pages/order/pay-result/success/index?".concat(h)
                            }) : e.$store.state.env.mpBd ? swan.webView.redirectTo({
                                url: "/pages/order/pay-result/success/index?".concat(h)
                            }) : e.$store.state.env.mpWechat ? uni.redirectTo({
                                url: "/pages/order/pay-result/success/index?".concat(h)
                            }) : uni.getEnv((function(e) {
                                e.plus && 1 == e.plus && uni.redirectTo({
                                    url: "/pages/order/pay-result/success/index?".concat(h)
                                })
                            }
                            ))
                        } else
                            t.indexOf("http://") > -1 || t.indexOf("https://") > -1 ? window.location.href = t : e.$router.push(t);
                    else
                        e.$store.state.env.mpAlipay ? my.navigateTo({
                            url: "/pages/member/bind?url=".concat(encodeURIComponent(window.location.href))
                        }) : e.$store.state.env.mpJd ? jd.miniProgram.navigateTo({
                            url: "/pages/user/memberbind/memberbind?url=".concat(encodeURIComponent(window.location.href))
                        }) : e.$store.state.env.mpBd ? swan.webView.navigateTo({
                            url: "/pages/user/memberbind/memberbind?url=".concat(encodeURIComponent(window.location.href))
                        }) : e.$store.state.env.mpWechat ? uni.navigateTo({
                            url: "/pages/member/bind?url=".concat(encodeURIComponent(window.location.href))
                        }) : uni.getEnv((function(n) {
                            n.plus && 1 == n.plus ? uni.navigateTo({
                                url: "/pages/member/bind?url=".concat(encodeURIComponent(window.location.href))
                            }) : e.$router.push(t)
                        }
                        ))
                } else
                    e.$store.state.env.mpAlipay ? my.switchTab({
                        url: "/pages/tabs/home"
                    }) : e.$store.state.env.mpJd ? jd.miniProgram.switchTab({
                        url: "/pages/tabs/home"
                    }) : e.$store.state.env.mpBd ? swan.webView.switchTab({
                        url: "/pages/tabs/home"
                    }) : e.$store.state.env.mpWechat ? uni.switchTab({
                        url: "/pages/tabs/home"
                    }) : uni.getEnv((function(e) {
                        e.plus && 1 == e.plus ? uni.switchTab({
                            url: "/pages/tabs/home"
                        }) : window.location.href = "/"
                    }
                    ))
        }
        function c(e) {
            if (null != e && null != e) {
                return e.replace(/(\d{3})\d*(\d{4})/, "$1****$2")
            }
            return ""
        }
        function d(e) {
            return null == e || null == e ? "" : e.length <= 3 ? "*" + e.substring(1, e.length) : e.length > 3 && e.length <= 6 ? "**" + e.substring(2, e.length) : e.length > 6 ? e.substring(0, 2) + "****" + e.substring(6, e.length) : void 0
        }
    },
    141: function(e, t, n) {
        "use strict";
        n.d(t, "a", (function() {
            return o
        }
        ));
        n(97),
        n(52);
        var o = /^[1][1, 2, 3, 4, 5, 6, 7, 8, 9][0-9]{9}$/
          , r = /^(^\d{18}$|^\d{17}(\d|X|x))$/
          , l = /^[\u4e00-\u9fa5]+[·]?[\u4e00-\u9fa5]+$/
          , c = {
            formatTime: function(e) {
                if (e <= 0)
                    return {
                        d: "00",
                        h: "00",
                        m: "00",
                        s: "00"
                    };
                var t = Math.floor(e / 86400);
                t = t < 10 ? "0" + t : t;
                var n = Math.floor((e - 3600 * t * 24) / 3600);
                n = n < 10 ? "0" + n : n;
                var o = Math.floor((e - 3600 * t * 24 - 3600 * n) / 60);
                o = o < 10 ? "0" + o : o;
                var s = Math.floor(e - 3600 * t * 24 - 3600 * n - 60 * o);
                return {
                    d: t,
                    h: n,
                    m: o,
                    s: s = s < 10 ? "0" + s : s
                }
            },
            formatDate: function(e, t) {
                e instanceof Date || "number" != typeof e || (e = (new Date).setTime(e));
                var n = {
                    "M+": e.getMonth() + 1,
                    "d+": e.getDate(),
                    "h+": e.getHours(),
                    "m+": e.getMinutes(),
                    "s+": e.getSeconds(),
                    "q+": Math.floor((e.getMonth() + 3) / 3),
                    S: e.getMilliseconds()
                };
                for (var o in /(y+)/.test(t) && (t = t.replace(RegExp.$1, (e.getFullYear() + "").substr(4 - RegExp.$1.length))),
                n)
                    new RegExp("(" + o + ")").test(t) && (t = t.replace(RegExp.$1, 1 === RegExp.$1.length ? n[o] : ("00" + n[o]).substr(("" + n[o]).length)));
                return t
            },
            trim: function(text) {
                return text.replace(/^(\s|\u00A0)+/, "").replace(/(\s|\u00A0)+$/, "")
            },
            removeAllBlanks: function(text) {
                return text.replace(/(\s|\u00A0)+/g, "")
            },
            isIdCardValid: function(code) {
                return !(code.length < 1) && r.test(code)
            },
            isCNNameValid: function(e) {
                return !(e.length < 1) && !!l.test(e)
            },
            isPhoneValid: function(e) {
                return !(e.length < 1) && !!o.test(e)
            },
            getNowFormatDate: function() {
                var e = new Date
                  , t = e.getFullYear()
                  , n = e.getMonth() + 1
                  , o = e.getDate();
                return n >= 1 && n <= 9 && (n = "0" + n),
                o >= 0 && o <= 9 && (o = "0" + o),
                t + "-" + n + "-" + o
            },
            initBrandBreadList: function(e, t) {
                var n = [{
                    name: "主页",
                    url: t
                }];
                return e.$route.query.firstKey && n.push({
                    name: e.$route.query.firstKey,
                    url: e.$route.query.firstUrl
                }),
                e.$route.query.secondKey && n.push({
                    name: e.$route.query.secondKey,
                    url: e.$route.query.secondUrl
                }),
                e.$route.query.thirdKey && n.push({
                    name: e.$route.query.thirdKey,
                    url: e.$route.query.thirdUrl
                }),
                n
            },
            randomStr: function(e) {
                for (var t = "abcdfsdferwrjhtjfdgofdgfdgrew1234569798ere", n = "", o = t.length, i = 0; i < e; i++)
                    n += t.charAt(Math.floor(Math.random() * o));
                return n
            }
        };
        window.randomStr = c.randomStr
        t.b = c
    },
    174: function(e, t, n) {
        "use strict";
        n.r(t),
        n.d(t, "state", (function() {
            return d
        }
        )),
        n.d(t, "mutations", (function() {
            return f
        }
        )),
        n.d(t, "actions", (function() {
            return m
        }
        ));
        n(21);
        var o = n(4)
          , r = n(35)
          , l = (n(1),
        n(12))
          , c = n(3)
          , d = function() {
            return {
                ident: null,
                UserToken: null,
                gid: null,
                mid: null,
                sid: null,
                pid: null,
                plid: null,
                sflsource: null,
                cart_goods_number: 0,
                orderInfo: {
                    bonus_count: 0,
                    coupons_count: 0,
                    pcode_count: 0,
                    unpay: 0,
                    unreceive: 0,
                    unship: 0,
                    apply_refund: 0,
                    tobe_picked_up: 0
                },
                package: {
                    completed: 0,
                    tobe_delivered: 0,
                    tobe_picked: 0,
                    tobe_received: 0
                },
                userInfo: {
                    id: void 0,
                    mobile_phone: void 0,
                    name: void 0,
                    nickName: void 0,
                    thumb: "",
                    isOneCodeUser: !1,
                    isagent: 0
                },
                oneCodeInfo: {
                    yimatong: 0,
                    name: "",
                    yimatong_userid: null,
                    yimatong_backurl: "",
                    hideBack: ""
                },
                consignorInfo: {
                    id: "",
                    name: "",
                    idcard: "",
                    phone: "",
                    is_native: "0",
                    native_type: "0",
                    native_no: ""
                },
                confirmConsignorInfo: {},
                outlandInfo: {},
                confirmOutlandInfo: {},
                tempConsignor: {},
                tempOutlandInfo: {},
                pickupInfo: [],
                showFaceAddr: {
                    show: !1,
                    orderId: ""
                },
                postAddress: {
                    type: "",
                    address: "",
                    backPickInfo: {
                        date: "",
                        flight: "",
                        pickPointIndex: ""
                    }
                },
                isToVerifyOutland: !1,
                is_verify_face_status: !0,
                is_pass_verify: !1,
                is_pass_outland: !1,
                setting_ts_status: 1
            }
        }
          , f = {
            updateUser: function(e, t) {
                e.UserToken = t
            },
            gidSet: function(e, t) {
                e.gid = t
            },
            deleteUser: function(e) {
                e.UserToken = null,
                e.orderInfo = {},
                e.userInfo = {},
                e.package = {}
            },
            HeadImg: function(e, t) {
                e.headImg = t
            },
            updateCartNumber: function(e, t) {
                e.cart_goods_number = t
            },
            updateUserInfo: function(e, data) {
                e.orderInfo = data.orderInfo,
                e.userInfo = data.userInfo,
                e.package = data.package,
                c.a.saveToSession("htdf_mid", data.userInfo.id),
                c.a.saveToCookie("user_id", data.userInfo.id, 86400)
            },
            updateShowFaceAddr: function(e, t) {
                t.hasOwnProperty("show") && (e.showFaceAddr.show = t.show),
                t.hasOwnProperty("orderId") && (e.showFaceAddr.orderId = t.orderId)
            },
            updateOneCodeInfo: function(e, data) {
                e.oneCodeInfo = data
            },
            updateMID: function(e, data) {
                e.mid = data
            },
            updateSID: function(e, data) {
                e.sid = data
            },
            updatePID: function(e, data) {
                e.pid = data
            },
            updatePLID: function(e, data) {
                e.plid = data
            },
            updateSflsource: function(e, data) {
                e.sflsource = data
            },
            updateConsignorInfo: function(e, data) {
                e.consignorInfo = data || {}
            },
            updateOutlandInfo: function(e, data) {
                e.outlandInfo = data
            },
            updatePostAddress: function(e, data) {
                e.postAddress = data || e.postAddress
            },
            updateVerifyFaceStatus: function(e, data) {
                e.is_verify_face_status = data
            },
            updatePassVerify: function(e, data) {
                e.is_pass_verify = data
            },
            updateIsToVerifyOutland: function(e, data) {
                e.isToVerifyOutland = data
            },
            updateConfirmConsignorInfo: function(e, data) {
                e.confirmConsignorInfo = data
            },
            updateConfirmOutlandInfo: function(e, data) {
                e.confirmOutlandInfo = data
            },
            updateTempConsignor: function(e, data) {
                e.tempConsignor = data
            },
            updateTempOutlandInfo: function(e, data) {
                e.tempOutlandInfo = data
            },
            updatePickupInfo: function(e, data) {
                e.pickupInfo = data
            },
            resetOutland: function(e) {
                e.isToVerifyOutland = !1,
                e.confirmConsignorInfo = {},
                e.confirmOutlandInfo = {},
                e.tempConsignor = {},
                e.tempOutlandInfo = {},
                e.consignorInfo = {},
                e.outlandInfo = {}
            },
            setIdent: function(e, data) {
                e.ident = data
            },
            setSettingTsStatus: function(e, data) {
                e.setting_ts_status = data
            }
        }
          , m = {
            setHeadImg: function(e, t) {
                t && e.commit("HeadImg", t)
            },
            updateCartGoodsNumber: function(e) {
                return Object(o.a)(regeneratorRuntime.mark((function t() {
                    var n;
                    return regeneratorRuntime.wrap((function(t) {
                        for (; ; )
                            switch (t.prev = t.next) {
                            case 0:
                                if (null !== e.state.UserToken) {
                                    t.next = 2;
                                    break
                                }
                                return t.abrupt("return");
                            case 2:
                                return t.next = 4,
                                Object(r.Tc)(e.state.UserToken);
                            case 4:
                                (n = t.sent).data && 200 === n.data.code && e.commit("updateCartNumber", parseInt(n.data.data.number));
                            case 6:
                            case "end":
                                return t.stop()
                            }
                    }
                    ), t)
                }
                )))()
            },
            updateUserInfo: function(e) {
                var t = arguments;
                return Object(o.a)(regeneratorRuntime.mark((function n() {
                    var o, c, d, f;
                    return regeneratorRuntime.wrap((function(n) {
                        for (; ; )
                            switch (n.prev = n.next) {
                            case 0:
                                if (o = e.state,
                                c = e.commit,
                                d = t.length > 1 && void 0 !== t[1] && t[1],
                                null !== o.UserToken) {
                                    n.next = 4;
                                    break
                                }
                                return n.abrupt("return");
                            case 4:
                                return n.next = 6,
                                Object(r.Tb)(o.gid, o.UserToken, d);
                            case 6:
                                (f = n.sent).data && 200 === f.data.code && (c("updateUserInfo", f.data.data),
                                window.__EVENT_BUS__.$emit(l.f));
                            case 8:
                            case "end":
                                return n.stop()
                            }
                    }
                    ), n)
                }
                )))()
            },
            upIdent: function(e, data) {
                e.commit("setIdent", data)
            }
        }
    },
    176: function(e, t, n) {
        var content = n(276);
        "string" == typeof content && (content = [[e.i, content, ""]]),
        content.locals && (e.exports = content.locals);
        (0,
        n(8).default)("4fba3696", content, !0, {
            sourceMap: !1
        })
    },
    177: function(e, t, n) {
        var content = n(278);
        "string" == typeof content && (content = [[e.i, content, ""]]),
        content.locals && (e.exports = content.locals);
        (0,
        n(8).default)("b0f53faa", content, !0, {
            sourceMap: !1
        })
    },
    178: function(e, t, n) {
        var content = n(297);
        "string" == typeof content && (content = [[e.i, content, ""]]),
        content.locals && (e.exports = content.locals);
        (0,
        n(8).default)("5a3e15e2", content, !0, {
            sourceMap: !1
        })
    },
    19: function(e, t, n) {
        "use strict";
        n.r(t);
        var o = n(2)
          , r = n(49);
        o.default.use(r.a);
        var l = new r.a.Store({
            state: function() {
                return {
                    mid: null,
                    sid: null,
                    pid: null,
                    plid: null,
                    sflsource: null
                }
            },
            getters: {
                getMid: function(e) {
                    return e.mid
                },
                getSid: function(e) {
                    return e.sid
                },
                getPid: function(e) {
                    return e.pid
                },
                getPlid: function(e) {
                    return e.plid
                },
                getSflsource: function(e) {
                    return e.sflsource
                }
            },
            mutations: {
                setMid: function(e, t) {
                    e.mid = void 0 !== t && null != t && "" != t && t ? t : ""
                },
                setSid: function(e, t) {
                    e.sid = void 0 !== t && null != t && "" != t && t ? t : ""
                },
                setPid: function(e, t) {
                    e.pid = void 0 !== t && null != t && "" != t && t ? t : ""
                },
                setPlid: function(e, t) {
                    e.plid = void 0 !== t && null != t && "" != t && t ? t : ""
                },
                setSflsource: function(e, t) {
                    e.sflsource = void 0 !== t && null != t && "" != t && t ? t : ""
                }
            },
            actions: {}
        });
        t.default = function() {
            return l
        }
    },
    191: function(e, t, n) {
        "use strict";
        n(16),
        n(21);
        var o = n(4)
          , r = n(2)
          , l = n(0)
          , c = window.__NUXT__;
        function d() {
            if (!this._hydrated)
                return this.$fetch()
        }
        function f() {
            if ((e = this).$vnode && e.$vnode.elm && e.$vnode.elm.dataset && e.$vnode.elm.dataset.fetchKey) {
                var e;
                this._hydrated = !0,
                this._fetchKey = this.$vnode.elm.dataset.fetchKey;
                var data = c.fetch[this._fetchKey];
                if (data && data._error)
                    this.$fetchState.error = data._error;
                else
                    for (var t in data)
                        r.default.set(this.$data, t, data[t])
            }
        }
        function m() {
            var e = this;
            return this._fetchPromise || (this._fetchPromise = h.call(this).then((function() {
                delete e._fetchPromise
            }
            ))),
            this._fetchPromise
        }
        function h() {
            return v.apply(this, arguments)
        }
        function v() {
            return (v = Object(o.a)(regeneratorRuntime.mark((function e() {
                var t, n, o, r = this;
                return regeneratorRuntime.wrap((function(e) {
                    for (; ; )
                        switch (e.prev = e.next) {
                        case 0:
                            return this.$nuxt.nbFetching++,
                            this.$fetchState.pending = !0,
                            this.$fetchState.error = null,
                            this._hydrated = !1,
                            t = null,
                            n = Date.now(),
                            e.prev = 6,
                            e.next = 9,
                            this.$options.fetch.call(this);
                        case 9:
                            e.next = 15;
                            break;
                        case 11:
                            e.prev = 11,
                            e.t0 = e.catch(6),
                            t = Object(l.p)(e.t0);
                        case 15:
                            if (!((o = this._fetchDelay - (Date.now() - n)) > 0)) {
                                e.next = 19;
                                break
                            }
                            return e.next = 19,
                            new Promise((function(e) {
                                return setTimeout(e, o)
                            }
                            ));
                        case 19:
                            this.$fetchState.error = t,
                            this.$fetchState.pending = !1,
                            this.$fetchState.timestamp = Date.now(),
                            this.$nextTick((function() {
                                return r.$nuxt.nbFetching--
                            }
                            ));
                        case 23:
                        case "end":
                            return e.stop()
                        }
                }
                ), e, this, [[6, 11]])
            }
            )))).apply(this, arguments)
        }
        t.a = {
            beforeCreate: function() {
                Object(l.l)(this) && (this._fetchDelay = "number" == typeof this.$options.fetchDelay ? this.$options.fetchDelay : 200,
                r.default.util.defineReactive(this, "$fetchState", {
                    pending: !1,
                    error: null,
                    timestamp: Date.now()
                }),
                this.$fetch = m.bind(this),
                Object(l.a)(this, "created", f),
                Object(l.a)(this, "beforeMount", d))
            }
        }
    },
    214: function(e, t, n) {
        e.exports = n(215)
    },
    215: function(e, t, n) {
        "use strict";
        n.r(t),
        function(e) {
            n(65),
            n(37),
            n(66),
            n(38),
            n(39),
            n(67);
            var t = n(27)
              , o = (n(21),
            n(68),
            n(4))
              , r = (n(76),
            n(88),
            n(31),
            n(16),
            n(53),
            n(36),
            n(125),
            n(226),
            n(232),
            n(234),
            n(2))
              , l = n(184)
              , c = n(132)
              , d = n(0)
              , f = n(41)
              , m = n(191)
              , h = n(100);
            function v(e, t) {
                var n;
                if ("undefined" == typeof Symbol || null == e[Symbol.iterator]) {
                    if (Array.isArray(e) || (n = function(e, t) {
                        if (!e)
                            return;
                        if ("string" == typeof e)
                            return x(e, t);
                        var n = Object.prototype.toString.call(e).slice(8, -1);
                        "Object" === n && e.constructor && (n = e.constructor.name);
                        if ("Map" === n || "Set" === n)
                            return Array.from(e);
                        if ("Arguments" === n || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n))
                            return x(e, t)
                    }(e)) || t && e && "number" == typeof e.length) {
                        n && (e = n);
                        var i = 0
                          , o = function() {};
                        return {
                            s: o,
                            n: function() {
                                return i >= e.length ? {
                                    done: !0
                                } : {
                                    done: !1,
                                    value: e[i++]
                                }
                            },
                            e: function(e) {
                                throw e
                            },
                            f: o
                        }
                    }
                    throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
                }
                var r, l = !0, c = !1;
                return {
                    s: function() {
                        n = e[Symbol.iterator]()
                    },
                    n: function() {
                        var e = n.next();
                        return l = e.done,
                        e
                    },
                    e: function(e) {
                        c = !0,
                        r = e
                    },
                    f: function() {
                        try {
                            l || null == n.return || n.return()
                        } finally {
                            if (c)
                                throw r
                        }
                    }
                }
            }
            function x(e, t) {
                (null == t || t > e.length) && (t = e.length);
                for (var i = 0, n = new Array(t); i < t; i++)
                    n[i] = e[i];
                return n
            }
            r.default.__nuxt__fetch__mixin__ || (r.default.mixin(m.a),
            r.default.__nuxt__fetch__mixin__ = !0),
            r.default.component(h.a.name, h.a),
            r.default.component("NLink", h.a),
            e.fetch || (e.fetch = l.a);
            var y, w, k = [], _ = window.__NUXT__ || {}, O = _.config || {};
            O.app && (n.p = Object(d.v)(O.app.cdnURL, O.app.assetsPath)),
            Object.assign(r.default.config, {
                silent: !0,
                performance: !1
            });
            var j = r.default.config.errorHandler || console.error;
            function P(e, t, n) {
                for (var o = function(component) {
                    var e = function(component, e) {
                        if (!component || !component.options || !component.options[e])
                            return {};
                        var option = component.options[e];
                        if ("function" == typeof option) {
                            for (var t = arguments.length, n = new Array(t > 2 ? t - 2 : 0), o = 2; o < t; o++)
                                n[o - 2] = arguments[o];
                            return option.apply(void 0, n)
                        }
                        return option
                    }(component, "transition", t, n) || {};
                    return "string" == typeof e ? {
                        name: e
                    } : e
                }, r = n ? Object(d.g)(n) : [], l = Math.max(e.length, r.length), c = [], f = function(i) {
                    var t = Object.assign({}, o(e[i]))
                      , n = Object.assign({}, o(r[i]));
                    Object.keys(t).filter((function(e) {
                        return void 0 !== t[e] && !e.toLowerCase().includes("leave")
                    }
                    )).forEach((function(e) {
                        n[e] = t[e]
                    }
                    )),
                    c.push(n)
                }, i = 0; i < l; i++)
                    f(i);
                return c
            }
            function z(e, t, n) {
                return S.apply(this, arguments)
            }
            function S() {
                return (S = Object(o.a)(regeneratorRuntime.mark((function e(t, n, o) {
                    var r, l, c, f, m = this;
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                if (this._routeChanged = Boolean(y.nuxt.err) || n.name !== t.name,
                                this._paramChanged = !this._routeChanged && n.path !== t.path,
                                this._queryChanged = !this._paramChanged && n.fullPath !== t.fullPath,
                                this._diffQuery = this._queryChanged ? Object(d.i)(t.query, n.query) : [],
                                (this._routeChanged || this._paramChanged) && this.$loading.start && !this.$loading.manual && this.$loading.start(),
                                e.prev = 5,
                                !this._queryChanged) {
                                    e.next = 12;
                                    break
                                }
                                return e.next = 9,
                                Object(d.r)(t, (function(e, t) {
                                    return {
                                        Component: e,
                                        instance: t
                                    }
                                }
                                ));
                            case 9:
                                r = e.sent,
                                r.some((function(e) {
                                    var o = e.Component
                                      , r = e.instance
                                      , l = o.options.watchQuery;
                                    return !0 === l || (Array.isArray(l) ? l.some((function(e) {
                                        return m._diffQuery[e]
                                    }
                                    )) : "function" == typeof l && l.apply(r, [t.query, n.query]))
                                }
                                )) && this.$loading.start && !this.$loading.manual && this.$loading.start();
                            case 12:
                                o(),
                                e.next = 26;
                                break;
                            case 15:
                                if (e.prev = 15,
                                e.t0 = e.catch(5),
                                l = e.t0 || {},
                                c = l.statusCode || l.status || l.response && l.response.status || 500,
                                f = l.message || "",
                                !/^Loading( CSS)? chunk (\d)+ failed\./.test(f)) {
                                    e.next = 23;
                                    break
                                }
                                return window.location.reload(!0),
                                e.abrupt("return");
                            case 23:
                                this.error({
                                    statusCode: c,
                                    message: f
                                }),
                                this.$nuxt.$emit("routeChanged", t, n, l),
                                o();
                            case 26:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e, this, [[5, 15]])
                }
                )))).apply(this, arguments)
            }
            function T(e, t) {
                return _.serverRendered && t && Object(d.b)(e, t),
                e._Ctor = e,
                e
            }
            function E(e) {
                var path = Object(d.f)(e.options.base, e.options.mode);
                return Object(d.d)(e.match(path), function() {
                    var e = Object(o.a)(regeneratorRuntime.mark((function e(t, n, o, r, l) {
                        var c;
                        return regeneratorRuntime.wrap((function(e) {
                            for (; ; )
                                switch (e.prev = e.next) {
                                case 0:
                                    if ("function" != typeof t || t.options) {
                                        e.next = 4;
                                        break
                                    }
                                    return e.next = 3,
                                    t();
                                case 3:
                                    t = e.sent;
                                case 4:
                                    return c = T(Object(d.s)(t), _.data ? _.data[l] : null),
                                    o.components[r] = c,
                                    e.abrupt("return", c);
                                case 7:
                                case "end":
                                    return e.stop()
                                }
                        }
                        ), e)
                    }
                    )));
                    return function(t, n, o, r, l) {
                        return e.apply(this, arguments)
                    }
                }())
            }
            function $(e, t, n) {
                var o = this
                  , r = ["checkLogin"]
                  , l = !1;
                if (void 0 !== n && (r = [],
                (n = Object(d.s)(n)).options.middleware && (r = r.concat(n.options.middleware)),
                e.forEach((function(e) {
                    e.options.middleware && (r = r.concat(e.options.middleware))
                }
                ))),
                r = r.map((function(e) {
                    return "function" == typeof e ? e : ("function" != typeof c.a[e] && (l = !0,
                    o.error({
                        statusCode: 500,
                        message: "Unknown middleware " + e
                    })),
                    c.a[e])
                }
                )),
                !l)
                    return Object(d.o)(r, t)
            }
            function C(e, t, n) {
                return R.apply(this, arguments)
            }
            function R() {
                return (R = Object(o.a)(regeneratorRuntime.mark((function e(t, n, r) {
                    var l, c, m, h, x, w, _, O, j, z, S, T, E, C, R, I = this;
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                if (!1 !== this._routeChanged || !1 !== this._paramChanged || !1 !== this._queryChanged) {
                                    e.next = 2;
                                    break
                                }
                                return e.abrupt("return", r());
                            case 2:
                                return !1,
                                t === n ? (k = [],
                                !0) : (l = [],
                                k = Object(d.g)(n, l).map((function(e, i) {
                                    return Object(d.c)(n.matched[l[i]].path)(n.params)
                                }
                                ))),
                                c = !1,
                                m = function(path) {
                                    n.path === path.path && I.$loading.finish && I.$loading.finish(),
                                    n.path !== path.path && I.$loading.pause && I.$loading.pause(),
                                    c || (c = !0,
                                    r(path))
                                }
                                ,
                                e.next = 8,
                                Object(d.t)(y, {
                                    route: t,
                                    from: n,
                                    next: m.bind(this)
                                });
                            case 8:
                                if (this._dateLastError = y.nuxt.dateErr,
                                this._hadError = Boolean(y.nuxt.err),
                                h = [],
                                (x = Object(d.g)(t, h)).length) {
                                    e.next = 27;
                                    break
                                }
                                return e.next = 15,
                                $.call(this, x, y.context);
                            case 15:
                                if (!c) {
                                    e.next = 17;
                                    break
                                }
                                return e.abrupt("return");
                            case 17:
                                return w = (f.a.options || f.a).layout,
                                e.next = 20,
                                this.loadLayout("function" == typeof w ? w.call(f.a, y.context) : w);
                            case 20:
                                return _ = e.sent,
                                e.next = 23,
                                $.call(this, x, y.context, _);
                            case 23:
                                if (!c) {
                                    e.next = 25;
                                    break
                                }
                                return e.abrupt("return");
                            case 25:
                                return y.context.error({
                                    statusCode: 404,
                                    message: "This page could not be found"
                                }),
                                e.abrupt("return", r());
                            case 27:
                                return x.forEach((function(e) {
                                    e._Ctor && e._Ctor.options && (e.options.asyncData = e._Ctor.options.asyncData,
                                    e.options.fetch = e._Ctor.options.fetch)
                                }
                                )),
                                this.setTransitions(P(x, t, n)),
                                e.prev = 29,
                                e.next = 32,
                                $.call(this, x, y.context);
                            case 32:
                                if (!c) {
                                    e.next = 34;
                                    break
                                }
                                return e.abrupt("return");
                            case 34:
                                if (!y.context._errored) {
                                    e.next = 36;
                                    break
                                }
                                return e.abrupt("return", r());
                            case 36:
                                return "function" == typeof (O = x[0].options.layout) && (O = O(y.context)),
                                e.next = 40,
                                this.loadLayout(O);
                            case 40:
                                return O = e.sent,
                                e.next = 43,
                                $.call(this, x, y.context, O);
                            case 43:
                                if (!c) {
                                    e.next = 45;
                                    break
                                }
                                return e.abrupt("return");
                            case 45:
                                if (!y.context._errored) {
                                    e.next = 47;
                                    break
                                }
                                return e.abrupt("return", r());
                            case 47:
                                j = !0,
                                e.prev = 48,
                                z = v(x),
                                e.prev = 50,
                                z.s();
                            case 52:
                                if ((S = z.n()).done) {
                                    e.next = 63;
                                    break
                                }
                                if ("function" == typeof (T = S.value).options.validate) {
                                    e.next = 56;
                                    break
                                }
                                return e.abrupt("continue", 61);
                            case 56:
                                return e.next = 58,
                                T.options.validate(y.context);
                            case 58:
                                if (j = e.sent) {
                                    e.next = 61;
                                    break
                                }
                                return e.abrupt("break", 63);
                            case 61:
                                e.next = 52;
                                break;
                            case 63:
                                e.next = 68;
                                break;
                            case 65:
                                e.prev = 65,
                                e.t0 = e.catch(50),
                                z.e(e.t0);
                            case 68:
                                return e.prev = 68,
                                z.f(),
                                e.finish(68);
                            case 71:
                                e.next = 77;
                                break;
                            case 73:
                                return e.prev = 73,
                                e.t1 = e.catch(48),
                                this.error({
                                    statusCode: e.t1.statusCode || "500",
                                    message: e.t1.message
                                }),
                                e.abrupt("return", r());
                            case 77:
                                if (j) {
                                    e.next = 80;
                                    break
                                }
                                return this.error({
                                    statusCode: 404,
                                    message: "This page could not be found"
                                }),
                                e.abrupt("return", r());
                            case 80:
                                return e.next = 82,
                                Promise.all(x.map(function() {
                                    var e = Object(o.a)(regeneratorRuntime.mark((function e(o, i) {
                                        var r, l, c, f, m, v, x, w, p;
                                        return regeneratorRuntime.wrap((function(e) {
                                            for (; ; )
                                                switch (e.prev = e.next) {
                                                case 0:
                                                    if (o._path = Object(d.c)(t.matched[h[i]].path)(t.params),
                                                    o._dataRefresh = !1,
                                                    r = o._path !== k[i],
                                                    I._routeChanged && r ? o._dataRefresh = !0 : I._paramChanged && r ? (l = o.options.watchParam,
                                                    o._dataRefresh = !1 !== l) : I._queryChanged && (!0 === (c = o.options.watchQuery) ? o._dataRefresh = !0 : Array.isArray(c) ? o._dataRefresh = c.some((function(e) {
                                                        return I._diffQuery[e]
                                                    }
                                                    )) : "function" == typeof c && (E || (E = Object(d.h)(t)),
                                                    o._dataRefresh = c.apply(E[i], [t.query, n.query]))),
                                                    I._hadError || !I._isMounted || o._dataRefresh) {
                                                        e.next = 6;
                                                        break
                                                    }
                                                    return e.abrupt("return");
                                                case 6:
                                                    return f = [],
                                                    m = o.options.asyncData && "function" == typeof o.options.asyncData,
                                                    v = Boolean(o.options.fetch) && o.options.fetch.length,
                                                    x = m && v ? 30 : 45,
                                                    m && ((w = Object(d.q)(o.options.asyncData, y.context)).then((function(e) {
                                                        Object(d.b)(o, e),
                                                        I.$loading.increase && I.$loading.increase(x)
                                                    }
                                                    )),
                                                    f.push(w)),
                                                    I.$loading.manual = !1 === o.options.loading,
                                                    v && ((p = o.options.fetch(y.context)) && (p instanceof Promise || "function" == typeof p.then) || (p = Promise.resolve(p)),
                                                    p.then((function(e) {
                                                        I.$loading.increase && I.$loading.increase(x)
                                                    }
                                                    )),
                                                    f.push(p)),
                                                    e.abrupt("return", Promise.all(f));
                                                case 14:
                                                case "end":
                                                    return e.stop()
                                                }
                                        }
                                        ), e)
                                    }
                                    )));
                                    return function(t, n) {
                                        return e.apply(this, arguments)
                                    }
                                }()));
                            case 82:
                                c || (this.$loading.finish && !this.$loading.manual && this.$loading.finish(),
                                r()),
                                e.next = 99;
                                break;
                            case 85:
                                if (e.prev = 85,
                                e.t2 = e.catch(29),
                                "ERR_REDIRECT" !== (C = e.t2 || {}).message) {
                                    e.next = 90;
                                    break
                                }
                                return e.abrupt("return", this.$nuxt.$emit("routeChanged", t, n, C));
                            case 90:
                                return k = [],
                                Object(d.k)(C),
                                "function" == typeof (R = (f.a.options || f.a).layout) && (R = R(y.context)),
                                e.next = 96,
                                this.loadLayout(R);
                            case 96:
                                this.error(C),
                                this.$nuxt.$emit("routeChanged", t, n, C),
                                r();
                            case 99:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e, this, [[29, 85], [48, 73], [50, 65, 68, 71]])
                }
                )))).apply(this, arguments)
            }
            function I(e, n) {
                Object(d.d)(e, (function(e, n, o, l) {
                    return "object" !== Object(t.a)(e) || e.options || ((e = r.default.extend(e))._Ctor = e,
                    o.components[l] = e),
                    e
                }
                ))
            }
            function A(e) {
                var t = Boolean(this.$options.nuxt.err);
                this._hadError && this._dateLastError === this.$options.nuxt.dateErr && (t = !1);
                var n = t ? (f.a.options || f.a).layout : e.matched[0].components.default.options.layout;
                "function" == typeof n && (n = n(y.context)),
                this.setLayout(n)
            }
            function U(e) {
                e._hadError && e._dateLastError === e.$options.nuxt.dateErr && e.error()
            }
            function D(e, t) {
                var n = this;
                if (!1 !== this._routeChanged || !1 !== this._paramChanged || !1 !== this._queryChanged) {
                    var o = Object(d.h)(e)
                      , l = Object(d.g)(e)
                      , c = !1;
                    r.default.nextTick((function() {
                        o.forEach((function(e, i) {
                            if (e && !e._isDestroyed && e.constructor._dataRefresh && l[i] === e.constructor && !0 !== e.$vnode.data.keepAlive && "function" == typeof e.constructor.options.data) {
                                var t = e.constructor.options.data.call(e);
                                for (var n in t)
                                    r.default.set(e.$data, n, t[n]);
                                c = !0
                            }
                        }
                        )),
                        c && window.$nuxt.$nextTick((function() {
                            window.$nuxt.$emit("triggerScroll")
                        }
                        )),
                        U(n)
                    }
                    ))
                }
            }
            function N(e) {
                window.onNuxtReadyCbs.forEach((function(t) {
                    "function" == typeof t && t(e)
                }
                )),
                "function" == typeof window._onNuxtLoaded && window._onNuxtLoaded(e),
                w.afterEach((function(t, n) {
                    r.default.nextTick((function() {
                        return e.$nuxt.$emit("routeChanged", t, n)
                    }
                    ))
                }
                ))
            }
            function L() {
                return (L = Object(o.a)(regeneratorRuntime.mark((function e(t) {
                    var n, o, l, c, f;
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                return y = t.app,
                                w = t.router,
                                t.store,
                                n = new r.default(y),
                                o = _.layout || "default",
                                e.next = 7,
                                n.loadLayout(o);
                            case 7:
                                return n.setLayout(o),
                                l = function() {
                                    n.$mount("#__nuxt"),
                                    w.afterEach(I),
                                    w.afterEach(A.bind(n)),
                                    w.afterEach(D.bind(n)),
                                    r.default.nextTick((function() {
                                        N(n)
                                    }
                                    ))
                                }
                                ,
                                e.next = 11,
                                Promise.all(E(w));
                            case 11:
                                if (c = e.sent,
                                n.setTransitions = n.$options.nuxt.setTransitions.bind(n),
                                c.length && (n.setTransitions(P(c, w.currentRoute)),
                                k = w.currentRoute.matched.map((function(e) {
                                    return Object(d.c)(e.path)(w.currentRoute.params)
                                }
                                ))),
                                n.$loading = {},
                                _.error && n.error(_.error),
                                w.beforeEach(z.bind(n)),
                                w.beforeEach(C.bind(n)),
                                !_.serverRendered || !Object(d.n)(_.routePath, n.context.route.path)) {
                                    e.next = 20;
                                    break
                                }
                                return e.abrupt("return", l());
                            case 20:
                                return f = function() {
                                    I(w.currentRoute, w.currentRoute),
                                    A.call(n, w.currentRoute),
                                    U(n),
                                    l()
                                }
                                ,
                                e.next = 23,
                                new Promise((function(e) {
                                    return setTimeout(e, 0)
                                }
                                ));
                            case 23:
                                C.call(n, w.currentRoute, w.currentRoute, (function(path) {
                                    if (path) {
                                        var e = w.afterEach((function(t, n) {
                                            e(),
                                            f()
                                        }
                                        ));
                                        w.push(path, void 0, (function(e) {
                                            e && j(e)
                                        }
                                        ))
                                    } else
                                        f()
                                }
                                ));
                            case 24:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                )))).apply(this, arguments)
            }
            Object(f.b)(null, _.config).then((function(e) {
                return L.apply(this, arguments)
            }
            )).catch(j)
        }
        .call(this, n(44))
    },
    235: function(e, t, n) {
        "use strict";
        n.r(t);
        var o = n(3)
          , r = ["/confirm", "/order", "/order/:ordersn", "/order/refund", "/order/refund/detail", "/order/refund/forbidden", "/order/express-detail/express-detail", "/order/order-off-detail/order-off-detail", "/order/order-off-list/order-off-list", "/order/order-on-detail/order-on-detail", "/order/order-on-list/order-on-list", "/order/order-receipt/order-receipt", "/order/order-receipt-open/order-receipt-open", "/order/order-reteat/order-reteat", "/order/order-reteat-list/order-reteat-list", "/order/order-reteat-open/order-reteat-open", "/user/info", "/user/changePass", "/user/receipt/receipt", "/user/changePhone", "/user/coupon", "/user/pcode", "/user/repassw", "/user/consignor", "/user/consignor/make", "/user/outlands/change", "/user/outlands/success", "/user/outlands/info", "/user/address-add/address-add", "/user/address-list/address-list", "/member", "/member/bind", "/member/level", "/member/points", "/confirm/goods/goods", "/payResult/:ordersn", "/payResult/success", "/payResult/fail"];
        t.default = function(e) {
            e.store;
            var t = e.route
              , n = e.redirect
              , l = e.req;
            if (t.matched.length > 0 && r.indexOf(t.matched[0].path) > -1) {
                var c = !0;
                if (c = null === o.a.fetchFromCookie("UserToken"),
                window.location.host,
                !1 === c)
                    return !1;
                var d = l ? l.url : t.fullPath
                  , f = encodeURIComponent("".concat(d));
                return n("/passport/login?backURL=".concat(f))
            }
        }
    },
    265: function(e, t, n) {
        "use strict";
        n.r(t),
        t.default = function(e) {
            return !0
        }
    },
    275: function(e, t, n) {
        "use strict";
        n(176)
    },
    276: function(e, t, n) {
        var o = n(7)(!1);
        o.push([e.i, '/*! normalize.css v4.1.1 | MIT License | github.com/necolas/normalize.css */html[data-v-4415c7f8]{font-family:"PingFang SC","Microsoft YaHei";-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}article[data-v-4415c7f8],aside[data-v-4415c7f8],details[data-v-4415c7f8],figcaption[data-v-4415c7f8],figure[data-v-4415c7f8],footer[data-v-4415c7f8],header[data-v-4415c7f8],main[data-v-4415c7f8],menu[data-v-4415c7f8],nav[data-v-4415c7f8],section[data-v-4415c7f8],summary[data-v-4415c7f8]{display:block}audio[data-v-4415c7f8],canvas[data-v-4415c7f8],progress[data-v-4415c7f8],video[data-v-4415c7f8]{display:inline-block}audio[data-v-4415c7f8]:not([controls]){display:none;height:0}progress[data-v-4415c7f8]{vertical-align:baseline}[hidden][data-v-4415c7f8],template[data-v-4415c7f8]{display:none}a[data-v-4415c7f8]{background-color:transparent;-webkit-text-decoration-skip:objects;text-decoration:none}a[data-v-4415c7f8]:active,a[data-v-4415c7f8]:hover{outline-width:0}a[data-v-4415c7f8]:hover,a[data-v-4415c7f8]:link,a[data-v-4415c7f8]:visited{color:#383838;text-decoration:none}abbr[title][data-v-4415c7f8]{border-bottom:none;text-decoration:underline;-webkit-text-decoration:underline dotted;text-decoration:underline dotted}b[data-v-4415c7f8],strong[data-v-4415c7f8]{font-weight:inherit;font-weight:bolder}dfn[data-v-4415c7f8]{font-style:italic}h1[data-v-4415c7f8]{font-size:2em;margin:.67em 0}mark[data-v-4415c7f8]{background-color:#ff0;color:#000}small[data-v-4415c7f8]{font-size:80%}sub[data-v-4415c7f8],sup[data-v-4415c7f8]{font-size:75%;line-height:0;position:relative;vertical-align:baseline}sub[data-v-4415c7f8]{bottom:-.25em}sup[data-v-4415c7f8]{top:-.5em}img[data-v-4415c7f8]{border-style:none}svg[data-v-4415c7f8]:not(:root){overflow:hidden}code[data-v-4415c7f8],kbd[data-v-4415c7f8],pre[data-v-4415c7f8],samp[data-v-4415c7f8]{font-family:monospace,monospace;font-size:1em}figure[data-v-4415c7f8]{margin:1em 40px}hr[data-v-4415c7f8]{box-sizing:content-box;height:0;overflow:visible}button[data-v-4415c7f8],input[data-v-4415c7f8],select[data-v-4415c7f8],textarea[data-v-4415c7f8]{font:inherit;margin:0;outline:none}optgroup[data-v-4415c7f8]{font-weight:700}button[data-v-4415c7f8],input[data-v-4415c7f8]{overflow:visible}button[data-v-4415c7f8],select[data-v-4415c7f8]{text-transform:none}[type=reset][data-v-4415c7f8],[type=submit][data-v-4415c7f8],button[data-v-4415c7f8],html [type=button][data-v-4415c7f8]{-webkit-appearance:button}[type=button][data-v-4415c7f8]::-moz-focus-inner,[type=reset][data-v-4415c7f8]::-moz-focus-inner,[type=submit][data-v-4415c7f8]::-moz-focus-inner,button[data-v-4415c7f8]::-moz-focus-inner{border-style:none;padding:0}[type=button][data-v-4415c7f8]:-moz-focusring,[type=reset][data-v-4415c7f8]:-moz-focusring,[type=submit][data-v-4415c7f8]:-moz-focusring,button[data-v-4415c7f8]:-moz-focusring{outline:1px dotted ButtonText}fieldset[data-v-4415c7f8]{border:1px solid silver;margin:0 2px;padding:.35em .625em .75em}legend[data-v-4415c7f8]{box-sizing:border-box;color:inherit;display:table;max-width:100%;padding:0;white-space:normal}textarea[data-v-4415c7f8]{overflow:auto}[type=checkbox][data-v-4415c7f8],[type=radio][data-v-4415c7f8]{box-sizing:border-box;padding:0}[type=number][data-v-4415c7f8]::-webkit-inner-spin-button,[type=number][data-v-4415c7f8]::-webkit-outer-spin-button{height:auto}[type=search][data-v-4415c7f8]{-webkit-appearance:textfield;outline-offset:-2px}[type=search][data-v-4415c7f8]::-webkit-search-cancel-button,[type=search][data-v-4415c7f8]::-webkit-search-decoration{-webkit-appearance:none}[data-v-4415c7f8]::-webkit-input-placeholder{color:inherit;opacity:.54}[data-v-4415c7f8]::-webkit-file-upload-button{-webkit-appearance:button;font:inherit}dl[data-v-4415c7f8],ol[data-v-4415c7f8],ul[data-v-4415c7f8]{list-style-type:none}body[data-v-4415c7f8],dd[data-v-4415c7f8],dl[data-v-4415c7f8],dt[data-v-4415c7f8],form[data-v-4415c7f8],h1[data-v-4415c7f8],h2[data-v-4415c7f8],h3[data-v-4415c7f8],h4[data-v-4415c7f8],h5[data-v-4415c7f8],h6[data-v-4415c7f8],html[data-v-4415c7f8],img[data-v-4415c7f8],li[data-v-4415c7f8],ol[data-v-4415c7f8],p[data-v-4415c7f8],table[data-v-4415c7f8],td[data-v-4415c7f8],textarea[data-v-4415c7f8],th[data-v-4415c7f8],tr[data-v-4415c7f8],ul[data-v-4415c7f8]{margin:0;padding:0}em[data-v-4415c7f8],i[data-v-4415c7f8]{font-style:normal}html[data-v-4415c7f8]{width:100%;height:100%}@media screen and (max-width:320px){html[data-v-4415c7f8]{font-size:17.0666667px}}@media screen and (max-width:374px){html[data-v-4415c7f8]{font-size:19.2px}}@media screen and (min-width:375px){html[data-v-4415c7f8]{font-size:20px}}@media screen and (min-width:414px){html[data-v-4415c7f8]{font-size:22.08px}}@media screen and (min-width:768px){html[data-v-4415c7f8]{font-size:40.96px}}@media screen and (min-width:1024px){html[data-v-4415c7f8]{font-size:54.6133333px}}body[data-v-4415c7f8]{position:relative;margin:0;background-color:#f9f9f9;color:#383838;font-size:.6rem}#__layout[data-v-4415c7f8],#__nuxt[data-v-4415c7f8],.page-container[data-v-4415c7f8],body[data-v-4415c7f8]{width:100%;height:100%;overflow:hidden}.page[data-v-4415c7f8]{position:absolute;top:0;right:0;bottom:0;left:0;width:100%;box-sizing:border-box;overflow:hidden;background:#f9f9f9}.page .page-header[data-v-4415c7f8]{position:absolute!important;top:0;right:0;left:0;background:#fff}.page .page-content[data-v-4415c7f8]{position:absolute;top:0;right:0;left:0;bottom:0;overflow-x:hidden;overflow-y:auto;overflow-scrolling:touch;-webkit-overflow-scrolling:touch}.page.has-nav .page-content[data-v-4415c7f8]{top:2.3rem}.page.has-bottom .page-content[data-v-4415c7f8]{bottom:50px}.page .page-section[data-v-4415c7f8]{margin-bottom:.4rem}.page-bottom .van-tabbar-item__icon .df-icon[data-v-4415c7f8]{font-size:26px}.page-bottom .van-tabbar-item__icon img[data-v-4415c7f8]{height:20px}.page-enter-active[data-v-4415c7f8],.page-leave-active[data-v-4415c7f8],.page-old[data-v-4415c7f8]{transition-duration:.5s;transition-timing-function:cubic-bezier(.36,.66,.04,1);transition-property:opacity,transform}[transition-direction=forward] .page-old[data-v-4415c7f8]{transform:translate3d(-80%,0,0);transition-duration:.55s;opacity:.8}[transition-direction=forward] .page-enter[data-v-4415c7f8]{transform:translate3d(100%,0,0);opacity:1;z-index:2}[transition-direction=forward] .page-enter-active[data-v-4415c7f8]{box-shadow:0 0 10px rgba(0,0,0,.15)}[transition-direction=forward] .page-enter-to[data-v-4415c7f8]{transform:translateZ(0);opacity:1;z-index:2}[transition-direction=forward] .page-leave[data-v-4415c7f8]{transform:translateZ(0);opacity:.8;z-index:0}[transition-direction=forward] .page-leave-to[data-v-4415c7f8]{transform:translate3d(-33%,0,0);opacity:0;z-index:0}[transition-direction=back] .page-old[data-v-4415c7f8]{transform:translate3d(100%,0,0);box-shadow:0 0 10px rgba(0,0,0,.15)}[transition-direction=back] .page-enter[data-v-4415c7f8]{transform:translate3d(-33%,0,0);opacity:.8;z-index:-1}[transition-direction=back] .page-enter-to[data-v-4415c7f8]{transform:translateZ(0);opacity:1;z-index:-1}[transition-direction=back] .page-leave[data-v-4415c7f8]{opacity:0}[transition-direction=none] .page-enter-active[data-v-4415c7f8],[transition-direction=none] .page-leave-active[data-v-4415c7f8]{transition-duration:0s}.page .floor[data-v-4415c7f8]{width:100%;box-sizing:border-box;color:#383838}.page .floor .title[data-v-4415c7f8]{position:relative;padding:.4rem}.page .floor .title .title-text[data-v-4415c7f8]{display:inline-block;font-weight:700;font-size:.8rem;color:#383838}.page .floor .title .sub-title[data-v-4415c7f8]{display:inline-block;margin-left:.4rem;height:.825rem;line-height:.825rem;letter-spacing:1px;color:#383838;font-size:.6rem;vertical-align:middle}.page .floor .title .lnk-more[data-v-4415c7f8]{position:absolute;bottom:.15rem;right:.4rem;display:inline-block;height:1.15rem;color:#707070;font-size:.5rem;text-align:center}.page .floor .title.large .title-text[data-v-4415c7f8]{font-size:1rem}.page .floor .floor-title2[data-v-4415c7f8]{position:relative;height:1.25rem}.page .floor .floor-title2 .title-text[data-v-4415c7f8]{position:absolute;left:50%;transform:translateX(-50%);display:inline-block;padding:0 1rem;font-size:.9rem;font-weight:700;color:#885332;white-space:nowrap}.page .floor .floor-title2[data-v-4415c7f8]:before{content:"";position:absolute;z-index:0;top:50%;left:.4rem;right:.4rem;height:.1rem;background:#ad8863}.good-item-list[data-v-4415c7f8],.page .floor .floor-content[data-v-4415c7f8]{width:100%;box-sizing:border-box}.good-item-list[data-v-4415c7f8]{display:flex;align-items:flex-start;flex-wrap:wrap;padding:0 .2rem;text-align:left}.good-item-list .good-item-wrap[data-v-4415c7f8]{width:100%;box-sizing:border-box;padding:.2rem}.good-item-list.col2 .good-item-wrap[data-v-4415c7f8]{width:50%}.good-item-list.col3 .good-item-wrap[data-v-4415c7f8]{width:33.333%}.main-origins .van-collapse-item__content[data-v-4415c7f8]{padding:0}input[data-v-4415c7f8]{-webkit-appearance:none}.hide[data-v-4415c7f8]{display:none!important}.clear-fix[data-v-4415c7f8]{clear:both;zoom:1}.clear-fix[data-v-4415c7f8]:after{clear:both;display:block;visibility:hidden;font-size:0;content:" ";height:0}.float-left[data-v-4415c7f8]{float:left}.float-right[data-v-4415c7f8]{float:right}.arrow-up[data-v-4415c7f8]{width:0;height:0;border-left:30px solid transparent;border-right:30px solid transparent;border-bottom:30px solid #fff}.swiper-container[data-v-4415c7f8]{width:100%;font-size:0}.swiper-slide[data-v-4415c7f8]{text-align:center}.swiper-slide img[data-v-4415c7f8]{width:100%}.scroll-box[data-v-4415c7f8]{background:#fff}.scroll-box .scroll-banner[data-v-4415c7f8]{position:relative}.scroll-box .scroll-banner img[data-v-4415c7f8]{display:block;width:100%}.scroll-box .scroll-banner .arrow[data-v-4415c7f8]{position:absolute;left:50%;bottom:0;margin-left:-8px;display:block;width:0;height:0;border:8px solid transparent;border-top:none;border-bottom:8px solid #fff}.scroll-box .scroll-con[data-v-4415c7f8]{width:100%;overflow:hidden}.scroll-box .scroll-con a[data-v-4415c7f8]{display:block}.scroll-box ul[data-v-4415c7f8]{margin:10px 0 10px 5px;position:relative;padding-right:10px}.scroll-box li[data-v-4415c7f8]{display:none;float:left;width:40%;padding:0 5px;box-sizing:border-box}.scroll-box li[data-v-4415c7f8]:nth-of-type(3){position:absolute;top:0;right:0;transform:translateX(50%)}.scroll-box li[data-v-4415c7f8]:first-of-type,.scroll-box li[data-v-4415c7f8]:nth-of-type(2),.scroll-box li[data-v-4415c7f8]:nth-of-type(3){display:block}.scroll-box li .checkmore[data-v-4415c7f8]{display:block;width:100%;padding-bottom:100%;background:#f0f0f0;position:relative}.scroll-box li .more-txt[data-v-4415c7f8]{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);font-size:.6rem;line-height:2.2rem;text-align:center}.scroll-box li .more-txt .cn[data-v-4415c7f8]{color:#b48b5a;display:block;padding:0 2px;border:1px solid #f0f0f0;border-bottom-color:#ccc}.scroll-box li .more-txt .en[data-v-4415c7f8]{color:#333}.scroll_ready li[data-v-4415c7f8]{display:block}.scroll_ready li[data-v-4415c7f8]:nth-of-type(3){position:static;transform:translateX(0)}.scroll-box .img[data-v-4415c7f8]{position:relative;width:100%;padding-bottom:100%}.scroll-box .img img[data-v-4415c7f8]{position:absolute;top:0;left:0;width:100%;height:100%}.scroll-box .img img.saleout-icon[data-v-4415c7f8]{position:absolute;top:30%;left:25%;width:50%!important;height:auto!important;z-index:2}.scroll-box .link-info[data-v-4415c7f8]{position:absolute;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,.4)}.scroll-box .link-info .v-c[data-v-4415c7f8]{position:absolute;top:50%;left:0;width:100%;transform:translateY(-50%)}.scroll-box .link-info p[data-v-4415c7f8]{width:100%;text-align:center;font-size:.7rem;color:#fff}.scroll-box .link-info .line[data-v-4415c7f8]{width:42.86%;height:1px;background:#fff;overflow:hidden;margin:8px auto 0}.scroll-box .desc[data-v-4415c7f8]{text-align:center;font-size:.6rem;color:#333;padding:6px 0 10px}.scroll-box .more[data-v-4415c7f8]{margin-top:2px;text-align:center}.scroll-box .brand[data-v-4415c7f8],.scroll-box .name[data-v-4415c7f8]{font-size:.6rem;line-height:1.5rem;color:#666;text-align:center;padding:0 5px}.scroll-box .price[data-v-4415c7f8]{float:left;color:#b48b5a}.scroll-box .price[data-v-4415c7f8],.scroll-box .price-old[data-v-4415c7f8]{margin-top:4px;font-size:.6rem;line-height:1.2rem}.scroll-box .price-old[data-v-4415c7f8]{float:right;color:#ccc}input[type=checkbox][data-v-4415c7f8]:checked,input[type=radio][data-v-4415c7f8]:checked{background-position:-20px 0;border:none}input[disabled][data-v-4415c7f8]{opacity:.5!important}.input-with-label[data-v-4415c7f8]{margin-top:5px;width:100%;line-height:30px}.input-with-label *[data-v-4415c7f8]{box-sizing:border-box;-webkit-box-sizing:border-box}.input-with-label span[data-v-4415c7f8]{display:inline-block;width:22%}.input-with-label input[data-v-4415c7f8]{width:78%;padding:0 10px}.point-right[data-v-4415c7f8]{transform:rotate(45deg)}.point-down[data-v-4415c7f8],.point-right[data-v-4415c7f8]{display:inline-block;width:.5rem;height:.5rem;border-top:2px solid #383838;border-right:2px solid #383838}.point-down[data-v-4415c7f8]{transform:rotate(135deg)}.tip[data-v-4415c7f8]{display:inline-block;width:1.725rem;height:1.75rem;line-height:1.75rem;border-radius:100px;background-color:#c20318}.triangle-down[data-v-4415c7f8]{width:0;height:0;border-left:.3rem solid transparent;border-right:.3rem solid transparent;border-top:.3rem solid #c20318;font-size:0}.selectFlag[data-v-4415c7f8]{display:inline-block;width:1.1rem;height:1.1rem;line-height:.95rem;background-color:#fff;border:1px solid #999;border-radius:200px;text-align:center;box-sizing:border-box}.selectFlag em[data-v-4415c7f8]{display:none}.focuson[data-v-4415c7f8]{border:0;background-color:#1f1f1f}.focuson em[data-v-4415c7f8]{display:inline-block;width:.55rem;height:.3rem;line-height:.4rem;border-left:2px solid #fff;border-bottom:2px solid #fff;transform:rotate(-45deg)}.errorToast[data-v-4415c7f8]{background-color:rgba(0,0,0,.5)!important;padding-left:1.35rem!important;padding-right:1.35rem!important;border-radius:100px!important}.scroll-x[data-v-4415c7f8]{overflow-x:scroll;overflow-y:hidden}.scroll-y[data-v-4415c7f8]{overflow-y:scroll;overflow-x:hidden}.scroll-x[data-v-4415c7f8],.scroll-y[data-v-4415c7f8]{-webkit-overflow-scrolling:touch}.mt20[data-v-4415c7f8]{margin-top:.5rem}.mb20[data-v-4415c7f8]{margin-bottom:.5rem}.mt16[data-v-4415c7f8],.mt32[data-v-4415c7f8]{margin-top:.4rem}.mt48[data-v-4415c7f8]{margin-top:1.2rem}.mb32[data-v-4415c7f8]{margin-bottom:.4rem}.hpd16[data-v-4415c7f8]{padding-left:.4rem;padding-right:.4rem}.vpd16[data-v-4415c7f8]{padding-top:.4rem;padding-bottom:.4rem}.pdt0[data-v-4415c7f8]{padding-top:0!important}.mr5[data-v-4415c7f8]{margin-right:5px}.mr10[data-v-4415c7f8]{margin-right:10px}.disabled[data-v-4415c7f8]{color:#999}.middle[data-v-4415c7f8]{display:inline-block;vertical-align:middle}.van-switch--on[data-v-4415c7f8]{background-color:#1f1f1f!important}[data-v-4415c7f8]::-webkit-scrollbar{width:0;height:0}.van-nav-bar[data-v-4415c7f8],.van-nav-bar__title[data-v-4415c7f8]{background:#fff!important}.van-nav-bar__title[data-v-4415c7f8]{font-size:.8rem!important;font-weight:400!important}.van-nav-bar .van-icon[data-v-4415c7f8],.van-nav-bar__title[data-v-4415c7f8]{color:#606266!important}.van-nav-bar__left[data-v-4415c7f8],.van-nav-bar__right[data-v-4415c7f8]{padding:0 .7rem!important}.tomford-col .van-grid-item__content[data-v-4415c7f8]{padding:0!important}.van-dialog[data-v-4415c7f8]{border-radius:.4rem}.price-color[data-v-4415c7f8],.rise[data-v-4415c7f8]{color:red!important}.rise[data-v-4415c7f8]{font-size:.5rem;display:inline-block}.nav-box .van-tabs__nav .van-tabs__line[data-v-4415c7f8]{display:none!important}.ios-bottom[data-v-4415c7f8]{padding-bottom:env(safe-area-inset-bottom)!important}.dj-swiper .van-swipe__indicator[data-v-4415c7f8]{width:.5rem!important;height:.5rem!important}.dj-swiper .van-swipe__indicator[data-v-4415c7f8]:not(:last-child){margin-right:.5rem!important}.module-swiper .van-swipe__indicator[data-v-4415c7f8]{width:.5rem!important;height:.5rem!important;border:1px solid #000!important;background-color:#fff}.module-swiper .van-swipe__indicator[data-v-4415c7f8]:not(:last-child){margin-right:.5rem!important}.ydstxt[data-v-4415c7f8]{text-decoration:underline}.common-header[data-v-4415c7f8],.header-holder[data-v-4415c7f8]{width:100%;height:2.2rem}.common-header[data-v-4415c7f8]{position:fixed;z-index:1000;top:0;right:0;left:0;background-color:#fff;border-bottom:1px solid #efefef}.common-header .back[data-v-4415c7f8]{position:absolute;left:0;top:0;padding:0 .5rem;width:auto;height:auto;line-height:2.2rem;background-color:transparent;border:none;color:#1f1f1f}.common-header .back span[data-v-4415c7f8]{display:inline-block;padding:.05rem 0 0 2.2rem}.common-header .back .iconfont[data-v-4415c7f8]{font-size:1rem;color:#999}.common-header .title[data-v-4415c7f8]{display:block;margin:0 auto;width:60%;line-height:2.2rem;text-align:center;font-size:1rem;color:#121212}.common-header .menu[data-v-4415c7f8]{position:absolute;top:50%;right:.5rem;transform:translateY(-50%)}.common-header .menu li[data-v-4415c7f8]{float:left;margin-right:.1rem}.common-header .menu li a.ico[data-v-4415c7f8]{display:block;width:1.5rem;height:1.5rem;font-size:.75rem;border:1px solid #999;text-align:center;color:#999;border-radius:100%;box-sizing:border-box}.common-header .menu li a.ico em[data-v-4415c7f8]{display:inline-block;line-height:1.5rem;font-size:.9rem}.common-header .menu li a.txt[data-v-4415c7f8]{color:#999;font-size:.6rem}.common-header .header-arrow[data-v-4415c7f8]{display:none;position:absolute;bottom:0;right:15px;margin-left:-7px;width:0;height:0;border:.35rem solid transparent;border-top:none;border-bottom:.35rem solid #000}.common-header .header-drop[data-v-4415c7f8]{display:none;width:100%;background:#000}.common-header .header-drop ul[data-v-4415c7f8]{padding:7px 0 4px;width:100%;overflow:hidden;background:#000}.common-header .header-drop li[data-v-4415c7f8]{width:25%;float:left;text-align:center}.common-header .header-drop li a[data-v-4415c7f8]{line-height:0}.common-header .header-drop li .icon[data-v-4415c7f8]{display:block;margin:0 auto}.common-header .header-drop li .txt[data-v-4415c7f8]{color:#1f1f1f;line-height:20px;display:block;margin:0 auto;font-size:14px}.common-header .right-bar[data-v-4415c7f8]{position:absolute;top:5px;right:15px}.common-header .icon[data-v-4415c7f8]{display:inline-block}.common-header .icon-about[data-v-4415c7f8]{width:22px;height:22px;background:url(/images/user/about.png);background-size:100% 100%;margin-top:9px;overflow:hidden}.common-header .txt-btn[data-v-4415c7f8]{padding:0 .5rem;line-height:2.2rem;position:absolute;top:0;right:0;font-size:.7rem}.common-header .txt-btn a[data-v-4415c7f8]{color:#999}.text-overflow[data-v-4415c7f8]{text-overflow:ellipsis;white-space:nowrap;overflow:hidden}.text-left[data-v-4415c7f8]{text-align:left}.text-right[data-v-4415c7f8]{text-align:right}.text-center[data-v-4415c7f8]{text-align:center}.text-ellipsis1[data-v-4415c7f8]{overflow:hidden;white-space:nowrap;text-overflow:ellipsis;word-break:break-all}.text-ellipsis2[data-v-4415c7f8]{-webkit-line-clamp:2}.text-ellipsis2[data-v-4415c7f8],.text-ellipsis3[data-v-4415c7f8]{overflow:hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-box-orient:vertical;word-wrap:break-word}.text-ellipsis3[data-v-4415c7f8]{-webkit-line-clamp:3}.font-sm[data-v-4415c7f8]{font-size:.6rem}.font-normal[data-v-4415c7f8]{font-size:.7rem}.font-lg[data-v-4415c7f8]{font-size:.8rem}.page .mint-button[data-v-4415c7f8]{font-weight:700}.page .mint-button--primary[data-v-4415c7f8]{background-color:#1f1f1f!important}.page .mint-button--large[data-v-4415c7f8]{height:2.75rem!important;font-size:.8rem!important}.mint-msgbox-confirm[data-v-4415c7f8]{color:#333!important}.mint-indicator-wrapper[data-v-4415c7f8]{z-index:9999}.mint-button--small[data-v-4415c7f8]{font-size:.6rem!important;height:1rem!important}.mint-button--normal[data-v-4415c7f8]{font-size:.7rem!important;height:1.5rem!important}.mint-button--large[data-v-4415c7f8]{font-size:.8rem!important;height:2rem!important}.mint-indicator-wrapper[data-v-4415c7f8]{background-color:transparent!important}.page .van-button--primary[data-v-4415c7f8]{color:#fff;background:linear-gradient(180deg,#1f1f1f,#1f1f1f);border:none}#YSF-BTN-HOLDER[data-v-4415c7f8]{display:none!important;right:.4rem!important;bottom:2.5rem!important}#YSF-CUSTOM-ENTRY-7 img[data-v-4415c7f8]{width:2rem!important}.color-gray[data-v-4415c7f8]{color:#707070}.color-more-gray[data-v-4415c7f8]{color:#999}.color-white[data-v-4415c7f8]{color:#fff}.color-primary[data-v-4415c7f8]{color:#1f1f1f}.font28[data-v-4415c7f8]{font-size:.7rem}.error-page[data-v-4415c7f8]{color:#000;text-align:center}.error-page .error-head[data-v-4415c7f8]{padding-top:3rem;background-color:#fff}.error-page .headimg[data-v-4415c7f8]{display:inline-block;margin:2.5rem 0;color:#1a8ca4;font-size:3rem}.error-page .error-con[data-v-4415c7f8]{margin-bottom:.5rem;padding:1rem 0 2rem;width:100%;background:#fff;border-bottom:1px solid #999}.error-page .error-con *[data-v-4415c7f8]{box-sizing:border-box}.error-page .error-code[data-v-4415c7f8]{display:inline-block;vertical-align:middle;padding:0 .5rem;width:50%;border-right:1px solid rgba(0,0,0,.298039);text-align:right;color:#333}.error-page .error-wrapper-message[data-v-4415c7f8]{display:inline-block;width:100%;vertical-align:middle;padding:0 .5rem;text-align:center}.error-page .error-message[data-v-4415c7f8]{margin:0;padding:0;color:#333}.error-page .todo[data-v-4415c7f8]{padding:.5rem;width:100%;text-align:left;background:#fff;border-bottom:1px solid #999}.error-page .todo[data-v-4415c7f8],.error-page .todo *[data-v-4415c7f8]{box-sizing:border-box}.error-page .todo .desc[data-v-4415c7f8]{color:#666;font-size:.7rem}.error-page .todo .desc.desc2[data-v-4415c7f8]{padding-top:.5rem}.error-page .todo .error-link[data-v-4415c7f8]{display:inline-block;margin:0 .25rem;padding:.5rem .5rem 0;color:#666;font-weight:400;text-decoration:none;font-size:.7rem}', ""]),
        e.exports = o
    },
    277: function(e, t, n) {
        "use strict";
        n(177)
    },
    278: function(e, t, n) {
        var o = n(7)(!1);
        o.push([e.i, ".nuxt-progress{position:fixed;top:0;left:0;right:0;height:2px;width:0;opacity:1;transition:width .1s,opacity .4s;background-color:#1a8ca4;z-index:999999}.nuxt-progress.nuxt-progress-notransition{transition:none}.nuxt-progress-failed{background-color:red}", ""]),
        e.exports = o
    },
    279: function(e, t, n) {
        var content = n(280);
        "string" == typeof content && (content = [[e.i, content, ""]]),
        content.locals && (e.exports = content.locals);
        (0,
        n(8).default)("3e001b99", content, !0, {
            sourceMap: !1
        })
    },
    280: function(e, t, n) {
        var o = n(7)(!1);
        o.push([e.i, '/*! normalize.css v4.1.1 | MIT License | github.com/necolas/normalize.css */.color-gray{color:#707070}.color-more-gray{color:#999}.color-white{color:#fff}.color-primary{color:#1f1f1f}.font28{font-size:.7rem}/*! normalize.css v4.1.1 | MIT License | github.com/necolas/normalize.css */html{font-family:"PingFang SC","Microsoft YaHei";-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}article,aside,details,figcaption,figure,footer,header,main,menu,nav,section,summary{display:block}audio,canvas,progress,video{display:inline-block}audio:not([controls]){display:none;height:0}progress{vertical-align:baseline}[hidden],template{display:none}a{background-color:transparent;-webkit-text-decoration-skip:objects;text-decoration:none}a:active,a:hover{outline-width:0}a:hover,a:link,a:visited{color:#383838;text-decoration:none}abbr[title]{border-bottom:none;text-decoration:underline;-webkit-text-decoration:underline dotted;text-decoration:underline dotted}b,strong{font-weight:inherit;font-weight:bolder}dfn{font-style:italic}h1{font-size:2em;margin:.67em 0}mark{background-color:#ff0;color:#000}small{font-size:80%}sub,sup{font-size:75%;line-height:0;position:relative;vertical-align:baseline}sub{bottom:-.25em}sup{top:-.5em}img{border-style:none}svg:not(:root){overflow:hidden}code,kbd,pre,samp{font-family:monospace,monospace;font-size:1em}figure{margin:1em 40px}hr{box-sizing:content-box;height:0;overflow:visible}button,input,select,textarea{font:inherit;margin:0;outline:none}optgroup{font-weight:700}button,input{overflow:visible}button,select{text-transform:none}[type=reset],[type=submit],button,html [type=button]{-webkit-appearance:button}[type=button]::-moz-focus-inner,[type=reset]::-moz-focus-inner,[type=submit]::-moz-focus-inner,button::-moz-focus-inner{border-style:none;padding:0}[type=button]:-moz-focusring,[type=reset]:-moz-focusring,[type=submit]:-moz-focusring,button:-moz-focusring{outline:1px dotted ButtonText}fieldset{border:1px solid silver;margin:0 2px;padding:.35em .625em .75em}legend{box-sizing:border-box;color:inherit;display:table;max-width:100%;padding:0;white-space:normal}textarea{overflow:auto}[type=checkbox],[type=radio]{box-sizing:border-box;padding:0}[type=number]::-webkit-inner-spin-button,[type=number]::-webkit-outer-spin-button{height:auto}[type=search]{-webkit-appearance:textfield;outline-offset:-2px}[type=search]::-webkit-search-cancel-button,[type=search]::-webkit-search-decoration{-webkit-appearance:none}::-webkit-input-placeholder{color:inherit;opacity:.54}::-webkit-file-upload-button{-webkit-appearance:button;font:inherit}dl,ol,ul{list-style-type:none}body,dd,dl,dt,form,h1,h2,h3,h4,h5,h6,html,img,li,ol,p,table,td,textarea,th,tr,ul{margin:0;padding:0}em,i{font-style:normal}html{width:100%;height:100%}@media screen and (max-width:320px){html{font-size:17.0666667px}}@media screen and (max-width:374px){html{font-size:19.2px}}@media screen and (min-width:375px){html{font-size:20px}}@media screen and (min-width:414px){html{font-size:22.08px}}@media screen and (min-width:768px){html{font-size:40.96px}}@media screen and (min-width:1024px){html{font-size:54.6133333px}}body{position:relative;margin:0;background-color:#f9f9f9;color:#383838;font-size:.6rem}#__layout,#__nuxt,.page-container,body{width:100%;height:100%;overflow:hidden}.page{position:absolute;top:0;right:0;bottom:0;left:0;width:100%;box-sizing:border-box;overflow:hidden;background:#f9f9f9}.page .page-header{position:absolute!important;top:0;right:0;left:0;background:#fff}.page .page-content{position:absolute;top:0;right:0;left:0;bottom:0;overflow-x:hidden;overflow-y:auto;overflow-scrolling:touch;-webkit-overflow-scrolling:touch}.page.has-nav .page-content{top:2.3rem}.page.has-bottom .page-content{bottom:50px}.page .page-section{margin-bottom:.4rem}.page-bottom .van-tabbar-item__icon .df-icon{font-size:26px}.page-bottom .van-tabbar-item__icon img{height:20px}.page-enter-active,.page-leave-active,.page-old{transition-duration:.5s;transition-timing-function:cubic-bezier(.36,.66,.04,1);transition-property:opacity,transform}[transition-direction=forward] .page-old{transform:translate3d(-80%,0,0);transition-duration:.55s;opacity:.8}[transition-direction=forward] .page-enter{transform:translate3d(100%,0,0);opacity:1;z-index:2}[transition-direction=forward] .page-enter-active{box-shadow:0 0 10px rgba(0,0,0,.15)}[transition-direction=forward] .page-enter-to{transform:translateZ(0);opacity:1;z-index:2}[transition-direction=forward] .page-leave{transform:translateZ(0);opacity:.8;z-index:0}[transition-direction=forward] .page-leave-to{transform:translate3d(-33%,0,0);opacity:0;z-index:0}[transition-direction=back] .page-old{transform:translate3d(100%,0,0);box-shadow:0 0 10px rgba(0,0,0,.15)}[transition-direction=back] .page-enter{transform:translate3d(-33%,0,0);opacity:.8;z-index:-1}[transition-direction=back] .page-enter-to{transform:translateZ(0);opacity:1;z-index:-1}[transition-direction=back] .page-leave{opacity:0}[transition-direction=none] .page-enter-active,[transition-direction=none] .page-leave-active{transition-duration:0s}.page .floor{width:100%;box-sizing:border-box;color:#383838}.page .floor .title{position:relative;padding:.4rem}.page .floor .title .title-text{display:inline-block;font-weight:700;font-size:.8rem;color:#383838}.page .floor .title .sub-title{display:inline-block;margin-left:.4rem;height:.825rem;line-height:.825rem;letter-spacing:1px;color:#383838;font-size:.6rem;vertical-align:middle}.page .floor .title .lnk-more{position:absolute;bottom:.15rem;right:.4rem;display:inline-block;height:1.15rem;color:#707070;font-size:.5rem;text-align:center}.page .floor .title.large .title-text{font-size:1rem}.page .floor .floor-title2{position:relative;height:1.25rem}.page .floor .floor-title2 .title-text{position:absolute;left:50%;transform:translateX(-50%);display:inline-block;padding:0 1rem;font-size:.9rem;font-weight:700;color:#885332;white-space:nowrap}.page .floor .floor-title2:before{content:"";position:absolute;z-index:0;top:50%;left:.4rem;right:.4rem;height:.1rem;background:#ad8863}.good-item-list,.page .floor .floor-content{width:100%;box-sizing:border-box}.good-item-list{display:flex;align-items:flex-start;flex-wrap:wrap;padding:0 .2rem;text-align:left}.good-item-list .good-item-wrap{width:100%;box-sizing:border-box;padding:.2rem}.good-item-list.col2 .good-item-wrap{width:50%}.good-item-list.col3 .good-item-wrap{width:33.333%}.main-origins .van-collapse-item__content{padding:0}input{-webkit-appearance:none}.hide{display:none!important}.clear-fix{clear:both;zoom:1}.clear-fix:after{clear:both;display:block;visibility:hidden;font-size:0;content:" ";height:0}.float-left{float:left}.float-right{float:right}.arrow-up{width:0;height:0;border-left:30px solid transparent;border-right:30px solid transparent;border-bottom:30px solid #fff}.swiper-container{width:100%;font-size:0}.swiper-slide{text-align:center}.swiper-slide img{width:100%}.scroll-box{background:#fff}.scroll-box .scroll-banner{position:relative}.scroll-box .scroll-banner img{display:block;width:100%}.scroll-box .scroll-banner .arrow{position:absolute;left:50%;bottom:0;margin-left:-8px;display:block;width:0;height:0;border:8px solid transparent;border-top:none;border-bottom:8px solid #fff}.scroll-box .scroll-con{width:100%;overflow:hidden}.scroll-box .scroll-con a{display:block}.scroll-box ul{margin:10px 0 10px 5px;position:relative;padding-right:10px}.scroll-box li{display:none;float:left;width:40%;padding:0 5px;box-sizing:border-box}.scroll-box li:nth-of-type(3){position:absolute;top:0;right:0;transform:translateX(50%)}.scroll-box li:first-of-type,.scroll-box li:nth-of-type(2),.scroll-box li:nth-of-type(3){display:block}.scroll-box li .checkmore{display:block;width:100%;padding-bottom:100%;background:#f0f0f0;position:relative}.scroll-box li .more-txt{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);font-size:.6rem;line-height:2.2rem;text-align:center}.scroll-box li .more-txt .cn{color:#b48b5a;display:block;padding:0 2px;border:1px solid #f0f0f0;border-bottom-color:#ccc}.scroll-box li .more-txt .en{color:#333}.scroll_ready li{display:block}.scroll_ready li:nth-of-type(3){position:static;transform:translateX(0)}.scroll-box .img{position:relative;width:100%;padding-bottom:100%}.scroll-box .img img{position:absolute;top:0;left:0;width:100%;height:100%}.scroll-box .img img.saleout-icon{position:absolute;top:30%;left:25%;width:50%!important;height:auto!important;z-index:2}.scroll-box .link-info{position:absolute;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,.4)}.scroll-box .link-info .v-c{position:absolute;top:50%;left:0;width:100%;transform:translateY(-50%)}.scroll-box .link-info p{width:100%;text-align:center;font-size:.7rem;color:#fff}.scroll-box .link-info .line{width:42.86%;height:1px;background:#fff;overflow:hidden;margin:8px auto 0}.scroll-box .desc{text-align:center;font-size:.6rem;color:#333;padding:6px 0 10px}.scroll-box .more{margin-top:2px;text-align:center}.scroll-box .brand,.scroll-box .name{font-size:.6rem;line-height:1.5rem;color:#666;text-align:center;padding:0 5px}.scroll-box .price{float:left;color:#b48b5a}.scroll-box .price,.scroll-box .price-old{margin-top:4px;font-size:.6rem;line-height:1.2rem}.scroll-box .price-old{float:right;color:#ccc}input[type=checkbox]:checked,input[type=radio]:checked{background-position:-20px 0;border:none}input[disabled]{opacity:.5!important}.input-with-label{margin-top:5px;width:100%;line-height:30px}.input-with-label *{box-sizing:border-box;-webkit-box-sizing:border-box}.input-with-label span{display:inline-block;width:22%}.input-with-label input{width:78%;padding:0 10px}.point-right{transform:rotate(45deg)}.point-down,.point-right{display:inline-block;width:.5rem;height:.5rem;border-top:2px solid #383838;border-right:2px solid #383838}.point-down{transform:rotate(135deg)}.tip{display:inline-block;width:1.725rem;height:1.75rem;line-height:1.75rem;border-radius:100px;background-color:#c20318}.triangle-down{width:0;height:0;border-left:.3rem solid transparent;border-right:.3rem solid transparent;border-top:.3rem solid #c20318;font-size:0}.selectFlag{display:inline-block;width:1.1rem;height:1.1rem;line-height:.95rem;background-color:#fff;border:1px solid #999;border-radius:200px;text-align:center;box-sizing:border-box}.selectFlag em{display:none}.focuson{border:0;background-color:#1f1f1f}.focuson em{display:inline-block;width:.55rem;height:.3rem;line-height:.4rem;border-left:2px solid #fff;border-bottom:2px solid #fff;transform:rotate(-45deg)}.errorToast{background-color:rgba(0,0,0,.5)!important;padding-left:1.35rem!important;padding-right:1.35rem!important;border-radius:100px!important}.scroll-x{overflow-x:scroll;overflow-y:hidden}.scroll-y{overflow-y:scroll;overflow-x:hidden}.scroll-x,.scroll-y{-webkit-overflow-scrolling:touch}.mt20{margin-top:.5rem}.mb20{margin-bottom:.5rem}.mt16,.mt32{margin-top:.4rem}.mt48{margin-top:1.2rem}.mb32{margin-bottom:.4rem}.hpd16{padding-left:.4rem;padding-right:.4rem}.vpd16{padding-top:.4rem;padding-bottom:.4rem}.pdt0{padding-top:0!important}.mr5{margin-right:5px}.mr10{margin-right:10px}.disabled{color:#999}.middle{display:inline-block;vertical-align:middle}.van-switch--on{background-color:#1f1f1f!important}::-webkit-scrollbar{width:0;height:0}.van-nav-bar,.van-nav-bar__title{background:#fff!important}.van-nav-bar__title{font-size:.8rem!important;font-weight:400!important}.van-nav-bar .van-icon,.van-nav-bar__title{color:#606266!important}.van-nav-bar__left,.van-nav-bar__right{padding:0 .7rem!important}.tomford-col .van-grid-item__content{padding:0!important}.van-dialog{border-radius:.4rem}.price-color,.rise{color:red!important}.rise{font-size:.5rem;display:inline-block}.nav-box .van-tabs__nav .van-tabs__line{display:none!important}.ios-bottom{padding-bottom:env(safe-area-inset-bottom)!important}.dj-swiper .van-swipe__indicator{width:.5rem!important;height:.5rem!important}.dj-swiper .van-swipe__indicator:not(:last-child){margin-right:.5rem!important}.module-swiper .van-swipe__indicator{width:.5rem!important;height:.5rem!important;border:1px solid #000!important;background-color:#fff}.module-swiper .van-swipe__indicator:not(:last-child){margin-right:.5rem!important}.ydstxt{text-decoration:underline}.common-header,.header-holder{width:100%;height:2.2rem}.common-header{position:fixed;z-index:1000;top:0;right:0;left:0;background-color:#fff;border-bottom:1px solid #efefef}.common-header .back{position:absolute;left:0;top:0;padding:0 .5rem;width:auto;height:auto;line-height:2.2rem;background-color:transparent;border:none;color:#1f1f1f}.common-header .back span{display:inline-block;padding:.05rem 0 0 2.2rem}.common-header .back .iconfont{font-size:1rem;color:#999}.common-header .title{display:block;margin:0 auto;width:60%;line-height:2.2rem;text-align:center;font-size:1rem;color:#121212}.common-header .menu{position:absolute;top:50%;right:.5rem;transform:translateY(-50%)}.common-header .menu li{float:left;margin-right:.1rem}.common-header .menu li a.ico{display:block;width:1.5rem;height:1.5rem;font-size:.75rem;border:1px solid #999;text-align:center;color:#999;border-radius:100%;box-sizing:border-box}.common-header .menu li a.ico em{display:inline-block;line-height:1.5rem;font-size:.9rem}.common-header .menu li a.txt{color:#999;font-size:.6rem}.common-header .header-arrow{display:none;position:absolute;bottom:0;right:15px;margin-left:-7px;width:0;height:0;border:.35rem solid transparent;border-top:none;border-bottom:.35rem solid #000}.common-header .header-drop{display:none;width:100%;background:#000}.common-header .header-drop ul{padding:7px 0 4px;width:100%;overflow:hidden;background:#000}.common-header .header-drop li{width:25%;float:left;text-align:center}.common-header .header-drop li a{line-height:0}.common-header .header-drop li .icon{display:block;margin:0 auto}.common-header .header-drop li .txt{color:#1f1f1f;line-height:20px;display:block;margin:0 auto;font-size:14px}.common-header .right-bar{position:absolute;top:5px;right:15px}.common-header .icon{display:inline-block}.common-header .icon-about{width:22px;height:22px;background:url(/images/user/about.png);background-size:100% 100%;margin-top:9px;overflow:hidden}.common-header .txt-btn{padding:0 .5rem;line-height:2.2rem;position:absolute;top:0;right:0;font-size:.7rem}.common-header .txt-btn a{color:#999}.text-overflow{text-overflow:ellipsis;white-space:nowrap;overflow:hidden}.text-left{text-align:left}.text-right{text-align:right}.text-center{text-align:center}.text-ellipsis1{overflow:hidden;white-space:nowrap;text-overflow:ellipsis;word-break:break-all}.text-ellipsis2{-webkit-line-clamp:2}.text-ellipsis2,.text-ellipsis3{overflow:hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-box-orient:vertical;word-wrap:break-word}.text-ellipsis3{-webkit-line-clamp:3}.font-sm{font-size:.6rem}.font-normal{font-size:.7rem}.font-lg{font-size:.8rem}.page .mint-button{font-weight:700}.page .mint-button--primary{background-color:#1f1f1f!important}.page .mint-button--large{height:2.75rem!important;font-size:.8rem!important}.mint-msgbox-confirm{color:#333!important}.mint-indicator-wrapper{z-index:9999}.mint-button--small{font-size:.6rem!important;height:1rem!important}.mint-button--normal{font-size:.7rem!important;height:1.5rem!important}.mint-button--large{font-size:.8rem!important;height:2rem!important}.mint-indicator-wrapper{background-color:transparent!important}.page .van-button--primary{color:#fff;background:linear-gradient(180deg,#1f1f1f,#1f1f1f);border:none}#YSF-BTN-HOLDER{display:none!important;right:.4rem!important;bottom:2.5rem!important}#YSF-CUSTOM-ENTRY-7 img{width:2rem!important}', ""]),
        e.exports = o
    },
    283: function(e, t, n) {
        var content = n(284);
        "string" == typeof content && (content = [[e.i, content, ""]]),
        content.locals && (e.exports = content.locals);
        (0,
        n(8).default)("1c23f4a8", content, !0, {
            sourceMap: !1
        })
    },
    284: function(e, t, n) {
        var o = n(7)
          , r = n(150)
          , l = n(285)
          , c = n(286)
          , d = n(287)
          , f = o(!1)
          , m = r(l)
          , h = r(c)
          , v = r(d);
        f.push([e.i, '@font-face{font-family:"df-icon";src:url(' + m + ') format("woff2"),url(' + h + ') format("woff"),url(' + v + ') format("truetype")}.df-icon{font-family:"df-icon"!important;font-size:16px;font-style:normal;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.df-icon-brand_selected:before{content:"\\e63a"}.df-icon-brand:before{content:"\\e638"}.df-icon-filter2x:before{content:"\\e628"}.df-icon-you:before{content:"\\e637"}.df-icon-shouyintai:before{content:"\\e635"}.df-icon-hongbao:before{content:"\\e61e"}.df-icon-right-arrow-1:before{content:"\\e699"}.df-icon-VIP:before{content:"\\e70a"}.df-icon-location_round:before{content:"\\e6aa"}.df-icon-logo:before{content:"\\e634"}.df-icon-kefu:before{content:"\\e620"}.df-icon-Refresh:before{content:"\\e61d"}.df-icon-buhuoing:before{content:"\\e61c"}.df-icon-iconset0113:before{content:"\\e618"}.df-icon-zhifufangshi:before{content:"\\e64d"}.df-icon-lipeixuzhi:before{content:"\\e61f"}.df-icon-lianxi:before{content:"\\e632"}.df-icon-didian1:before{content:"\\e619"}.df-icon-tuikuan1:before{content:"\\e641"}.df-icon-yonghuxieyi:before{content:"\\e61a"}.df-icon-lianxiwomen:before{content:"\\e663"}.df-icon-gongzhonghao:before{content:"\\e698"}.df-icon-icon-test:before{content:"\\e607"}.df-icon-8:before{content:"\\e61b"}.df-icon-shouhou:before{content:"\\e63c"}.df-icon-zhengcezhinanzhen:before{content:"\\e734"}.df-icon-xianxingtubiaozhizuomoban-43:before{content:"\\e633"}.df-icon-cart:before{content:"\\e631"}.df-icon-home:before{content:"\\e62e"}.df-icon-user:before{content:"\\e62d"}.df-icon-sanjiaoxia:before{content:"\\e615"}.df-icon-loudou:before{content:"\\e614"}.df-icon-shang:before{content:"\\e60f"}.df-icon-caidan:before{content:"\\e610"}.df-icon-menu1:before{content:"\\e611"}.df-icon-caidan1:before{content:"\\e612"}.df-icon-shanchu:before{content:"\\e613"}.df-icon-menu:before{content:"\\e60c"}.df-icon-account:before{content:"\\e629"}.df-icon-guard:before{content:"\\e62a"}.df-icon-lock:before{content:"\\e62c"}.df-icon-weibo:before{content:"\\e63e"}.df-icon-wechat:before{content:"\\e6b4"}.df-icon-edit:before{content:"\\e627"}.df-icon-back:before{content:"\\e7c3"}.df-icon-yishouhuo:before{content:"\\e617"}.df-icon-daifahuo:before{content:"\\e60a"}.df-icon-gouwujianying:before{content:"\\e67d"}.df-icon-huochepiao:before{content:"\\e651"}.df-icon-feiji:before{content:"\\e60d"}.df-icon-lunchuan:before{content:"\\e60e"}.df-icon-zhifubao:before{content:"\\e6b8"}.df-icon-yinhangqia:before{content:"\\e680"}.df-icon-fenlei:before{content:"\\e625"}.df-icon-sidebar:before{content:"\\e691"}.df-icon-fahuo:before{content:"\\e63b"}.df-icon-character-avatar:before{content:"\\e630"}.df-icon-dizhi:before{content:"\\e640"}.df-icon-lianxikefu:before{content:"\\e667"}.df-icon-liulanjilu:before{content:"\\e62f"}.df-icon-tuikuan:before{content:"\\e64c"}.df-icon-change:before{content:"\\e602"}.df-icon-yiquxiao:before{content:"\\e616"}.df-icon-daifukuan:before{content:"\\e626"}.df-icon-bangzhu:before{content:"\\e68c"}.df-icon-youhuiquan:before{content:"\\e60b"}.df-icon-anquanzhuye:before{content:"\\e64f"}.df-icon-ziyuan137:before{content:"\\e6e1"}.df-icon-shoucang:before{content:"\\e639"}.df-icon-search:before{content:"\\e609"}.df-icon-fail:before{content:"\\e636"}.df-icon-success:before{content:"\\e62b"}.df-icon-xinjianwenbenwendang:before{content:"\\e605"}.df-icon-address:before{content:"\\e603"}.df-icon-fangda:before{content:"\\e604"}.df-icon-suoxiao:before{content:"\\e608"}.df-icon-we-chat:before{content:"\\e6c3"}.df-icon-location:before{content:"\\e623"}.df-icon-contact:before{content:"\\e624"}.df-icon-avatar:before{content:"\\e622"}.df-icon-vip:before{content:"\\e621"}', ""]),
        e.exports = f
    },
    285: function(e, t, n) {
        e.exports = n.p + "fonts/font_2177670_mt0e8nqzzhg.5228237.woff2"
    },
    286: function(e, t, n) {
        e.exports = n.p + "fonts/font_2177670_mt0e8nqzzhg.ea35090.woff"
    },
    287: function(e, t, n) {
        e.exports = n.p + "fonts/font_2177670_mt0e8nqzzhg.9c0959f.ttf"
    },
    288: function(e, t, n) {
        var content = n(289);
        "string" == typeof content && (content = [[e.i, content, ""]]),
        content.locals && (e.exports = content.locals);
        (0,
        n(8).default)("a214a166", content, !0, {
            sourceMap: !1
        })
    },
    289: function(e, t, n) {
        var o = n(7)
          , r = n(150)
          , l = n(290)
          , c = n(291)
          , d = n(292)
          , f = o(!1)
          , m = r(l)
          , h = r(c)
          , v = r(d);
        f.push([e.i, '.color-gray{color:#707070}.color-more-gray{color:#999}.color-white{color:#fff}.color-primary{color:#1f1f1f}.font28{font-size:.7rem}/*! normalize.css v4.1.1 | MIT License | github.com/necolas/normalize.css */html{font-family:"PingFang SC","Microsoft YaHei";-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}article,aside,details,figcaption,figure,footer,header,main,menu,nav,section,summary{display:block}audio,canvas,progress,video{display:inline-block}audio:not([controls]){display:none;height:0}progress{vertical-align:baseline}[hidden],template{display:none}a{background-color:transparent;-webkit-text-decoration-skip:objects;text-decoration:none}a:active,a:hover{outline-width:0}a:hover,a:link,a:visited{color:#383838;text-decoration:none}abbr[title]{border-bottom:none;text-decoration:underline;-webkit-text-decoration:underline dotted;text-decoration:underline dotted}b,strong{font-weight:inherit;font-weight:bolder}dfn{font-style:italic}h1{font-size:2em;margin:.67em 0}mark{background-color:#ff0;color:#000}small{font-size:80%}sub,sup{font-size:75%;line-height:0;position:relative;vertical-align:baseline}sub{bottom:-.25em}sup{top:-.5em}img{border-style:none}svg:not(:root){overflow:hidden}code,kbd,pre,samp{font-family:monospace,monospace;font-size:1em}figure{margin:1em 40px}hr{box-sizing:content-box;height:0;overflow:visible}button,input,select,textarea{font:inherit;margin:0;outline:none}optgroup{font-weight:700}button,input{overflow:visible}button,select{text-transform:none}[type=reset],[type=submit],button,html [type=button]{-webkit-appearance:button}[type=button]::-moz-focus-inner,[type=reset]::-moz-focus-inner,[type=submit]::-moz-focus-inner,button::-moz-focus-inner{border-style:none;padding:0}[type=button]:-moz-focusring,[type=reset]:-moz-focusring,[type=submit]:-moz-focusring,button:-moz-focusring{outline:1px dotted ButtonText}fieldset{border:1px solid silver;margin:0 2px;padding:.35em .625em .75em}legend{box-sizing:border-box;color:inherit;display:table;max-width:100%;padding:0;white-space:normal}textarea{overflow:auto}[type=checkbox],[type=radio]{box-sizing:border-box;padding:0}[type=number]::-webkit-inner-spin-button,[type=number]::-webkit-outer-spin-button{height:auto}[type=search]{-webkit-appearance:textfield;outline-offset:-2px}[type=search]::-webkit-search-cancel-button,[type=search]::-webkit-search-decoration{-webkit-appearance:none}::-webkit-input-placeholder{color:inherit;opacity:.54}::-webkit-file-upload-button{-webkit-appearance:button;font:inherit}dl,ol,ul{list-style-type:none}body,dd,dl,dt,form,h1,h2,h3,h4,h5,h6,html,img,li,ol,p,table,td,textarea,th,tr,ul{margin:0;padding:0}em,i{font-style:normal}html{width:100%;height:100%}@media screen and (max-width:320px){html{font-size:17.0666667px}}@media screen and (max-width:374px){html{font-size:19.2px}}@media screen and (min-width:375px){html{font-size:20px}}@media screen and (min-width:414px){html{font-size:22.08px}}@media screen and (min-width:768px){html{font-size:40.96px}}@media screen and (min-width:1024px){html{font-size:54.6133333px}}body{position:relative;margin:0;background-color:#f9f9f9;color:#383838;font-size:.6rem}#__layout,#__nuxt,.page-container,body{width:100%;height:100%;overflow:hidden}.page{position:absolute;top:0;right:0;bottom:0;left:0;width:100%;box-sizing:border-box;overflow:hidden;background:#f9f9f9}.page .page-header{position:absolute!important;top:0;right:0;left:0;background:#fff}.page .page-content{position:absolute;top:0;right:0;left:0;bottom:0;overflow-x:hidden;overflow-y:auto;overflow-scrolling:touch;-webkit-overflow-scrolling:touch}.page.has-nav .page-content{top:2.3rem}.page.has-bottom .page-content{bottom:50px}.page .page-section{margin-bottom:.4rem}.page-bottom .van-tabbar-item__icon .df-icon{font-size:26px}.page-bottom .van-tabbar-item__icon img{height:20px}.page-enter-active,.page-leave-active,.page-old{transition-duration:.5s;transition-timing-function:cubic-bezier(.36,.66,.04,1);transition-property:opacity,transform}[transition-direction=forward] .page-old{transform:translate3d(-80%,0,0);transition-duration:.55s;opacity:.8}[transition-direction=forward] .page-enter{transform:translate3d(100%,0,0);opacity:1;z-index:2}[transition-direction=forward] .page-enter-active{box-shadow:0 0 10px rgba(0,0,0,.15)}[transition-direction=forward] .page-enter-to{transform:translateZ(0);opacity:1;z-index:2}[transition-direction=forward] .page-leave{transform:translateZ(0);opacity:.8;z-index:0}[transition-direction=forward] .page-leave-to{transform:translate3d(-33%,0,0);opacity:0;z-index:0}[transition-direction=back] .page-old{transform:translate3d(100%,0,0);box-shadow:0 0 10px rgba(0,0,0,.15)}[transition-direction=back] .page-enter{transform:translate3d(-33%,0,0);opacity:.8;z-index:-1}[transition-direction=back] .page-enter-to{transform:translateZ(0);opacity:1;z-index:-1}[transition-direction=back] .page-leave{opacity:0}[transition-direction=none] .page-enter-active,[transition-direction=none] .page-leave-active{transition-duration:0s}.page .floor{width:100%;box-sizing:border-box;color:#383838}.page .floor .title{position:relative;padding:.4rem}.page .floor .title .title-text{display:inline-block;font-weight:700;font-size:.8rem;color:#383838}.page .floor .title .sub-title{display:inline-block;margin-left:.4rem;height:.825rem;line-height:.825rem;letter-spacing:1px;color:#383838;font-size:.6rem;vertical-align:middle}.page .floor .title .lnk-more{position:absolute;bottom:.15rem;right:.4rem;display:inline-block;height:1.15rem;color:#707070;font-size:.5rem;text-align:center}.page .floor .title.large .title-text{font-size:1rem}.page .floor .floor-title2{position:relative;height:1.25rem}.page .floor .floor-title2 .title-text{position:absolute;left:50%;transform:translateX(-50%);display:inline-block;padding:0 1rem;font-size:.9rem;font-weight:700;color:#885332;white-space:nowrap}.page .floor .floor-title2:before{content:"";position:absolute;z-index:0;top:50%;left:.4rem;right:.4rem;height:.1rem;background:#ad8863}.good-item-list,.page .floor .floor-content{width:100%;box-sizing:border-box}.good-item-list{display:flex;align-items:flex-start;flex-wrap:wrap;padding:0 .2rem;text-align:left}.good-item-list .good-item-wrap{width:100%;box-sizing:border-box;padding:.2rem}.good-item-list.col2 .good-item-wrap{width:50%}.good-item-list.col3 .good-item-wrap{width:33.333%}.main-origins .van-collapse-item__content{padding:0}input{-webkit-appearance:none}.hide{display:none!important}.clear-fix{clear:both;zoom:1}.clear-fix:after{clear:both;display:block;visibility:hidden;font-size:0;content:" ";height:0}.float-left{float:left}.float-right{float:right}.arrow-up{width:0;height:0;border-left:30px solid transparent;border-right:30px solid transparent;border-bottom:30px solid #fff}.swiper-container{width:100%;font-size:0}.swiper-slide{text-align:center}.swiper-slide img{width:100%}.scroll-box{background:#fff}.scroll-box .scroll-banner{position:relative}.scroll-box .scroll-banner img{display:block;width:100%}.scroll-box .scroll-banner .arrow{position:absolute;left:50%;bottom:0;margin-left:-8px;display:block;width:0;height:0;border:8px solid transparent;border-top:none;border-bottom:8px solid #fff}.scroll-box .scroll-con{width:100%;overflow:hidden}.scroll-box .scroll-con a{display:block}.scroll-box ul{margin:10px 0 10px 5px;position:relative;padding-right:10px}.scroll-box li{display:none;float:left;width:40%;padding:0 5px;box-sizing:border-box}.scroll-box li:nth-of-type(3){position:absolute;top:0;right:0;transform:translateX(50%)}.scroll-box li:first-of-type,.scroll-box li:nth-of-type(2),.scroll-box li:nth-of-type(3){display:block}.scroll-box li .checkmore{display:block;width:100%;padding-bottom:100%;background:#f0f0f0;position:relative}.scroll-box li .more-txt{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);font-size:.6rem;line-height:2.2rem;text-align:center}.scroll-box li .more-txt .cn{color:#b48b5a;display:block;padding:0 2px;border:1px solid #f0f0f0;border-bottom-color:#ccc}.scroll-box li .more-txt .en{color:#333}.scroll_ready li{display:block}.scroll_ready li:nth-of-type(3){position:static;transform:translateX(0)}.scroll-box .img{position:relative;width:100%;padding-bottom:100%}.scroll-box .img img{position:absolute;top:0;left:0;width:100%;height:100%}.scroll-box .img img.saleout-icon{position:absolute;top:30%;left:25%;width:50%!important;height:auto!important;z-index:2}.scroll-box .link-info{position:absolute;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,.4)}.scroll-box .link-info .v-c{position:absolute;top:50%;left:0;width:100%;transform:translateY(-50%)}.scroll-box .link-info p{width:100%;text-align:center;font-size:.7rem;color:#fff}.scroll-box .link-info .line{width:42.86%;height:1px;background:#fff;overflow:hidden;margin:8px auto 0}.scroll-box .desc{text-align:center;font-size:.6rem;color:#333;padding:6px 0 10px}.scroll-box .more{margin-top:2px;text-align:center}.scroll-box .brand,.scroll-box .name{font-size:.6rem;line-height:1.5rem;color:#666;text-align:center;padding:0 5px}.scroll-box .price{float:left;color:#b48b5a}.scroll-box .price,.scroll-box .price-old{margin-top:4px;font-size:.6rem;line-height:1.2rem}.scroll-box .price-old{float:right;color:#ccc}input[type=checkbox]:checked,input[type=radio]:checked{background-position:-20px 0;border:none}input[disabled]{opacity:.5!important}.input-with-label{margin-top:5px;width:100%;line-height:30px}.input-with-label *{box-sizing:border-box;-webkit-box-sizing:border-box}.input-with-label span{display:inline-block;width:22%}.input-with-label input{width:78%;padding:0 10px}.point-right{transform:rotate(45deg)}.point-down,.point-right{display:inline-block;width:.5rem;height:.5rem;border-top:2px solid #383838;border-right:2px solid #383838}.point-down{transform:rotate(135deg)}.tip{display:inline-block;width:1.725rem;height:1.75rem;line-height:1.75rem;border-radius:100px;background-color:#c20318}.triangle-down{width:0;height:0;border-left:.3rem solid transparent;border-right:.3rem solid transparent;border-top:.3rem solid #c20318;font-size:0}.selectFlag{display:inline-block;width:1.1rem;height:1.1rem;line-height:.95rem;background-color:#fff;border:1px solid #999;border-radius:200px;text-align:center;box-sizing:border-box}.selectFlag em{display:none}.focuson{border:0;background-color:#1f1f1f}.focuson em{display:inline-block;width:.55rem;height:.3rem;line-height:.4rem;border-left:2px solid #fff;border-bottom:2px solid #fff;transform:rotate(-45deg)}.errorToast{background-color:rgba(0,0,0,.5)!important;padding-left:1.35rem!important;padding-right:1.35rem!important;border-radius:100px!important}.scroll-x{overflow-x:scroll;overflow-y:hidden}.scroll-y{overflow-y:scroll;overflow-x:hidden}.scroll-x,.scroll-y{-webkit-overflow-scrolling:touch}.mt20{margin-top:.5rem}.mb20{margin-bottom:.5rem}.mt16,.mt32{margin-top:.4rem}.mt48{margin-top:1.2rem}.mb32{margin-bottom:.4rem}.hpd16{padding-left:.4rem;padding-right:.4rem}.vpd16{padding-top:.4rem;padding-bottom:.4rem}.pdt0{padding-top:0!important}.mr5{margin-right:5px}.mr10{margin-right:10px}.disabled{color:#999}.middle{display:inline-block;vertical-align:middle}.van-switch--on{background-color:#1f1f1f!important}::-webkit-scrollbar{width:0;height:0}.van-nav-bar,.van-nav-bar__title{background:#fff!important}.van-nav-bar__title{font-size:.8rem!important;font-weight:400!important}.van-nav-bar .van-icon,.van-nav-bar__title{color:#606266!important}.van-nav-bar__left,.van-nav-bar__right{padding:0 .7rem!important}.tomford-col .van-grid-item__content{padding:0!important}.van-dialog{border-radius:.4rem}.price-color,.rise{color:red!important}.rise{font-size:.5rem;display:inline-block}.nav-box .van-tabs__nav .van-tabs__line{display:none!important}.ios-bottom{padding-bottom:env(safe-area-inset-bottom)!important}.dj-swiper .van-swipe__indicator{width:.5rem!important;height:.5rem!important}.dj-swiper .van-swipe__indicator:not(:last-child){margin-right:.5rem!important}.module-swiper .van-swipe__indicator{width:.5rem!important;height:.5rem!important;border:1px solid #000!important;background-color:#fff}.module-swiper .van-swipe__indicator:not(:last-child){margin-right:.5rem!important}.ydstxt{text-decoration:underline}.common-header,.header-holder{width:100%;height:2.2rem}.common-header{position:fixed;z-index:1000;top:0;right:0;left:0;background-color:#fff;border-bottom:1px solid #efefef}.common-header .back{position:absolute;left:0;top:0;padding:0 .5rem;width:auto;height:auto;line-height:2.2rem;background-color:transparent;border:none;color:#1f1f1f}.common-header .back span{display:inline-block;padding:.05rem 0 0 2.2rem}.common-header .back .iconfont{font-size:1rem;color:#999}.common-header .title{display:block;margin:0 auto;width:60%;line-height:2.2rem;text-align:center;font-size:1rem;color:#121212}.common-header .menu{position:absolute;top:50%;right:.5rem;transform:translateY(-50%)}.common-header .menu li{float:left;margin-right:.1rem}.common-header .menu li a.ico{display:block;width:1.5rem;height:1.5rem;font-size:.75rem;border:1px solid #999;text-align:center;color:#999;border-radius:100%;box-sizing:border-box}.common-header .menu li a.ico em{display:inline-block;line-height:1.5rem;font-size:.9rem}.common-header .menu li a.txt{color:#999;font-size:.6rem}.common-header .header-arrow{display:none;position:absolute;bottom:0;right:15px;margin-left:-7px;width:0;height:0;border:.35rem solid transparent;border-top:none;border-bottom:.35rem solid #000}.common-header .header-drop{display:none;width:100%;background:#000}.common-header .header-drop ul{padding:7px 0 4px;width:100%;overflow:hidden;background:#000}.common-header .header-drop li{width:25%;float:left;text-align:center}.common-header .header-drop li a{line-height:0}.common-header .header-drop li .icon{display:block;margin:0 auto}.common-header .header-drop li .txt{color:#1f1f1f;line-height:20px;display:block;margin:0 auto;font-size:14px}.common-header .right-bar{position:absolute;top:5px;right:15px}.common-header .icon{display:inline-block}.common-header .icon-about{width:22px;height:22px;background:url(/images/user/about.png);background-size:100% 100%;margin-top:9px;overflow:hidden}.common-header .txt-btn{padding:0 .5rem;line-height:2.2rem;position:absolute;top:0;right:0;font-size:.7rem}.common-header .txt-btn a{color:#999}.text-overflow{text-overflow:ellipsis;white-space:nowrap;overflow:hidden}.text-left{text-align:left}.text-right{text-align:right}.text-center{text-align:center}.text-ellipsis1{overflow:hidden;white-space:nowrap;text-overflow:ellipsis;word-break:break-all}.text-ellipsis2{-webkit-line-clamp:2}.text-ellipsis2,.text-ellipsis3{overflow:hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-box-orient:vertical;word-wrap:break-word}.text-ellipsis3{-webkit-line-clamp:3}.font-sm{font-size:.6rem}.font-normal{font-size:.7rem}.font-lg{font-size:.8rem}.page .mint-button{font-weight:700}.page .mint-button--primary{background-color:#1f1f1f!important}.page .mint-button--large{height:2.75rem!important;font-size:.8rem!important}.mint-msgbox-confirm{color:#333!important}.mint-indicator-wrapper{z-index:9999}.mint-button--small{font-size:.6rem!important;height:1rem!important}.mint-button--normal{font-size:.7rem!important;height:1.5rem!important}.mint-button--large{font-size:.8rem!important;height:2rem!important}.mint-indicator-wrapper{background-color:transparent!important}.page .van-button--primary{color:#fff;background:linear-gradient(180deg,#1f1f1f,#1f1f1f);border:none}#YSF-BTN-HOLDER{display:none!important;right:.4rem!important;bottom:2.5rem!important}#YSF-CUSTOM-ENTRY-7 img{width:2rem!important}@font-face{font-family:"iconfont";src:url(' + m + ') format("woff2"),url(' + h + ') format("woff"),url(' + v + ') format("truetype")}.iconfont{font-family:"iconfont"!important;font-size:16px;font-style:normal;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.htdf-backspace-outline:before{content:"\\e971"}.htdf-shuaxin:before{content:"\\e627"}.htdf-shumashouji:before{content:"\\e601"}.htdf-avatar:before{content:"\\e61b"}.htdf-ysgouwuche1:before{content:"\\e62e"}.htdf-ysgouwuche2:before{content:"\\e62f"}.htdf-yonghu:before{content:"\\e63d"}.htdf-jingdong-:before{content:"\\e643"}.htdf-zhifupingtai-yinlian:before{content:"\\e615"}.htdf-jiansheyinhang:before{content:"\\e619"}.htdf-ziyuanxhdpi:before{content:"\\e64c"}.htdf-yanzhengma:before{content:"\\e61a"}.htdf-zhifubao:before{content:"\\e60a"}.htdf-yunshanfu:before{content:"\\e68b"}.htdf-baidu:before{content:"\\e613"}.htdf-weixin:before{content:"\\e608"}.htdf-zhongguojiaotongyinhang:before{content:"\\e61d"}.htdf-bianji:before{content:"\\e600"}.htdf-gengduo:before{content:"\\e60d"}.htdf-shanchu:before{content:"\\e68e"}.htdf-guanbi2:before{content:"\\e652"}.htdf-shezhi:before{content:"\\e637"}.htdf-jiangjiatongzhi:before{content:"\\e668"}.htdf-sousuo:before{content:"\\e622"}.htdf-xuanzhong:before{content:"\\e606"}.htdf-huidaodingbu:before{content:"\\e88d"}.htdf-bangzhu_o:before{content:"\\eb72"}.htdf-guanbi_o:before{content:"\\eb76"}.htdf-guanbi:before{content:"\\e611"}.htdf-gouwuche:before{content:"\\e612"}.htdf-shezhi1:before{content:"\\e6d8"}.htdf-radio:before{content:"\\e607"}.htdf-bangzhu:before{content:"\\e8c3"}.htdf-fuxuanxiangxuanzhong:before{content:"\\e625"}.htdf-jiangjia:before{content:"\\e61c"}.htdf-a-31Cfuxuankuang:before{content:"\\e691"}.htdf-xiaoxi:before{content:"\\e614"}.htdf-xiangyoujiantou:before{content:"\\e65f"}.htdf-xiangzuojiantou:before{content:"\\e660"}.htdf-shouye:before{content:"\\e61f"}.htdf-xiangshangjiantou:before{content:"\\e65d"}.htdf-xiangxiajiantou:before{content:"\\e65e"}.htdf-tuichu:before{content:"\\e616"}.htdf-kefu:before{content:"\\e88f"}.htdf-aixin:before{content:"\\e83f"}.htdf-aixin1:before{content:"\\e60f"}.htdf-shaixuan:before{content:"\\e650"}.htdf-saoyisao_o:before{content:"\\eb81"}.htdf-fenxiang:before{content:"\\e624"}.htdf-iconzhengli_tiaozhuan:before{content:"\\e648"}.htdf-tiaozhuan:before{content:"\\e65b"}.htdf-dizhiguanli:before{content:"\\e63f"}.htdf-24gl-bag:before{content:"\\e877"}.htdf-shoucangdaogouwudai:before{content:"\\e6a9"}.htdf-dagoucheck:before{content:"\\e7bc"}', ""]),
        e.exports = f
    },
    290: function(e, t, n) {
        e.exports = n.p + "fonts/iconfont.4a9a7d3.woff2"
    },
    291: function(e, t, n) {
        e.exports = n.p + "fonts/iconfont.f11215f.woff"
    },
    292: function(e, t, n) {
        e.exports = n.p + "fonts/iconfont.d61ad37.ttf"
    },
    296: function(e, t, n) {
        "use strict";
        n(178)
    },
    297: function(e, t, n) {
        var o = n(7)(!1);
        o.push([e.i, '.color-gray[data-v-6baf7f6e]{color:#707070}.color-more-gray[data-v-6baf7f6e]{color:#999}.color-white[data-v-6baf7f6e]{color:#fff}.color-primary[data-v-6baf7f6e]{color:#1f1f1f}.font28[data-v-6baf7f6e]{font-size:.7rem}/*! normalize.css v4.1.1 | MIT License | github.com/necolas/normalize.css */html[data-v-6baf7f6e]{font-family:"PingFang SC","Microsoft YaHei";-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}article[data-v-6baf7f6e],aside[data-v-6baf7f6e],details[data-v-6baf7f6e],figcaption[data-v-6baf7f6e],figure[data-v-6baf7f6e],footer[data-v-6baf7f6e],header[data-v-6baf7f6e],main[data-v-6baf7f6e],menu[data-v-6baf7f6e],nav[data-v-6baf7f6e],section[data-v-6baf7f6e],summary[data-v-6baf7f6e]{display:block}audio[data-v-6baf7f6e],canvas[data-v-6baf7f6e],progress[data-v-6baf7f6e],video[data-v-6baf7f6e]{display:inline-block}audio[data-v-6baf7f6e]:not([controls]){display:none;height:0}progress[data-v-6baf7f6e]{vertical-align:baseline}[hidden][data-v-6baf7f6e],template[data-v-6baf7f6e]{display:none}a[data-v-6baf7f6e]{background-color:transparent;-webkit-text-decoration-skip:objects;text-decoration:none}a[data-v-6baf7f6e]:active,a[data-v-6baf7f6e]:hover{outline-width:0}a[data-v-6baf7f6e]:hover,a[data-v-6baf7f6e]:link,a[data-v-6baf7f6e]:visited{color:#383838;text-decoration:none}abbr[title][data-v-6baf7f6e]{border-bottom:none;text-decoration:underline;-webkit-text-decoration:underline dotted;text-decoration:underline dotted}b[data-v-6baf7f6e],strong[data-v-6baf7f6e]{font-weight:inherit;font-weight:bolder}dfn[data-v-6baf7f6e]{font-style:italic}h1[data-v-6baf7f6e]{font-size:2em;margin:.67em 0}mark[data-v-6baf7f6e]{background-color:#ff0;color:#000}small[data-v-6baf7f6e]{font-size:80%}sub[data-v-6baf7f6e],sup[data-v-6baf7f6e]{font-size:75%;line-height:0;position:relative;vertical-align:baseline}sub[data-v-6baf7f6e]{bottom:-.25em}sup[data-v-6baf7f6e]{top:-.5em}img[data-v-6baf7f6e]{border-style:none}svg[data-v-6baf7f6e]:not(:root){overflow:hidden}code[data-v-6baf7f6e],kbd[data-v-6baf7f6e],pre[data-v-6baf7f6e],samp[data-v-6baf7f6e]{font-family:monospace,monospace;font-size:1em}figure[data-v-6baf7f6e]{margin:1em 40px}hr[data-v-6baf7f6e]{box-sizing:content-box;height:0;overflow:visible}button[data-v-6baf7f6e],input[data-v-6baf7f6e],select[data-v-6baf7f6e],textarea[data-v-6baf7f6e]{font:inherit;margin:0;outline:none}optgroup[data-v-6baf7f6e]{font-weight:700}button[data-v-6baf7f6e],input[data-v-6baf7f6e]{overflow:visible}button[data-v-6baf7f6e],select[data-v-6baf7f6e]{text-transform:none}[type=reset][data-v-6baf7f6e],[type=submit][data-v-6baf7f6e],button[data-v-6baf7f6e],html [type=button][data-v-6baf7f6e]{-webkit-appearance:button}[type=button][data-v-6baf7f6e]::-moz-focus-inner,[type=reset][data-v-6baf7f6e]::-moz-focus-inner,[type=submit][data-v-6baf7f6e]::-moz-focus-inner,button[data-v-6baf7f6e]::-moz-focus-inner{border-style:none;padding:0}[type=button][data-v-6baf7f6e]:-moz-focusring,[type=reset][data-v-6baf7f6e]:-moz-focusring,[type=submit][data-v-6baf7f6e]:-moz-focusring,button[data-v-6baf7f6e]:-moz-focusring{outline:1px dotted ButtonText}fieldset[data-v-6baf7f6e]{border:1px solid silver;margin:0 2px;padding:.35em .625em .75em}legend[data-v-6baf7f6e]{box-sizing:border-box;color:inherit;display:table;max-width:100%;padding:0;white-space:normal}textarea[data-v-6baf7f6e]{overflow:auto}[type=checkbox][data-v-6baf7f6e],[type=radio][data-v-6baf7f6e]{box-sizing:border-box;padding:0}[type=number][data-v-6baf7f6e]::-webkit-inner-spin-button,[type=number][data-v-6baf7f6e]::-webkit-outer-spin-button{height:auto}[type=search][data-v-6baf7f6e]{-webkit-appearance:textfield;outline-offset:-2px}[type=search][data-v-6baf7f6e]::-webkit-search-cancel-button,[type=search][data-v-6baf7f6e]::-webkit-search-decoration{-webkit-appearance:none}[data-v-6baf7f6e]::-webkit-input-placeholder{color:inherit;opacity:.54}[data-v-6baf7f6e]::-webkit-file-upload-button{-webkit-appearance:button;font:inherit}dl[data-v-6baf7f6e],ol[data-v-6baf7f6e],ul[data-v-6baf7f6e]{list-style-type:none}body[data-v-6baf7f6e],dd[data-v-6baf7f6e],dl[data-v-6baf7f6e],dt[data-v-6baf7f6e],form[data-v-6baf7f6e],h1[data-v-6baf7f6e],h2[data-v-6baf7f6e],h3[data-v-6baf7f6e],h4[data-v-6baf7f6e],h5[data-v-6baf7f6e],h6[data-v-6baf7f6e],html[data-v-6baf7f6e],img[data-v-6baf7f6e],li[data-v-6baf7f6e],ol[data-v-6baf7f6e],p[data-v-6baf7f6e],table[data-v-6baf7f6e],td[data-v-6baf7f6e],textarea[data-v-6baf7f6e],th[data-v-6baf7f6e],tr[data-v-6baf7f6e],ul[data-v-6baf7f6e]{margin:0;padding:0}em[data-v-6baf7f6e],i[data-v-6baf7f6e]{font-style:normal}html[data-v-6baf7f6e]{width:100%;height:100%}@media screen and (max-width:320px){html[data-v-6baf7f6e]{font-size:17.0666667px}}@media screen and (max-width:374px){html[data-v-6baf7f6e]{font-size:19.2px}}@media screen and (min-width:375px){html[data-v-6baf7f6e]{font-size:20px}}@media screen and (min-width:414px){html[data-v-6baf7f6e]{font-size:22.08px}}@media screen and (min-width:768px){html[data-v-6baf7f6e]{font-size:40.96px}}@media screen and (min-width:1024px){html[data-v-6baf7f6e]{font-size:54.6133333px}}body[data-v-6baf7f6e]{position:relative;margin:0;background-color:#f9f9f9;color:#383838;font-size:.6rem}#__layout[data-v-6baf7f6e],#__nuxt[data-v-6baf7f6e],.page-container[data-v-6baf7f6e],body[data-v-6baf7f6e]{width:100%;height:100%;overflow:hidden}.page[data-v-6baf7f6e]{position:absolute;top:0;right:0;bottom:0;left:0;width:100%;box-sizing:border-box;overflow:hidden;background:#f9f9f9}.page .page-header[data-v-6baf7f6e]{position:absolute!important;top:0;right:0;left:0;background:#fff}.page .page-content[data-v-6baf7f6e]{position:absolute;top:0;right:0;left:0;bottom:0;overflow-x:hidden;overflow-y:auto;overflow-scrolling:touch;-webkit-overflow-scrolling:touch}.page.has-nav .page-content[data-v-6baf7f6e]{top:2.3rem}.page.has-bottom .page-content[data-v-6baf7f6e]{bottom:50px}.page .page-section[data-v-6baf7f6e]{margin-bottom:.4rem}.page-bottom .van-tabbar-item__icon .df-icon[data-v-6baf7f6e]{font-size:26px}.page-bottom .van-tabbar-item__icon img[data-v-6baf7f6e]{height:20px}.page-enter-active[data-v-6baf7f6e],.page-leave-active[data-v-6baf7f6e],.page-old[data-v-6baf7f6e]{transition-duration:.5s;transition-timing-function:cubic-bezier(.36,.66,.04,1);transition-property:opacity,transform}[transition-direction=forward] .page-old[data-v-6baf7f6e]{transform:translate3d(-80%,0,0);transition-duration:.55s;opacity:.8}[transition-direction=forward] .page-enter[data-v-6baf7f6e]{transform:translate3d(100%,0,0);opacity:1;z-index:2}[transition-direction=forward] .page-enter-active[data-v-6baf7f6e]{box-shadow:0 0 10px rgba(0,0,0,.15)}[transition-direction=forward] .page-enter-to[data-v-6baf7f6e]{transform:translateZ(0);opacity:1;z-index:2}[transition-direction=forward] .page-leave[data-v-6baf7f6e]{transform:translateZ(0);opacity:.8;z-index:0}[transition-direction=forward] .page-leave-to[data-v-6baf7f6e]{transform:translate3d(-33%,0,0);opacity:0;z-index:0}[transition-direction=back] .page-old[data-v-6baf7f6e]{transform:translate3d(100%,0,0);box-shadow:0 0 10px rgba(0,0,0,.15)}[transition-direction=back] .page-enter[data-v-6baf7f6e]{transform:translate3d(-33%,0,0);opacity:.8;z-index:-1}[transition-direction=back] .page-enter-to[data-v-6baf7f6e]{transform:translateZ(0);opacity:1;z-index:-1}[transition-direction=back] .page-leave[data-v-6baf7f6e]{opacity:0}[transition-direction=none] .page-enter-active[data-v-6baf7f6e],[transition-direction=none] .page-leave-active[data-v-6baf7f6e]{transition-duration:0s}.page .floor[data-v-6baf7f6e]{width:100%;box-sizing:border-box;color:#383838}.page .floor .title[data-v-6baf7f6e]{position:relative;padding:.4rem}.page .floor .title .title-text[data-v-6baf7f6e]{display:inline-block;font-weight:700;font-size:.8rem;color:#383838}.page .floor .title .sub-title[data-v-6baf7f6e]{display:inline-block;margin-left:.4rem;height:.825rem;line-height:.825rem;letter-spacing:1px;color:#383838;font-size:.6rem;vertical-align:middle}.page .floor .title .lnk-more[data-v-6baf7f6e]{position:absolute;bottom:.15rem;right:.4rem;display:inline-block;height:1.15rem;color:#707070;font-size:.5rem;text-align:center}.page .floor .title.large .title-text[data-v-6baf7f6e]{font-size:1rem}.page .floor .floor-title2[data-v-6baf7f6e]{position:relative;height:1.25rem}.page .floor .floor-title2 .title-text[data-v-6baf7f6e]{position:absolute;left:50%;transform:translateX(-50%);display:inline-block;padding:0 1rem;font-size:.9rem;font-weight:700;color:#885332;white-space:nowrap}.page .floor .floor-title2[data-v-6baf7f6e]:before{content:"";position:absolute;z-index:0;top:50%;left:.4rem;right:.4rem;height:.1rem;background:#ad8863}.good-item-list[data-v-6baf7f6e],.page .floor .floor-content[data-v-6baf7f6e]{width:100%;box-sizing:border-box}.good-item-list[data-v-6baf7f6e]{display:flex;align-items:flex-start;flex-wrap:wrap;padding:0 .2rem;text-align:left}.good-item-list .good-item-wrap[data-v-6baf7f6e]{width:100%;box-sizing:border-box;padding:.2rem}.good-item-list.col2 .good-item-wrap[data-v-6baf7f6e]{width:50%}.good-item-list.col3 .good-item-wrap[data-v-6baf7f6e]{width:33.333%}.main-origins .van-collapse-item__content[data-v-6baf7f6e]{padding:0}input[data-v-6baf7f6e]{-webkit-appearance:none}.hide[data-v-6baf7f6e]{display:none!important}.clear-fix[data-v-6baf7f6e]{clear:both;zoom:1}.clear-fix[data-v-6baf7f6e]:after{clear:both;display:block;visibility:hidden;font-size:0;content:" ";height:0}.float-left[data-v-6baf7f6e]{float:left}.float-right[data-v-6baf7f6e]{float:right}.arrow-up[data-v-6baf7f6e]{width:0;height:0;border-left:30px solid transparent;border-right:30px solid transparent;border-bottom:30px solid #fff}.swiper-container[data-v-6baf7f6e]{width:100%;font-size:0}.swiper-slide[data-v-6baf7f6e]{text-align:center}.swiper-slide img[data-v-6baf7f6e]{width:100%}.scroll-box[data-v-6baf7f6e]{background:#fff}.scroll-box .scroll-banner[data-v-6baf7f6e]{position:relative}.scroll-box .scroll-banner img[data-v-6baf7f6e]{display:block;width:100%}.scroll-box .scroll-banner .arrow[data-v-6baf7f6e]{position:absolute;left:50%;bottom:0;margin-left:-8px;display:block;width:0;height:0;border:8px solid transparent;border-top:none;border-bottom:8px solid #fff}.scroll-box .scroll-con[data-v-6baf7f6e]{width:100%;overflow:hidden}.scroll-box .scroll-con a[data-v-6baf7f6e]{display:block}.scroll-box ul[data-v-6baf7f6e]{margin:10px 0 10px 5px;position:relative;padding-right:10px}.scroll-box li[data-v-6baf7f6e]{display:none;float:left;width:40%;padding:0 5px;box-sizing:border-box}.scroll-box li[data-v-6baf7f6e]:nth-of-type(3){position:absolute;top:0;right:0;transform:translateX(50%)}.scroll-box li[data-v-6baf7f6e]:first-of-type,.scroll-box li[data-v-6baf7f6e]:nth-of-type(2),.scroll-box li[data-v-6baf7f6e]:nth-of-type(3){display:block}.scroll-box li .checkmore[data-v-6baf7f6e]{display:block;width:100%;padding-bottom:100%;background:#f0f0f0;position:relative}.scroll-box li .more-txt[data-v-6baf7f6e]{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);font-size:.6rem;line-height:2.2rem;text-align:center}.scroll-box li .more-txt .cn[data-v-6baf7f6e]{color:#b48b5a;display:block;padding:0 2px;border:1px solid #f0f0f0;border-bottom-color:#ccc}.scroll-box li .more-txt .en[data-v-6baf7f6e]{color:#333}.scroll_ready li[data-v-6baf7f6e]{display:block}.scroll_ready li[data-v-6baf7f6e]:nth-of-type(3){position:static;transform:translateX(0)}.scroll-box .img[data-v-6baf7f6e]{position:relative;width:100%;padding-bottom:100%}.scroll-box .img img[data-v-6baf7f6e]{position:absolute;top:0;left:0;width:100%;height:100%}.scroll-box .img img.saleout-icon[data-v-6baf7f6e]{position:absolute;top:30%;left:25%;width:50%!important;height:auto!important;z-index:2}.scroll-box .link-info[data-v-6baf7f6e]{position:absolute;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,.4)}.scroll-box .link-info .v-c[data-v-6baf7f6e]{position:absolute;top:50%;left:0;width:100%;transform:translateY(-50%)}.scroll-box .link-info p[data-v-6baf7f6e]{width:100%;text-align:center;font-size:.7rem;color:#fff}.scroll-box .link-info .line[data-v-6baf7f6e]{width:42.86%;height:1px;background:#fff;overflow:hidden;margin:8px auto 0}.scroll-box .desc[data-v-6baf7f6e]{text-align:center;font-size:.6rem;color:#333;padding:6px 0 10px}.scroll-box .more[data-v-6baf7f6e]{margin-top:2px;text-align:center}.scroll-box .brand[data-v-6baf7f6e],.scroll-box .name[data-v-6baf7f6e]{font-size:.6rem;line-height:1.5rem;color:#666;text-align:center;padding:0 5px}.scroll-box .price[data-v-6baf7f6e]{float:left;color:#b48b5a}.scroll-box .price[data-v-6baf7f6e],.scroll-box .price-old[data-v-6baf7f6e]{margin-top:4px;font-size:.6rem;line-height:1.2rem}.scroll-box .price-old[data-v-6baf7f6e]{float:right;color:#ccc}input[type=checkbox][data-v-6baf7f6e]:checked,input[type=radio][data-v-6baf7f6e]:checked{background-position:-20px 0;border:none}input[disabled][data-v-6baf7f6e]{opacity:.5!important}.input-with-label[data-v-6baf7f6e]{margin-top:5px;width:100%;line-height:30px}.input-with-label *[data-v-6baf7f6e]{box-sizing:border-box;-webkit-box-sizing:border-box}.input-with-label span[data-v-6baf7f6e]{display:inline-block;width:22%}.input-with-label input[data-v-6baf7f6e]{width:78%;padding:0 10px}.point-right[data-v-6baf7f6e]{transform:rotate(45deg)}.point-down[data-v-6baf7f6e],.point-right[data-v-6baf7f6e]{display:inline-block;width:.5rem;height:.5rem;border-top:2px solid #383838;border-right:2px solid #383838}.point-down[data-v-6baf7f6e]{transform:rotate(135deg)}.tip[data-v-6baf7f6e]{display:inline-block;width:1.725rem;height:1.75rem;line-height:1.75rem;border-radius:100px;background-color:#c20318}.triangle-down[data-v-6baf7f6e]{width:0;height:0;border-left:.3rem solid transparent;border-right:.3rem solid transparent;border-top:.3rem solid #c20318;font-size:0}.selectFlag[data-v-6baf7f6e]{display:inline-block;width:1.1rem;height:1.1rem;line-height:.95rem;background-color:#fff;border:1px solid #999;border-radius:200px;text-align:center;box-sizing:border-box}.selectFlag em[data-v-6baf7f6e]{display:none}.focuson[data-v-6baf7f6e]{border:0;background-color:#1f1f1f}.focuson em[data-v-6baf7f6e]{display:inline-block;width:.55rem;height:.3rem;line-height:.4rem;border-left:2px solid #fff;border-bottom:2px solid #fff;transform:rotate(-45deg)}.errorToast[data-v-6baf7f6e]{background-color:rgba(0,0,0,.5)!important;padding-left:1.35rem!important;padding-right:1.35rem!important;border-radius:100px!important}.scroll-x[data-v-6baf7f6e]{overflow-x:scroll;overflow-y:hidden}.scroll-y[data-v-6baf7f6e]{overflow-y:scroll;overflow-x:hidden}.scroll-x[data-v-6baf7f6e],.scroll-y[data-v-6baf7f6e]{-webkit-overflow-scrolling:touch}.mt20[data-v-6baf7f6e]{margin-top:.5rem}.mb20[data-v-6baf7f6e]{margin-bottom:.5rem}.mt16[data-v-6baf7f6e],.mt32[data-v-6baf7f6e]{margin-top:.4rem}.mt48[data-v-6baf7f6e]{margin-top:1.2rem}.mb32[data-v-6baf7f6e]{margin-bottom:.4rem}.hpd16[data-v-6baf7f6e]{padding-left:.4rem;padding-right:.4rem}.vpd16[data-v-6baf7f6e]{padding-top:.4rem;padding-bottom:.4rem}.pdt0[data-v-6baf7f6e]{padding-top:0!important}.mr5[data-v-6baf7f6e]{margin-right:5px}.mr10[data-v-6baf7f6e]{margin-right:10px}.disabled[data-v-6baf7f6e]{color:#999}.middle[data-v-6baf7f6e]{display:inline-block;vertical-align:middle}.van-switch--on[data-v-6baf7f6e]{background-color:#1f1f1f!important}[data-v-6baf7f6e]::-webkit-scrollbar{width:0;height:0}.van-nav-bar[data-v-6baf7f6e],.van-nav-bar__title[data-v-6baf7f6e]{background:#fff!important}.van-nav-bar__title[data-v-6baf7f6e]{font-size:.8rem!important;font-weight:400!important}.van-nav-bar .van-icon[data-v-6baf7f6e],.van-nav-bar__title[data-v-6baf7f6e]{color:#606266!important}.van-nav-bar__left[data-v-6baf7f6e],.van-nav-bar__right[data-v-6baf7f6e]{padding:0 .7rem!important}.tomford-col .van-grid-item__content[data-v-6baf7f6e]{padding:0!important}.van-dialog[data-v-6baf7f6e]{border-radius:.4rem}.price-color[data-v-6baf7f6e],.rise[data-v-6baf7f6e]{color:red!important}.rise[data-v-6baf7f6e]{font-size:.5rem;display:inline-block}.nav-box .van-tabs__nav .van-tabs__line[data-v-6baf7f6e]{display:none!important}.ios-bottom[data-v-6baf7f6e]{padding-bottom:env(safe-area-inset-bottom)!important}.dj-swiper .van-swipe__indicator[data-v-6baf7f6e]{width:.5rem!important;height:.5rem!important}.dj-swiper .van-swipe__indicator[data-v-6baf7f6e]:not(:last-child){margin-right:.5rem!important}.module-swiper .van-swipe__indicator[data-v-6baf7f6e]{width:.5rem!important;height:.5rem!important;border:1px solid #000!important;background-color:#fff}.module-swiper .van-swipe__indicator[data-v-6baf7f6e]:not(:last-child){margin-right:.5rem!important}.ydstxt[data-v-6baf7f6e]{text-decoration:underline}.common-header[data-v-6baf7f6e],.header-holder[data-v-6baf7f6e]{width:100%;height:2.2rem}.common-header[data-v-6baf7f6e]{position:fixed;z-index:1000;top:0;right:0;left:0;background-color:#fff;border-bottom:1px solid #efefef}.common-header .back[data-v-6baf7f6e]{position:absolute;left:0;top:0;padding:0 .5rem;width:auto;height:auto;line-height:2.2rem;background-color:transparent;border:none;color:#1f1f1f}.common-header .back span[data-v-6baf7f6e]{display:inline-block;padding:.05rem 0 0 2.2rem}.common-header .back .iconfont[data-v-6baf7f6e]{font-size:1rem;color:#999}.common-header .title[data-v-6baf7f6e]{display:block;margin:0 auto;width:60%;line-height:2.2rem;text-align:center;font-size:1rem;color:#121212}.common-header .menu[data-v-6baf7f6e]{position:absolute;top:50%;right:.5rem;transform:translateY(-50%)}.common-header .menu li[data-v-6baf7f6e]{float:left;margin-right:.1rem}.common-header .menu li a.ico[data-v-6baf7f6e]{display:block;width:1.5rem;height:1.5rem;font-size:.75rem;border:1px solid #999;text-align:center;color:#999;border-radius:100%;box-sizing:border-box}.common-header .menu li a.ico em[data-v-6baf7f6e]{display:inline-block;line-height:1.5rem;font-size:.9rem}.common-header .menu li a.txt[data-v-6baf7f6e]{color:#999;font-size:.6rem}.common-header .header-arrow[data-v-6baf7f6e]{display:none;position:absolute;bottom:0;right:15px;margin-left:-7px;width:0;height:0;border:.35rem solid transparent;border-top:none;border-bottom:.35rem solid #000}.common-header .header-drop[data-v-6baf7f6e]{display:none;width:100%;background:#000}.common-header .header-drop ul[data-v-6baf7f6e]{padding:7px 0 4px;width:100%;overflow:hidden;background:#000}.common-header .header-drop li[data-v-6baf7f6e]{width:25%;float:left;text-align:center}.common-header .header-drop li a[data-v-6baf7f6e]{line-height:0}.common-header .header-drop li .icon[data-v-6baf7f6e]{display:block;margin:0 auto}.common-header .header-drop li .txt[data-v-6baf7f6e]{color:#1f1f1f;line-height:20px;display:block;margin:0 auto;font-size:14px}.common-header .right-bar[data-v-6baf7f6e]{position:absolute;top:5px;right:15px}.common-header .icon[data-v-6baf7f6e]{display:inline-block}.common-header .icon-about[data-v-6baf7f6e]{width:22px;height:22px;background:url(/images/user/about.png);background-size:100% 100%;margin-top:9px;overflow:hidden}.common-header .txt-btn[data-v-6baf7f6e]{padding:0 .5rem;line-height:2.2rem;position:absolute;top:0;right:0;font-size:.7rem}.common-header .txt-btn a[data-v-6baf7f6e]{color:#999}.text-overflow[data-v-6baf7f6e]{text-overflow:ellipsis;white-space:nowrap;overflow:hidden}.text-left[data-v-6baf7f6e]{text-align:left}.text-right[data-v-6baf7f6e]{text-align:right}.text-center[data-v-6baf7f6e]{text-align:center}.text-ellipsis1[data-v-6baf7f6e]{overflow:hidden;white-space:nowrap;text-overflow:ellipsis;word-break:break-all}.text-ellipsis2[data-v-6baf7f6e]{-webkit-line-clamp:2}.text-ellipsis2[data-v-6baf7f6e],.text-ellipsis3[data-v-6baf7f6e]{overflow:hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-box-orient:vertical;word-wrap:break-word}.text-ellipsis3[data-v-6baf7f6e]{-webkit-line-clamp:3}.font-sm[data-v-6baf7f6e]{font-size:.6rem}.font-normal[data-v-6baf7f6e]{font-size:.7rem}.font-lg[data-v-6baf7f6e]{font-size:.8rem}.page .mint-button[data-v-6baf7f6e]{font-weight:700}.page .mint-button--primary[data-v-6baf7f6e]{background-color:#1f1f1f!important}.page .mint-button--large[data-v-6baf7f6e]{height:2.75rem!important;font-size:.8rem!important}.mint-msgbox-confirm[data-v-6baf7f6e]{color:#333!important}.mint-indicator-wrapper[data-v-6baf7f6e]{z-index:9999}.mint-button--small[data-v-6baf7f6e]{font-size:.6rem!important;height:1rem!important}.mint-button--normal[data-v-6baf7f6e]{font-size:.7rem!important;height:1.5rem!important}.mint-button--large[data-v-6baf7f6e]{font-size:.8rem!important;height:2rem!important}.mint-indicator-wrapper[data-v-6baf7f6e]{background-color:transparent!important}.page .van-button--primary[data-v-6baf7f6e]{color:#fff;background:linear-gradient(180deg,#1f1f1f,#1f1f1f);border:none}#YSF-BTN-HOLDER[data-v-6baf7f6e]{display:none!important;right:.4rem!important;bottom:2.5rem!important}#YSF-CUSTOM-ENTRY-7 img[data-v-6baf7f6e]{width:2rem!important}.van-tabbar-item--active[data-v-6baf7f6e]{color:#1f1f1f}', ""]),
        e.exports = o
    },
    298: function(e, t, n) {
        "use strict";
        n.r(t),
        function(e) {
            n.d(t, "state", (function() {
                return w
            }
            )),
            n.d(t, "actions", (function() {
                return k
            }
            )),
            n.d(t, "getters", (function() {
                return _
            }
            )),
            n.d(t, "mutations", (function() {
                return O
            }
            ));
            n(68),
            n(21);
            var o = n(4)
              , r = n(3)
              , l = n(35)
              , c = n(19)
              , d = n(6)
              , f = /&?mid=(\d+)&?/
              , m = /&?sid=(\d+)&?/
              , h = /&?pid=(\d+)&?/
              , v = /&?platform=(\d+)&?/
              , x = /&?sflsource=(\d+)&?/
              , y = /&?dftk=([0-9a-zA-Z]+)&?/
              , w = function() {
                return {
                    ORDER_STATUS_PAY: 0,
                    ORDER_STATUS_SEND: 1,
                    ORDER_STATUS_SHIP: 2,
                    ORDER_STATUS_RECEIVED: 3,
                    ORDER_STATUS_COMPLETE: 4,
                    ORDER_STATUS_REFUND: 5,
                    ORDER_STATUS_CLOSE: 100,
                    ORDER_STATUS_DEL: "200",
                    ORDER_STATUS_SERVICE_PROCCESS: "300",
                    serverTime: 0,
                    homeData: null,
                    homeDataCacheTime: 0,
                    cateListData: null,
                    cateListCacheTime: 0,
                    brandsListData: {
                        brandIndexList: [],
                        brandItems: []
                    },
                    brandsListCacheTime: 0,
                    searchDefaultwords: [],
                    searchHotwords: [],
                    currentPage: {
                        nav: null,
                        tabbar: !1
                    },
                    env: {
                        KJ_API: "production",
                        wechat: !1,
                        mpWechat: !1,
                        mpAlipay: !1,
                        mpJd: !1,
                        mpBd: !1,
                        app: !1
                    },
                    isH5Client: !0,
                    homeMaskShow: !0,
                    payInfo: {
                        type: 1,
                        barcode: "",
                        count: 1,
                        suit_code: "",
                        pcode: ""
                    }
                }
            }
              , k = {
                nuxtServerInit: function(t, n) {
                    return Object(o.a)(regeneratorRuntime.mark((function o() {
                        var w, k, _, O, j, P, z, S, T, E, $, C, R, I, A, U, D, N, L;
                        return regeneratorRuntime.wrap((function(o) {
                            for (; ; )
                                switch (o.prev = o.next) {
                                case 0:
                                    return w = t.commit,
                                    k = n.req,
                                    _ = n.redirect,
                                    o.next = 4,
                                    Object(l.hd)();
                                case 4:
                                    (O = o.sent).data && 1e4 === O.data.code && _("/help/stop?message=".concat(O.data.data.message)),
                                    j = {
                                        KJ_API: "production",
                                        wechat: !1,
                                        mpWechat: !1,
                                        mpAlipay: !1,
                                        app: !1,
                                        mpJd: !1,
                                        mpBd: !1
                                    },
                                    e.env && e.env.hasOwnProperty("KJ_API") && (j.KJ_API = e.env.KJ_API),
                                    (P = k.headers["user-agent"]) && P.toLowerCase().indexOf("micromessenger") > -1 && (j.wechat = !0),
                                    k._parsedUrl.query && (k._parsedUrl.query.indexOf("from=mpweixin") > -1 && (j.wechat = !0,
                                    j.mpWechat = !0),
                                    k._parsedUrl.query.indexOf("from=mpalipay") > -1 && (j.mpWechat = !0,
                                    j.mpAlipay = !0),
                                    k._parsedUrl.query.indexOf("from=mptoutiao") > -1 && (j.mpWechat = !0),
                                    k._parsedUrl.query.indexOf("from=mpjd") > -1 && (j.mpWechat = !0,
                                    j.mpJd = !0),
                                    k._parsedUrl.query.indexOf("from=mpbaidu") > -1 && (j.mpWechat = !0,
                                    j.mpBd = !0),
                                    j.app = k._parsedUrl.query.indexOf("from=appplus") > -1),
                                    w("updateEnv", j),
                                    k._parsedUrl.query && k._parsedUrl.query.indexOf("dftk") > -1 ? (z = k._parsedUrl.query.match(y)) && w("User/updateUser", z[1]) : k.headers.cookie && (null === (S = r.a.fetchFromCookie("UserToken", k.headers.cookie)) ? w("User/deleteUser") : null !== (T = decodeURIComponent(S)) ? w("User/updateUser", T) : console.error("无法解析token, cookie值为：", S)),
                                    k._parsedUrl.query && k._parsedUrl.query.indexOf("mid") > -1 ? (E = k._parsedUrl.query.match(f)) && (Object(c.default)().commit("setMid", E[1]),
                                    w("User/updateMID", E[1])) : k.headers.cookie && null !== ($ = r.a.fetchFromCookie("mid", k.headers.cookie)) && (Object(c.default)().commit("setMid", $),
                                    w("User/updateMID", $)),
                                    k._parsedUrl.query && k._parsedUrl.query.indexOf("sid") > -1 ? (C = k._parsedUrl.query.match(m)) && (Object(c.default)().commit("setSid", C[1]),
                                    w("User/updateSID", C[1])) : k.headers.cookie && null !== (R = r.a.fetchFromCookie("sid", k.headers.cookie)) && (Object(c.default)().commit("setSid", R),
                                    w("User/updateSID", R)),
                                    k._parsedUrl.query && k._parsedUrl.query.indexOf("pid") > -1 ? (I = k._parsedUrl.query.match(h)) && (Object(c.default)().commit("setPid", I[1]),
                                    w("User/updatePID", I[1])) : k.headers.cookie && null !== (A = r.a.fetchFromCookie("pid", k.headers.cookie)) && (Object(c.default)().commit("setPid", A),
                                    w("User/updatePID", A)),
                                    Object(c.default)().commit("setPlid", d.a.platFormId),
                                    w("User/updatePLID", d.a.platFormId),
                                    k._parsedUrl.query && k._parsedUrl.query.indexOf("from") > -1 && k._parsedUrl.query.indexOf("platform") > -1 ? (U = k._parsedUrl.query.match(v)) && (Object(c.default)().commit("setPlid", U[1]),
                                    w("User/updatePLID", U[1])) : k.headers.cookie && null !== (D = r.a.fetchFromCookie("plid", k.headers.cookie)) && (Object(c.default)().commit("setPlid", D),
                                    w("User/updatePLID", D)),
                                    k._parsedUrl.query && k._parsedUrl.query.indexOf("sflsource") > -1 ? (N = k._parsedUrl.query.match(x)) && (Object(c.default)().commit("setSflsource", N[1]),
                                    w("User/updateSflsource", N[1])) : k.headers.cookie && null !== (L = r.a.fetchFromCookie("sflsource", k.headers.cookie)) && (Object(c.default)().commit("setSflsource", L),
                                    w("User/updateSflsource", L)),
                                    w("setServerTime", (new Date).getTime());
                                case 21:
                                case "end":
                                    return o.stop()
                                }
                        }
                        ), o)
                    }
                    )))()
                },
                querySearchWords: function(e) {
                    return Object(o.a)(regeneratorRuntime.mark((function t() {
                        var n, o;
                        return regeneratorRuntime.wrap((function(t) {
                            for (; ; )
                                switch (t.prev = t.next) {
                                case 0:
                                    return n = e.commit,
                                    t.next = 3,
                                    Object(l.fd)(r.a.fetchFromCookie("gid"));
                                case 3:
                                    (o = t.sent).data && 200 === o.data.code && n("updateSearchWords", o.data.data);
                                case 5:
                                case "end":
                                    return t.stop()
                                }
                        }
                        ), t)
                    }
                    )))()
                },
                querySearchHotWords: function(e) {
                    return Object(o.a)(regeneratorRuntime.mark((function t() {
                        var n, o;
                        return regeneratorRuntime.wrap((function(t) {
                            for (; ; )
                                switch (t.prev = t.next) {
                                case 0:
                                    return n = e.commit,
                                    t.next = 3,
                                    Object(l.hd)(r.a.fetchFromCookie("gid"));
                                case 3:
                                    (o = t.sent).data && 200 === o.data.code && n("updateHotWords", o.data.data);
                                case 5:
                                case "end":
                                    return t.stop()
                                }
                        }
                        ), t)
                    }
                    )))()
                }
            }
              , _ = {
                cachedHomeData: function(e) {
                    return null !== e.homeData && (new Date).getTime() - e.homeDataCacheTime > 6e5 ? null : e.homeData
                },
                cachedCateListData: function(e) {
                    return null !== e.cateListData && (new Date).getTime() - e.cateListCacheTime > 6e5 ? null : e.cateListData
                },
                cachedBrandsListData: function(e) {
                    return e.brandsListData.brandIndexList.length > 0 ? (new Date).getTime() - e.brandsListCacheTime > 6e5 ? null : e.brandsListData : null
                }
            }
              , O = {
                setHomeMaskShow: function(e, t) {
                    e.homeMaskShow = t
                },
                updateIsH5Client: function(e, t) {
                    e.isH5Client = t
                },
                updateEnv: function(e, t) {
                    e.env = t
                },
                setServerTime: function(e, t) {
                    e.serverTime = t
                },
                updateHomeData: function(e, data) {
                    e.homeData = data,
                    e.homeDataCacheTime = (new Date).getTime()
                },
                updateCateListData: function(e, data) {
                    e.cateListData = data,
                    e.cateListCacheTime = (new Date).getTime()
                },
                updateShowCateId: function(e, t) {
                    e.cateListData.selectedCateId = t
                },
                updateBrandsListData: function(e, data) {
                    e.brandsListData = data,
                    e.brandsListCacheTime = (new Date).getTime()
                },
                updateSearchWords: function(e, data) {
                    e.searchDefaultwords = data
                },
                updateHotWords: function(e, data) {
                    e.searchHotwords = data
                },
                updatePage: function(e, t) {
                    e.currentPage = t
                },
                updatePayInfo: function(e, data) {
                    e.payInfo = data || e.payInfo
                }
            }
        }
        .call(this, n(77))
    },
    299: function(e, t, n) {
        "use strict";
        n.r(t),
        n.d(t, "state", (function() {
            return o
        }
        )),
        n.d(t, "mutations", (function() {
            return r
        }
        )),
        n.d(t, "actions", (function() {
            return l
        }
        ));
        n(36);
        var o = function() {
            return {
                idcard: "",
                name: "",
                phone: "",
                province: "",
                city: "",
                city_area: "",
                address: "",
                addressId: "",
                supplementIdcard: "",
                ExPrice: 0
            }
        }
          , r = {
            updateAddr: function(e, t) {
                e.id = t.id,
                e.idcard = t.idcard,
                e.name = t.name,
                e.phone = t.phone,
                e.province = t.province,
                e.city = t.city,
                e.city_area = t.city_area,
                e.address = t.address,
                e.addressId = t.addressId,
                e.img1 = t.img1,
                e.img2 = t.img2,
                e.ExPrice = t.ExPrice,
                e.area_code = t.area_code
            },
            updateSupplement: function(e, t) {
                e.supplementIdcard = t
            }
        }
          , l = {
            setAddr: function(e, t) {
                t && e.commit("updateAddr", t)
            },
            setSupplement: function(e, t) {
                t && e.commit("updateSupplement", t)
            }
        }
    },
    3: function(e, t, n) {
        "use strict";
        var o = n(27)
          , r = (n(68),
        n(97),
        {
            fetchFromLocal: function(e) {
                if (Storage)
                    try {
                        return window.localStorage.getItem(e)
                    } catch (e) {
                        return null
                    }
            },
            saveToLocal: function(e, t) {
                if (Storage)
                    try {
                        return window.localStorage.setItem(e, t),
                        !0
                    } catch (e) {
                        return !1
                    }
            },
            removeFromLocal: function(e) {
                if (Storage)
                    try {
                        return window.localStorage.removeItem(e),
                        !0
                    } catch (e) {
                        return !1
                    }
            },
            fetchFromCookie: function(e, t) {
                var n = new RegExp("(^| )" + e + "=([^;]*)(;|$)")
                  , o = (t || document.cookie).match(n);
                return void 0 !== o && null != o ? o[2] : null
            },
            saveToCookie: function(e, t, n, o) {
                var r = new Date;
                null !== n && r.setTime(r.getTime() + 1e3 * n),
                document.cookie = e + "=" + encodeURIComponent(t) + (null == n ? "" : ";path=/;expires=" + r.toGMTString()) + (null == o ? "" : ";path=/;domain=" + o)
            },
            removeFromCookie: function(e) {
                var t = new Date;
                t.setTime(t.getTime() - 1e3);
                var n = this.fetchFromCookie(e);
                null != n && (document.cookie = e + "=" + n + ";expires=" + t.toGMTString() + ";path=/;")
            },
            fetchFromSession: function(e) {
                var t = sessionStorage.getItem(e);
                return /^\{.*\}$/.test(t) && (t = JSON.parse(t)),
                t
            },
            saveToSession: function(e, t) {
                return Object(o.a)(t) === Object(o.a)({}) && (t = JSON.stringify(t)),
                sessionStorage.setItem(e, t)
            },
            removeFromSession: function(e) {
                return sessionStorage.removeItem(e)
            }
        });
        t.a = r
    },
    300: function(e, t, n) {
        "use strict";
        n.r(t),
        n.d(t, "state", (function() {
            return f
        }
        )),
        n.d(t, "mutations", (function() {
            return m
        }
        )),
        n.d(t, "actions", (function() {
            return h
        }
        ));
        n(75),
        n(37),
        n(31),
        n(16),
        n(53),
        n(21);
        var o = n(4)
          , r = n(32)
          , l = n(35);
        function c(object, e) {
            var t = Object.keys(object);
            if (Object.getOwnPropertySymbols) {
                var n = Object.getOwnPropertySymbols(object);
                e && (n = n.filter((function(e) {
                    return Object.getOwnPropertyDescriptor(object, e).enumerable
                }
                ))),
                t.push.apply(t, n)
            }
            return t
        }
        function d(e) {
            for (var i = 1; i < arguments.length; i++) {
                var source = null != arguments[i] ? arguments[i] : {};
                i % 2 ? c(Object(source), !0).forEach((function(t) {
                    Object(r.a)(e, t, source[t])
                }
                )) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(source)) : c(Object(source)).forEach((function(t) {
                    Object.defineProperty(e, t, Object.getOwnPropertyDescriptor(source, t))
                }
                ))
            }
            return e
        }
        var f = function() {
            return {
                pageTitle: "",
                placeHolder: "请输入搜索内容",
                iptKeyword: "",
                list: [],
                inited: !1,
                loading: !1,
                isPageTurn: !1,
                nomore: !1,
                params: {
                    type: 0,
                    sort: 0,
                    page: 1,
                    keyword: "",
                    brandId: null,
                    classId: null,
                    hasStock: 1
                },
                pageTotal: 10,
                fetchCache: !1
            }
        }
          , m = {
            setFetchCache: function(e, t) {
                e.fetchCache = t
            },
            updateParam: function(e, t) {
                e.params = t
            },
            updateTitle: function(e, t) {
                e.pageTitle = t
            },
            updateKeyword: function(e, t) {
                e.iptKeyword = t
            },
            setInited: function(e, t) {
                e.inited = t
            },
            resetData: function(e) {
                e.nomore = !1,
                e.list = [],
                e.inited = !1
            },
            setLoading: function(e, t) {
                e.loading = t
            },
            setPageTurn: function(e, t) {
                e.isPageTurn = t
            },
            setNoMore: function(e, t) {
                e.nomore = t
            },
            setList: function(e, t) {
                e.list = t
            },
            setPageData: function(e, t) {
                if (e.isPageTurn) {
                    var n = JSON.parse(JSON.stringify(e.list));
                    n = n.concat(t.goodsList),
                    e.list = n,
                    e.isPageTurn = !1
                } else
                    e.list = t.goodsList;
                e.pageTotal = t.pageTotal,
                e.inited = !0,
                e.loading = !1,
                e.params.page >= e.pageTotal && (e.nomore = !0)
            }
        }
          , h = {
            sortByAll: function(e) {
                var t = e.dispatch
                  , n = e.state
                  , o = e.commit;
                if (0 !== n.params.sort) {
                    var r = d({}, n.params);
                    r.page = 1,
                    r.sort = 0,
                    o("updateParam", r),
                    o("resetData"),
                    t("loadData")
                }
            },
            loadData: function(e) {
                return Object(o.a)(regeneratorRuntime.mark((function t() {
                    var n, o, r, c;
                    return regeneratorRuntime.wrap((function(t) {
                        for (; ; )
                            switch (t.prev = t.next) {
                            case 0:
                                return n = e.state,
                                (o = e.commit)("setLoading", !0),
                                r = d({}, n.params),
                                t.next = 5,
                                Object(l.Ac)(r, n.isPageTurn);
                            case 5:
                                200 === (c = t.sent).data.code && o("setPageData", c.data.data);
                            case 7:
                            case "end":
                                return t.stop()
                            }
                    }
                    ), t)
                }
                )))()
            },
            sortBySales: function(e) {
                var t = e.dispatch
                  , n = e.state
                  , o = e.commit;
                if (1 !== n.params.sort) {
                    var r = d({}, n.params);
                    r.page = 1,
                    r.sort = 1,
                    o("updateParam", r),
                    o("resetData"),
                    t("loadData")
                }
            },
            sortByPrice: function(e) {
                var t = e.dispatch
                  , n = e.state
                  , o = e.commit
                  , r = d({}, n.params);
                r.page = 1,
                r.sort = -2 === r.sort ? 2 : -2,
                o("updateParam", r),
                o("resetData"),
                t("loadData")
            },
            loadMore: function(e) {
                var t = e.dispatch
                  , n = e.state
                  , o = e.commit;
                if (!n.loading && n.params.page !== n.pageTotal) {
                    var r = d({}, n.params);
                    r.page++,
                    o("updateParam", r),
                    o("setPageTurn", !0),
                    t("loadData")
                }
            }
        }
    },
    301: function(e, t, n) {
        "use strict";
        n.r(t),
        function(e) {
            n.d(t, "state", (function() {
                return o
            }
            ));
            var o = function() {
                return {
                    STATIC_DOMAIN: e.env.KJ_STATIC_DOMAIN_M ? e.env.KJ_STATIC_DOMAIN_M : "",
                    IMG_DOMAIN: "//img.kuajing0898.com"
                }
            }
        }
        .call(this, n(77))
    },
    302: function(e, t, n) {
        "use strict";
        n.r(t),
        n.d(t, "state", (function() {
            return o
        }
        )),
        n.d(t, "mutations", (function() {
            return r
        }
        ));
        var o = function() {
            return {
                keyword: null,
                brandId: null,
                class3Id: null,
                hasStock: 0,
                page: 1
            }
        }
          , r = {
            changeParam: function(e, t) {
                for (var n in t)
                    e[n] = t[n]
            },
            resetParam: function(e, t) {}
        }
    },
    35: function(e, t, n) {
        "use strict";
        n.d(t, "mc", (function() {
            return l
        }
        )),
        n.d(t, "oc", (function() {
            return c
        }
        )),
        n.d(t, "nc", (function() {
            return d
        }
        )),
        n.d(t, "hc", (function() {
            return f
        }
        )),
        n.d(t, "Nb", (function() {
            return m
        }
        )),
        n.d(t, "fd", (function() {
            return h
        }
        )),
        n.d(t, "hd", (function() {
            return v
        }
        )),
        n.d(t, "Ac", (function() {
            return x
        }
        )),
        n.d(t, "a", (function() {
            return y
        }
        )),
        n.d(t, "gc", (function() {
            return w
        }
        )),
        n.d(t, "Uc", (function() {
            return k
        }
        )),
        n.d(t, "Ec", (function() {
            return _
        }
        )),
        n.d(t, "M", (function() {
            return O
        }
        )),
        n.d(t, "ad", (function() {
            return j
        }
        )),
        n.d(t, "A", (function() {
            return P
        }
        )),
        n.d(t, "e", (function() {
            return z
        }
        )),
        n.d(t, "Pc", (function() {
            return S
        }
        )),
        n.d(t, "Oc", (function() {
            return T
        }
        )),
        n.d(t, "Qc", (function() {
            return E
        }
        )),
        n.d(t, "yb", (function() {
            return $
        }
        )),
        n.d(t, "x", (function() {
            return C
        }
        )),
        n.d(t, "Lc", (function() {
            return R
        }
        )),
        n.d(t, "Jc", (function() {
            return I
        }
        )),
        n.d(t, "od", (function() {
            return A
        }
        )),
        n.d(t, "P", (function() {
            return U
        }
        )),
        n.d(t, "S", (function() {
            return D
        }
        )),
        n.d(t, "Db", (function() {
            return N
        }
        )),
        n.d(t, "Tb", (function() {
            return L
        }
        )),
        n.d(t, "Ed", (function() {
            return M
        }
        )),
        n.d(t, "c", (function() {
            return address
        }
        )),
        n.d(t, "Kc", (function() {
            return B
        }
        )),
        n.d(t, "wb", (function() {
            return F
        }
        )),
        n.d(t, "yc", (function() {
            return H
        }
        )),
        n.d(t, "Ib", (function() {
            return V
        }
        )),
        n.d(t, "Jb", (function() {
            return G
        }
        )),
        n.d(t, "xb", (function() {
            return J
        }
        )),
        n.d(t, "Cb", (function() {
            return X
        }
        )),
        n.d(t, "Bb", (function() {
            return W
        }
        )),
        n.d(t, "Ab", (function() {
            return Y
        }
        )),
        n.d(t, "Q", (function() {
            return K
        }
        )),
        n.d(t, "xc", (function() {
            return Z
        }
        )),
        n.d(t, "wc", (function() {
            return Q
        }
        )),
        n.d(t, "Lb", (function() {
            return ee
        }
        )),
        n.d(t, "zb", (function() {
            return te
        }
        )),
        n.d(t, "Bd", (function() {
            return ne
        }
        )),
        n.d(t, "Bc", (function() {
            return oe
        }
        )),
        n.d(t, "t", (function() {
            return re
        }
        )),
        n.d(t, "R", (function() {
            return ae
        }
        )),
        n.d(t, "U", (function() {
            return ie
        }
        )),
        n.d(t, "V", (function() {
            return le
        }
        )),
        n.d(t, "Ad", (function() {
            return ce
        }
        )),
        n.d(t, "fb", (function() {
            return de
        }
        )),
        n.d(t, "db", (function() {
            return se
        }
        )),
        n.d(t, "mb", (function() {
            return ue
        }
        )),
        n.d(t, "lb", (function() {
            return fe
        }
        )),
        n.d(t, "y", (function() {
            return pe
        }
        )),
        n.d(t, "Dd", (function() {
            return me
        }
        )),
        n.d(t, "Y", (function() {
            return he
        }
        )),
        n.d(t, "Z", (function() {
            return be
        }
        )),
        n.d(t, "Ic", (function() {
            return ge
        }
        )),
        n.d(t, "T", (function() {
            return ve
        }
        )),
        n.d(t, "yd", (function() {
            return xe
        }
        )),
        n.d(t, "Zc", (function() {
            return ye
        }
        )),
        n.d(t, "Wc", (function() {
            return we
        }
        )),
        n.d(t, "Xc", (function() {
            return ke
        }
        )),
        n.d(t, "u", (function() {
            return _e
        }
        )),
        n.d(t, "Yc", (function() {
            return Oe
        }
        )),
        n.d(t, "ud", (function() {
            return je
        }
        )),
        n.d(t, "Sc", (function() {
            return Pe
        }
        )),
        n.d(t, "d", (function() {
            return ze
        }
        )),
        n.d(t, "Tc", (function() {
            return Se
        }
        )),
        n.d(t, "Rc", (function() {
            return Te
        }
        )),
        n.d(t, "bb", (function() {
            return Ee
        }
        )),
        n.d(t, "ab", (function() {
            return $e
        }
        )),
        n.d(t, "Fd", (function() {
            return Ce
        }
        )),
        n.d(t, "Zb", (function() {
            return Re
        }
        )),
        n.d(t, "dd", (function() {
            return Ie
        }
        )),
        n.d(t, "cd", (function() {
            return Ae
        }
        )),
        n.d(t, "Nc", (function() {
            return Ue
        }
        )),
        n.d(t, "kb", (function() {
            return De
        }
        )),
        n.d(t, "md", (function() {
            return Ne
        }
        )),
        n.d(t, "bd", (function() {
            return Le
        }
        )),
        n.d(t, "W", (function() {
            return Me
        }
        )),
        n.d(t, "jb", (function() {
            return Be
        }
        )),
        n.d(t, "Fc", (function() {
            return qe
        }
        )),
        n.d(t, "zc", (function() {
            return Fe
        }
        )),
        n.d(t, "Sb", (function() {
            return He
        }
        )),
        n.d(t, "Cd", (function() {
            return Ve
        }
        )),
        n.d(t, "i", (function() {
            return Ge
        }
        )),
        n.d(t, "j", (function() {
            return Je
        }
        )),
        n.d(t, "zd", (function() {
            return Xe
        }
        )),
        n.d(t, "w", (function() {
            return We
        }
        )),
        n.d(t, "G", (function() {
            return Ye
        }
        )),
        n.d(t, "ub", (function() {
            return Ke
        }
        )),
        n.d(t, "K", (function() {
            return Ze
        }
        )),
        n.d(t, "L", (function() {
            return Qe
        }
        )),
        n.d(t, "I", (function() {
            return et
        }
        )),
        n.d(t, "E", (function() {
            return tt
        }
        )),
        n.d(t, "J", (function() {
            return nt
        }
        )),
        n.d(t, "F", (function() {
            return ot
        }
        )),
        n.d(t, "H", (function() {
            return at
        }
        )),
        n.d(t, "vd", (function() {
            return it
        }
        )),
        n.d(t, "Mc", (function() {
            return lt
        }
        )),
        n.d(t, "ec", (function() {
            return ct
        }
        )),
        n.d(t, "Yb", (function() {
            return st
        }
        )),
        n.d(t, "ic", (function() {
            return ut
        }
        )),
        n.d(t, "jc", (function() {
            return ft
        }
        )),
        n.d(t, "kc", (function() {
            return pt
        }
        )),
        n.d(t, "Rb", (function() {
            return mt
        }
        )),
        n.d(t, "g", (function() {
            return ht
        }
        )),
        n.d(t, "h", (function() {
            return bt
        }
        )),
        n.d(t, "Mb", (function() {
            return gt
        }
        )),
        n.d(t, "C", (function() {
            return vt
        }
        )),
        n.d(t, "xd", (function() {
            return xt
        }
        )),
        n.d(t, "l", (function() {
            return yt
        }
        )),
        n.d(t, "kd", (function() {
            return wt
        }
        )),
        n.d(t, "ed", (function() {
            return kt
        }
        )),
        n.d(t, "jd", (function() {
            return _t
        }
        )),
        n.d(t, "vb", (function() {
            return Ot
        }
        )),
        n.d(t, "Cc", (function() {
            return jt
        }
        )),
        n.d(t, "Dc", (function() {
            return Pt
        }
        )),
        n.d(t, "qc", (function() {
            return zt
        }
        )),
        n.d(t, "pc", (function() {
            return St
        }
        )),
        n.d(t, "rc", (function() {
            return Tt
        }
        )),
        n.d(t, "dc", (function() {
            return Et
        }
        )),
        n.d(t, "Kb", (function() {
            return $t
        }
        )),
        n.d(t, "m", (function() {
            return Ct
        }
        )),
        n.d(t, "n", (function() {
            return Rt
        }
        )),
        n.d(t, "o", (function() {
            return It
        }
        )),
        n.d(t, "Fb", (function() {
            return At
        }
        )),
        n.d(t, "Eb", (function() {
            return Ut
        }
        )),
        n.d(t, "X", (function() {
            return Dt
        }
        )),
        n.d(t, "p", (function() {
            return Nt
        }
        )),
        n.d(t, "q", (function() {
            return Lt
        }
        )),
        n.d(t, "r", (function() {
            return Mt
        }
        )),
        n.d(t, "s", (function() {
            return Bt
        }
        )),
        n.d(t, "k", (function() {
            return qt
        }
        )),
        n.d(t, "O", (function() {
            return Ft
        }
        )),
        n.d(t, "vc", (function() {
            return Ht
        }
        )),
        n.d(t, "Gc", (function() {
            return Vt
        }
        )),
        n.d(t, "lc", (function() {
            return Gt
        }
        )),
        n.d(t, "sc", (function() {
            return Jt
        }
        )),
        n.d(t, "uc", (function() {
            return Xt
        }
        )),
        n.d(t, "tc", (function() {
            return Wt
        }
        )),
        n.d(t, "bc", (function() {
            return Yt
        }
        )),
        n.d(t, "cc", (function() {
            return Kt
        }
        )),
        n.d(t, "td", (function() {
            return Zt
        }
        )),
        n.d(t, "ac", (function() {
            return Qt
        }
        )),
        n.d(t, "Ob", (function() {
            return en
        }
        )),
        n.d(t, "sb", (function() {
            return tn
        }
        )),
        n.d(t, "Wb", (function() {
            return nn
        }
        )),
        n.d(t, "Ub", (function() {
            return on
        }
        )),
        n.d(t, "Xb", (function() {
            return rn
        }
        )),
        n.d(t, "N", (function() {
            return an
        }
        )),
        n.d(t, "b", (function() {
            return ln
        }
        )),
        n.d(t, "f", (function() {
            return cn
        }
        )),
        n.d(t, "Pb", (function() {
            return dn
        }
        )),
        n.d(t, "wd", (function() {
            return sn
        }
        )),
        n.d(t, "Gd", (function() {
            return un
        }
        )),
        n.d(t, "Hd", (function() {
            return fn
        }
        )),
        n.d(t, "z", (function() {
            return pn
        }
        )),
        n.d(t, "v", (function() {
            return mn
        }
        )),
        n.d(t, "D", (function() {
            return hn
        }
        )),
        n.d(t, "ld", (function() {
            return bn
        }
        )),
        n.d(t, "cb", (function() {
            return gn
        }
        )),
        n.d(t, "ib", (function() {
            return vn
        }
        )),
        n.d(t, "hb", (function() {
            return xn
        }
        )),
        n.d(t, "Vb", (function() {
            return yn
        }
        )),
        n.d(t, "Vc", (function() {
            return wn
        }
        )),
        n.d(t, "gd", (function() {
            return kn
        }
        )),
        n.d(t, "id", (function() {
            return _n
        }
        )),
        n.d(t, "ob", (function() {
            return On
        }
        )),
        n.d(t, "nd", (function() {
            return jn
        }
        )),
        n.d(t, "nb", (function() {
            return Pn
        }
        )),
        n.d(t, "rb", (function() {
            return zn
        }
        )),
        n.d(t, "gb", (function() {
            return Sn
        }
        )),
        n.d(t, "tb", (function() {
            return Tn
        }
        )),
        n.d(t, "eb", (function() {
            return En
        }
        )),
        n.d(t, "pb", (function() {
            return $n
        }
        )),
        n.d(t, "qb", (function() {
            return Cn
        }
        )),
        n.d(t, "pd", (function() {
            return Rn
        }
        )),
        n.d(t, "qd", (function() {
            return In
        }
        )),
        n.d(t, "Qb", (function() {
            return An
        }
        )),
        n.d(t, "rd", (function() {
            return Un
        }
        )),
        n.d(t, "B", (function() {
            return Dn
        }
        )),
        n.d(t, "sd", (function() {
            return Nn
        }
        )),
        n.d(t, "Hc", (function() {
            return Ln
        }
        )),
        n.d(t, "Hb", (function() {
            return Mn
        }
        )),
        n.d(t, "Gb", (function() {
            return Bn
        }
        )),
        n.d(t, "fc", (function() {
            return qn
        }
        ));
        var o = n(1)
          , r = n(6);
        n(81);
        function l() {
            var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : null
              , t = arguments.length > 1 ? arguments[1] : void 0;
            return o.a.get("/home/mobile/index", {
                token: e,
                cache: !0,
                platformId: t
            }, !0)
        }
        function c() {
            return o.a.get("/home/mobile/get-top-ad", null, !0)
        }
        function d() {
            return o.a.get("/home/mobile/member-point", null, !0)
        }
        function f(e, t, n) {
            return o.a.get("/home/mobile/new-goods-list", {
                typeid: e,
                page: t,
                adid: n
            }, !0)
        }
        function m() {
            return o.a.get("/shop/shop/info", null, !0)
        }
        function h(e) {
            return o.a.get("/search/search/defaultwords", {
                gid: e
            }, !0)
        }
        function v(e) {
            return o.a.get("/search/search/hotwords", {
                gid: e
            }, !0)
        }
        function x(e, t) {
            return o.a.get("/search/search/index", e, t)
        }
        function y(e, t, n) {
            return o.a.post("/sms/send", {
                mobile: e,
                type: 1,
                used: t,
                ident: n
            }, !0)
        }
        function w(e) {
            return o.a.post("/user/index/isuser", {
                mobile: e
            })
        }
        function k(e) {
            return o.a.post("/user/index/backpassword", e)
        }
        function _(e, t) {
            return o.a.post("/user/index/login", {
                mobile: e,
                password: t
            })
        }
        function O(e, code, t) {
            return o.a.post("/user/index/mobilelogin", {
                mobile: e,
                code: code,
                ident: t
            })
        }
        function j(e) {
            return o.a.post("/user/index/register", e)
        }
        function P(e) {
            return o.a.post("/user/info/change-mobile", e)
        }
        function z(e, t, n, r, l, c) {
            return o.a.post("/weixin/index/register-erp", {
                token: e,
                name: t,
                idtype: n,
                idcard: r,
                mobile: l,
                smscode: c
            })
        }
        function S(e) {
            return o.a.post("/weixin/index/erp-user", {
                mobile: e
            })
        }
        function T(e) {
            return o.a.post("/weixin/index/user-bar-code", {
                cid: e
            })
        }
        function E(e, t, n, r, l) {
            return o.a.get("/weixin/index/points-detail", {
                token: e,
                page_no: t,
                page_size: n,
                type: r
            }, l)
        }
        function $(e) {
            return o.a.post("/order/order/available-point", e, !0)
        }
        var C = {
            pageData: function(e, t) {
                return o.a.post("/cart/cart/cartlist", {
                    token: e,
                    gid: t
                })
            },
            addpro: function(e) {
                return o.a.post("/cart/cart/add", e)
            },
            addPartner: function(e) {
                return o.a.post("/cart/cart/add-partner", e)
            },
            delpro: function(e) {
                return o.a.post("/cart/cart/del", e)
            },
            clearcart: function(e) {
                return o.a.post("/cart/cart/delall", {
                    uid: e
                })
            },
            changeCount: function(e) {
                return o.a.post("/cart/cart/count", e, !0)
            },
            selectpro: function(e) {
                return o.a.post("/cart/cart/select", e)
            },
            selectAll: function(param) {
                return o.a.post("/cart/cart/select-all", param)
            },
            selectGroup: function(param) {
                return o.a.post("/cart/cart/select-group-all", param)
            },
            changeSku: function(param) {
                return o.a.post("/cart/cart/swap-sku", param)
            }
        }
          , R = {
            title: function(e, t) {
                var n = arguments.length > 2 && void 0 !== arguments[2] && arguments[2];
                return o.a.get("/goods/goods/getbybarcode", {
                    barcode: e,
                    token: t
                }, n)
            },
            info: function(e) {
                return o.a.get("/goods/goods/getdesc", {
                    barcode: e
                }, !0)
            }
        };
        function I(e) {
            return o.a.post("/order/order/buy", e, !0)
        }
        function A(e) {
            return o.a.post("/order/order/first-back", {
                token: e
            }, !1)
        }
        function U(e) {
            var t = !(arguments.length > 1 && void 0 !== arguments[1]) || arguments[1];
            return o.a.post("/cart/cart/toconform", e, t)
        }
        function D(e) {
            return o.a.post("/cart/cart/getconsigneepickupinfo", e)
        }
        function N(e, t, n) {
            return o.a.post("/cart/cart/get-order-tax", {
                token: e,
                idcard: t,
                barcodes: n
            }, !0)
        }
        function L(e, t) {
            var n = arguments.length > 2 && void 0 !== arguments[2] && arguments[2];
            return o.a.post("/user/info/index", {
                gid: e,
                token: t
            }, n)
        }
        function M(e) {
            return o.a.get("/login/logout", {
                token: e
            }, !0)
        }
        var address = {
            getAll: function(e) {
                var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : null
                  , p = {
                    token: e
                };
                return null !== t && (p.barcode = t),
                o.a.post("/user/order/addressall", p)
            },
            add: function(e) {
                return o.a.post("/user/order/addressadd", e)
            },
            remove: function(e, t) {
                return o.a.post("/user/order/addressdel", {
                    id: e,
                    token: t
                })
            },
            setdefault: function(e) {
                return o.a.post("/user/order/addressdefault", e)
            },
            edit: function(e) {
                return o.a.post("/user/order/addressadd", e)
            }
        };
        function B(e) {
            return o.a.post("/order/order/post-life-face-verify", e, !0, {
                headers: {
                    "Content-Type": "multipart/form-data"
                }
            })
        }
        function F(e, t, n, r) {
            return o.a.post("/order/order/get-life-face-verify-valid", {
                type: e,
                order_sn: t,
                package_id: n,
                token: r
            })
        }
        function H(e, t, n, r) {
            return o.a.post("/order/face/is-verify", {
                name: t,
                idcard: n,
                token: e,
                consignee_id: r
            })
        }
        function V(e) {
            return o.a.post("/pay/index/paylist", {
                order_sn: e
            })
        }
        function G(e, t) {
            return o.a.post("/index/common-pay-list", {
                order_sn: e,
                type: t
            }, !1, r.a.payService)
        }
        function J(e, t) {
            return o.a.post("/order/order/get-logistics-by-ordersn", {
                order_sn: e,
                token: t
            })
        }
        function X(e, t, n, r) {
            return o.a.post("/order/order/get-order-list", {
                token: e,
                order_status: t,
                page: n
            }, r)
        }
        function W(e, t) {
            return o.a.post("/order/order/get-order-detail", {
                order_sn: e,
                token: t
            }, !0)
        }
        function Y(e, t, n, r) {
            return o.a.post("/order/order/get-trace-list", {
                token: e,
                status: t,
                page: n
            }, r)
        }
        function K(e, t) {
            return o.a.post("/order/order/confirm-receipt-order", {
                order_sn: e,
                token: t
            })
        }
        function Z(e) {
            return o.a.post("/order/invoice/set", e, !0)
        }
        function Q(e, t) {
            return o.a.post("/order/invoice/invoice-info", {
                order_sn: e,
                token: t
            }, !1)
        }
        function ee(e, t, n, r) {
            return o.a.post("/order/aftersale/index", {
                page: e,
                token: n,
                status: t
            }, r)
        }
        function te(e, t) {
            return o.a.post("/order/order/get-package-detail", {
                package_id: e,
                token: t
            }, !0)
        }
        function ne(e, t, n, r) {
            return o.a.post("/order/order/update-trace-info", {
                package_id: t,
                token: e,
                address_id: n,
                is_force: r
            }, !0)
        }
        function oe(e, t) {
            return o.a.post("/order/order/get-logistics-info", {
                package_id: t,
                token: e
            })
        }
        function re(e, t) {
            return o.a.post("/order/order/cancel-order", {
                order_sn: e,
                token: t
            })
        }
        function ae(e, t) {
            return o.a.post("/order/order/confirm-receipt", {
                package_id: e,
                token: t
            })
        }
        function ie(e, t) {
            return o.a.post("/order/order/get-backpick", {
                package_id: e,
                token: t
            })
        }
        function le(e, t) {
            return o.a.post("/order/order/get-backpick", {
                order_sn: e,
                token: t
            })
        }
        function ce(data) {
            return o.a.post("/order/order/update-backpick", data, !0)
        }
        function de() {
            return o.a.get("/cate/list", null)
        }
        function se() {
            return o.a.get("/brand/list", null)
        }
        function ue(link) {
            var e = arguments.length > 1 && void 0 !== arguments[1] && arguments[1];
            return o.a.post("/coupon/coupon/couponlink", {
                link: link
            }, e)
        }
        function fe(e, link) {
            var t = arguments.length > 2 && void 0 !== arguments[2] && arguments[2];
            return o.a.post("/coupon/coupon/receivecoupon", {
                link: link,
                token: e
            }, t)
        }
        function pe(e) {
            return o.a.post("/coupon/coupon/ordercoupon", e)
        }
        function me(e, t) {
            var n = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : 0
              , r = arguments.length > 3 ? arguments[3] : void 0;
            return o.a.post("/coupon/coupon/mycoupon", {
                status: e,
                token: t,
                special: n,
                order_sn: r
            })
        }
        function he(code, e, t) {
            return o.a.post("/coupon/coupon/exchangecoupon", {
                code: code,
                token: e,
                type: t
            })
        }
        function be(param) {
            return o.a.get("/coupon/coupon/exchange-notice", param)
        }
        function ge(e, t, n, r, l) {
            return o.a.post("/order/order/order-to-mail", {
                type: e,
                order_sn: t,
                address_id: n,
                token: r,
                is_force: l
            }, !0)
        }
        function ve(code, e) {
            return o.a.get("/coupon/coupon/detail", {
                code: code,
                token: e
            })
        }
        function xe(e) {
            return o.a.post("/shop/refund/upload", e, !1)
        }
        function ye(e) {
            return o.a.post("/order/refund/addrefund", e)
        }
        function we(e, t, n, r) {
            return o.a.post("/order/refund/refunddetails", {
                order_sn: e,
                barcode: t,
                refund_sn: n,
                token: r
            })
        }
        function ke(e, t, n, r) {
            return o.a.post("/order/refund/setexpressinfo", {
                express_company: e,
                express_sn: t,
                refund_sn: n,
                token: r
            })
        }
        function _e(e, t) {
            return o.a.post("/order/refund/cancelrefund", {
                refund_sn: e,
                token: t
            })
        }
        function Oe(e, t) {
            return o.a.get("/order/refund/get-refund-deduct", {
                order_sn: e,
                token: t
            }, !0)
        }
        function je(e) {
            var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : 1;
            return o.a.get("/special/special/getspecial", {
                id: e,
                mobile: t
            })
        }
        function Pe(e) {
            return o.a.post("/weixin/index/get-signature", {
                url: e
            }, !0)
        }
        function ze(e) {
            return o.a.post("/alipay/mobile", {
                order_sn: e
            }, !1)
        }
        function Se(e) {
            return o.a.post("cart/cart/get-number", {
                token: e
            }, !0)
        }
        function Te(e, t) {
            return o.a.post("/oms/pushstatus", {
                token: e,
                orderNo: t
            }, !0)
        }
        function Ee() {
            return o.a.get("/home/mobile/salelist")
        }
        function $e(e, t) {
            return o.a.post("/special/special/get-country-special", {
                code: e,
                platformId: t,
                cache: !0,
                refresh: 0
            })
        }
        function Ce(e, t) {
            return o.a.post("/order/order/check-user-real", {
                token: e,
                order_sn: t
            }, !0)
        }
        function Re() {
            var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : null
              , t = "production" === document.getElementById("ipt_env_api").value
              , n = t ? r.a.defaultService.baseURL : r.a.defaultService.baseURL_TEST
              , o = "".concat(n, "/weixin/index/proxy?shop_id=").concat(r.a.shopId);
            e && (o = "".concat(o, "&r_url=").concat(encodeURIComponent(e))),
            window.location.href = o
        }
        function Ie(e, t) {
            return o.a.post("/weixin/index/get-user-info", {
                access_token: e,
                openid: t
            }, !0)
        }
        function Ae(e, t, n) {
            return o.a.post("/user/index/bind-user-mobile", {
                token: e,
                mobile: t,
                sms_code: n
            })
        }
        function Ue(e) {
            return o.a.post("/promotion/privileged-code/cart-banner", {
                token: e
            }, !0)
        }
        function De(e) {
            return o.a.post("/user/consignee/list", {
                token: e
            })
        }
        function Ne(e) {
            return o.a.post("/user/consignee/set", e, !0)
        }
        function Le(e, t) {
            return o.a.post("/user/consignee/remove", {
                token: e,
                id: t
            })
        }
        function Me(e, t) {
            return o.a.post("/user/consignee/default", {
                token: e,
                id: t
            })
        }
        function Be(e, t) {
            return o.a.post("/cart/cart/get-consignee-info", {
                token: e,
                consignee_id: t
            })
        }
        function qe(e) {
            return o.a.get("/order/order/check-ticket-all", e)
        }
        function Fe(e, t, n) {
            return o.a.get("/order/order/flights", {
                type: e,
                token: t,
                port: n
            })
        }
        function He(e) {
            return o.a.post("/order/flight/get-flight-list", {
                token: e
            })
        }
        function Ve(e) {
            return o.a.post("/order/flight/update-flight", e, !0)
        }
        function Ge(e) {
            return o.a.get("/brand/shop", {
                brand: e
            })
        }
        function Je(e) {
            return o.a.get("/brand/specials", {
                brand: e
            }, !1)
        }
        function Xe(e, t, n) {
            return o.a.post("/order/order/update-batch-trace-info", {
                package_id: e,
                address_id: t,
                token: n
            }, !0)
        }
        function We(e, t) {
            return o.a.post("/cart/cart/deletes", {
                barcodes: e,
                token: t
            }, !0)
        }
        function Ye(e) {
            return o.a.post("/citbrand/brand-data/index", {
                key: e
            }, !0)
        }
        function Ke(e) {
            return o.a.post("/citbrand/brand-data/get-home-page-el-mod?code=home_page_el_mod_jjhf", {
                key: e
            }, !0)
        }
        function Ze(e) {
            return o.a.post("/citbrand/brand-data/indexnew", {
                key: e
            }, !0)
        }
        function Qe(code) {
            return o.a.post("/citbrand/brand-data/get-home-page-el ", {
                code: code
            }, !0)
        }
        function et(e, t) {
            return o.a.get("/brands/brand/menus", {
                brand_id: e,
                isjomalone: t
            }, !1)
        }
        function tt(e, code) {
            return o.a.post("/citbrand/brand-data/best-seller", {
                key: e,
                code: code
            }, !0)
        }
        function nt(e, code) {
            return o.a.post("/citbrand/brand-data/get-special-data", {
                key: e,
                code: code
            }, !1)
        }
        function ot(e, code) {
            return o.a.get("/brands/lauder/beautifully-tips", {
                key: e,
                code: code
            }, !0)
        }
        function at(code) {
            return o.a.get("/brands/brand/subject-with-goods", {
                code: code
            }, !0)
        }
        function it() {
            return o.a.get("/promotion/index/spring-coupon-activities", {}, !0)
        }
        function lt(e) {
            return o.a.get("/promotion/index/privilege-sales", {
                id: e
            }, !0)
        }
        function ct(e, t, n) {
            return o.a.post("/promotion/index/grab-privileged-code", {
                privileged_id: e,
                sale_id: t,
                token: n
            }, !0)
        }
        function st(code, e) {
            return o.a.post("/coupon/coupon/getcoupon", {
                code: code,
                token: e
            }, !0)
        }
        function ut() {
            return o.a.get("/home/mobile/activity", {}, !0)
        }
        function ft(e) {
            return o.a.post("/home/mobile/get-config", {
                config_key: e
            }, !0)
        }
        function pt(e) {
            return o.a.post("/home/mobile/get-config-item", {
                config_key: e
            }, !0)
        }
        function mt(e) {
            return o.a.post("/bonus/bonus/get-bonus-valid-amount", e, !0)
        }
        function ht(e, t, n) {
            return o.a.get("/bonus/bonus/get-my-bonus", {
                token: e,
                page: t,
                limit: n
            }, !0)
        }
        function bt(e, t) {
            return o.a.get("/bonus/bonus/get-bonus-detail", {
                id: e,
                token: t
            }, !0)
        }
        function gt(e, t) {
            return o.a.post("/bonus/bonus/get-order-give-bonus", {
                token: e,
                order_sn: t
            }, !0)
        }
        function vt(e) {
            return o.a.post("/home/mobile/agent-code", {
                token: e
            }, !0)
        }
        function xt(code) {
            return o.a.get("/user/subscribe/url-scheme", {
                code: code
            }, !0)
        }
        function yt(e) {
            return o.a.get("/brands/brand/select-hot", {
                hotkey: e
            }, !0)
        }
        function wt(e, t) {
            return o.a.get("/search/search/screen", e, !0)
        }
        function kt(e) {
            return o.a.get("/search/search/association", {
                keyword: e
            }, !0)
        }
        function _t(data) {
            return o.a.get("/search/search/association", data, !0)
        }
        function Ot(data) {
            return o.a.get("/info/index", data, !0)
        }
        function jt(data) {
            return o.a.post("/meijj/form", data, !0)
        }
        function Pt(data) {
            return o.a.post("/meijj/tocart", data, !1)
        }
        function zt(data, e) {
            return o.a.get("/hotel/get-info", data, e)
        }
        function St(data) {
            return o.a.post("/hotel/create-info", data, !0)
        }
        function Tt(data) {
            return o.a.get("/hotel/get-record", data, !1)
        }
        function Et() {
            return o.a.get("/index/tgoods", {}, !1)
        }
        function $t(data) {
            return o.a.post("/cart/cart/get-realpay-gift", data, !0)
        }
        function Ct() {
            return o.a.get("/brands/dr-jart/index", {}, !1)
        }
        function Rt(data) {
            return o.a.get("/brands/dr-jart/goods-list", data, !1)
        }
        function It(data) {
            return o.a.get("/brands/dr-jart/mx-goods", data, !1)
        }
        function At(e) {
            return o.a.get("/goods/partner/detail", {
                barcode: e
            }, !1)
        }
        function Ut(data) {
            return o.a.get("/special/special/get-package-info?package_id=".concat(data.id), !1)
        }
        function Dt(data) {
            return o.a.get("/cart/cart/del-shop-cart", data, !0)
        }
        function Nt() {
            return o.a.get("/brands/prada/index", {}, !1)
        }
        function Lt(e, title, t) {
            return o.a.get("/brands/prada/goods-list", {
                type: e,
                title: title,
                sort: t
            }, !1)
        }
        function Mt() {
            return o.a.get("/brands/ud/index", {}, !1)
        }
        function Bt(e, t) {
            return o.a.get("/brands/ud/goods-list", {
                type: e,
                sort: t
            }, !1)
        }
        function qt(e, title, t) {
            return o.a.get("/brands/atelier-cologne/goods-list", {
                type: e,
                title: title,
                sort: t
            }, !1)
        }
        function Ft(data) {
            return o.a.post("/common/check-area", data, !0)
        }
        function Ht(e) {
            return o.a.get("/order/invoice/invoice-center", {
                token: e
            }, !1)
        }
        function Vt(e, t) {
            return o.a.post("/order/invoice/open-invoice", {
                token: e,
                order_sn: t
            }, !1)
        }
        function Gt(e) {
            return o.a.post("/home/mobile/getcategoods", {}, e || !1)
        }
        function Jt(e) {
            return o.a.post("/sc/index", {
                hid: e
            }, !0)
        }
        function Xt(e) {
            return o.a.post("/sc/result", {
                token: e
            }, !0)
        }
        function Wt(e, t, n, r) {
            return o.a.post("/sc/excode", {
                token: e,
                hid: t,
                roomno: n,
                date: r
            }, !0)
        }
        function Yt(data) {
            return o.a.get("/goods/goods/collect", data, !0)
        }
        function Kt(data) {
            return o.a.get("/goods/goods/collection-list", data, !0)
        }
        function Zt(data) {
            return o.a.get("/goods/goods/similar-goods", data, !0)
        }
        function Qt(data) {
            return o.a.get("/goods/goods/arrival-notice", data, !0)
        }
        function en(e) {
            return o.a.post("citbrand/brand-data/get-special-data-laprairie", {
                firstKey: e
            }, !0)
        }
        function tn(data) {
            return o.a.get("/citbrand/brand-data/get-hennessy-story", data, !1)
        }
        function nn(data) {
            return o.a.post("/citbrand/brand-data/getallcodegoods", data, !1)
        }
        function on(data) {
            return o.a.post("/citbrand/brand-data/get-widget-data", data, !1)
        }
        function rn(data) {
            return o.a.post("/citbrand/brand-data/getallcodegoodsindexbycode", data, !1)
        }
        function an(code, e, t) {
            return o.a.post("/coupon/coupon/receive-one", {
                code: code,
                token: e,
                is_batch: t
            }, !1)
        }
        function ln(data) {
            return o.a.get("/cart/cart/addbyordersn", data, !1)
        }
        function cn(data) {
            return o.a.post("/citbrand/brand-data/getbrandallgoods", data, !1)
        }
        function dn(data) {
            return o.a.post("/user/info/member-grade-apply", data, !1)
        }
        function sn(data) {
            return o.a.post("/user/info/member-grade-submit", data, !1)
        }
        function un(data) {
            return o.a.post("/wx/scheme", data, !1)
        }
        function fn(data) {
            return o.a.post("wx/url-link", data, !1)
        }
        function pn(param) {
            return o.a.post("/user/info/change-nickname", param, !1)
        }
        function mn(param) {
            return o.a.post("/user/info/cancel", param, !1)
        }
        function hn(param) {
            return o.a.post("/tools/checkcode", param, !1)
        }
        function bn(param) {
            return o.a.get("/search/search/top-cate", param, !1)
        }
        function gn(param) {
            return o.a.post("/citbrand/brand-data/get-widget-data", param, !1)
        }
        function vn(param) {
            return o.a.get("/slider/index/get-code", param)
        }
        function xn(param) {
            return o.a.get("/slider/index/check", param)
        }
        function yn(param) {
            return o.a.get("/coupon/coupon/couponlink-zhubao", param)
        }
        function wn(param) {
            return o.a.get("/coupon/coupon/receive-zhubao-coupon", param)
        }
        function kn(param) {
            return o.a.get("/search/search/hot-search-goods", param)
        }
        function _n(param) {
            return o.a.get("/search/search/personal-recommand", param)
        }
        function On(param) {
            return o.a.get("/order/invoice/byte-invoice-center", param)
        }
        function jn(param) {
            return o.a.post("/order/invoice/open-byte-invoice", param)
        }
        function Pn(param) {
            return o.a.get("/order/invoice/byte-invoice-info", param)
        }
        function zn(param) {
            return o.a.post("/citbrand/brand-data/get-special-data-set", param)
        }
        function Sn(e) {
            return o.a.post("/citbrand/brand-data/indexnew", {
                key: e
            }, !0)
        }
        function Tn(param, e) {
            return o.a.post("/citbrand/brand-data/get-home-page-data", param, e)
        }
        function En(param, e) {
            return o.a.get("/search/search/get-cate-ad-goods", param, e)
        }
        function $n(param) {
            return o.a.get("/promotion/index/flashsales-list", param)
        }
        function Cn(param) {
            return o.a.get("/promotion/index/flash-sale", param)
        }
        function Rn(param) {
            return o.a.get("/goods/goods/flashsale-notice", param)
        }
        function In(param) {
            return o.a.get("/goods/goods/set-is-lowerprice", param)
        }
        function An(param) {
            return o.a.post("/user/info/ct-exchange-points-info", param)
        }
        function Un(param) {
            return o.a.post("/user/info/ct-exchange-points", param)
        }
        function Dn(param) {
            return o.a.post("/order/order/check-breakable-goods", param, !0)
        }
        function Nn(param) {
            return o.a.post("/order/order/in-yellow-list", param, !0)
        }
        function Ln(data) {
            return o.a.get("/order/order/points-trace", data, !1)
        }
        function Mn(param) {
            return o.a.get("/page/page-config/index", param)
        }
        function Bn(param) {
            return o.a.get("/page/page-config/get-page-com-goods", param)
        }
        function qn(param) {
            return o.a.post("/coupon/coupon/cancel-coupon", param, !0)
        }
    },
    358: function(e, t, n) {
        "use strict";
        n.r(t);
        n(21);
        var o = n(4)
          , r = n(1);
        function l(e) {
            return r.a.post("/user/index/agent-check", {
                token: e
            }, !0)
        }
        var c = ["/commission", "/commission/bonusCenter", "/commission/bonusDetails", "/commission/cash", "/commission/college", "/commission/experience", "/commission/fansDetails", "/commission/hot", "/commission/ordersDetails", "/commission/overall", "/commission/hot", "/commission/highpayment"];
        t.default = function(e) {
            return d.apply(this, arguments)
        }
        ;
        function d() {
            return (d = Object(o.a)(regeneratorRuntime.mark((function e(t) {
                var n, o, r, d;
                return regeneratorRuntime.wrap((function(e) {
                    for (; ; )
                        switch (e.prev = e.next) {
                        case 0:
                            if (n = t.store,
                            o = t.route,
                            r = t.redirect,
                            t.req,
                            !(o.matched.length > 0 && c.indexOf(o.matched[0].path) > -1)) {
                                e.next = 8;
                                break
                            }
                            return e.next = 4,
                            l(n.state.User.UserToken);
                        case 4:
                            if (!(d = e.sent).data || 200 !== d.data.code) {
                                e.next = 8;
                                break
                            }
                            if (0 !== d.data.data.allow) {
                                e.next = 8;
                                break
                            }
                            return e.abrupt("return", r("/commission/register"));
                        case 8:
                        case "end":
                            return e.stop()
                        }
                }
                ), e)
            }
            )))).apply(this, arguments)
        }
    },
    41: function(e, t, n) {
        "use strict";
        n.d(t, "b", (function() {
            return Je
        }
        )),
        n.d(t, "a", (function() {
            return C
        }
        ));
        n(75),
        n(37),
        n(31),
        n(53),
        n(16),
        n(21);
        var o = n(4)
          , r = n(32)
          , l = (n(36),
        n(2))
          , c = n(49)
          , d = n(186)
          , f = n(133)
          , m = n.n(f)
          , h = n(71)
          , v = n.n(h)
          , x = n(134)
          , y = n(40)
          , w = n(0);
        "scrollRestoration"in window.history && (Object(w.u)("manual"),
        window.addEventListener("beforeunload", (function() {
            Object(w.u)("auto")
        }
        )),
        window.addEventListener("load", (function() {
            Object(w.u)("manual")
        }
        )));
        function k(object, e) {
            var t = Object.keys(object);
            if (Object.getOwnPropertySymbols) {
                var n = Object.getOwnPropertySymbols(object);
                e && (n = n.filter((function(e) {
                    return Object.getOwnPropertyDescriptor(object, e).enumerable
                }
                ))),
                t.push.apply(t, n)
            }
            return t
        }
        function _(e) {
            for (var i = 1; i < arguments.length; i++) {
                var source = null != arguments[i] ? arguments[i] : {};
                i % 2 ? k(Object(source), !0).forEach((function(t) {
                    Object(r.a)(e, t, source[t])
                }
                )) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(source)) : k(Object(source)).forEach((function(t) {
                    Object.defineProperty(e, t, Object.getOwnPropertyDescriptor(source, t))
                }
                ))
            }
            return e
        }
        var O = function() {};
        l.default.use(x.a);
        var j = {
            mode: "history",
            base: "/",
            linkActiveClass: "nuxt-link-active",
            linkExactActiveClass: "nuxt-link-exact-active",
            scrollBehavior: function(e, t, n) {
                var o = !1
                  , r = e !== t;
                n ? o = n : r && function(e) {
                    var t = Object(w.g)(e);
                    if (1 === t.length) {
                        var n = t[0].options;
                        return !1 !== (void 0 === n ? {} : n).scrollToTop
                    }
                    return t.some((function(e) {
                        var t = e.options;
                        return t && t.scrollToTop
                    }
                    ))
                }(e) && (o = {
                    x: 0,
                    y: 0
                });
                var l = window.$nuxt;
                return (!r || e.path === t.path && e.hash !== t.hash) && l.$nextTick((function() {
                    return l.$emit("triggerScroll")
                }
                )),
                new Promise((function(t) {
                    l.$once("triggerScroll", (function() {
                        if (e.hash) {
                            var n = e.hash;
                            void 0 !== window.CSS && void 0 !== window.CSS.escape && (n = "#" + window.CSS.escape(n.substr(1)));
                            try {
                                document.querySelector(n) && (o = {
                                    selector: n
                                })
                            } catch (e) {
                                console.warn("Failed to save scroll position. Please add CSS.escape() polyfill (https://github.com/mathiasbynens/CSS.escape).")
                            }
                        }
                        t(o)
                    }
                    ))
                }
                ))
            },
            routes: [{
                path: "/app",
                component: function() {
                    return Object(w.m)(n.e(75).then(n.bind(null, 2403)))
                },
                name: "app"
            }, {
                path: "/brand",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(497), n.e(40), n.e(77)]).then(n.bind(null, 2404)))
                },
                name: "brand"
            }, {
                path: "/cate",
                component: function() {
                    return Object(w.m)(n.e(303).then(n.bind(null, 2405)))
                },
                name: "cate"
            }, {
                path: "/confirm",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(11), n.e(500), n.e(10), n.e(29), n.e(305)]).then(n.bind(null, 2406)))
                },
                name: "confirm"
            }, {
                path: "/flashsale",
                component: function() {
                    return Object(w.m)(n.e(307).then(n.bind(null, 2407)))
                },
                name: "flashsale"
            }, {
                path: "/getcoupon",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(2), n.e(314)]).then(n.bind(null, 2408)))
                },
                name: "getcoupon"
            }, {
                path: "/help",
                component: function() {
                    return Object(w.m)(n.e(372).then(n.bind(null, 2409)))
                },
                name: "help"
            }, {
                path: "/list",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(32), n.e(501), n.e(0), n.e(54), n.e(384)]).then(n.bind(null, 2410)))
                },
                name: "list"
            }, {
                path: "/member",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(66), n.e(407)]).then(n.bind(null, 2411)))
                },
                name: "member"
            }, {
                path: "/novice",
                component: function() {
                    return Object(w.m)(n.e(411).then(n.bind(null, 2412)))
                },
                name: "novice"
            }, {
                path: "/officialAccount",
                component: function() {
                    return Object(w.m)(n.e(412).then(n.bind(null, 2413)))
                },
                name: "officialAccount"
            }, {
                path: "/search",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(32), n.e(452)]).then(n.bind(null, 2414)))
                },
                name: "search"
            }, {
                path: "/slidecode",
                component: function() {
                    return Object(w.m)(n.e(453).then(n.bind(null, 2415)))
                },
                name: "slidecode"
            }, {
                path: "/sp",
                component: function() {
                    return Object(w.m)(n.e(454).then(n.bind(null, 2416)))
                },
                name: "sp"
            }, {
                path: "/special",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(0), n.e(457)]).then(n.bind(null, 2417)))
                },
                name: "special"
            }, {
                path: "/user",
                component: function() {
                    return Object(w.m)(n.e(474).then(n.bind(null, 2418)))
                },
                name: "user"
            }, {
                path: "/wechatlogin",
                component: function() {
                    return Object(w.m)(n.e(494).then(n.bind(null, 2419)))
                },
                name: "wechatlogin"
            }, {
                path: "/activity/extension-poster",
                component: function() {
                    return Object(w.m)(n.e(69).then(n.bind(null, 2420)))
                },
                name: "activity-extension-poster"
            }, {
                path: "/app/jufenqiback",
                component: function() {
                    return Object(w.m)(n.e(76).then(n.bind(null, 2421)))
                },
                name: "app-jufenqiback"
            }, {
                path: "/brandhall/anessa",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(498), n.e(3), n.e(81)]).then(n.bind(null, 2422)))
                },
                name: "brandhall-anessa"
            }, {
                path: "/brandhall/apple",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(32), n.e(85)]).then(n.bind(null, 2423)))
                },
                name: "brandhall-apple"
            }, {
                path: "/brandhall/armani",
                component: function() {
                    return Object(w.m)(n.e(90).then(n.bind(null, 2424)))
                },
                name: "brandhall-armani"
            }, {
                path: "/brandhall/atelierCologne",
                component: function() {
                    return Object(w.m)(n.e(95).then(n.bind(null, 2425)))
                },
                name: "brandhall-atelierCologne"
            }, {
                path: "/brandhall/biotherm",
                component: function() {
                    return Object(w.m)(n.e(100).then(n.bind(null, 2426)))
                },
                name: "brandhall-biotherm"
            }, {
                path: "/brandhall/bobbiebrown",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(1), n.e(106)]).then(n.bind(null, 2427)))
                },
                name: "brandhall-bobbiebrown"
            }, {
                path: "/brandhall/burberry",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(15), n.e(118)]).then(n.bind(null, 2428)))
                },
                name: "brandhall-burberry"
            }, {
                path: "/brandhall/clinique",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(16), n.e(125)]).then(n.bind(null, 2429)))
                },
                name: "brandhall-clinique"
            }, {
                path: "/brandhall/darphin",
                component: function() {
                    return Object(w.m)(n.e(127).then(n.bind(null, 2430)))
                },
                name: "brandhall-darphin"
            }, {
                path: "/brandhall/dedepeau",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(17), n.e(128)]).then(n.bind(null, 2431)))
                },
                name: "brandhall-dedepeau"
            }, {
                path: "/brandhall/dj",
                component: function() {
                    return Object(w.m)(n.e(135).then(n.bind(null, 2432)))
                },
                name: "brandhall-dj"
            }, {
                path: "/brandhall/esteelauder",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(14), n.e(5), n.e(44), n.e(141)]).then(n.bind(null, 2433)))
                },
                name: "brandhall-esteelauder"
            }, {
                path: "/brandhall/fredericmalle",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(18), n.e(148)]).then(n.bind(null, 2434)))
                },
                name: "brandhall-fredericmalle"
            }, {
                path: "/brandhall/gucci",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(19), n.e(153)]).then(n.bind(null, 2435)))
                },
                name: "brandhall-gucci"
            }, {
                path: "/brandhall/helena",
                component: function() {
                    return Object(w.m)(n.e(158).then(n.bind(null, 2436)))
                },
                name: "brandhall-helena"
            }, {
                path: "/brandhall/hennessy",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(6), n.e(166)]).then(n.bind(null, 2437)))
                },
                name: "brandhall-hennessy"
            }, {
                path: "/brandhall/jomalone",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(4), n.e(20), n.e(171)]).then(n.bind(null, 2438)))
                },
                name: "brandhall-jomalone"
            }, {
                path: "/brandhall/kerastase",
                component: function() {
                    return Object(w.m)(n.e(178).then(n.bind(null, 2439)))
                },
                name: "brandhall-kerastase"
            }, {
                path: "/brandhall/kiehl",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(14), n.e(21), n.e(180)]).then(n.bind(null, 2440)))
                },
                name: "brandhall-kiehl"
            }, {
                path: "/brandhall/kilian",
                component: function() {
                    return Object(w.m)(n.e(187).then(n.bind(null, 2441)))
                },
                name: "brandhall-kilian"
            }, {
                path: "/brandhall/labseries",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(22), n.e(191)]).then(n.bind(null, 2442)))
                },
                name: "brandhall-labseries"
            }, {
                path: "/brandhall/lamer",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(4), n.e(7), n.e(13), n.e(198)]).then(n.bind(null, 2443)))
                },
                name: "brandhall-lamer"
            }, {
                path: "/brandhall/lancome",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(25), n.e(46), n.e(206)]).then(n.bind(null, 2444)))
                },
                name: "brandhall-lancome"
            }, {
                path: "/brandhall/laprairie",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(47), n.e(208)]).then(n.bind(null, 2445)))
                },
                name: "brandhall-laprairie"
            }, {
                path: "/brandhall/larocheposay",
                component: function() {
                    return Object(w.m)(n.e(212).then(n.bind(null, 2446)))
                },
                name: "brandhall-larocheposay"
            }, {
                path: "/brandhall/loreal",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(14), n.e(24), n.e(217)]).then(n.bind(null, 2447)))
                },
                name: "brandhall-loreal"
            }, {
                path: "/brandhall/lorealActivity",
                component: function() {
                    return Object(w.m)(n.e(221).then(n.bind(null, 2448)))
                },
                name: "brandhall-lorealActivity"
            }, {
                path: "/brandhall/mac",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(14), n.e(26), n.e(226)]).then(n.bind(null, 2449)))
                },
                name: "brandhall-mac"
            }, {
                path: "/brandhall/margiela",
                component: function() {
                    return Object(w.m)(n.e(231).then(n.bind(null, 2450)))
                },
                name: "brandhall-margiela"
            }, {
                path: "/brandhall/nars",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(27), n.e(235)]).then(n.bind(null, 2451)))
                },
                name: "brandhall-nars"
            }, {
                path: "/brandhall/origins",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(14), n.e(8), n.e(244)]).then(n.bind(null, 2452)))
                },
                name: "brandhall-origins"
            }, {
                path: "/brandhall/prada",
                component: function() {
                    return Object(w.m)(n.e(248).then(n.bind(null, 2453)))
                },
                name: "brandhall-prada"
            }, {
                path: "/brandhall/shiseido",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(3), n.e(251)]).then(n.bind(null, 2454)))
                },
                name: "brandhall-shiseido"
            }, {
                path: "/brandhall/tomford",
                component: function() {
                    return Object(w.m)(n.e(259).then(n.bind(null, 2455)))
                },
                name: "brandhall-tomford"
            }, {
                path: "/brandhall/ud",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(50), n.e(264)]).then(n.bind(null, 2456)))
                },
                name: "brandhall-ud"
            }, {
                path: "/brandhall/uemura",
                component: function() {
                    return Object(w.m)(n.e(273).then(n.bind(null, 2457)))
                },
                name: "brandhall-uemura"
            }, {
                path: "/brandhall/valentino",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(28), n.e(284)]).then(n.bind(null, 2458)))
                },
                name: "brandhall-valentino"
            }, {
                path: "/brandhall/vichy",
                component: function() {
                    return Object(w.m)(n.e(288).then(n.bind(null, 2459)))
                },
                name: "brandhall-vichy"
            }, {
                path: "/brandhall/ysl",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(53), n.e(298)]).then(n.bind(null, 2460)))
                },
                name: "brandhall-ysl"
            }, {
                path: "/cart/cart",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(0), n.e(9), n.e(54), n.e(301)]).then(n.bind(null, 2390)))
                },
                name: "cart-cart"
            }, {
                path: "/cart/checkbox",
                component: function() {
                    return Object(w.m)(n.e(302).then(n.bind(null, 1418)))
                },
                name: "cart-checkbox"
            }, {
                path: "/getcoupon/about",
                component: function() {
                    return Object(w.m)(n.e(308).then(n.bind(null, 2461)))
                },
                name: "getcoupon-about"
            }, {
                path: "/getcoupon/channel",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(2), n.e(309)]).then(n.bind(null, 2462)))
                },
                name: "getcoupon-channel"
            }, {
                path: "/getcoupon/channel2",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(2), n.e(310)]).then(n.bind(null, 2463)))
                },
                name: "getcoupon-channel2"
            }, {
                path: "/getcoupon/hotel",
                component: function() {
                    return Object(w.m)(n.e(311).then(n.bind(null, 2464)))
                },
                name: "getcoupon-hotel"
            }, {
                path: "/getcoupon/index2",
                component: function() {
                    return Object(w.m)(n.e(315).then(n.bind(null, 2391)))
                },
                name: "getcoupon-index2"
            }, {
                path: "/getcoupon/off",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(2), n.e(316)]).then(n.bind(null, 2465)))
                },
                name: "getcoupon-off"
            }, {
                path: "/getcoupon/othercp",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(2), n.e(317)]).then(n.bind(null, 2466)))
                },
                name: "getcoupon-othercp"
            }, {
                path: "/getcoupon/rule",
                component: function() {
                    return Object(w.m)(n.e(318).then(n.bind(null, 2467)))
                },
                name: "getcoupon-rule"
            }, {
                path: "/goods/brand",
                component: function() {
                    return Object(w.m)(n.e(323).then(n.bind(null, 2387)))
                },
                name: "goods-brand"
            }, {
                path: "/goods/goods",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(1), n.e(7), n.e(8), n.e(5), n.e(346)]).then(n.bind(null, 2402)))
                },
                name: "goods-goods"
            }, {
                path: "/help/community",
                component: function() {
                    return Object(w.m)(n.e(363).then(n.bind(null, 2468)))
                },
                name: "help-community"
            }, {
                path: "/help/contact",
                component: function() {
                    return Object(w.m)(n.e(364).then(n.bind(null, 2469)))
                },
                name: "help-contact"
            }, {
                path: "/help/customer",
                component: function() {
                    return Object(w.m)(n.e(365).then(n.bind(null, 2470)))
                },
                name: "help-customer"
            }, {
                path: "/help/doc",
                component: function() {
                    return Object(w.m)(n.e(366).then(n.bind(null, 2471)))
                },
                name: "help-doc"
            }, {
                path: "/help/hhcw",
                component: function() {
                    return Object(w.m)(n.e(367).then(n.bind(null, 2472)))
                },
                name: "help-hhcw"
            }, {
                path: "/help/huawei",
                component: function() {
                    return Object(w.m)(n.e(368).then(n.bind(null, 2473)))
                },
                name: "help-huawei"
            }, {
                path: "/help/outlands",
                component: function() {
                    return Object(w.m)(n.e(373).then(n.bind(null, 2474)))
                },
                name: "help-outlands"
            }, {
                path: "/help/page",
                component: function() {
                    return Object(w.m)(n.e(374).then(n.bind(null, 2475)))
                },
                name: "help-page"
            }, {
                path: "/help/privacy",
                component: function() {
                    return Object(w.m)(n.e(375).then(n.bind(null, 2476)))
                },
                name: "help-privacy"
            }, {
                path: "/help/site",
                component: function() {
                    return Object(w.m)(n.e(377).then(n.bind(null, 2477)))
                },
                name: "help-site"
            }, {
                path: "/help/stop",
                component: function() {
                    return Object(w.m)(n.e(378).then(n.bind(null, 2478)))
                },
                name: "help-stop"
            }, {
                path: "/help/tools",
                component: function() {
                    return Object(w.m)(n.e(379).then(n.bind(null, 2479)))
                },
                name: "help-tools"
            }, {
                path: "/help/upgrade",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(65), n.e(380)]).then(n.bind(null, 2480)))
                },
                name: "help-upgrade"
            }, {
                path: "/marketing/packageDetails",
                component: function() {
                    return Object(w.m)(n.e(400).then(n.bind(null, 2481)))
                },
                name: "marketing-packageDetails"
            }, {
                path: "/marketing/specialcomplex",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(0), n.e(36), n.e(402)]).then(n.bind(null, 2482)))
                },
                name: "marketing-specialcomplex"
            }, {
                path: "/member/agreement",
                component: function() {
                    return Object(w.m)(n.e(404).then(n.bind(null, 1429)))
                },
                name: "member-agreement"
            }, {
                path: "/member/bind",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(2), n.e(405)]).then(n.bind(null, 2483)))
                },
                name: "member-bind"
            }, {
                path: "/member/detail",
                component: function() {
                    return Object(w.m)(n.e(406).then(n.bind(null, 2484)))
                },
                name: "member-detail"
            }, {
                path: "/member/level",
                component: function() {
                    return Object(w.m)(n.e(408).then(n.bind(null, 2485)))
                },
                name: "member-level"
            }, {
                path: "/member/points",
                component: function() {
                    return Object(w.m)(n.e(409).then(n.bind(null, 2486)))
                },
                name: "member-points"
            }, {
                path: "/order/back-pick",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(11), n.e(502), n.e(0), n.e(9), n.e(413)]).then(n.bind(null, 2487)))
                },
                name: "order-back-pick"
            }, {
                path: "/passport/findPw",
                component: function() {
                    return Object(w.m)(n.e(442).then(n.bind(null, 2488)))
                },
                name: "passport-findPw"
            }, {
                path: "/passport/login",
                component: function() {
                    return Object(w.m)(n.e(443).then(n.bind(null, 2392)))
                },
                name: "passport-login"
            }, {
                path: "/passport/register",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(504), n.e(444)]).then(n.bind(null, 2489)))
                },
                name: "passport-register"
            }, {
                path: "/passport/wifi",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(505), n.e(35), n.e(445)]).then(n.bind(null, 2490)))
                },
                name: "passport-wifi"
            }, {
                path: "/payResult/fail",
                component: function() {
                    return Object(w.m)(n.e(447).then(n.bind(null, 2491)))
                },
                name: "payResult-fail"
            }, {
                path: "/payResult/success",
                component: function() {
                    return Object(w.m)(n.e(449).then(n.bind(null, 2492)))
                },
                name: "payResult-success"
            }, {
                path: "/sp/sc",
                component: function() {
                    return Object(w.m)(n.e(455).then(n.bind(null, 2493)))
                },
                name: "sp-sc"
            }, {
                path: "/sp/sr",
                component: function() {
                    return Object(w.m)(n.e(456).then(n.bind(null, 2494)))
                },
                name: "sp-sr"
            }, {
                path: "/user/beSimilarGoods",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(0), n.e(461)]).then(n.bind(null, 2495)))
                },
                name: "user-beSimilarGoods"
            }, {
                path: "/user/cancel",
                component: function() {
                    return Object(w.m)(n.e(463).then(n.bind(null, 2496)))
                },
                name: "user-cancel"
            }, {
                path: "/user/consignor",
                component: function() {
                    return Object(w.m)(n.e(465).then(n.bind(null, 2497)))
                },
                name: "user-consignor"
            }, {
                path: "/user/coupon",
                component: function() {
                    return Object(w.m)(n.e(468).then(n.bind(null, 2498)))
                },
                name: "user-coupon"
            }, {
                path: "/user/discount",
                component: function() {
                    return Object(w.m)(n.e(469).then(n.bind(null, 2499)))
                },
                name: "user-discount"
            }, {
                path: "/user/info",
                component: function() {
                    return Object(w.m)(n.e(478).then(n.bind(null, 2500)))
                },
                name: "user-info"
            }, {
                path: "/user/myCollection",
                component: function() {
                    return Object(w.m)(n.e(480).then(n.bind(null, 2501)))
                },
                name: "user-myCollection"
            }, {
                path: "/user/pcode",
                component: function() {
                    return Object(w.m)(n.e(487).then(n.bind(null, 2502)))
                },
                name: "user-pcode"
            }, {
                path: "/user/supermall-integral",
                component: function() {
                    return Object(w.m)(n.e(493).then(n.bind(null, 2503)))
                },
                name: "user-supermall-integral"
            }, {
                path: "/activity/hotel/bus",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(2), n.e(64), n.e(70)]).then(n.bind(null, 2504)))
                },
                name: "activity-hotel-bus"
            }, {
                path: "/activity/hotel/gift",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(11), n.e(72)]).then(n.bind(null, 2505)))
                },
                name: "activity-hotel-gift"
            }, {
                path: "/activity/spring/coupon",
                component: function() {
                    return Object(w.m)(n.e(73).then(n.bind(null, 2506)))
                },
                name: "activity-spring-coupon"
            }, {
                path: "/activity/spring/promotion",
                component: function() {
                    return Object(w.m)(n.e(74).then(n.bind(null, 2507)))
                },
                name: "activity-spring-promotion"
            }, {
                path: "/brandhall/anessa/list",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(3), n.e(82)]).then(n.bind(null, 2508)))
                },
                name: "brandhall-anessa-list"
            }, {
                path: "/brandhall/anessa/story",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(499), n.e(3), n.e(83)]).then(n.bind(null, 2509)))
                },
                name: "brandhall-anessa-story"
            }, {
                path: "/brandhall/apple/GoodsItem",
                component: function() {
                    return Object(w.m)(n.e(84).then(n.bind(null, 1430)))
                },
                name: "brandhall-apple-GoodsItem"
            }, {
                path: "/brandhall/apple/more",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(32), n.e(86)]).then(n.bind(null, 2510)))
                },
                name: "brandhall-apple-more"
            }, {
                path: "/brandhall/argentum/land230207",
                component: function() {
                    return Object(w.m)(n.e(87).then(n.bind(null, 2511)))
                },
                name: "brandhall-argentum-land230207"
            }, {
                path: "/brandhall/armani/brandstory",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(41), n.e(89)]).then(n.bind(null, 2512)))
                },
                name: "brandhall-armani-brandstory"
            }, {
                path: "/brandhall/armani/GoodsItem",
                component: function() {
                    return Object(w.m)(n.e(88).then(n.bind(null, 1431)))
                },
                name: "brandhall-armani-GoodsItem"
            }, {
                path: "/brandhall/armani/list",
                component: function() {
                    return Object(w.m)(n.e(91).then(n.bind(null, 2513)))
                },
                name: "brandhall-armani-list"
            }, {
                path: "/brandhall/armani/store",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(41), n.e(92)]).then(n.bind(null, 2514)))
                },
                name: "brandhall-armani-store"
            }, {
                path: "/brandhall/atelierCologne/brand-story",
                component: function() {
                    return Object(w.m)(n.e(94).then(n.bind(null, 2515)))
                },
                name: "brandhall-atelierCologne-brand-story"
            }, {
                path: "/brandhall/atelierCologne/GoodsItem",
                component: function() {
                    return Object(w.m)(n.e(93).then(n.bind(null, 823)))
                },
                name: "brandhall-atelierCologne-GoodsItem"
            }, {
                path: "/brandhall/atelierCologne/list",
                component: function() {
                    return Object(w.m)(n.e(96).then(n.bind(null, 2516)))
                },
                name: "brandhall-atelierCologne-list"
            }, {
                path: "/brandhall/atelierCologne/special",
                component: function() {
                    return Object(w.m)(n.e(97).then(n.bind(null, 2517)))
                },
                name: "brandhall-atelierCologne-special"
            }, {
                path: "/brandhall/biotherm/GoodsItem",
                component: function() {
                    return Object(w.m)(n.e(98).then(n.bind(null, 1432)))
                },
                name: "brandhall-biotherm-GoodsItem"
            }, {
                path: "/brandhall/biotherm/list",
                component: function() {
                    return Object(w.m)(n.e(101).then(n.bind(null, 2518)))
                },
                name: "brandhall-biotherm-list"
            }, {
                path: "/brandhall/biotherm/promise",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(42), n.e(102)]).then(n.bind(null, 2519)))
                },
                name: "brandhall-biotherm-promise"
            }, {
                path: "/brandhall/biotherm/story",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(42), n.e(103)]).then(n.bind(null, 2520)))
                },
                name: "brandhall-biotherm-story"
            }, {
                path: "/brandhall/bobbiebrown/bestseller",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(1), n.e(43), n.e(104)]).then(n.bind(null, 2521)))
                },
                name: "brandhall-bobbiebrown-bestseller"
            }, {
                path: "/brandhall/bobbiebrown/brandstory",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(1), n.e(4), n.e(105)]).then(n.bind(null, 2522)))
                },
                name: "brandhall-bobbiebrown-brandstory"
            }, {
                path: "/brandhall/bobbiebrown/list",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(1), n.e(43), n.e(107)]).then(n.bind(null, 2523)))
                },
                name: "brandhall-bobbiebrown-list"
            }, {
                path: "/brandhall/bobbiebrown/mpp",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(1), n.e(108)]).then(n.bind(null, 2524)))
                },
                name: "brandhall-bobbiebrown-mpp"
            }, {
                path: "/brandhall/bobbiebrown/position",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(1), n.e(109)]).then(n.bind(null, 2525)))
                },
                name: "brandhall-bobbiebrown-position"
            }, {
                path: "/brandhall/bobbiebrown/txcgsh",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(1), n.e(110)]).then(n.bind(null, 2526)))
                },
                name: "brandhall-bobbiebrown-txcgsh"
            }, {
                path: "/brandhall/bobbiebrown/xtxfdsh",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(1), n.e(111)]).then(n.bind(null, 2527)))
                },
                name: "brandhall-bobbiebrown-xtxfdsh"
            }, {
                path: "/brandhall/bobbiebrown/zhinanchungao",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(1), n.e(112)]).then(n.bind(null, 2528)))
                },
                name: "brandhall-bobbiebrown-zhinanchungao"
            }, {
                path: "/brandhall/bobbiebrown/zhinanfendi",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(1), n.e(113)]).then(n.bind(null, 2529)))
                },
                name: "brandhall-bobbiebrown-zhinanfendi"
            }, {
                path: "/brandhall/bobbiebrown/zhinangaoguang",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(1), n.e(114)]).then(n.bind(null, 2530)))
                },
                name: "brandhall-bobbiebrown-zhinangaoguang"
            }, {
                path: "/brandhall/bobbiebrown/zhinanmeimao",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(1), n.e(115)]).then(n.bind(null, 2531)))
                },
                name: "brandhall-bobbiebrown-zhinanmeimao"
            }, {
                path: "/brandhall/burberry/brandStory",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(15), n.e(116)]).then(n.bind(null, 2532)))
                },
                name: "brandhall-burberry-brandStory"
            }, {
                path: "/brandhall/burberry/counterGuide",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(15), n.e(117)]).then(n.bind(null, 2533)))
                },
                name: "brandhall-burberry-counterGuide"
            }, {
                path: "/brandhall/burberry/list",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(15), n.e(119)]).then(n.bind(null, 2534)))
                },
                name: "brandhall-burberry-list"
            }, {
                path: "/brandhall/burberry/secondaryList",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(15), n.e(120)]).then(n.bind(null, 2535)))
                },
                name: "brandhall-burberry-secondaryList"
            }, {
                path: "/brandhall/clinique/bestSellerList",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(16), n.e(122)]).then(n.bind(null, 2536)))
                },
                name: "brandhall-clinique-bestSellerList"
            }, {
                path: "/brandhall/clinique/brandstory",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(16), n.e(123)]).then(n.bind(null, 2393)))
                },
                name: "brandhall-clinique-brandstory"
            }, {
                path: "/brandhall/clinique/counter-guide",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(16), n.e(124)]).then(n.bind(null, 2537)))
                },
                name: "brandhall-clinique-counter-guide"
            }, {
                path: "/brandhall/clinique/list",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(16), n.e(126)]).then(n.bind(null, 2394)))
                },
                name: "brandhall-clinique-list"
            }, {
                path: "/brandhall/dedepeau/list",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(17), n.e(129)]).then(n.bind(null, 2395)))
                },
                name: "brandhall-dedepeau-list"
            }, {
                path: "/brandhall/dedepeau/startlist",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(17), n.e(130)]).then(n.bind(null, 2538)))
                },
                name: "brandhall-dedepeau-startlist"
            }, {
                path: "/brandhall/dedepeau/store",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(17), n.e(131)]).then(n.bind(null, 2539)))
                },
                name: "brandhall-dedepeau-store"
            }, {
                path: "/brandhall/dedepeau/story",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(17), n.e(132)]).then(n.bind(null, 2540)))
                },
                name: "brandhall-dedepeau-story"
            }, {
                path: "/brandhall/dj/counter-guide",
                component: function() {
                    return Object(w.m)(n.e(134).then(n.bind(null, 2541)))
                },
                name: "brandhall-dj-counter-guide"
            }, {
                path: "/brandhall/dj/star-products",
                component: function() {
                    return Object(w.m)(n.e(136).then(n.bind(null, 2542)))
                },
                name: "brandhall-dj-star-products"
            }, {
                path: "/brandhall/esteelauder/bestlist",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(5), n.e(139)]).then(n.bind(null, 2543)))
                },
                name: "brandhall-esteelauder-bestlist"
            }, {
                path: "/brandhall/esteelauder/GoodsItem",
                component: function() {
                    return Object(w.m)(n.e(137).then(n.bind(null, 1433)))
                },
                name: "brandhall-esteelauder-GoodsItem"
            }, {
                path: "/brandhall/esteelauder/goodslist",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(5), n.e(140)]).then(n.bind(null, 2544)))
                },
                name: "brandhall-esteelauder-goodslist"
            }, {
                path: "/brandhall/esteelauder/intro",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(5), n.e(142)]).then(n.bind(null, 2545)))
                },
                name: "brandhall-esteelauder-intro"
            }, {
                path: "/brandhall/esteelauder/page",
                component: function() {
                    return Object(w.m)(n.e(143).then(n.bind(null, 2546)))
                },
                name: "brandhall-esteelauder-page"
            }, {
                path: "/brandhall/esteelauder/storelist",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(5), n.e(144)]).then(n.bind(null, 2547)))
                },
                name: "brandhall-esteelauder-storelist"
            }, {
                path: "/brandhall/esteelauder/typelist",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(5), n.e(145)]).then(n.bind(null, 2548)))
                },
                name: "brandhall-esteelauder-typelist"
            }, {
                path: "/brandhall/fredericmalle/bestSellerList",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(18), n.e(146)]).then(n.bind(null, 2549)))
                },
                name: "brandhall-fredericmalle-bestSellerList"
            }, {
                path: "/brandhall/fredericmalle/brandstory",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(18), n.e(147)]).then(n.bind(null, 2396)))
                },
                name: "brandhall-fredericmalle-brandstory"
            }, {
                path: "/brandhall/fredericmalle/list",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(18), n.e(149)]).then(n.bind(null, 2397)))
                },
                name: "brandhall-fredericmalle-list"
            }, {
                path: "/brandhall/fredericmalle/position",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(18), n.e(150)]).then(n.bind(null, 2550)))
                },
                name: "brandhall-fredericmalle-position"
            }, {
                path: "/brandhall/gucci/brandStory",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(19), n.e(151)]).then(n.bind(null, 2551)))
                },
                name: "brandhall-gucci-brandStory"
            }, {
                path: "/brandhall/gucci/counterGuide",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(19), n.e(152)]).then(n.bind(null, 2552)))
                },
                name: "brandhall-gucci-counterGuide"
            }, {
                path: "/brandhall/gucci/list",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(19), n.e(154)]).then(n.bind(null, 2553)))
                },
                name: "brandhall-gucci-list"
            }, {
                path: "/brandhall/gucci/secondaryList",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(19), n.e(155)]).then(n.bind(null, 2554)))
                },
                name: "brandhall-gucci-secondaryList"
            }, {
                path: "/brandhall/helena/counter",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(33), n.e(157)]).then(n.bind(null, 2555)))
                },
                name: "brandhall-helena-counter"
            }, {
                path: "/brandhall/helena/GoodsItem",
                component: function() {
                    return Object(w.m)(n.e(156).then(n.bind(null, 1434)))
                },
                name: "brandhall-helena-GoodsItem"
            }, {
                path: "/brandhall/helena/list",
                component: function() {
                    return Object(w.m)(n.e(159).then(n.bind(null, 2556)))
                },
                name: "brandhall-helena-list"
            }, {
                path: "/brandhall/helena/promise",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(33), n.e(160)]).then(n.bind(null, 2557)))
                },
                name: "brandhall-helena-promise"
            }, {
                path: "/brandhall/helena/story",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(33), n.e(161)]).then(n.bind(null, 2558)))
                },
                name: "brandhall-helena-story"
            }, {
                path: "/brandhall/hennessy/artOfGifting",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(6), n.e(162)]).then(n.bind(null, 2559)))
                },
                name: "brandhall-hennessy-artOfGifting"
            }, {
                path: "/brandhall/hennessy/brandStory",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(6), n.e(163)]).then(n.bind(null, 2560)))
                },
                name: "brandhall-hennessy-brandStory"
            }, {
                path: "/brandhall/hennessy/explorationJourney",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(6), n.e(164)]).then(n.bind(null, 2561)))
                },
                name: "brandhall-hennessy-explorationJourney"
            }, {
                path: "/brandhall/hennessy/foodPairin",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(6), n.e(165)]).then(n.bind(null, 2562)))
                },
                name: "brandhall-hennessy-foodPairin"
            }, {
                path: "/brandhall/hennessy/list",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(6), n.e(167)]).then(n.bind(null, 2563)))
                },
                name: "brandhall-hennessy-list"
            }, {
                path: "/brandhall/hennessy/special",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(6), n.e(168)]).then(n.bind(null, 2398)))
                },
                name: "brandhall-hennessy-special"
            }, {
                path: "/brandhall/hennessy/wineList",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(6), n.e(169)]).then(n.bind(null, 2564)))
                },
                name: "brandhall-hennessy-wineList"
            }, {
                path: "/brandhall/jomalone/counter",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(4), n.e(20), n.e(170)]).then(n.bind(null, 2565)))
                },
                name: "brandhall-jomalone-counter"
            }, {
                path: "/brandhall/jomalone/list",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(20), n.e(34), n.e(172)]).then(n.bind(null, 2566)))
                },
                name: "brandhall-jomalone-list"
            }, {
                path: "/brandhall/jomalone/mppmo",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(20), n.e(34), n.e(173)]).then(n.bind(null, 2567)))
                },
                name: "brandhall-jomalone-mppmo"
            }, {
                path: "/brandhall/jomalone/step",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(20), n.e(34), n.e(174)]).then(n.bind(null, 2568)))
                },
                name: "brandhall-jomalone-step"
            }, {
                path: "/brandhall/kerastase/all",
                component: function() {
                    return Object(w.m)(n.e(176).then(n.bind(null, 2569)))
                },
                name: "brandhall-kerastase-all"
            }, {
                path: "/brandhall/kerastase/counter",
                component: function() {
                    return Object(w.m)(n.e(177).then(n.bind(null, 2570)))
                },
                name: "brandhall-kerastase-counter"
            }, {
                path: "/brandhall/kerastase/GoodsItem",
                component: function() {
                    return Object(w.m)(n.e(175).then(n.bind(null, 824)))
                },
                name: "brandhall-kerastase-GoodsItem"
            }, {
                path: "/brandhall/kerastase/list",
                component: function() {
                    return Object(w.m)(n.e(179).then(n.bind(null, 2571)))
                },
                name: "brandhall-kerastase-list"
            }, {
                path: "/brandhall/kiehl/intro",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(21), n.e(181)]).then(n.bind(null, 2572)))
                },
                name: "brandhall-kiehl-intro"
            }, {
                path: "/brandhall/kiehl/list",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(21), n.e(182)]).then(n.bind(null, 2399)))
                },
                name: "brandhall-kiehl-list"
            }, {
                path: "/brandhall/kiehl/storelist",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(21), n.e(183)]).then(n.bind(null, 2573)))
                },
                name: "brandhall-kiehl-storelist"
            }, {
                path: "/brandhall/kiehl/story",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(21), n.e(184)]).then(n.bind(null, 2574)))
                },
                name: "brandhall-kiehl-story"
            }, {
                path: "/brandhall/kilian/brandstory",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(45), n.e(186)]).then(n.bind(null, 2575)))
                },
                name: "brandhall-kilian-brandstory"
            }, {
                path: "/brandhall/kilian/GoodsItem",
                component: function() {
                    return Object(w.m)(n.e(185).then(n.bind(null, 1435)))
                },
                name: "brandhall-kilian-GoodsItem"
            }, {
                path: "/brandhall/kilian/list",
                component: function() {
                    return Object(w.m)(n.e(188).then(n.bind(null, 2576)))
                },
                name: "brandhall-kilian-list"
            }, {
                path: "/brandhall/kilian/store",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(45), n.e(189)]).then(n.bind(null, 2577)))
                },
                name: "brandhall-kilian-store"
            }, {
                path: "/brandhall/labseries/bestseller",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(22), n.e(190)]).then(n.bind(null, 2578)))
                },
                name: "brandhall-labseries-bestseller"
            }, {
                path: "/brandhall/labseries/list",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(22), n.e(192)]).then(n.bind(null, 2400)))
                },
                name: "brandhall-labseries-list"
            }, {
                path: "/brandhall/labseries/position",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(22), n.e(193)]).then(n.bind(null, 2579)))
                },
                name: "brandhall-labseries-position"
            }, {
                path: "/brandhall/labseries/story",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(22), n.e(194)]).then(n.bind(null, 2580)))
                },
                name: "brandhall-labseries-story"
            }, {
                path: "/brandhall/lamer/all",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(4), n.e(7), n.e(13), n.e(195)]).then(n.bind(null, 2581)))
                },
                name: "brandhall-lamer-all"
            }, {
                path: "/brandhall/lamer/bestseller",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(4), n.e(7), n.e(13), n.e(196)]).then(n.bind(null, 2582)))
                },
                name: "brandhall-lamer-bestseller"
            }, {
                path: "/brandhall/lamer/brandstory",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(4), n.e(7), n.e(13), n.e(197)]).then(n.bind(null, 2583)))
                },
                name: "brandhall-lamer-brandstory"
            }, {
                path: "/brandhall/lamer/list",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(4), n.e(7), n.e(13), n.e(199)]).then(n.bind(null, 2584)))
                },
                name: "brandhall-lamer-list"
            }, {
                path: "/brandhall/lamer/topic",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(4), n.e(7), n.e(13), n.e(200)]).then(n.bind(null, 2585)))
                },
                name: "brandhall-lamer-topic"
            }, {
                path: "/brandhall/lancome/activity",
                component: function() {
                    return Object(w.m)(n.e(201).then(n.bind(null, 2586)))
                },
                name: "brandhall-lancome-activity"
            }, {
                path: "/brandhall/lancome/april",
                component: function() {
                    return Object(w.m)(n.e(203).then(n.bind(null, 2587)))
                },
                name: "brandhall-lancome-april"
            }, {
                path: "/brandhall/lancome/bestseller",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(25), n.e(204)]).then(n.bind(null, 2588)))
                },
                name: "brandhall-lancome-bestseller"
            }, {
                path: "/brandhall/lancome/guide",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(25), n.e(205)]).then(n.bind(null, 2589)))
                },
                name: "brandhall-lancome-guide"
            }, {
                path: "/brandhall/lancome/list",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(25), n.e(46), n.e(207)]).then(n.bind(null, 2590)))
                },
                name: "brandhall-lancome-list"
            }, {
                path: "/brandhall/laprairie/list",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(47), n.e(209)]).then(n.bind(null, 2591)))
                },
                name: "brandhall-laprairie-list"
            }, {
                path: "/brandhall/larocheposay/brandstory",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(23), n.e(211)]).then(n.bind(null, 2592)))
                },
                name: "brandhall-larocheposay-brandstory"
            }, {
                path: "/brandhall/larocheposay/GoodsItem",
                component: function() {
                    return Object(w.m)(n.e(210).then(n.bind(null, 1436)))
                },
                name: "brandhall-larocheposay-GoodsItem"
            }, {
                path: "/brandhall/larocheposay/list",
                component: function() {
                    return Object(w.m)(n.e(213).then(n.bind(null, 2593)))
                },
                name: "brandhall-larocheposay-list"
            }, {
                path: "/brandhall/larocheposay/store",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(23), n.e(214)]).then(n.bind(null, 2594)))
                },
                name: "brandhall-larocheposay-store"
            }, {
                path: "/brandhall/loreal/GoodsItem",
                component: function() {
                    return Object(w.m)(n.e(215).then(n.bind(null, 705)))
                },
                name: "brandhall-loreal-GoodsItem"
            }, {
                path: "/brandhall/loreal/goodslist",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(24), n.e(216)]).then(n.bind(null, 2595)))
                },
                name: "brandhall-loreal-goodslist"
            }, {
                path: "/brandhall/loreal/special",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(24), n.e(218)]).then(n.bind(null, 2596)))
                },
                name: "brandhall-loreal-special"
            }, {
                path: "/brandhall/loreal/special1",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(24), n.e(219)]).then(n.bind(null, 2597)))
                },
                name: "brandhall-loreal-special1"
            }, {
                path: "/brandhall/loreal/youthcode",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(24), n.e(220)]).then(n.bind(null, 2598)))
                },
                name: "brandhall-loreal-youthcode"
            }, {
                path: "/brandhall/lorealActivity/infoForm",
                component: function() {
                    return Object(w.m)(n.e(222).then(n.bind(null, 2599)))
                },
                name: "brandhall-lorealActivity-infoForm"
            }, {
                path: "/brandhall/lorealActivity/product",
                component: function() {
                    return Object(w.m)(n.e(223).then(n.bind(null, 2600)))
                },
                name: "brandhall-lorealActivity-product"
            }, {
                path: "/brandhall/mac/GoodsItem",
                component: function() {
                    return Object(w.m)(n.e(224).then(n.bind(null, 1437)))
                },
                name: "brandhall-mac-GoodsItem"
            }, {
                path: "/brandhall/mac/goodslist",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(26), n.e(225)]).then(n.bind(null, 2601)))
                },
                name: "brandhall-mac-goodslist"
            }, {
                path: "/brandhall/mac/store",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(23), n.e(26), n.e(227)]).then(n.bind(null, 2602)))
                },
                name: "brandhall-mac-store"
            }, {
                path: "/brandhall/mac/theme",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(14), n.e(26), n.e(228)]).then(n.bind(null, 2603)))
                },
                name: "brandhall-mac-theme"
            }, {
                path: "/brandhall/margiela/brandstory",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(48), n.e(230)]).then(n.bind(null, 2604)))
                },
                name: "brandhall-margiela-brandstory"
            }, {
                path: "/brandhall/margiela/GoodsItem",
                component: function() {
                    return Object(w.m)(n.e(229).then(n.bind(null, 1438)))
                },
                name: "brandhall-margiela-GoodsItem"
            }, {
                path: "/brandhall/margiela/list",
                component: function() {
                    return Object(w.m)(n.e(232).then(n.bind(null, 2605)))
                },
                name: "brandhall-margiela-list"
            }, {
                path: "/brandhall/margiela/store",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(48), n.e(233)]).then(n.bind(null, 2606)))
                },
                name: "brandhall-margiela-store"
            }, {
                path: "/brandhall/nars/GoodsItem",
                component: function() {
                    return Object(w.m)(n.e(234).then(n.bind(null, 1439)))
                },
                name: "brandhall-nars-GoodsItem"
            }, {
                path: "/brandhall/nars/list",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(27), n.e(236)]).then(n.bind(null, 2607)))
                },
                name: "brandhall-nars-list"
            }, {
                path: "/brandhall/nars/page",
                component: function() {
                    return Object(w.m)(n.e(237).then(n.bind(null, 2608)))
                },
                name: "brandhall-nars-page"
            }, {
                path: "/brandhall/nars/storyabout",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(27), n.e(238)]).then(n.bind(null, 2609)))
                },
                name: "brandhall-nars-storyabout"
            }, {
                path: "/brandhall/nars/storyfan",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(27), n.e(239)]).then(n.bind(null, 2610)))
                },
                name: "brandhall-nars-storyfan"
            }, {
                path: "/brandhall/origins/all",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(8), n.e(241)]).then(n.bind(null, 2611)))
                },
                name: "brandhall-origins-all"
            }, {
                path: "/brandhall/origins/bestlist",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(8), n.e(242)]).then(n.bind(null, 2612)))
                },
                name: "brandhall-origins-bestlist"
            }, {
                path: "/brandhall/origins/GoodsItem",
                component: function() {
                    return Object(w.m)(n.e(240).then(n.bind(null, 825)))
                },
                name: "brandhall-origins-GoodsItem"
            }, {
                path: "/brandhall/origins/goodslist",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(8), n.e(243)]).then(n.bind(null, 2613)))
                },
                name: "brandhall-origins-goodslist"
            }, {
                path: "/brandhall/origins/intro",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(8), n.e(245)]).then(n.bind(null, 2614)))
                },
                name: "brandhall-origins-intro"
            }, {
                path: "/brandhall/origins/story",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(8), n.e(246)]).then(n.bind(null, 2615)))
                },
                name: "brandhall-origins-story"
            }, {
                path: "/brandhall/prada/GoodsItem",
                component: function() {
                    return Object(w.m)(n.e(247).then(n.bind(null, 1440)))
                },
                name: "brandhall-prada-GoodsItem"
            }, {
                path: "/brandhall/prada/list",
                component: function() {
                    return Object(w.m)(n.e(249).then(n.bind(null, 2616)))
                },
                name: "brandhall-prada-list"
            }, {
                path: "/brandhall/shiseido/entry",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(3), n.e(250)]).then(n.bind(null, 2617)))
                },
                name: "brandhall-shiseido-entry"
            }, {
                path: "/brandhall/shiseido/list",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(3), n.e(49), n.e(252)]).then(n.bind(null, 2618)))
                },
                name: "brandhall-shiseido-list"
            }, {
                path: "/brandhall/shiseido/special",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(3), n.e(49), n.e(253)]).then(n.bind(null, 2619)))
                },
                name: "brandhall-shiseido-special"
            }, {
                path: "/brandhall/shiseido/start",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(3), n.e(254)]).then(n.bind(null, 2620)))
                },
                name: "brandhall-shiseido-start"
            }, {
                path: "/brandhall/shiseido/store",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(3), n.e(255)]).then(n.bind(null, 2621)))
                },
                name: "brandhall-shiseido-store"
            }, {
                path: "/brandhall/shiseido/story",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(3), n.e(256)]).then(n.bind(null, 2622)))
                },
                name: "brandhall-shiseido-story"
            }, {
                path: "/brandhall/tomford/brandstory",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(23), n.e(258)]).then(n.bind(null, 2623)))
                },
                name: "brandhall-tomford-brandstory"
            }, {
                path: "/brandhall/tomford/GoodsItem",
                component: function() {
                    return Object(w.m)(n.e(257).then(n.bind(null, 1441)))
                },
                name: "brandhall-tomford-GoodsItem"
            }, {
                path: "/brandhall/tomford/list",
                component: function() {
                    return Object(w.m)(n.e(260).then(n.bind(null, 2624)))
                },
                name: "brandhall-tomford-list"
            }, {
                path: "/brandhall/tomford/store",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(23), n.e(261)]).then(n.bind(null, 2625)))
                },
                name: "brandhall-tomford-store"
            }, {
                path: "/brandhall/ud/GoodsItem",
                component: function() {
                    return Object(w.m)(n.e(262).then(n.bind(null, 1442)))
                },
                name: "brandhall-ud-GoodsItem"
            }, {
                path: "/brandhall/ud/list",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(50), n.e(265)]).then(n.bind(null, 2626)))
                },
                name: "brandhall-ud-list"
            }, {
                path: "/brandhall/ud/page",
                component: function() {
                    return Object(w.m)(n.e(266).then(n.bind(null, 2627)))
                },
                name: "brandhall-ud-page"
            }, {
                path: "/brandhall/uemura/brandstory",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(51), n.e(272)]).then(n.bind(null, 2628)))
                },
                name: "brandhall-uemura-brandstory"
            }, {
                path: "/brandhall/uemura/GoodsItem",
                component: function() {
                    return Object(w.m)(n.e(267).then(n.bind(null, 1443)))
                },
                name: "brandhall-uemura-GoodsItem"
            }, {
                path: "/brandhall/uemura/list",
                component: function() {
                    return Object(w.m)(n.e(274).then(n.bind(null, 2629)))
                },
                name: "brandhall-uemura-list"
            }, {
                path: "/brandhall/uemura/page",
                component: function() {
                    return Object(w.m)(n.e(275).then(n.bind(null, 2630)))
                },
                name: "brandhall-uemura-page"
            }, {
                path: "/brandhall/uemura/spring",
                component: function() {
                    return Object(w.m)(n.e(276).then(n.bind(null, 2631)))
                },
                name: "brandhall-uemura-spring"
            }, {
                path: "/brandhall/uemura/store",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(51), n.e(277)]).then(n.bind(null, 2632)))
                },
                name: "brandhall-uemura-store"
            }, {
                path: "/brandhall/valentino/brandStory",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(28), n.e(282)]).then(n.bind(null, 2633)))
                },
                name: "brandhall-valentino-brandStory"
            }, {
                path: "/brandhall/valentino/guide",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(28), n.e(283)]).then(n.bind(null, 2634)))
                },
                name: "brandhall-valentino-guide"
            }, {
                path: "/brandhall/valentino/list",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(28), n.e(285)]).then(n.bind(null, 2635)))
                },
                name: "brandhall-valentino-list"
            }, {
                path: "/brandhall/vichy/brandstory",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(52), n.e(287)]).then(n.bind(null, 2636)))
                },
                name: "brandhall-vichy-brandstory"
            }, {
                path: "/brandhall/vichy/GoodsItem",
                component: function() {
                    return Object(w.m)(n.e(286).then(n.bind(null, 1444)))
                },
                name: "brandhall-vichy-GoodsItem"
            }, {
                path: "/brandhall/vichy/list",
                component: function() {
                    return Object(w.m)(n.e(289).then(n.bind(null, 2637)))
                },
                name: "brandhall-vichy-list"
            }, {
                path: "/brandhall/vichy/store",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(52), n.e(290)]).then(n.bind(null, 2638)))
                },
                name: "brandhall-vichy-store"
            }, {
                path: "/brandhall/ysl/GoodsItem",
                component: function() {
                    return Object(w.m)(n.e(291).then(n.bind(null, 1445)))
                },
                name: "brandhall-ysl-GoodsItem"
            }, {
                path: "/brandhall/ysl/list",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(53), n.e(299)]).then(n.bind(null, 2639)))
                },
                name: "brandhall-ysl-list"
            }, {
                path: "/brandhall/ysl/page",
                component: function() {
                    return Object(w.m)(n.e(300).then(n.bind(null, 2640)))
                },
                name: "brandhall-ysl-page"
            }, {
                path: "/confirm/goods/goods",
                component: function() {
                    return Object(w.m)(n.e(304).then(n.bind(null, 2641)))
                },
                name: "confirm-goods-goods"
            }, {
                path: "/confirm/verify-face/verify-face",
                component: function() {
                    return Object(w.m)(n.e(306).then(n.bind(null, 2734)))
                },
                name: "confirm-verify-face-verify-face"
            }, {
                path: "/getcoupon/hotel/rule",
                component: function() {
                    return Object(w.m)(n.e(312).then(n.bind(null, 2642)))
                },
                name: "getcoupon-hotel-rule"
            }, {
                path: "/getcoupon/hotel/test",
                component: function() {
                    return Object(w.m)(n.e(313).then(n.bind(null, 2643)))
                },
                name: "getcoupon-hotel-test"
            }, {
                path: "/goods/brand/armani",
                component: function() {
                    return Object(w.m)(n.e(319).then(n.bind(null, 1082)))
                },
                name: "goods-brand-armani"
            }, {
                path: "/goods/brand/bobbiebrown",
                component: function() {
                    return Object(w.m)(n.e(320).then(n.bind(null, 1074)))
                },
                name: "goods-brand-bobbiebrown"
            }, {
                path: "/goods/brand/clinique",
                component: function() {
                    return Object(w.m)(n.e(321).then(n.bind(null, 1075)))
                },
                name: "goods-brand-clinique"
            }, {
                path: "/goods/brand/esteelauder",
                component: function() {
                    return Object(w.m)(n.e(322).then(n.bind(null, 1072)))
                },
                name: "goods-brand-esteelauder"
            }, {
                path: "/goods/brand/jomalone",
                component: function() {
                    return Object(w.m)(n.e(324).then(n.bind(null, 1077)))
                },
                name: "goods-brand-jomalone"
            }, {
                path: "/goods/brand/kiehl",
                component: function() {
                    return Object(w.m)(n.e(325).then(n.bind(null, 1070)))
                },
                name: "goods-brand-kiehl"
            }, {
                path: "/goods/brand/lamer",
                component: function() {
                    return Object(w.m)(n.e(326).then(n.bind(null, 1071)))
                },
                name: "goods-brand-lamer"
            }, {
                path: "/goods/brand/larocheposay",
                component: function() {
                    return Object(w.m)(n.e(327).then(n.bind(null, 1079)))
                },
                name: "goods-brand-larocheposay"
            }, {
                path: "/goods/brand/loreal",
                component: function() {
                    return Object(w.m)(n.e(328).then(n.bind(null, 1073)))
                },
                name: "goods-brand-loreal"
            }, {
                path: "/goods/brand/margiela",
                component: function() {
                    return Object(w.m)(n.e(329).then(n.bind(null, 1080)))
                },
                name: "goods-brand-margiela"
            }, {
                path: "/goods/brand/nav-brand",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(1), n.e(7), n.e(8), n.e(5), n.e(330)]).then(n.bind(null, 1414)))
                },
                name: "goods-brand-nav-brand"
            }, {
                path: "/goods/brand/origins",
                component: function() {
                    return Object(w.m)(n.e(331).then(n.bind(null, 1083)))
                },
                name: "goods-brand-origins"
            }, {
                path: "/goods/brand/tomford",
                component: function() {
                    return Object(w.m)(n.e(332).then(n.bind(null, 1076)))
                },
                name: "goods-brand-tomford"
            }, {
                path: "/goods/brand/uemura",
                component: function() {
                    return Object(w.m)(n.e(333).then(n.bind(null, 1081)))
                },
                name: "goods-brand-uemura"
            }, {
                path: "/goods/brand/vichy",
                component: function() {
                    return Object(w.m)(n.e(334).then(n.bind(null, 1078)))
                },
                name: "goods-brand-vichy"
            }, {
                path: "/goods/com/detail",
                component: function() {
                    return Object(w.m)(n.e(335).then(n.bind(null, 1420)))
                },
                name: "goods-com-detail"
            }, {
                path: "/goods/com/flash",
                component: function() {
                    return Object(w.m)(n.e(336).then(n.bind(null, 1428)))
                },
                name: "goods-com-flash"
            }, {
                path: "/goods/com/g-brand",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(55), n.e(337)]).then(n.bind(null, 1421)))
                },
                name: "goods-com-g-brand"
            }, {
                path: "/goods/com/g-group",
                component: function() {
                    return Object(w.m)(n.e(338).then(n.bind(null, 1424)))
                },
                name: "goods-com-g-group"
            }, {
                path: "/goods/com/g-info",
                component: function() {
                    return Object(w.m)(n.e(339).then(n.bind(null, 821)))
                },
                name: "goods-com-g-info"
            }, {
                path: "/goods/com/g-pickup",
                component: function() {
                    return Object(w.m)(n.e(340).then(n.bind(null, 1422)))
                },
                name: "goods-com-g-pickup"
            }, {
                path: "/goods/com/g-promotion",
                component: function() {
                    return Object(w.m)(n.e(341).then(n.bind(null, 1425)))
                },
                name: "goods-com-g-promotion"
            }, {
                path: "/goods/com/g-swiper",
                component: function() {
                    return Object(w.m)(n.e(342).then(n.bind(null, 1419)))
                },
                name: "goods-com-g-swiper"
            }, {
                path: "/goods/com/g-tip",
                component: function() {
                    return Object(w.m)(n.e(343).then(n.bind(null, 1423)))
                },
                name: "goods-com-g-tip"
            }, {
                path: "/goods/com/spu-box",
                component: function() {
                    return Object(w.m)(n.e(344).then(n.bind(null, 1426)))
                },
                name: "goods-com-spu-box"
            }, {
                path: "/goods/couponitem/couponitem",
                component: function() {
                    return Object(w.m)(n.e(345).then(n.bind(null, 1427)))
                },
                name: "goods-couponitem-couponitem"
            }, {
                path: "/help/aboutus/aboutcoupon",
                component: function() {
                    return Object(w.m)(n.e(347).then(n.bind(null, 2644)))
                },
                name: "help-aboutus-aboutcoupon"
            }, {
                path: "/help/aboutus/mallintro",
                component: function() {
                    return Object(w.m)(n.e(348).then(n.bind(null, 2645)))
                },
                name: "help-aboutus-mallintro"
            }, {
                path: "/help/aboutus/officenum",
                component: function() {
                    return Object(w.m)(n.e(349).then(n.bind(null, 2646)))
                },
                name: "help-aboutus-officenum"
            }, {
                path: "/help/aboutus/officenuma",
                component: function() {
                    return Object(w.m)(n.e(350).then(n.bind(null, 2647)))
                },
                name: "help-aboutus-officenuma"
            }, {
                path: "/help/aboutus/shopintro",
                component: function() {
                    return Object(w.m)(n.e(351).then(n.bind(null, 2648)))
                },
                name: "help-aboutus-shopintro"
            }, {
                path: "/help/aftersale/contact",
                component: function() {
                    return Object(w.m)(n.e(352).then(n.bind(null, 2649)))
                },
                name: "help-aftersale-contact"
            }, {
                path: "/help/aftersale/policy",
                component: function() {
                    return Object(w.m)(n.e(353).then(n.bind(null, 2650)))
                },
                name: "help-aftersale-policy"
            }, {
                path: "/help/aftersale/refund",
                component: function() {
                    return Object(w.m)(n.e(354).then(n.bind(null, 2651)))
                },
                name: "help-aftersale-refund"
            }, {
                path: "/help/agreement/limit",
                component: function() {
                    return Object(w.m)(n.e(355).then(n.bind(null, 2652)))
                },
                name: "help-agreement-limit"
            }, {
                path: "/help/agreement/member",
                component: function() {
                    return Object(w.m)(n.e(356).then(n.bind(null, 2653)))
                },
                name: "help-agreement-member"
            }, {
                path: "/help/agreement/packagepoint",
                component: function() {
                    return Object(w.m)(n.e(357).then(n.bind(null, 2654)))
                },
                name: "help-agreement-packagepoint"
            }, {
                path: "/help/agreement/pay",
                component: function() {
                    return Object(w.m)(n.e(358).then(n.bind(null, 2655)))
                },
                name: "help-agreement-pay"
            }, {
                path: "/help/agreement/payway",
                component: function() {
                    return Object(w.m)(n.e(359).then(n.bind(null, 2656)))
                },
                name: "help-agreement-payway"
            }, {
                path: "/help/agreement/process",
                component: function() {
                    return Object(w.m)(n.e(360).then(n.bind(null, 2657)))
                },
                name: "help-agreement-process"
            }, {
                path: "/help/agreement/shoptime",
                component: function() {
                    return Object(w.m)(n.e(361).then(n.bind(null, 2658)))
                },
                name: "help-agreement-shoptime"
            }, {
                path: "/help/agreement/user",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(35), n.e(362)]).then(n.bind(null, 2659)))
                },
                name: "help-agreement-user"
            }, {
                path: "/help/huawei/policy",
                component: function() {
                    return Object(w.m)(n.e(369).then(n.bind(null, 2660)))
                },
                name: "help-huawei-policy"
            }, {
                path: "/help/huawei/privacy",
                component: function() {
                    return Object(w.m)(n.e(370).then(n.bind(null, 2661)))
                },
                name: "help-huawei-privacy"
            }, {
                path: "/help/huawei/user",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(35), n.e(371)]).then(n.bind(null, 2662)))
                },
                name: "help-huawei-user"
            }, {
                path: "/help/privacy/othermnapp",
                component: function() {
                    return Object(w.m)(n.e(376).then(n.bind(null, 2663)))
                },
                name: "help-privacy-othermnapp"
            }, {
                path: "/list/brand_info/brand-info",
                component: function() {
                    return Object(w.m)(n.e(382).then(n.bind(null, 1416)))
                },
                name: "list-brand_info-brand-info"
            }, {
                path: "/list/brand_relation/brand-relation",
                component: function() {
                    return Object(w.m)(n.e(383).then(n.bind(null, 1417)))
                },
                name: "list-brand_relation-brand-relation"
            }, {
                path: "/list/tabs/tabs",
                component: function() {
                    return Object(w.m)(n.e(385).then(n.bind(null, 1415)))
                },
                name: "list-tabs-tabs"
            }, {
                path: "/marketing/active/flash",
                component: function() {
                    return Object(w.m)(n.e(388).then(n.bind(null, 2664)))
                },
                name: "marketing-active-flash"
            }, {
                path: "/marketing/active/group",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(0), n.e(36), n.e(389)]).then(n.bind(null, 2389)))
                },
                name: "marketing-active-group"
            }, {
                path: "/marketing/active/page",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(0), n.e(57), n.e(56), n.e(390)]).then(n.bind(null, 2665)))
                },
                name: "marketing-active-page"
            }, {
                path: "/marketing/newspecial/newspecial",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(30), n.e(37), n.e(58), n.e(399)]).then(n.bind(null, 2666)))
                },
                name: "marketing-newspecial-newspecial"
            }, {
                path: "/marketing/promotion/promotion",
                component: function() {
                    return Object(w.m)(n.e(401).then(n.bind(null, 2667)))
                },
                name: "marketing-promotion-promotion"
            }, {
                path: "/marketing/suit/all",
                component: function() {
                    return Object(w.m)(n.e(403).then(n.bind(null, 2668)))
                },
                name: "marketing-suit-all"
            }, {
                path: "/order/express-detail/express-detail",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(12), n.e(0), n.e(9), n.e(414)]).then(n.bind(null, 2669)))
                },
                name: "order-express-detail-express-detail"
            }, {
                path: "/order/order-face/order-face",
                component: function() {
                    return Object(w.m)(n.e(415).then(n.bind(null, 2670)))
                },
                name: "order-order-face-order-face"
            }, {
                path: "/order/order-off-detail/order-off-detail",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(12), n.e(0), n.e(9), n.e(10), n.e(416)]).then(n.bind(null, 2671)))
                },
                name: "order-order-off-detail-order-off-detail"
            }, {
                path: "/order/order-off-list/order-item",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(12), n.e(10), n.e(417)]).then(n.bind(null, 1454)))
                },
                name: "order-order-off-list-order-item"
            }, {
                path: "/order/order-off-list/order-off-list",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(12), n.e(0), n.e(9), n.e(10), n.e(418)]).then(n.bind(null, 2672)))
                },
                name: "order-order-off-list-order-off-list"
            }, {
                path: "/order/order-off-list/tabs",
                component: function() {
                    return Object(w.m)(n.e(419).then(n.bind(null, 1455)))
                },
                name: "order-order-off-list-tabs"
            }, {
                path: "/order/order-on-detail/order-on-detail",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(0), n.e(9), n.e(10), n.e(29), n.e(420)]).then(n.bind(null, 2673)))
                },
                name: "order-order-on-detail-order-on-detail"
            }, {
                path: "/order/order-on-detail/suit",
                component: function() {
                    return Object(w.m)(n.e(421).then(n.bind(null, 2674)))
                },
                name: "order-order-on-detail-suit"
            }, {
                path: "/order/order-on-list/order-item",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(10), n.e(29), n.e(422)]).then(n.bind(null, 1456)))
                },
                name: "order-order-on-list-order-item"
            }, {
                path: "/order/order-on-list/order-on-list",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(0), n.e(9), n.e(10), n.e(29), n.e(423)]).then(n.bind(null, 2675)))
                },
                name: "order-order-on-list-order-on-list"
            }, {
                path: "/order/order-on-list/tabs",
                component: function() {
                    return Object(w.m)(n.e(424).then(n.bind(null, 1457)))
                },
                name: "order-order-on-list-tabs"
            }, {
                path: "/order/order-receipt-open/order-receipt-open",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(2), n.e(425)]).then(n.bind(null, 2676)))
                },
                name: "order-order-receipt-open-order-receipt-open"
            }, {
                path: "/order/order-receipt/order-receipt",
                component: function() {
                    return Object(w.m)(n.e(426).then(n.bind(null, 2677)))
                },
                name: "order-order-receipt-order-receipt"
            }, {
                path: "/order/order-receipt/preview",
                component: function() {
                    return Object(w.m)(n.e(427).then(n.bind(null, 2678)))
                },
                name: "order-order-receipt-preview"
            }, {
                path: "/order/order-reteat-list/order-item",
                component: function() {
                    return Object(w.m)(n.e(59).then(n.bind(null, 2383)))
                },
                name: "order-order-reteat-list-order-item"
            }, {
                path: "/order/order-reteat-list/order-reteat-list",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(59), n.e(428)]).then(n.bind(null, 2679)))
                },
                name: "order-order-reteat-list-order-reteat-list"
            }, {
                path: "/order/order-reteat-list/tabs",
                component: function() {
                    return Object(w.m)(n.e(429).then(n.bind(null, 1458)))
                },
                name: "order-order-reteat-list-tabs"
            }, {
                path: "/order/order-reteat-open/order-reteat-open",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(65), n.e(503), n.e(430)]).then(n.bind(null, 2680)))
                },
                name: "order-order-reteat-open-order-reteat-open"
            }, {
                path: "/order/order-reteat/order-reteat",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(2), n.e(431)]).then(n.bind(null, 2681)))
                },
                name: "order-order-reteat-order-reteat"
            }, {
                path: "/pages/mall/web",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(31), n.e(38), n.e(39), n.e(60), n.e(441)]).then(n.bind(null, 2682)))
                },
                name: "pages-mall-web"
            }, {
                path: "/payResult/success/pre",
                component: function() {
                    return Object(w.m)(n.e(450).then(n.bind(null, 2401)))
                },
                name: "payResult-success-pre"
            }, {
                path: "/rank/ranklist/ranklist",
                component: function() {
                    return Object(w.m)(n.e(451).then(n.bind(null, 2683)))
                },
                name: "rank-ranklist-ranklist"
            }, {
                path: "/user/address-add/address-add",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(2), n.e(64), n.e(61), n.e(459)]).then(n.bind(null, 2684)))
                },
                name: "user-address-add-address-add"
            }, {
                path: "/user/address-add/area",
                component: function() {
                    return Object(w.m)(n.e(61).then(n.bind(null, 2253)))
                },
                name: "user-address-add-area"
            }, {
                path: "/user/address-list/address-item",
                component: function() {
                    return Object(w.m)(n.e(62).then(n.bind(null, 2385)))
                },
                name: "user-address-list-address-item"
            }, {
                path: "/user/address-list/address-list",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(62), n.e(460)]).then(n.bind(null, 2685)))
                },
                name: "user-address-list-address-list"
            }, {
                path: "/user/cancel/agree",
                component: function() {
                    return Object(w.m)(n.e(462).then(n.bind(null, 2686)))
                },
                name: "user-cancel-agree"
            }, {
                path: "/user/cancel/result",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(2), n.e(464)]).then(n.bind(null, 2687)))
                },
                name: "user-cancel-result"
            }, {
                path: "/user/consignor/make",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(506), n.e(466)]).then(n.bind(null, 2688)))
                },
                name: "user-consignor-make"
            }, {
                path: "/user/coupon/detail",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(66), n.e(467)]).then(n.bind(null, 2689)))
                },
                name: "user-coupon-detail"
            }, {
                path: "/user/discount/ofcoupon",
                component: function() {
                    return Object(w.m)(n.e(470).then(n.bind(null, 2690)))
                },
                name: "user-discount-ofcoupon"
            }, {
                path: "/user/discount/other",
                component: function() {
                    return Object(w.m)(n.e(471).then(n.bind(null, 2691)))
                },
                name: "user-discount-other"
            }, {
                path: "/user/dy-invoice/detail",
                component: function() {
                    return Object(w.m)(n.e(472).then(n.bind(null, 2692)))
                },
                name: "user-dy-invoice-detail"
            }, {
                path: "/user/dy-invoice/list",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(11), n.e(507), n.e(473)]).then(n.bind(null, 2693)))
                },
                name: "user-dy-invoice-list"
            }, {
                path: "/user/info/changeName",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(2), n.e(475)]).then(n.bind(null, 2694)))
                },
                name: "user-info-changeName"
            }, {
                path: "/user/info/changePass",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(2), n.e(476)]).then(n.bind(null, 2695)))
                },
                name: "user-info-changePass"
            }, {
                path: "/user/info/changePhone",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(2), n.e(477)]).then(n.bind(null, 2696)))
                },
                name: "user-info-changePhone"
            }, {
                path: "/user/info/privacy",
                component: function() {
                    return Object(w.m)(n.e(479).then(n.bind(null, 2697)))
                },
                name: "user-info-privacy"
            }, {
                path: "/user/order-detail/order-detail",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(12), n.e(481)]).then(n.bind(null, 2698)))
                },
                name: "user-order-detail-order-detail"
            }, {
                path: "/user/order-list/order-item",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(12), n.e(63)]).then(n.bind(null, 2386)))
                },
                name: "user-order-list-order-item"
            }, {
                path: "/user/order-list/order-list",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(12), n.e(63), n.e(482)]).then(n.bind(null, 2699)))
                },
                name: "user-order-list-order-list"
            }, {
                path: "/user/order-list/tabs",
                component: function() {
                    return Object(w.m)(n.e(483).then(n.bind(null, 1465)))
                },
                name: "user-order-list-tabs"
            }, {
                path: "/user/outlands/change",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(11), n.e(508), n.e(484)]).then(n.bind(null, 2700)))
                },
                name: "user-outlands-change"
            }, {
                path: "/user/outlands/info",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(11), n.e(509), n.e(485)]).then(n.bind(null, 2701)))
                },
                name: "user-outlands-info"
            }, {
                path: "/user/outlands/success",
                component: function() {
                    return Object(w.m)(n.e(486).then(n.bind(null, 2702)))
                },
                name: "user-outlands-success"
            }, {
                path: "/user/receipt/receipt",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(11), n.e(510), n.e(488)]).then(n.bind(null, 2703)))
                },
                name: "user-receipt-receipt"
            }, {
                path: "/user/redbag/desc",
                component: function() {
                    return Object(w.m)(n.e(489).then(n.bind(null, 2704)))
                },
                name: "user-redbag-desc"
            }, {
                path: "/user/redbag/detail",
                component: function() {
                    return Object(w.m)(n.e(490).then(n.bind(null, 2705)))
                },
                name: "user-redbag-detail"
            }, {
                path: "/user/redbag/list",
                component: function() {
                    return Object(w.m)(n.e(491).then(n.bind(null, 2706)))
                },
                name: "user-redbag-list"
            }, {
                path: "/user/redbag/use-desc",
                component: function() {
                    return Object(w.m)(n.e(492).then(n.bind(null, 2707)))
                },
                name: "user-redbag-use-desc"
            }, {
                path: "/activity/hotel/bus/list",
                component: function() {
                    return Object(w.m)(n.e(71).then(n.bind(null, 2708)))
                },
                name: "activity-hotel-bus-list"
            }, {
                path: "/brandhall/anessa/com/GoodsItem",
                component: function() {
                    return Object(w.m)(n.e(78).then(n.bind(null, 822)))
                },
                name: "brandhall-anessa-com-GoodsItem"
            }, {
                path: "/brandhall/anessa/com/logo",
                component: function() {
                    return Object(w.m)(n.e(79).then(n.bind(null, 703)))
                },
                name: "brandhall-anessa-com-logo"
            }, {
                path: "/brandhall/anessa/com/scroll-top",
                component: function() {
                    return Object(w.m)(n.e(80).then(n.bind(null, 704)))
                },
                name: "brandhall-anessa-com-scroll-top"
            }, {
                path: "/brandhall/biotherm/activity/land220701",
                component: function() {
                    return Object(w.m)(n.e(99).then(n.bind(null, 2709)))
                },
                name: "brandhall-biotherm-activity-land220701"
            }, {
                path: "/brandhall/clinique/activity/land220815",
                component: function() {
                    return Object(w.m)(n.e(121).then(n.bind(null, 2710)))
                },
                name: "brandhall-clinique-activity-land220815"
            }, {
                path: "/brandhall/esteelauder/activity/land220803",
                component: function() {
                    return Object(w.m)(n.e(138).then(n.bind(null, 2711)))
                },
                name: "brandhall-esteelauder-activity-land220803"
            }, {
                path: "/brandhall/esteelauder/components/price",
                component: function() {
                    return Object(w.m)(n.e(44).then(n.bind(null, 2378)))
                },
                name: "brandhall-esteelauder-components-price"
            }, {
                path: "/brandhall/lancome/activity/landing",
                component: function() {
                    return Object(w.m)(n.e(202).then(n.bind(null, 2712)))
                },
                name: "brandhall-lancome-activity-landing"
            }, {
                path: "/brandhall/ud/activity/land220615",
                component: function() {
                    return Object(w.m)(n.e(263).then(n.bind(null, 2713)))
                },
                name: "brandhall-ud-activity-land220615"
            }, {
                path: "/brandhall/uemura/activity/land220615",
                component: function() {
                    return Object(w.m)(n.e(268).then(n.bind(null, 2714)))
                },
                name: "brandhall-uemura-activity-land220615"
            }, {
                path: "/brandhall/uemura/activity/land221121",
                component: function() {
                    return Object(w.m)(n.e(269).then(n.bind(null, 2715)))
                },
                name: "brandhall-uemura-activity-land221121"
            }, {
                path: "/brandhall/uemura/activity/land230207",
                component: function() {
                    return Object(w.m)(n.e(270).then(n.bind(null, 2716)))
                },
                name: "brandhall-uemura-activity-land230207"
            }, {
                path: "/brandhall/uemura/activity/land230309",
                component: function() {
                    return Object(w.m)(n.e(271).then(n.bind(null, 2717)))
                },
                name: "brandhall-uemura-activity-land230309"
            }, {
                path: "/brandhall/valentino/activity/land220615",
                component: function() {
                    return Object(w.m)(n.e(278).then(n.bind(null, 2718)))
                },
                name: "brandhall-valentino-activity-land220615"
            }, {
                path: "/brandhall/valentino/activity/land220728",
                component: function() {
                    return Object(w.m)(n.e(279).then(n.bind(null, 2719)))
                },
                name: "brandhall-valentino-activity-land220728"
            }, {
                path: "/brandhall/valentino/activity/land220812",
                component: function() {
                    return Object(w.m)(n.e(280).then(n.bind(null, 2720)))
                },
                name: "brandhall-valentino-activity-land220812"
            }, {
                path: "/brandhall/valentino/activity/land221215",
                component: function() {
                    return Object(w.m)(n.e(281).then(n.bind(null, 2721)))
                },
                name: "brandhall-valentino-activity-land221215"
            }, {
                path: "/brandhall/ysl/activity/land220615",
                component: function() {
                    return Object(w.m)(n.e(292).then(n.bind(null, 2722)))
                },
                name: "brandhall-ysl-activity-land220615"
            }, {
                path: "/brandhall/ysl/activity/land220725",
                component: function() {
                    return Object(w.m)(n.e(293).then(n.bind(null, 2723)))
                },
                name: "brandhall-ysl-activity-land220725"
            }, {
                path: "/brandhall/ysl/activity/land2207251",
                component: function() {
                    return Object(w.m)(n.e(294).then(n.bind(null, 2724)))
                },
                name: "brandhall-ysl-activity-land2207251"
            }, {
                path: "/brandhall/ysl/activity/land220811",
                component: function() {
                    return Object(w.m)(n.e(295).then(n.bind(null, 2725)))
                },
                name: "brandhall-ysl-activity-land220811"
            }, {
                path: "/brandhall/ysl/activity/land2208111",
                component: function() {
                    return Object(w.m)(n.e(296).then(n.bind(null, 2726)))
                },
                name: "brandhall-ysl-activity-land2208111"
            }, {
                path: "/brandhall/ysl/activity/land221213",
                component: function() {
                    return Object(w.m)(n.e(297).then(n.bind(null, 2727)))
                },
                name: "brandhall-ysl-activity-land221213"
            }, {
                path: "/marketing/active/components/GoodItemSimple",
                component: function() {
                    return Object(w.m)(n.e(56).then(n.bind(null, 2379)))
                },
                name: "marketing-active-components-GoodItemSimple"
            }, {
                path: "/marketing/active/components/goods-3-col",
                component: function() {
                    return Object(w.m)(n.e(57).then(n.bind(null, 2380)))
                },
                name: "marketing-active-components-goods-3-col"
            }, {
                path: "/marketing/active/components/homeNav",
                component: function() {
                    return Object(w.m)(n.e(386).then(n.bind(null, 1446)))
                },
                name: "marketing-active-components-homeNav"
            }, {
                path: "/marketing/active/components/tag-item",
                component: function() {
                    return Object(w.m)(n.e(387).then(n.bind(null, 1447)))
                },
                name: "marketing-active-components-tag-item"
            }, {
                path: "/marketing/newspecial/com/goods-1-col",
                component: function() {
                    return Object(w.m)(n.e(391).then(n.bind(null, 2728)))
                },
                name: "marketing-newspecial-com-goods-1-col"
            }, {
                path: "/marketing/newspecial/com/goods-2-col",
                component: function() {
                    return Object(w.m)(n.e(392).then(n.bind(null, 1449)))
                },
                name: "marketing-newspecial-com-goods-2-col"
            }, {
                path: "/marketing/newspecial/com/goods-3-col",
                component: function() {
                    return Object(w.m)(n.e(393).then(n.bind(null, 1450)))
                },
                name: "marketing-newspecial-com-goods-3-col"
            }, {
                path: "/marketing/newspecial/com/goods-com",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(30), n.e(37)]).then(n.bind(null, 953)))
                },
                name: "marketing-newspecial-com-goods-com"
            }, {
                path: "/marketing/newspecial/com/goods-scroll-2-col",
                component: function() {
                    return Object(w.m)(n.e(30).then(n.bind(null, 2382)))
                },
                name: "marketing-newspecial-com-goods-scroll-2-col"
            }, {
                path: "/marketing/newspecial/com/goods-scroll-3-col",
                component: function() {
                    return Object(w.m)(n.e(394).then(n.bind(null, 1451)))
                },
                name: "marketing-newspecial-com-goods-scroll-3-col"
            }, {
                path: "/marketing/newspecial/com/img-com",
                component: function() {
                    return Object(w.m)(n.e(395).then(n.bind(null, 1448)))
                },
                name: "marketing-newspecial-com-img-com"
            }, {
                path: "/marketing/newspecial/com/img-flex-com",
                component: function() {
                    return Object(w.m)(n.e(58).then(n.bind(null, 2381)))
                },
                name: "marketing-newspecial-com-img-flex-com"
            }, {
                path: "/marketing/newspecial/com/menu-com",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(30), n.e(37), n.e(396)]).then(n.bind(null, 1453)))
                },
                name: "marketing-newspecial-com-menu-com"
            }, {
                path: "/marketing/newspecial/com/tag-item",
                component: function() {
                    return Object(w.m)(n.e(397).then(n.bind(null, 623)))
                },
                name: "marketing-newspecial-com-tag-item"
            }, {
                path: "/marketing/newspecial/com/video-com",
                component: function() {
                    return Object(w.m)(n.e(398).then(n.bind(null, 1452)))
                },
                name: "marketing-newspecial-com-video-com"
            }, {
                path: "/pages/mall/com/ht-banner",
                component: function() {
                    return Object(w.m)(n.e(432).then(n.bind(null, 954)))
                },
                name: "pages-mall-com-ht-banner"
            }, {
                path: "/pages/mall/com/ht-banner-goods",
                component: function() {
                    return Object(w.m)(n.e(433).then(n.bind(null, 1461)))
                },
                name: "pages-mall-com-ht-banner-goods"
            }, {
                path: "/pages/mall/com/ht-font",
                component: function() {
                    return Object(w.m)(n.e(434).then(n.bind(null, 1462)))
                },
                name: "pages-mall-com-ht-font"
            }, {
                path: "/pages/mall/com/ht-goods",
                component: function() {
                    return Object(w.m)(n.e(38).then(n.bind(null, 1460)))
                },
                name: "pages-mall-com-ht-goods"
            }, {
                path: "/pages/mall/com/ht-img",
                component: function() {
                    return Object(w.m)(n.e(435).then(n.bind(null, 955)))
                },
                name: "pages-mall-com-ht-img"
            }, {
                path: "/pages/mall/com/ht-nav",
                component: function() {
                    return Object(w.m)(n.e(436).then(n.bind(null, 957)))
                },
                name: "pages-mall-com-ht-nav"
            }, {
                path: "/pages/mall/com/ht-scroll-goods",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(39), n.e(437)]).then(n.bind(null, 1459)))
                },
                name: "pages-mall-com-ht-scroll-goods"
            }, {
                path: "/pages/mall/com/ht-space",
                component: function() {
                    return Object(w.m)(n.e(438).then(n.bind(null, 956)))
                },
                name: "pages-mall-com-ht-space"
            }, {
                path: "/pages/mall/com/ht-tabs",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(31), n.e(38), n.e(39), n.e(60)]).then(n.bind(null, 2384)))
                },
                name: "pages-mall-com-ht-tabs"
            }, {
                path: "/pages/mall/com/ht-video",
                component: function() {
                    return Object(w.m)(n.e(439).then(n.bind(null, 1463)))
                },
                name: "pages-mall-com-ht-video"
            }, {
                path: "/pages/mall/com/ht-water-goods",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(31), n.e(440)]).then(n.bind(null, 958)))
                },
                name: "pages-mall-com-ht-water-goods"
            }, {
                path: "/pages/mall/com/ht-water-goods-item",
                component: function() {
                    return Object(w.m)(n.e(31).then(n.bind(null, 1464)))
                },
                name: "pages-mall-com-ht-water-goods-item"
            }, {
                path: "/brandhall/dj/:goodsList",
                component: function() {
                    return Object(w.m)(n.e(133).then(n.bind(null, 2729)))
                },
                name: "brandhall-dj-goodsList"
            }, {
                path: "/payResult/pre/:ordersn",
                component: function() {
                    return Object(w.m)(n.e(448).then(n.bind(null, 2730)))
                },
                name: "payResult-pre-ordersn"
            }, {
                path: "/newspecial/:code",
                component: function() {
                    return Object(w.m)(n.e(410).then(n.bind(null, 2731)))
                },
                name: "newspecial-code"
            }, {
                path: "/payResult/:ordersn",
                component: function() {
                    return Object(w.m)(n.e(446).then(n.bind(null, 2732)))
                },
                name: "payResult-ordersn"
            }, {
                path: "/specialcomplex/:code",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(0), n.e(36), n.e(458)]).then(n.bind(null, 2733)))
                },
                name: "specialcomplex-code"
            }, {
                path: "/",
                component: function() {
                    return Object(w.m)(Promise.all([n.e(0), n.e(40), n.e(55), n.e(381)]).then(n.bind(null, 2388)))
                },
                name: "index"
            }],
            fallback: !1
        };
        function P(e, t) {
            var base = t.app && t.app.basePath || j.base
              , n = new x.a(_(_({}, j), {}, {
                base: base
            }))
              , o = n.push;
            n.push = function(e) {
                var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : O
                  , n = arguments.length > 2 ? arguments[2] : void 0;
                return o.call(this, e, t, n)
            }
            ;
            var r = n.resolve.bind(n);
            return n.resolve = function(e, t, n) {
                return "string" == typeof e && (e = Object(y.c)(e)),
                r(e, t, n)
            }
            ,
            n
        }
        var z = {
            name: "NuxtChild",
            functional: !0,
            props: {
                nuxtChildKey: {
                    type: String,
                    default: ""
                },
                keepAlive: Boolean,
                keepAliveProps: {
                    type: Object,
                    default: void 0
                }
            },
            render: function(e, t) {
                var n = t.parent
                  , data = t.data
                  , o = t.props
                  , r = n.$createElement;
                data.nuxtChild = !0;
                for (var l = n, c = n.$nuxt.nuxt.transitions, d = n.$nuxt.nuxt.defaultTransition, f = 0; n; )
                    n.$vnode && n.$vnode.data.nuxtChild && f++,
                    n = n.$parent;
                data.nuxtChildDepth = f;
                var m = c[f] || d
                  , h = {};
                S.forEach((function(e) {
                    void 0 !== m[e] && (h[e] = m[e])
                }
                ));
                var v = {};
                T.forEach((function(e) {
                    "function" == typeof m[e] && (v[e] = m[e].bind(l))
                }
                ));
                var x = v.beforeEnter;
                if (v.beforeEnter = function(e) {
                    if (window.$nuxt.$nextTick((function() {
                        window.$nuxt.$emit("triggerScroll")
                    }
                    )),
                    x)
                        return x.call(l, e)
                }
                ,
                !1 === m.css) {
                    var y = v.leave;
                    (!y || y.length < 2) && (v.leave = function(e, t) {
                        y && y.call(l, e),
                        l.$nextTick(t)
                    }
                    )
                }
                var w = r("routerView", data);
                return o.keepAlive && (w = r("keep-alive", {
                    props: o.keepAliveProps
                }, [w])),
                r("transition", {
                    props: h,
                    on: v
                }, [w])
            }
        }
          , S = ["name", "mode", "appear", "css", "type", "duration", "enterClass", "leaveClass", "appearClass", "enterActiveClass", "enterActiveClass", "leaveActiveClass", "appearActiveClass", "enterToClass", "leaveToClass", "appearToClass"]
          , T = ["beforeEnter", "enter", "afterEnter", "enterCancelled", "beforeLeave", "leave", "afterLeave", "leaveCancelled", "beforeAppear", "appear", "afterAppear", "appearCancelled"]
          , E = {
            name: "error",
            props: ["error"],
            head: function() {
                return {
                    title: this.error.statusCode || "系统错误"
                }
            },
            mounted: function() {
                console.error(this.error)
            }
        }
          , $ = (n(275),
        n(57))
          , C = Object($.a)(E, (function() {
            var e = this
              , t = e.$createElement
              , n = e._self._c || t;
            return n("div", {
                directives: [{
                    name: "page",
                    rawName: "v-page"
                }],
                staticClass: "page error-page"
            }, [e._m(0), e._v(" "), n("div", {
                staticClass: "error-con clear-fix"
            }, [n("div", {
                staticClass: "error-wrapper-message"
            }, [404 === e.error.statusCode ? n("h2", {
                staticClass: "error-message"
            }, [e._v("404 页面找不着了")]) : 500 === e.error.statusCode ? n("h2", {
                staticClass: "error-message"
            }, [e._v("500 服务器错误" + e._s(e.error.message || ""))]) : n("h3", {
                staticClass: "error-message"
            }, [e._v(e._s(e.error.statusCode) + " " + e._s(e.error.message))])])]), e._v(" "), n("div", {
                staticClass: "todo"
            }, [n("p", {
                staticClass: "desc"
            }, [e._v("您可以选择前往：")]), e._v(" "), n("div", {
                staticClass: "links"
            }, [n("nuxt-link", {
                staticClass: "error-link",
                attrs: {
                    to: "/"
                }
            }, [e._v("首页")]), e._v(" "), n("nuxt-link", {
                staticClass: "error-link",
                attrs: {
                    to: "/cate"
                }
            }, [e._v("分类")]), e._v(" "), n("nuxt-link", {
                staticClass: "error-link",
                attrs: {
                    to: "/cart/cart"
                }
            }, [e._v("购物车")]), e._v(" "), n("nuxt-link", {
                staticClass: "error-link",
                attrs: {
                    to: "/user"
                }
            }, [e._v("个人中心")])], 1), e._v(" "), n("p", {
                staticClass: "desc desc2"
            }, [e._v("或者")]), e._v(" "), n("div", {
                staticClass: "links"
            }, [n("a", {
                staticClass: "error-link",
                on: {
                    click: function(t) {
                        return e.$router.go(-1)
                    }
                }
            }, [e._v("返回上一页")])])])])
        }
        ), [function() {
            var e = this.$createElement
              , t = this._self._c || e;
            return t("div", {
                staticClass: "error-head"
            }, [t("em", {
                staticClass: "df-icon df-icon-logo headimg"
            })])
        }
        ], !1, null, "4415c7f8", null).exports
          , R = (n(38),
        n(39),
        n(52),
        n(25))
          , I = {
            name: "Nuxt",
            components: {
                NuxtChild: z,
                NuxtError: C
            },
            props: {
                nuxtChildKey: {
                    type: String,
                    default: void 0
                },
                keepAlive: Boolean,
                keepAliveProps: {
                    type: Object,
                    default: void 0
                },
                name: {
                    type: String,
                    default: "default"
                }
            },
            errorCaptured: function(e) {
                this.displayingNuxtError && (this.errorFromNuxtError = e,
                this.$forceUpdate())
            },
            computed: {
                routerViewKey: function() {
                    if (void 0 !== this.nuxtChildKey || this.$route.matched.length > 1)
                        return this.nuxtChildKey || Object(w.c)(this.$route.matched[0].path)(this.$route.params);
                    var e = Object(R.a)(this.$route.matched, 1)[0];
                    if (!e)
                        return this.$route.path;
                    var t = e.components.default;
                    if (t && t.options) {
                        var n = t.options;
                        if (n.key)
                            return "function" == typeof n.key ? n.key(this.$route) : n.key
                    }
                    return /\/$/.test(e.path) ? this.$route.path : this.$route.path.replace(/\/$/, "")
                }
            },
            beforeCreate: function() {
                l.default.util.defineReactive(this, "nuxt", this.$root.$options.nuxt)
            },
            render: function(e) {
                var t = this;
                return this.nuxt.err ? this.errorFromNuxtError ? (this.$nextTick((function() {
                    return t.errorFromNuxtError = !1
                }
                )),
                e("div", {}, [e("h2", "An error occurred while showing the error page"), e("p", "Unfortunately an error occurred and while showing the error page another error occurred"), e("p", "Error details: ".concat(this.errorFromNuxtError.toString())), e("nuxt-link", {
                    props: {
                        to: "/"
                    }
                }, "Go back to home")])) : (this.displayingNuxtError = !0,
                this.$nextTick((function() {
                    return t.displayingNuxtError = !1
                }
                )),
                e(C, {
                    props: {
                        error: this.nuxt.err
                    }
                })) : e("NuxtChild", {
                    key: this.routerViewKey,
                    props: this.$props
                })
            }
        }
          , A = (n(65),
        n(66),
        n(67),
        {
            name: "NuxtLoading",
            data: function() {
                return {
                    percent: 0,
                    show: !1,
                    canSucceed: !0,
                    reversed: !1,
                    skipTimerCount: 0,
                    rtl: !1,
                    throttle: 200,
                    duration: 5e3,
                    continuous: !1
                }
            },
            computed: {
                left: function() {
                    return !(!this.continuous && !this.rtl) && (this.rtl ? this.reversed ? "0px" : "auto" : this.reversed ? "auto" : "0px")
                }
            },
            beforeDestroy: function() {
                this.clear()
            },
            methods: {
                clear: function() {
                    clearInterval(this._timer),
                    clearTimeout(this._throttle),
                    this._timer = null
                },
                start: function() {
                    var e = this;
                    return this.clear(),
                    this.percent = 0,
                    this.reversed = !1,
                    this.skipTimerCount = 0,
                    this.canSucceed = !0,
                    this.throttle ? this._throttle = setTimeout((function() {
                        return e.startTimer()
                    }
                    ), this.throttle) : this.startTimer(),
                    this
                },
                set: function(e) {
                    return this.show = !0,
                    this.canSucceed = !0,
                    this.percent = Math.min(100, Math.max(0, Math.floor(e))),
                    this
                },
                get: function() {
                    return this.percent
                },
                increase: function(e) {
                    return this.percent = Math.min(100, Math.floor(this.percent + e)),
                    this
                },
                decrease: function(e) {
                    return this.percent = Math.max(0, Math.floor(this.percent - e)),
                    this
                },
                pause: function() {
                    return clearInterval(this._timer),
                    this
                },
                resume: function() {
                    return this.startTimer(),
                    this
                },
                finish: function() {
                    return this.percent = this.reversed ? 0 : 100,
                    this.hide(),
                    this
                },
                hide: function() {
                    var e = this;
                    return this.clear(),
                    setTimeout((function() {
                        e.show = !1,
                        e.$nextTick((function() {
                            e.percent = 0,
                            e.reversed = !1
                        }
                        ))
                    }
                    ), 500),
                    this
                },
                fail: function(e) {
                    return this.canSucceed = !1,
                    this
                },
                startTimer: function() {
                    var e = this;
                    this.show || (this.show = !0),
                    void 0 === this._cut && (this._cut = 1e4 / Math.floor(this.duration)),
                    this._timer = setInterval((function() {
                        e.skipTimerCount > 0 ? e.skipTimerCount-- : (e.reversed ? e.decrease(e._cut) : e.increase(e._cut),
                        e.continuous && (e.percent >= 100 || e.percent <= 0) && (e.skipTimerCount = 1,
                        e.reversed = !e.reversed))
                    }
                    ), 100)
                }
            },
            render: function(e) {
                var t = e(!1);
                return this.show && (t = e("div", {
                    staticClass: "nuxt-progress",
                    class: {
                        "nuxt-progress-notransition": this.skipTimerCount > 0,
                        "nuxt-progress-failed": !this.canSucceed
                    },
                    style: {
                        width: this.percent + "%",
                        left: this.left
                    }
                })),
                t
            }
        })
          , U = (n(277),
        Object($.a)(A, undefined, undefined, !1, null, null, null).exports)
          , D = (n(279),
        n(281),
        n(283),
        n(288),
        n(3))
          , N = n(135)
          , L = n(28)
          , M = n(12)
          , B = n(74)
          , F = 0
          , H = null
          , V = {
            beforeMount: function() {
                var e = this;
                if (null != D.a.fetchFromCookie("gid") && this.$store.commit("User/gidSet", D.a.fetchFromCookie("gid")),
                Object(B.c)()) {
                    var t = {
                        KJ_API: this.$store.state.env.KJ_API,
                        wechat: this.$store.state.env.wechat,
                        mpWechat: !0
                    };
                    this.$store.commit("updateEnv", t)
                }
                this.$route.query.hasOwnProperty("dftk") && (D.a.saveToCookie("UserToken", this.$route.query.dftk, 86400),
                this.$store.commit("User/updateUser", this.$route.query.dftk),
                this.$store.dispatch("User/updateUserInfo")),
                this.$store.state.env.mpWechat && !this.$route.query.dftk && (D.a.removeFromCookie("UserToken"),
                this.$store.commit("User/deleteUser")),
                "back" === document.getElementsByClassName("page-container")[0].getAttribute("transition-direction") && (this.$store.state.User.UserToken || this.$store.commit("User/updateUser", D.a.fetchFromCookie("UserToken"))),
                null !== this.$store.state.User.mid && D.a.saveToCookie("mid", this.$store.state.User.mid, 86400),
                null !== this.$store.state.User.sid && D.a.saveToCookie("sid", this.$store.state.User.sid, 86400),
                null !== this.$store.state.User.pid && D.a.saveToCookie("pid", this.$store.state.User.pid, 86400),
                null !== this.$store.state.User.plid && D.a.saveToCookie("plid", this.$store.state.User.plid, 86400),
                null !== this.$store.state.User.sflsource && D.a.saveToCookie("sflsource", this.$store.state.User.sflsource, 86400),
                window.__EVENT_BUS__.$on("globalMessage", (function(t) {
                    e.$toast({
                        message: t,
                        position: "middle",
                        duration: 2e3
                    })
                }
                )),
                window.__EVENT_BUS__.$on(M.d, (function(t) {
                    e.$store.commit("updatePage", t)
                }
                )),
                window.__EVENT_BUS__.$on(M.b, (function(e) {
                    !0 === e ? (F = F < 0 ? 0 : F,
                    1 === (F += 1) && (null != H && clearTimeout(H),
                    L.Indicator.open({
                        spinnerType: "triple-bounce"
                    }))) : 0 === (F -= 1) && (L.Indicator.close(),
                    H = setTimeout((function() {
                        H = null
                    }
                    ), 500))
                }
                )),
                window.__EVENT_BUS__.$on(M.e, function() {
                    var t = Object(o.a)(regeneratorRuntime.mark((function t(n) {
                        var o;
                        return regeneratorRuntime.wrap((function(t) {
                            for (; ; )
                                switch (t.prev = t.next) {
                                case 0:
                                    if (e.$store.commit("User/deleteUser"),
                                    D.a.removeFromCookie("UserToken"),
                                    !n) {
                                        t.next = 8;
                                        break
                                    }
                                    return t.next = 5,
                                    e.$dialog.alert({
                                        message: "登录已过期，请重新登录"
                                    });
                                case 5:
                                    t.sent,
                                    o = encodeURIComponent("//".concat(window.location.host).concat(e.$route.fullPath)),
                                    Object(N.d)(e, o);
                                case 8:
                                case "end":
                                    return t.stop()
                                }
                        }
                        ), t)
                    }
                    )));
                    return function(e) {
                        return t.apply(this, arguments)
                    }
                }()),
                window.__EVENT_BUS__.$on(M.c, function() {
                    var t = Object(o.a)(regeneratorRuntime.mark((function t(n) {
                        return regeneratorRuntime.wrap((function(t) {
                            for (; ; )
                                switch (t.prev = t.next) {
                                case 0:
                                    e.$router.push("/help/stop?message=".concat(n));
                                case 1:
                                case "end":
                                    return t.stop()
                                }
                        }
                        ), t)
                    }
                    )));
                    return function(e) {
                        return t.apply(this, arguments)
                    }
                }()),
                window.__EVENT_BUS__.$on(M.g, (function() {
                    e.$router.push("/slidecode")
                }
                )),
                this.$store.dispatch("User/updateUserInfo", !0)
            },
            methods: {
                goBack: function() {
                    this.$router.go(-1)
                }
            }
        }
          , G = (n(296),
        Object($.a)(V, (function() {
            var e = this
              , t = e.$createElement
              , n = e._self._c || t;
            return n("div", {
                staticClass: "page-container",
                attrs: {
                    "idea-app": ""
                }
            }, [e.$store.state.currentPage.nav ? n("van-nav-bar", {
                staticClass: "page-header",
                attrs: {
                    title: e.$store.state.currentPage.nav.title,
                    "left-arrow": ""
                },
                on: {
                    "click-left": function(t) {
                        return e.goBack()
                    }
                }
            }) : e._e(), e._v(" "), n("nuxt"), e._v(" "), e.$store.state.currentPage.tabBar ? n("van-tabbar", {
                staticClass: "page-bottom footer-tabs",
                attrs: {
                    route: "",
                    "safe-area-inset-bottom": !0
                }
            }, [n("van-tabbar-item", {
                attrs: {
                    to: "/"
                },
                scopedSlots: e._u([{
                    key: "icon",
                    fn: function(e) {
                        return [n("img", {
                            attrs: {
                                src: e.active ? "/images/ui/f1_active.png" : "/images/ui/f1.png"
                            }
                        })]
                    }
                }], null, !1, 3455028918)
            }, [e._v("\n      首页\n      ")]), e._v(" "), n("van-tabbar-item", {
                attrs: {
                    to: "/cate"
                },
                scopedSlots: e._u([{
                    key: "icon",
                    fn: function(e) {
                        return [n("img", {
                            attrs: {
                                src: e.active ? "/images/ui/f2_active.png" : "/images/ui/f2.png"
                            }
                        })]
                    }
                }], null, !1, 3004342934)
            }, [e._v("\n      分类\n      ")]), e._v(" "), n("van-tabbar-item", {
                attrs: {
                    to: "/brand"
                },
                scopedSlots: e._u([{
                    key: "icon",
                    fn: function(e) {
                        return [n("img", {
                            attrs: {
                                src: e.active ? "/images/ui/f31_active.png" : "/images/ui/f31.png"
                            }
                        })]
                    }
                }], null, !1, 3270799734)
            }, [e._v("\n      品牌\n      ")]), e._v(" "), n("van-tabbar-item", {
                attrs: {
                    to: "/cart/cart"
                },
                scopedSlots: e._u([{
                    key: "icon",
                    fn: function(e) {
                        return [n("img", {
                            attrs: {
                                src: e.active ? "/images/ui/f3_active.png" : "/images/ui/f3.png"
                            }
                        })]
                    }
                }], null, !1, 865144566)
            }, [e._v("\n      购物车\n      ")]), e._v(" "), n("van-tabbar-item", {
                attrs: {
                    to: "/user"
                },
                scopedSlots: e._u([{
                    key: "icon",
                    fn: function(e) {
                        return [n("img", {
                            attrs: {
                                src: e.active ? "/images/ui/f4_active.png" : "/images/ui/f4.png"
                            }
                        })]
                    }
                }], null, !1, 1588995286)
            }, [e._v("\n      我的\n      ")])], 1) : e._e(), e._v(" "), n("input", {
                attrs: {
                    id: "ipt_env_api",
                    type: "hidden"
                },
                domProps: {
                    value: this.$store.state.env.KJ_API
                }
            }), e._v(" "), n("input", {
                attrs: {
                    id: "ipt_env_mid",
                    type: "hidden"
                },
                domProps: {
                    value: this.$store.state.User.mid
                }
            }), e._v(" "), n("input", {
                attrs: {
                    id: "ipt_env_sid",
                    type: "hidden"
                },
                domProps: {
                    value: this.$store.state.User.sid
                }
            }), e._v(" "), n("input", {
                attrs: {
                    id: "ipt_env_pid",
                    type: "hidden"
                },
                domProps: {
                    value: this.$store.state.User.pid
                }
            }), e._v(" "), n("input", {
                attrs: {
                    id: "ipt_env_plid",
                    type: "hidden"
                },
                domProps: {
                    value: this.$store.state.User.plid
                }
            }), e._v(" "), n("input", {
                attrs: {
                    id: "sflsource",
                    type: "hidden"
                },
                domProps: {
                    value: this.$store.state.User.sflsource
                }
            })], 1)
        }
        ), [], !1, null, "6baf7f6e", null).exports);
        function J(e, t) {
            var n;
            if ("undefined" == typeof Symbol || null == e[Symbol.iterator]) {
                if (Array.isArray(e) || (n = function(e, t) {
                    if (!e)
                        return;
                    if ("string" == typeof e)
                        return X(e, t);
                    var n = Object.prototype.toString.call(e).slice(8, -1);
                    "Object" === n && e.constructor && (n = e.constructor.name);
                    if ("Map" === n || "Set" === n)
                        return Array.from(e);
                    if ("Arguments" === n || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n))
                        return X(e, t)
                }(e)) || t && e && "number" == typeof e.length) {
                    n && (e = n);
                    var i = 0
                      , o = function() {};
                    return {
                        s: o,
                        n: function() {
                            return i >= e.length ? {
                                done: !0
                            } : {
                                done: !1,
                                value: e[i++]
                            }
                        },
                        e: function(e) {
                            throw e
                        },
                        f: o
                    }
                }
                throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
            }
            var r, l = !0, c = !1;
            return {
                s: function() {
                    n = e[Symbol.iterator]()
                },
                n: function() {
                    var e = n.next();
                    return l = e.done,
                    e
                },
                e: function(e) {
                    c = !0,
                    r = e
                },
                f: function() {
                    try {
                        l || null == n.return || n.return()
                    } finally {
                        if (c)
                            throw r
                    }
                }
            }
        }
        function X(e, t) {
            (null == t || t > e.length) && (t = e.length);
            for (var i = 0, n = new Array(t); i < t; i++)
                n[i] = e[i];
            return n
        }
        var W = {
            _default: Object(w.s)(G)
        }
          , Y = {
            render: function(e, t) {
                var n = e("NuxtLoading", {
                    ref: "loading"
                })
                  , o = e(this.layout || "nuxt")
                  , r = e("div", {
                    domProps: {
                        id: "__layout"
                    },
                    key: this.layoutName
                }, [o])
                  , l = e("transition", {
                    props: {
                        name: "layout",
                        mode: "out-in"
                    },
                    on: {
                        beforeEnter: function(e) {
                            window.$nuxt.$nextTick((function() {
                                window.$nuxt.$emit("triggerScroll")
                            }
                            ))
                        }
                    }
                }, [r]);
                return e("div", {
                    domProps: {
                        id: "__nuxt"
                    }
                }, [n, l])
            },
            data: function() {
                return {
                    isOnline: !0,
                    layout: null,
                    layoutName: "",
                    nbFetching: 0
                }
            },
            beforeCreate: function() {
                l.default.util.defineReactive(this, "nuxt", this.$options.nuxt)
            },
            created: function() {
                this.$root.$options.$nuxt = this,
                window.$nuxt = this,
                this.refreshOnlineStatus(),
                window.addEventListener("online", this.refreshOnlineStatus),
                window.addEventListener("offline", this.refreshOnlineStatus),
                this.error = this.nuxt.error,
                this.context = this.$options.context
            },
            mounted: function() {
                var e = this;
                return Object(o.a)(regeneratorRuntime.mark((function t() {
                    return regeneratorRuntime.wrap((function(t) {
                        for (; ; )
                            switch (t.prev = t.next) {
                            case 0:
                                e.$loading = e.$refs.loading;
                            case 1:
                            case "end":
                                return t.stop()
                            }
                    }
                    ), t)
                }
                )))()
            },
            watch: {
                "nuxt.err": "errorChanged"
            },
            computed: {
                isOffline: function() {
                    return !this.isOnline
                },
                isFetching: function() {
                    return this.nbFetching > 0
                }
            },
            methods: {
                refreshOnlineStatus: function() {
                    void 0 === window.navigator.onLine ? this.isOnline = !0 : this.isOnline = window.navigator.onLine
                },
                refresh: function() {
                    var e = this;
                    return Object(o.a)(regeneratorRuntime.mark((function t() {
                        var n, o;
                        return regeneratorRuntime.wrap((function(t) {
                            for (; ; )
                                switch (t.prev = t.next) {
                                case 0:
                                    if ((n = Object(w.h)(e.$route)).length) {
                                        t.next = 3;
                                        break
                                    }
                                    return t.abrupt("return");
                                case 3:
                                    return e.$loading.start(),
                                    o = n.map((function(t) {
                                        var p = [];
                                        if (t.$options.fetch && t.$options.fetch.length && p.push(Object(w.q)(t.$options.fetch, e.context)),
                                        t.$fetch)
                                            p.push(t.$fetch());
                                        else {
                                            var n, o = J(Object(w.e)(t.$vnode.componentInstance));
                                            try {
                                                for (o.s(); !(n = o.n()).done; ) {
                                                    var component = n.value;
                                                    p.push(component.$fetch())
                                                }
                                            } catch (e) {
                                                o.e(e)
                                            } finally {
                                                o.f()
                                            }
                                        }
                                        return t.$options.asyncData && p.push(Object(w.q)(t.$options.asyncData, e.context).then((function(e) {
                                            for (var n in e)
                                                l.default.set(t.$data, n, e[n])
                                        }
                                        ))),
                                        Promise.all(p)
                                    }
                                    )),
                                    t.prev = 5,
                                    t.next = 8,
                                    Promise.all(o);
                                case 8:
                                    t.next = 15;
                                    break;
                                case 10:
                                    t.prev = 10,
                                    t.t0 = t.catch(5),
                                    e.$loading.fail(t.t0),
                                    Object(w.k)(t.t0),
                                    e.error(t.t0);
                                case 15:
                                    e.$loading.finish();
                                case 16:
                                case "end":
                                    return t.stop()
                                }
                        }
                        ), t, null, [[5, 10]])
                    }
                    )))()
                },
                errorChanged: function() {
                    if (this.nuxt.err) {
                        this.$loading && (this.$loading.fail && this.$loading.fail(this.nuxt.err),
                        this.$loading.finish && this.$loading.finish());
                        var e = (C.options || C).layout;
                        "function" == typeof e && (e = e(this.context)),
                        this.setLayout(e)
                    }
                },
                setLayout: function(e) {
                    return e && W["_" + e] || (e = "default"),
                    this.layoutName = e,
                    this.layout = W["_" + e],
                    this.layout
                },
                loadLayout: function(e) {
                    return e && W["_" + e] || (e = "default"),
                    Promise.resolve(W["_" + e])
                }
            },
            components: {
                NuxtLoading: U
            }
        };
        n(76),
        n(87);
        function K(e, t) {
            var n;
            if ("undefined" == typeof Symbol || null == e[Symbol.iterator]) {
                if (Array.isArray(e) || (n = function(e, t) {
                    if (!e)
                        return;
                    if ("string" == typeof e)
                        return Z(e, t);
                    var n = Object.prototype.toString.call(e).slice(8, -1);
                    "Object" === n && e.constructor && (n = e.constructor.name);
                    if ("Map" === n || "Set" === n)
                        return Array.from(e);
                    if ("Arguments" === n || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n))
                        return Z(e, t)
                }(e)) || t && e && "number" == typeof e.length) {
                    n && (e = n);
                    var i = 0
                      , o = function() {};
                    return {
                        s: o,
                        n: function() {
                            return i >= e.length ? {
                                done: !0
                            } : {
                                done: !1,
                                value: e[i++]
                            }
                        },
                        e: function(e) {
                            throw e
                        },
                        f: o
                    }
                }
                throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
            }
            var r, l = !0, c = !1;
            return {
                s: function() {
                    n = e[Symbol.iterator]()
                },
                n: function() {
                    var e = n.next();
                    return l = e.done,
                    e
                },
                e: function(e) {
                    c = !0,
                    r = e
                },
                f: function() {
                    try {
                        l || null == n.return || n.return()
                    } finally {
                        if (c)
                            throw r
                    }
                }
            }
        }
        function Z(e, t) {
            (null == t || t > e.length) && (t = e.length);
            for (var i = 0, n = new Array(t); i < t; i++)
                n[i] = e[i];
            return n
        }
        l.default.use(c.a);
        var Q = ["state", "getters", "actions", "mutations"]
          , ee = {};
        (ee = function(e, t) {
            if ((e = e.default || e).commit)
                throw new Error("[nuxt] ".concat(t, " should export a method that returns a Vuex instance."));
            return "function" != typeof e && (e = Object.assign({}, e)),
            ne(e, t)
        }(n(298), "store/index.js")).modules = ee.modules || {},
        oe(n(299), "address.js"),
        oe(n(19), "channel.js"),
        oe(n(300), "list.js"),
        oe(n(301), "Main.js"),
        oe(n(302), "search.js"),
        oe(n(174), "User.js");
        var te = ee instanceof Function ? ee : function() {
            return new c.a.Store(Object.assign({
                strict: !1
            }, ee))
        }
        ;
        function ne(e, t) {
            if (e.state && "function" != typeof e.state) {
                console.warn("'state' should be a method that returns an object in ".concat(t));
                var n = Object.assign({}, e.state);
                e = Object.assign({}, e, {
                    state: function() {
                        return n
                    }
                })
            }
            return e
        }
        function oe(e, t) {
            e = e.default || e;
            var n = t.replace(/\.(js|mjs)$/, "").split("/")
              , o = n[n.length - 1]
              , r = "store/".concat(t);
            if (e = "state" === o ? function(e, t) {
                if ("function" != typeof e) {
                    console.warn("".concat(t, " should export a method that returns an object"));
                    var n = Object.assign({}, e);
                    return function() {
                        return n
                    }
                }
                return ne(e, t)
            }(e, r) : ne(e, r),
            Q.includes(o)) {
                var l = o;
                ae(re(ee, n, {
                    isProperty: !0
                }), e, l)
            } else {
                "index" === o && (n.pop(),
                o = n[n.length - 1]);
                var c, d = re(ee, n), f = K(Q);
                try {
                    for (f.s(); !(c = f.n()).done; ) {
                        var m = c.value;
                        ae(d, e[m], m)
                    }
                } catch (e) {
                    f.e(e)
                } finally {
                    f.f()
                }
                !1 === e.namespaced && delete d.namespaced
            }
        }
        function re(e, t) {
            var n = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : {}
              , o = n.isProperty
              , r = void 0 !== o && o;
            if (!t.length || r && 1 === t.length)
                return e;
            var l = t.shift();
            return e.modules[l] = e.modules[l] || {},
            e.modules[l].namespaced = !0,
            e.modules[l].modules = e.modules[l].modules || {},
            re(e.modules[l], t, {
                isProperty: r
            })
        }
        function ae(e, t, n) {
            t && ("state" === n ? e.state = t || e.state : e[n] = Object.assign({}, e[n], t))
        }
        n(211);
        var ie = n(182)
          , le = n.n(ie)
          , dialog = (n(200),
        n(142))
          , ce = n.n(dialog)
          , de = (n(201),
        n(145))
          , se = n.n(de)
          , ue = (n(320),
        n(188))
          , fe = n.n(ue)
          , pe = (n(323),
        n(189))
          , me = n.n(pe)
          , he = (n(199),
        n(85))
          , be = n.n(he)
          , ge = (n(203),
        n(146))
          , ve = n.n(ge)
          , xe = (n(204),
        n(147))
          , ye = n.n(xe)
          , we = (n(195),
        n(140))
          , ke = n.n(we)
          , _e = (n(194),
        n(139))
          , Oe = n.n(_e)
          , je = (n(193),
        n(137))
          , Pe = n.n(je)
          , ze = (n(197),
        n(103))
          , Se = n.n(ze);
        n(334);
        l.default.component(L.Picker.name, L.Picker),
        l.default.component(L.Popup.name, L.Popup),
        l.default.component(L.Spinner.name, L.Spinner),
        l.default.use(L.Lazyload, {
            preLoad: 1.3,
            error: "/images/common/img_load_fail.jpg",
            loading: "/images/common/img_loading.jpg",
            attempt: 1
        }),
        Se.a.setDefaultOptions({
            position: "bottom"
        }),
        l.default.use(Se.a).use(le.a).use(ce.a).use(se.a).use(fe.a).use(me.a).use(be.a).use(ve.a).use(ye.a).use(ke.a).use(Oe.a).use(Pe.a);
        var Te = n(190)
          , Ee = n.n(Te);
        if (l.default.use(Ee.a),
        "dev" === document.getElementById("ipt_env_api").value) {
            var $e = n(357);
            l.default.use(new $e)
        }
        n(111),
        n(88);
        var Ce = {
            install: function(e, t) {},
            app: {
                install: function(e, t) {
                    var n = this
                      , o = t.router
                      , r = t.tabbarRoutes || [];
                    o._go = o.go,
                    o._push = o.push,
                    o._replace = o.replace;
                    var l = !1;
                    o.push = function(e) {
                        n.nextDirection("forward"),
                        setTimeout((function() {
                            o._push(e)
                        }
                        ))
                    }
                    ,
                    o.replace = function(e) {
                        n.nextDirection("forward"),
                        setTimeout((function() {
                            o._replace(e)
                        }
                        ))
                    }
                    ,
                    o.go = function(e) {
                        -1 === e && (window.uni && window.uni.postMessage({
                            data: "navigateBack"
                        }),
                        l = !0,
                        n.nextDirection("back")),
                        setTimeout((function() {
                            o._go(e)
                        }
                        ))
                    }
                    ,
                    o.beforeEach((function(e, t, o) {
                        if ("/goods/goods" === e.path && Object(B.c)())
                            return window.wx.miniProgram.navigateTo({
                                url: "/pages/goods/goods?barcode=".concat(e.query.barcode)
                            }),
                            !1;
                        var c = e.fullPath
                          , d = t.fullPath
                          , f = JSON.parse(D.a.fetchFromSession("nav_history")) || [];
                        if (l ? (n.nextDirection("back"),
                        f.pop(),
                        l = !1) : f.length > 0 && f[f.length - 1] == c ? n.nextDirection("none") : f.length > 1 && f[f.length - 2] == c ? (n.nextDirection("back"),
                        f.pop()) : (f.push(c),
                        n.nextDirection("forward")),
                        D.a.saveToSession("nav_history", f),
                        r.includes(t.path) && r.includes(e.path) && n.nextDirection("none"),
                        "back" === n.direction)
                            D.a.removeFromSession(d);
                        else {
                            var m = n.pageContentScrollTop();
                            D.a.saveToSession(d, {
                                scrollTop: m
                            })
                        }
                        o()
                    }
                    )),
                    o.afterEach((function(e, t) {
                        window.statTracking && window.statTracking.pv(e.fullPath, t ? t.fullPath : "")
                    }
                    )),
                    window.__EVENT_BUS__.$on("beforePageEnter", (function(t) {
                        document.getElementsByClassName("page")[0].classList.add("page-old");
                        var n = D.a.fetchFromSession(window.location.pathname + window.location.search);
                        if (n && n.scrollTop) {
                            var o = t.querySelectorAll(".page-content")
                              , content = o[o.length - 1];
                            content && e.nextTick((function() {
                                content.scrollTop = n.scrollTop
                            }
                            ))
                        }
                    }
                    ));
                    var c = function() {
                        document.documentElement.style.fontSize = 20 * document.documentElement.clientWidth / 375 + "px"
                    };
                    if (c(),
                    window.addEventListener("resize", c, !1),
                    document.documentElement.addEventListener("touchstart", (function(e) {
                        e.touches.length > 1 && e.preventDefault()
                    }
                    ), !1),
                    Object(B.a)()) {
                        var d = 0;
                        document.documentElement.addEventListener("touchend", (function(e) {
                            var t = (new Date).getTime();
                            t - d < 300 && e.preventDefault(),
                            d = t
                        }
                        ), !1)
                    }
                },
                direction: "none",
                nextDirection: function(e) {
                    this.direction = e;
                    var t = document.querySelector("[idea-app]");
                    t && t.setAttribute("transition-direction", e)
                },
                root: function() {
                    return document.querySelector("[idea-app]")
                },
                pageContentScrollTop: function(e) {
                    var t = this.root();
                    if ("number" != typeof e)
                        return t && t.querySelector(".page-content") ? t.querySelector(".page-content").scrollTop : 0;
                    var n = t && t.querySelectorAll(".page-content")
                      , content = n[n.length - 1];
                    content && (content.scrollTop = e)
                }
            }
        }
          , Re = n(6)
          , Ie = function(e) {
            var t = e.app
              , n = e.store;
            window.__EVENT_BUS__ = new l.default;
            l.default.use(Ce.app, {
                router: t.router,
                tabbarRoutes: ["/", "/cate", "/cart/cart", "/user"]
            });
            var o, r = document.createElement("script");
            r.type = "text/javascript",
            r.async = !0,
            r.src = "/js/uni.webview.1.5.2.js",
            n.state.env.mpWechat || ((o = document.createElement("script")).type = "text/javascript",
            o.async = !0,
            o.src = "https://hm.baidu.com/hm.js?bcd90586685c3dc20f70646ea1cd01e1");
            var c = "";
            n.state.env.mpAlipay && ((c = document.createElement("script")).type = "text/javascript",
            c.async = !0,
            c.src = "https://appx/web-view.min.js");
            var d = "";
            n.state.env.mpJd && ((d = document.createElement("script")).type = "text/javascript",
            d.async = !0,
            d.src = "/js/jd-webview.js",
            Re.a.platFormId = 8);
            var f = "";
            n.state.env.mpBd && ((f = document.createElement("script")).type = "text/javascript",
            f.async = !0,
            f.src = "/js/swan-2.0.29.js",
            Re.a.platFormId = 11);
            var m = document.getElementsByTagName("body")[0];
            if (m.parentNode.append ? (m.parentNode.append(r),
            o && m.parentNode.append(o),
            c && m.parentNode.append(c),
            d && m.parentNode.append(d),
            f && m.parentNode.append(f)) : (m.parentNode.append(c),
            m.parentNode.append(d),
            m.parentNode.append(f)),
            "production" === document.getElementById("ipt_env_api").value) {
                var h = document.createElement("script");
                h.type = "text/javascript",
                h.async = !0;
                var v = document.getElementsByTagName("body")[0];
                v.parentNode.append ? v.parentNode.append(h, h) : v.parentNode.appendChild(h),
                window.statTracking = {
                    pv: function(e) {
                        var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : "";
                        window._czc && window._czc.push(["_trackPageview", e, t])
                    },
                    event: function(data) {
                        window._czc && window._czc.push(["_trackEvent", data.category, data.action, data.label, data.value, data.nodeid])
                    }
                }
            }
            l.default.directive("stat", {
                bind: function(e, t) {
                    e.addEventListener("click", (function() {
                        var e = window.aplus_queue;
                        if (t.value && e) {
                            var data = t.value
                              , n = data && data.eventCode ? data.eventCode : "general_events_code"
                              , o = "";
                            data && data.category && (o = o + data.category + "_"),
                            data && data.action && (o = o + data.action + "_"),
                            data && data.label && (o = o + data.label + "_"),
                            data && data.value && (o = o + data.value + "_");
                            var param = {
                                action: o
                            };
                            e.push({
                                action: "aplus.record",
                                arguments: [n, "CLK", param]
                            })
                        }
                    }
                    ), !1)
                }
            }),
            window.onload = function() {
                uni.getEnv((function(e) {
                    e.h5 && 1 == e.h5 ? n.commit("updateIsH5Client", !0) : n.commit("updateIsH5Client", !1)
                }
                ))
            }
            ,
            l.default.directive("page", {
                bind: function(e, t) {
                    if (e.classList.contains("page")) {
                        var data = t.value || {};
                        data.tabBar ? e.classList.add("has-bottom") : e.classList.remove("has-bottom"),
                        window.__EVENT_BUS__.$emit(M.d, data)
                    }
                },
                update: function(e, t) {
                    if (e.classList.contains("page")) {
                        var data = t.value || {};
                        data.tabBar ? e.classList.add("has-bottom") : e.classList.remove("has-bottom"),
                        window.__EVENT_BUS__.$emit(M.d, data)
                    }
                }
            })
        }
          , Ae = {
            install: function(e) {
                e.prototype.$sendEvent = function(e, param) {
                    window.aplus_queue.push({
                        action: "aplus.record",
                        arguments: [e, "CLK", param]
                    })
                }
            }
        };
        l.default.use(Ae);
        var Ue = n(98)
          , De = n(99)
          , Ne = n(34)
          , Le = n.n(Ne)
          , Me = function() {
            function e() {
                var t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {
                    appkey: "2"
                };
                Object(Ue.a)(this, e),
                this.initData = {
                    appkey: t.appkey,
                    isAgreeEmpower: !0
                },
                this.routes = {
                    lastRoute: "",
                    currRoute: ""
                },
                this.route()
            }
            var t;
            return Object(De.a)(e, [{
                key: "setPassStatus",
                value: function(e) {
                    var t = e ? 1 : 2;
                    this.initData.isAgreeEmpower = e,
                    sessionStorage.setItem("empower_status", t)
                }
            }, {
                key: "route",
                value: function() {
                    var e = this;
                    l.default.mixin({
                        beforeRouteEnter: function(t, n, o) {
                            var r = n.fullPath || ""
                              , l = t.fullPath || "";
                            e.routes = {
                                lastRoute: r,
                                currRoute: l
                            },
                            e.watchRouter(),
                            o()
                        }
                    })
                }
            }, {
                key: "watchRouter",
                value: function() {
                    var e = D.a.fetchFromCookie("user_id");
                    this.send("page_view", "", "页面访问", {}, e)
                }
            }, {
                key: "setInitUuid",
                value: function() {
                    sessionStorage.getItem("htdf_uuid") ? this.initData.uuid = sessionStorage.getItem("htdf_uuid") : (this.initData.uuid = function() {
                        for (var s = [], e = "0123456789abcdefg!@#$&*_STUVWXYZ", t = (new Date).getTime(), i = 0; i < 36; i++) {
                            var n = Math.floor(32 * Math.random());
                            s[i] = e.substring(n, n + 1)
                        }
                        s[14] = "4",
                        s[8] = s[13] = s[18] = s[23] = "-";
                        var o = s.join("");
                        return o = t + "-" + o
                    }(),
                    sessionStorage.setItem("htdf_uuid", this.initData.uuid))
                }
            }, {
                key: "setInitEmpower",
                value: function() {
                    sessionStorage.getItem("empower_status") ? this.initData.isAgreeEmpower = 1 == sessionStorage.getItem("empower_status") : (this.initData.isAgreeEmpower = !0,
                    sessionStorage.setItem("empower_status", 1))
                }
            }, {
                key: "send",
                value: function(e, t, label) {
                    var n = arguments.length > 3 && void 0 !== arguments[3] ? arguments[3] : {}
                      , o = arguments.length > 4 ? arguments[4] : void 0;
                    this.setInitUuid(),
                    this.setInitEmpower();
                    var r = {
                        app_user_identification: this.initData.uuid,
                        platform_id: 1,
                        platform_type: this.initData.appkey,
                        category: e,
                        action: t,
                        user_id: o,
                        origin: this.routes.currRoute,
                        referer: this.routes.lastRoute,
                        label: label,
                        value: JSON.stringify(n)
                    };
                    r = Object.assign({}, r),
                    this.request(r)
                }
            }, {
                key: "request",
                value: (t = Object(o.a)(regeneratorRuntime.mark((function e(data) {
                    var t, n, o;
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                if (t = "production" === document.getElementById("ipt_env_api").value) {
                                    e.next = 3;
                                    break
                                }
                                return e.abrupt("return");
                            case 3:
                                if (this.initData.isAgreeEmpower) {
                                    e.next = 5;
                                    break
                                }
                                return e.abrupt("return");
                            case 5:
                                return n = Le.a.create(),
                                o = "".concat(t ? Re.a.statService.baseURL : Re.a.statService.baseURL_TEST, "/user/default/log"),
                                n.interceptors.request.use((function(e) {
                                    return e
                                }
                                ), (function(e) {
                                    return e
                                }
                                )),
                                n.interceptors.response.use((function(e) {
                                    return e
                                }
                                ), (function(e) {
                                    return e
                                }
                                )),
                                e.next = 11,
                                n({
                                    method: "post",
                                    url: o,
                                    data: data,
                                    headers: {
                                        "content-type": "application/json"
                                    }
                                });
                            case 11:
                                e.sent;
                            case 12:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e, this)
                }
                ))),
                function(e) {
                    return t.apply(this, arguments)
                }
                )
            }]),
            e
        }();
        l.default.prototype.$stat = new Me({
            appkey: "2",
            isAgreeEmpower: !0
        });
        var Be = l.default.prototype.$stat;
        function qe(object, e) {
            var t = Object.keys(object);
            if (Object.getOwnPropertySymbols) {
                var n = Object.getOwnPropertySymbols(object);
                e && (n = n.filter((function(e) {
                    return Object.getOwnPropertyDescriptor(object, e).enumerable
                }
                ))),
                t.push.apply(t, n)
            }
            return t
        }
        function Fe(e) {
            for (var i = 1; i < arguments.length; i++) {
                var source = null != arguments[i] ? arguments[i] : {};
                i % 2 ? qe(Object(source), !0).forEach((function(t) {
                    Object(r.a)(e, t, source[t])
                }
                )) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(source)) : qe(Object(source)).forEach((function(t) {
                    Object.defineProperty(e, t, Object.getOwnPropertyDescriptor(source, t))
                }
                ))
            }
            return e
        }
        l.default.component(m.a.name, m.a),
        l.default.component(v.a.name, Fe(Fe({}, v.a), {}, {
            render: function(e, t) {
                return v.a._warned || (v.a._warned = !0,
                console.warn("<no-ssr> has been deprecated and will be removed in Nuxt 3, please use <client-only> instead")),
                v.a.render(e, t)
            }
        })),
        l.default.component(z.name, z),
        l.default.component("NChild", z),
        l.default.component(I.name, I),
        Object.defineProperty(l.default.prototype, "$nuxt", {
            get: function() {
                return this.$root.$options.$nuxt
            },
            configurable: !0
        }),
        l.default.use(d.a, {
            keyName: "head",
            attribute: "data-n-head",
            ssrAttribute: "data-n-head-ssr",
            tagIDKeyName: "hid"
        });
        var He = {
            name: "page",
            mode: "in-out",
            type: "transition",
            beforeEnter: function(e) {
                window.__EVENT_BUS__.$emit("beforePageEnter", e)
            },
            appear: !1,
            appearClass: "appear",
            appearActiveClass: "appear-active",
            appearToClass: "appear-to"
        }
          , Ve = c.a.Store.prototype.registerModule;
        function Ge(path, e) {
            var t = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : {}
              , n = Array.isArray(path) ? !!path.reduce((function(e, path) {
                return e && e[path]
            }
            ), this.state) : path in this.state;
            return Ve.call(this, path, e, Fe({
                preserveState: n
            }, t))
        }
        function Je(e) {
            return Xe.apply(this, arguments)
        }
        function Xe() {
            return (Xe = Object(o.a)(regeneratorRuntime.mark((function e(t) {
                var n, o, r, c, d, f, path, m, h = arguments;
                return regeneratorRuntime.wrap((function(e) {
                    for (; ; )
                        switch (e.prev = e.next) {
                        case 0:
                            return m = function(e, t) {
                                if (!e)
                                    throw new Error("inject(key, value) has no key provided");
                                if (void 0 === t)
                                    throw new Error("inject('".concat(e, "', value) has no value provided"));
                                c[e = "$" + e] = t,
                                c.context[e] || (c.context[e] = t),
                                r[e] = c[e];
                                var n = "__nuxt_" + e + "_installed__";
                                l.default[n] || (l.default[n] = !0,
                                l.default.use((function() {
                                    Object.prototype.hasOwnProperty.call(l.default.prototype, e) || Object.defineProperty(l.default.prototype, e, {
                                        get: function() {
                                            return this.$root.$options[e]
                                        }
                                    })
                                }
                                )))
                            }
                            ,
                            n = h.length > 1 && void 0 !== h[1] ? h[1] : {},
                            e.next = 4,
                            P(0, n);
                        case 4:
                            return o = e.sent,
                            (r = te(t)).$router = o,
                            r.registerModule = Ge,
                            c = Fe({
                                head: {
                                    title: "海南免税-离岛免税",
                                    titleTemplate: "%s | 海旅免税城",
                                    meta: [{
                                        charset: "utf-8"
                                    }, {
                                        name: "viewport",
                                        content: "width=device-width, initial-scale=1, user-scalable=no, minimal-ui"
                                    }, {
                                        name: "wap-font-scale",
                                        content: "no"
                                    }, {
                                        name: "apple-mobile-web-app-capable",
                                        content: "yes"
                                    }, {
                                        name: "apple-mobile-web-app-status-bar-style",
                                        content: "white"
                                    }, {
                                        name: "author",
                                        content: "m.hltmsp.com"
                                    }, {
                                        "http-equiv": "Content-Security-Policy",
                                        content: "script-src 'self' 'unsafe-eval' 'unsafe-inline' d.alicdn.com hm.baidu.com appx/web-view.min.js umini.shujupie.com qiyukf.com;"
                                    }, {
                                        name: "description",
                                        content: "欢乐购，随心游。海旅免税城官方商城100%免税正品。涵盖了手表、首饰、箱包、香水、化妆品、电子产品、进口酒等45大类免税商品，近350个国际知名品牌。手机轻松下单，支持三亚、海口、琼海（博鳌）机场、轮渡、火车站提货，或选择邮寄到家，免去排队提货烦恼。"
                                    }, {
                                        name: 'keywords"',
                                        content: "免税正品,品牌折扣,限时抢购。手表、首饰、箱包、香水、化妆品、电子产品、进口酒。离岛免税,邮寄自提。"
                                    }],
                                    link: [{
                                        rel: "icon",
                                        type: "image/x-icon",
                                        href: "/favicon.ico"
                                    }],
                                    script: [{
                                        src: "/js/jweixin-1.6.0.js"
                                    }, {
                                        src: "/js/aplus_queue.js"
                                    }],
                                    style: []
                                },
                                store: r,
                                router: o,
                                nuxt: {
                                    defaultTransition: He,
                                    transitions: [He],
                                    setTransitions: function(e) {
                                        return Array.isArray(e) || (e = [e]),
                                        e = e.map((function(e) {
                                            return e = e ? "string" == typeof e ? Object.assign({}, He, {
                                                name: e
                                            }) : Object.assign({}, He, e) : He
                                        }
                                        )),
                                        this.$options.nuxt.transitions = e,
                                        e
                                    },
                                    err: null,
                                    dateErr: null,
                                    error: function(e) {
                                        e = e || null,
                                        c.context._errored = Boolean(e),
                                        e = e ? Object(w.p)(e) : null;
                                        var n = c.nuxt;
                                        return this && (n = this.nuxt || this.$options.nuxt),
                                        n.dateErr = Date.now(),
                                        n.err = e,
                                        t && (t.nuxt.error = e),
                                        e
                                    }
                                }
                            }, Y),
                            r.app = c,
                            d = t ? t.next : function(e) {
                                return c.router.push(e)
                            }
                            ,
                            t ? f = o.resolve(t.url).route : (path = Object(w.f)(o.options.base, o.options.mode),
                            f = o.resolve(path).route),
                            e.next = 14,
                            Object(w.t)(c, {
                                store: r,
                                route: f,
                                next: d,
                                error: c.nuxt.error.bind(c),
                                payload: t ? t.payload : void 0,
                                req: t ? t.req : void 0,
                                res: t ? t.res : void 0,
                                beforeRenderFns: t ? t.beforeRenderFns : void 0,
                                ssrContext: t
                            });
                        case 14:
                            m("config", n),
                            window.__NUXT__ && window.__NUXT__.state && r.replaceState(window.__NUXT__.state),
                            e.next = 20;
                            break;
                        case 20:
                            e.next = 23;
                            break;
                        case 23:
                            e.next = 26;
                            break;
                        case 26:
                            return e.next = 29,
                            Ie(c.context);
                        case 29:
                            e.next = 32;
                            break;
                        case 32:
                            if ("function" != typeof Be) {
                                e.next = 35;
                                break
                            }
                            return e.next = 35,
                            Be(c.context, m);
                        case 35:
                            0,
                            e.next = 39;
                            break;
                        case 39:
                            return e.abrupt("return", {
                                store: r,
                                app: c,
                                router: o
                            });
                        case 40:
                        case "end":
                            return e.stop()
                        }
                }
                ), e)
            }
            )))).apply(this, arguments)
        }
    },
    6: function(e, t, n) {
        "use strict";
        n(31),
        n(53),
        n(38),
        n(39),
        n(16);
        var o = n(81)
          , r = n.n(o)
          , l = n(141)
          , c = "wxa5o7oo8yqsj4b1clncve1iqb0ftqvp"
          , d = "&&SMR3#!JZFH7Z&XJ8VT*PP*3RY9QR&@"
          , time = function() {
            return Math.floor(Date.now() / 1e3)
        }
          , f = {
            onLineMall: {
                name: "线上商城",
                id: 6
            }
        }
          , m = {
            web: 1,
            scanBuy: 2,
            casher: 3
        };
        t.a = {
            defaultService: {
                baseURL: "https://api.hltmsp.com",
                baseURL_TEST: "https://apilocal.hltmsp.com",
                timeout: 3e5,
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
                }
            },
            payService: {
                baseURL: "https://pay.hltmsp.com",
                baseURL_TEST: "https://pay-dev.hltmsp.com",
                timeout: 3e5,
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
                }
            },
            statService: {
                baseURL: "https://bigdata-api.hltmsp.com",
                baseURL_TEST: "http://bigdata-api.dev.hltmsp.com",
                timeout: 3e4,
                headers: {
                    "Content-Type": "application/json"
                }
            },
            platFormId: m.web,
            shopId: f.onLineMall.id,
            shops: [f.onLineMall],
            dfAPPId: c,
            dfSecret: d,
            sign: function() {
                var e = time();
                return r()("".concat(c).concat(d).concat(e.toString()))
            },
            time: time,
            commonShareImg: "/images/common/share_logo.jpg",
            commonShareDesc: "海旅免税城！",
            commonShareTitle: "元宵喜购惠，68香化特权每天15点限量发，全场68折起",
            setSignData: function(data) {
                data || (data = {}),
                data.appid = "duty_h5";
                var e = "hltmsp5615466";
                4 != data.platformId && 5 != data.platformId || (data.appid = "duty_app",
                e = "hltmsp89226416"),
                2 != data.platformId && 6 != data.platformId && 8 != data.platformId && 11 != data.platformId || (data.appid = "duty_xcx",
                e = "hltmsp5689456"),
                data.nonce_str = l.b.randomStr(Math.floor(26 * Math.random()) + 6);
                var t = 2022051288 + Math.floor(Date.now() / 1e3) + ""
                  , n = Math.floor(9 * Math.random()) + 1;
                t = "" + n + t.substring(t.length - n, t.length) + t.substring(0, t.length - n),
                data.time_stamp = t;
                var o = "";
                return Object.keys(data).sort().map((function(e) {
                    null === data[e] || void 0 === data[e] || "" === data[e] || Array.isArray(data[e]) || (o += "".concat(e, "=").concat(data[e], "&"))
                }
                )),
                o += "app_key=".concat(e),
                (data = JSON.parse(JSON.stringify(data))).sign = r()(o).toUpperCase(),
                data
            },
            setMidPidandSoOn: function(data, e) {
                return data || (data = {}),
                data.platformId || (data.platformId = m.web,
                e.state.User.plid && (data.platformId = e.state.User.plid)),
                data.mid || e.state.User.mid && (data.mid = e.state.User.mid),
                data.sid || e.state.User.sid && (data.sid = e.state.User.sid),
                data.pid || e.state.User.pid && (data.pid = e.state.User.pid),
                data.sflsource || e.state.User.sflsource && (data.sflsource = e.state.User.sflsource),
                data
            }
        }
    },
    74: function(e, t, n) {
        "use strict";
        n.d(t, "b", (function() {
            return o
        }
        )),
        n.d(t, "c", (function() {
            return r
        }
        )),
        n.d(t, "a", (function() {
            return l
        }
        ));
        n(68);
        function o() {
            return !!navigator.userAgent.match(/MicroMessenger/i)
        }
        function r() {
            return "miniprogram" === window.__wxjs_environment
        }
        function l() {
            return !!navigator.userAgent.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/)
        }
    },
    81: function(module, exports, __webpack_require__) {
        (function(process, global, module) {
            var __WEBPACK_AMD_DEFINE_RESULT__;
            __webpack_require__(38),
            __webpack_require__(39),
            __webpack_require__(16),
            __webpack_require__(256),
            __webpack_require__(262),
            __webpack_require__(87);
            var _typeof = __webpack_require__(263);
            (function() {
                "use strict";
                var ERROR = "input is invalid type"
                  , WINDOW = "object" === ("undefined" == typeof window ? "undefined" : _typeof(window))
                  , root = WINDOW ? window : {};
                root.JS_MD5_NO_WINDOW && (WINDOW = !1);
                var WEB_WORKER = !WINDOW && "object" === ("undefined" == typeof self ? "undefined" : _typeof(self))
                  , NODE_JS = !root.JS_MD5_NO_NODE_JS && "object" === (void 0 === process ? "undefined" : _typeof(process)) && process.versions && process.versions.node;
                NODE_JS ? root = global : WEB_WORKER && (root = self);
                var COMMON_JS = !root.JS_MD5_NO_COMMON_JS && "object" === _typeof(module) && module.exports, AMD = __webpack_require__(264), ARRAY_BUFFER = !root.JS_MD5_NO_ARRAY_BUFFER && "undefined" != typeof ArrayBuffer, HEX_CHARS = "0123456789abcdef".split(""), EXTRA = [128, 32768, 8388608, -2147483648], SHIFT = [0, 8, 16, 24], OUTPUT_TYPES = ["hex", "array", "digest", "buffer", "arrayBuffer", "base64"], BASE64_ENCODE_CHAR = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".split(""), blocks = [], buffer8;
                if (ARRAY_BUFFER) {
                    var buffer = new ArrayBuffer(68);
                    buffer8 = new Uint8Array(buffer),
                    blocks = new Uint32Array(buffer)
                }
                !root.JS_MD5_NO_NODE_JS && Array.isArray || (Array.isArray = function(e) {
                    return "[object Array]" === Object.prototype.toString.call(e)
                }
                ),
                !ARRAY_BUFFER || !root.JS_MD5_NO_ARRAY_BUFFER_IS_VIEW && ArrayBuffer.isView || (ArrayBuffer.isView = function(e) {
                    return "object" === _typeof(e) && e.buffer && e.buffer.constructor === ArrayBuffer
                }
                );
                var createOutputMethod = function(e) {
                    return function(t) {
                        return new Md5(!0).update(t)[e]()
                    }
                }
                  , createMethod = function() {
                    var e = createOutputMethod("hex");
                    NODE_JS && (e = nodeWrap(e)),
                    e.create = function() {
                        return new Md5
                    }
                    ,
                    e.update = function(t) {
                        return e.create().update(t)
                    }
                    ;
                    for (var i = 0; i < OUTPUT_TYPES.length; ++i) {
                        var t = OUTPUT_TYPES[i];
                        e[t] = createOutputMethod(t)
                    }
                    return e
                }
                  , nodeWrap = function nodeWrap(method) {
                    var crypto = eval("require('crypto')")
                      , Buffer = eval("require('buffer').Buffer")
                      , nodeMethod = function(e) {
                        if ("string" == typeof e)
                            return crypto.createHash("md5").update(e, "utf8").digest("hex");
                        if (null == e)
                            throw ERROR;
                        return e.constructor === ArrayBuffer && (e = new Uint8Array(e)),
                        Array.isArray(e) || ArrayBuffer.isView(e) || e.constructor === Buffer ? crypto.createHash("md5").update(new Buffer(e)).digest("hex") : method(e)
                    };
                    return nodeMethod
                };
                function Md5(e) {
                    if (e)
                        blocks[0] = blocks[16] = blocks[1] = blocks[2] = blocks[3] = blocks[4] = blocks[5] = blocks[6] = blocks[7] = blocks[8] = blocks[9] = blocks[10] = blocks[11] = blocks[12] = blocks[13] = blocks[14] = blocks[15] = 0,
                        this.blocks = blocks,
                        this.buffer8 = buffer8;
                    else if (ARRAY_BUFFER) {
                        var t = new ArrayBuffer(68);
                        this.buffer8 = new Uint8Array(t),
                        this.blocks = new Uint32Array(t)
                    } else
                        this.blocks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
                    this.h0 = this.h1 = this.h2 = this.h3 = this.start = this.bytes = this.hBytes = 0,
                    this.finalized = this.hashed = !1,
                    this.first = !0
                }
                Md5.prototype.update = function(e) {
                    if (!this.finalized) {
                        var t, n = _typeof(e);
                        if ("string" !== n) {
                            if ("object" !== n)
                                throw ERROR;
                            if (null === e)
                                throw ERROR;
                            if (ARRAY_BUFFER && e.constructor === ArrayBuffer)
                                e = new Uint8Array(e);
                            else if (!(Array.isArray(e) || ARRAY_BUFFER && ArrayBuffer.isView(e)))
                                throw ERROR;
                            t = !0
                        }
                        for (var code, i, o = 0, r = e.length, l = this.blocks, c = this.buffer8; o < r; ) {
                            if (this.hashed && (this.hashed = !1,
                            l[0] = l[16],
                            l[16] = l[1] = l[2] = l[3] = l[4] = l[5] = l[6] = l[7] = l[8] = l[9] = l[10] = l[11] = l[12] = l[13] = l[14] = l[15] = 0),
                            t)
                                if (ARRAY_BUFFER)
                                    for (i = this.start; o < r && i < 64; ++o)
                                        c[i++] = e[o];
                                else
                                    for (i = this.start; o < r && i < 64; ++o)
                                        l[i >> 2] |= e[o] << SHIFT[3 & i++];
                            else if (ARRAY_BUFFER)
                                for (i = this.start; o < r && i < 64; ++o)
                                    (code = e.charCodeAt(o)) < 128 ? c[i++] = code : code < 2048 ? (c[i++] = 192 | code >> 6,
                                    c[i++] = 128 | 63 & code) : code < 55296 || code >= 57344 ? (c[i++] = 224 | code >> 12,
                                    c[i++] = 128 | code >> 6 & 63,
                                    c[i++] = 128 | 63 & code) : (code = 65536 + ((1023 & code) << 10 | 1023 & e.charCodeAt(++o)),
                                    c[i++] = 240 | code >> 18,
                                    c[i++] = 128 | code >> 12 & 63,
                                    c[i++] = 128 | code >> 6 & 63,
                                    c[i++] = 128 | 63 & code);
                            else
                                for (i = this.start; o < r && i < 64; ++o)
                                    (code = e.charCodeAt(o)) < 128 ? l[i >> 2] |= code << SHIFT[3 & i++] : code < 2048 ? (l[i >> 2] |= (192 | code >> 6) << SHIFT[3 & i++],
                                    l[i >> 2] |= (128 | 63 & code) << SHIFT[3 & i++]) : code < 55296 || code >= 57344 ? (l[i >> 2] |= (224 | code >> 12) << SHIFT[3 & i++],
                                    l[i >> 2] |= (128 | code >> 6 & 63) << SHIFT[3 & i++],
                                    l[i >> 2] |= (128 | 63 & code) << SHIFT[3 & i++]) : (code = 65536 + ((1023 & code) << 10 | 1023 & e.charCodeAt(++o)),
                                    l[i >> 2] |= (240 | code >> 18) << SHIFT[3 & i++],
                                    l[i >> 2] |= (128 | code >> 12 & 63) << SHIFT[3 & i++],
                                    l[i >> 2] |= (128 | code >> 6 & 63) << SHIFT[3 & i++],
                                    l[i >> 2] |= (128 | 63 & code) << SHIFT[3 & i++]);
                            this.lastByteIndex = i,
                            this.bytes += i - this.start,
                            i >= 64 ? (this.start = i - 64,
                            this.hash(),
                            this.hashed = !0) : this.start = i
                        }
                        return this.bytes > 4294967295 && (this.hBytes += this.bytes / 4294967296 << 0,
                        this.bytes = this.bytes % 4294967296),
                        this
                    }
                }
                ,
                Md5.prototype.finalize = function() {
                    if (!this.finalized) {
                        this.finalized = !0;
                        var e = this.blocks
                          , i = this.lastByteIndex;
                        e[i >> 2] |= EXTRA[3 & i],
                        i >= 56 && (this.hashed || this.hash(),
                        e[0] = e[16],
                        e[16] = e[1] = e[2] = e[3] = e[4] = e[5] = e[6] = e[7] = e[8] = e[9] = e[10] = e[11] = e[12] = e[13] = e[14] = e[15] = 0),
                        e[14] = this.bytes << 3,
                        e[15] = this.hBytes << 3 | this.bytes >>> 29,
                        this.hash()
                    }
                }
                ,
                Md5.prototype.hash = function() {
                    var a, b, e, t, n, o, r = this.blocks;
                    this.first ? b = ((b = ((a = ((a = r[0] - 680876937) << 7 | a >>> 25) - 271733879 << 0) ^ (e = ((e = (-271733879 ^ (t = ((t = (-1732584194 ^ 2004318071 & a) + r[1] - 117830708) << 12 | t >>> 20) + a << 0) & (-271733879 ^ a)) + r[2] - 1126478375) << 17 | e >>> 15) + t << 0) & (t ^ a)) + r[3] - 1316259209) << 22 | b >>> 10) + e << 0 : (a = this.h0,
                    b = this.h1,
                    e = this.h2,
                    b = ((b += ((a = ((a += ((t = this.h3) ^ b & (e ^ t)) + r[0] - 680876936) << 7 | a >>> 25) + b << 0) ^ (e = ((e += (b ^ (t = ((t += (e ^ a & (b ^ e)) + r[1] - 389564586) << 12 | t >>> 20) + a << 0) & (a ^ b)) + r[2] + 606105819) << 17 | e >>> 15) + t << 0) & (t ^ a)) + r[3] - 1044525330) << 22 | b >>> 10) + e << 0),
                    b = ((b += ((a = ((a += (t ^ b & (e ^ t)) + r[4] - 176418897) << 7 | a >>> 25) + b << 0) ^ (e = ((e += (b ^ (t = ((t += (e ^ a & (b ^ e)) + r[5] + 1200080426) << 12 | t >>> 20) + a << 0) & (a ^ b)) + r[6] - 1473231341) << 17 | e >>> 15) + t << 0) & (t ^ a)) + r[7] - 45705983) << 22 | b >>> 10) + e << 0,
                    b = ((b += ((a = ((a += (t ^ b & (e ^ t)) + r[8] + 1770035416) << 7 | a >>> 25) + b << 0) ^ (e = ((e += (b ^ (t = ((t += (e ^ a & (b ^ e)) + r[9] - 1958414417) << 12 | t >>> 20) + a << 0) & (a ^ b)) + r[10] - 42063) << 17 | e >>> 15) + t << 0) & (t ^ a)) + r[11] - 1990404162) << 22 | b >>> 10) + e << 0,
                    b = ((b += ((a = ((a += (t ^ b & (e ^ t)) + r[12] + 1804603682) << 7 | a >>> 25) + b << 0) ^ (e = ((e += (b ^ (t = ((t += (e ^ a & (b ^ e)) + r[13] - 40341101) << 12 | t >>> 20) + a << 0) & (a ^ b)) + r[14] - 1502002290) << 17 | e >>> 15) + t << 0) & (t ^ a)) + r[15] + 1236535329) << 22 | b >>> 10) + e << 0,
                    b = ((b += ((t = ((t += (b ^ e & ((a = ((a += (e ^ t & (b ^ e)) + r[1] - 165796510) << 5 | a >>> 27) + b << 0) ^ b)) + r[6] - 1069501632) << 9 | t >>> 23) + a << 0) ^ a & ((e = ((e += (a ^ b & (t ^ a)) + r[11] + 643717713) << 14 | e >>> 18) + t << 0) ^ t)) + r[0] - 373897302) << 20 | b >>> 12) + e << 0,
                    b = ((b += ((t = ((t += (b ^ e & ((a = ((a += (e ^ t & (b ^ e)) + r[5] - 701558691) << 5 | a >>> 27) + b << 0) ^ b)) + r[10] + 38016083) << 9 | t >>> 23) + a << 0) ^ a & ((e = ((e += (a ^ b & (t ^ a)) + r[15] - 660478335) << 14 | e >>> 18) + t << 0) ^ t)) + r[4] - 405537848) << 20 | b >>> 12) + e << 0,
                    b = ((b += ((t = ((t += (b ^ e & ((a = ((a += (e ^ t & (b ^ e)) + r[9] + 568446438) << 5 | a >>> 27) + b << 0) ^ b)) + r[14] - 1019803690) << 9 | t >>> 23) + a << 0) ^ a & ((e = ((e += (a ^ b & (t ^ a)) + r[3] - 187363961) << 14 | e >>> 18) + t << 0) ^ t)) + r[8] + 1163531501) << 20 | b >>> 12) + e << 0,
                    b = ((b += ((t = ((t += (b ^ e & ((a = ((a += (e ^ t & (b ^ e)) + r[13] - 1444681467) << 5 | a >>> 27) + b << 0) ^ b)) + r[2] - 51403784) << 9 | t >>> 23) + a << 0) ^ a & ((e = ((e += (a ^ b & (t ^ a)) + r[7] + 1735328473) << 14 | e >>> 18) + t << 0) ^ t)) + r[12] - 1926607734) << 20 | b >>> 12) + e << 0,
                    b = ((b += ((o = (t = ((t += ((n = b ^ e) ^ (a = ((a += (n ^ t) + r[5] - 378558) << 4 | a >>> 28) + b << 0)) + r[8] - 2022574463) << 11 | t >>> 21) + a << 0) ^ a) ^ (e = ((e += (o ^ b) + r[11] + 1839030562) << 16 | e >>> 16) + t << 0)) + r[14] - 35309556) << 23 | b >>> 9) + e << 0,
                    b = ((b += ((o = (t = ((t += ((n = b ^ e) ^ (a = ((a += (n ^ t) + r[1] - 1530992060) << 4 | a >>> 28) + b << 0)) + r[4] + 1272893353) << 11 | t >>> 21) + a << 0) ^ a) ^ (e = ((e += (o ^ b) + r[7] - 155497632) << 16 | e >>> 16) + t << 0)) + r[10] - 1094730640) << 23 | b >>> 9) + e << 0,
                    b = ((b += ((o = (t = ((t += ((n = b ^ e) ^ (a = ((a += (n ^ t) + r[13] + 681279174) << 4 | a >>> 28) + b << 0)) + r[0] - 358537222) << 11 | t >>> 21) + a << 0) ^ a) ^ (e = ((e += (o ^ b) + r[3] - 722521979) << 16 | e >>> 16) + t << 0)) + r[6] + 76029189) << 23 | b >>> 9) + e << 0,
                    b = ((b += ((o = (t = ((t += ((n = b ^ e) ^ (a = ((a += (n ^ t) + r[9] - 640364487) << 4 | a >>> 28) + b << 0)) + r[12] - 421815835) << 11 | t >>> 21) + a << 0) ^ a) ^ (e = ((e += (o ^ b) + r[15] + 530742520) << 16 | e >>> 16) + t << 0)) + r[2] - 995338651) << 23 | b >>> 9) + e << 0,
                    b = ((b += ((t = ((t += (b ^ ((a = ((a += (e ^ (b | ~t)) + r[0] - 198630844) << 6 | a >>> 26) + b << 0) | ~e)) + r[7] + 1126891415) << 10 | t >>> 22) + a << 0) ^ ((e = ((e += (a ^ (t | ~b)) + r[14] - 1416354905) << 15 | e >>> 17) + t << 0) | ~a)) + r[5] - 57434055) << 21 | b >>> 11) + e << 0,
                    b = ((b += ((t = ((t += (b ^ ((a = ((a += (e ^ (b | ~t)) + r[12] + 1700485571) << 6 | a >>> 26) + b << 0) | ~e)) + r[3] - 1894986606) << 10 | t >>> 22) + a << 0) ^ ((e = ((e += (a ^ (t | ~b)) + r[10] - 1051523) << 15 | e >>> 17) + t << 0) | ~a)) + r[1] - 2054922799) << 21 | b >>> 11) + e << 0,
                    b = ((b += ((t = ((t += (b ^ ((a = ((a += (e ^ (b | ~t)) + r[8] + 1873313359) << 6 | a >>> 26) + b << 0) | ~e)) + r[15] - 30611744) << 10 | t >>> 22) + a << 0) ^ ((e = ((e += (a ^ (t | ~b)) + r[6] - 1560198380) << 15 | e >>> 17) + t << 0) | ~a)) + r[13] + 1309151649) << 21 | b >>> 11) + e << 0,
                    b = ((b += ((t = ((t += (b ^ ((a = ((a += (e ^ (b | ~t)) + r[4] - 145523070) << 6 | a >>> 26) + b << 0) | ~e)) + r[11] - 1120210379) << 10 | t >>> 22) + a << 0) ^ ((e = ((e += (a ^ (t | ~b)) + r[2] + 718787259) << 15 | e >>> 17) + t << 0) | ~a)) + r[9] - 343485551) << 21 | b >>> 11) + e << 0,
                    this.first ? (this.h0 = a + 1732584193 << 0,
                    this.h1 = b - 271733879 << 0,
                    this.h2 = e - 1732584194 << 0,
                    this.h3 = t + 271733878 << 0,
                    this.first = !1) : (this.h0 = this.h0 + a << 0,
                    this.h1 = this.h1 + b << 0,
                    this.h2 = this.h2 + e << 0,
                    this.h3 = this.h3 + t << 0)
                }
                ,
                Md5.prototype.hex = function() {
                    this.finalize();
                    var e = this.h0
                      , h1 = this.h1
                      , h2 = this.h2
                      , h3 = this.h3;
                    return HEX_CHARS[e >> 4 & 15] + HEX_CHARS[15 & e] + HEX_CHARS[e >> 12 & 15] + HEX_CHARS[e >> 8 & 15] + HEX_CHARS[e >> 20 & 15] + HEX_CHARS[e >> 16 & 15] + HEX_CHARS[e >> 28 & 15] + HEX_CHARS[e >> 24 & 15] + HEX_CHARS[h1 >> 4 & 15] + HEX_CHARS[15 & h1] + HEX_CHARS[h1 >> 12 & 15] + HEX_CHARS[h1 >> 8 & 15] + HEX_CHARS[h1 >> 20 & 15] + HEX_CHARS[h1 >> 16 & 15] + HEX_CHARS[h1 >> 28 & 15] + HEX_CHARS[h1 >> 24 & 15] + HEX_CHARS[h2 >> 4 & 15] + HEX_CHARS[15 & h2] + HEX_CHARS[h2 >> 12 & 15] + HEX_CHARS[h2 >> 8 & 15] + HEX_CHARS[h2 >> 20 & 15] + HEX_CHARS[h2 >> 16 & 15] + HEX_CHARS[h2 >> 28 & 15] + HEX_CHARS[h2 >> 24 & 15] + HEX_CHARS[h3 >> 4 & 15] + HEX_CHARS[15 & h3] + HEX_CHARS[h3 >> 12 & 15] + HEX_CHARS[h3 >> 8 & 15] + HEX_CHARS[h3 >> 20 & 15] + HEX_CHARS[h3 >> 16 & 15] + HEX_CHARS[h3 >> 28 & 15] + HEX_CHARS[h3 >> 24 & 15]
                }
                ,
                Md5.prototype.toString = Md5.prototype.hex,
                Md5.prototype.digest = function() {
                    this.finalize();
                    var e = this.h0
                      , h1 = this.h1
                      , h2 = this.h2
                      , h3 = this.h3;
                    return [255 & e, e >> 8 & 255, e >> 16 & 255, e >> 24 & 255, 255 & h1, h1 >> 8 & 255, h1 >> 16 & 255, h1 >> 24 & 255, 255 & h2, h2 >> 8 & 255, h2 >> 16 & 255, h2 >> 24 & 255, 255 & h3, h3 >> 8 & 255, h3 >> 16 & 255, h3 >> 24 & 255]
                }
                ,
                Md5.prototype.array = Md5.prototype.digest,
                Md5.prototype.arrayBuffer = function() {
                    this.finalize();
                    var e = new ArrayBuffer(16)
                      , t = new Uint32Array(e);
                    return t[0] = this.h0,
                    t[1] = this.h1,
                    t[2] = this.h2,
                    t[3] = this.h3,
                    e
                }
                ,
                Md5.prototype.buffer = Md5.prototype.arrayBuffer,
                Md5.prototype.base64 = function(e) {
                    for (var t, n, o, r = "", l = this.array(), i = 0; i < 15; )
                        t = l[i++],
                        n = l[i++],
                        o = l[i++],
                        r += BASE64_ENCODE_CHAR[t >>> 2] + BASE64_ENCODE_CHAR[63 & (t << 4 | n >>> 4)] + BASE64_ENCODE_CHAR[63 & (n << 2 | o >>> 6)] + BASE64_ENCODE_CHAR[63 & o];
                    return t = l[i],
                    r += BASE64_ENCODE_CHAR[t >>> 2] + BASE64_ENCODE_CHAR[t << 4 & 63] + "=="
                }
                ;
                var exports = createMethod();
                COMMON_JS ? module.exports = exports : (root.md5 = exports,
                AMD && (__WEBPACK_AMD_DEFINE_RESULT__ = function() {
                    return exports
                }
                .call(exports, __webpack_require__, exports, module),
                void 0 === __WEBPACK_AMD_DEFINE_RESULT__ || (module.exports = __WEBPACK_AMD_DEFINE_RESULT__)))
            }
            )()
        }
        ).call(this, __webpack_require__(77), __webpack_require__(44), __webpack_require__(210)(module))
    }
},
    [[214, 495, 68, 496]],
]);

// console.log(window.webpackJsonp)
console.log(window.webpackJsonp[0][1]['141'])
console.log(window.randomStr)
