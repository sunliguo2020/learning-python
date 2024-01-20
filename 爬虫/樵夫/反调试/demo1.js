!function (e, t) {
    "object" == typeof exports && "undefined" != typeof module ? module.exports = t() : "function" == typeof define && define.amd ? define(t) : (e = "undefined" != typeof globalThis ? globalThis : e || self).DisableDevtool = t()
}(this, function () {
    "use strict";

    function o(e) {
        return (o = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (e) {
            return typeof e
        } : function (e) {
            return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
        })(e)
    }

    function i(e, t) {
        if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function")
    }

    function r(e, t) {
        for (var n = 0; n < t.length; n++) {
            var i = t[n];
            i.enumerable = i.enumerable || !1, i.configurable = !0, "value" in i && (i.writable = !0), Object.defineProperty(e, i.key, i)
        }
    }

    function u(e, t, n) {
        t && r(e.prototype, t), n && r(e, n), Object.defineProperty(e, "prototype", {writable: !1})
    }

    function e(e, t, n) {
        t in e ? Object.defineProperty(e, t, {value: n, enumerable: !0, configurable: !0, writable: !0}) : e[t] = n
    }

    function n(e, t) {
        if ("function" != typeof t && null !== t) throw new TypeError("Super expression must either be null or a function");
        e.prototype = Object.create(t && t.prototype, {
            constructor: {
                value: e,
                writable: !0,
                configurable: !0
            }
        }), Object.defineProperty(e, "prototype", {writable: !1}), t && a(e, t)
    }

    function c(e) {
        return (c = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function (e) {
            return e.__proto__ || Object.getPrototypeOf(e)
        })(e)
    }

    function a(e, t) {
        return (a = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function (e, t) {
            return e.__proto__ = t, e
        })(e, t)
    }

    function z(e, t) {
        if (t && ("object" == typeof t || "function" == typeof t)) return t;
        if (void 0 !== t) throw new TypeError("Derived constructors may only return object or undefined");
        t = e;
        if (void 0 === t) throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
        return t
    }

    function l(n) {
        var i = function () {
            if ("undefined" == typeof Reflect || !Reflect.construct) return !1;
            if (Reflect.construct.sham) return !1;
            if ("function" == typeof Proxy) return !0;
            try {
                return Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function () {
                })), !0
            } catch (e) {
                return !1
            }
        }();
        return function () {
            var e, t = c(n);
            return z(this, i ? (e = c(this).constructor, Reflect.construct(t, arguments, e)) : t.apply(this, arguments))
        }
    }

    function W(e, t) {
        (null == t || t > e.length) && (t = e.length);
        for (var n = 0, i = new Array(t); n < t; n++) i[n] = e[n];
        return i
    }

    function U(e, t) {
        var n, i = "undefined" != typeof Symbol && e[Symbol.iterator] || e["@@iterator"];
        if (!i) {
            if (Array.isArray(e) || (i = function (e, t) {
                if (e) {
                    if ("string" == typeof e) return W(e, t);
                    var n = Object.prototype.toString.call(e).slice(8, -1);
                    return "Map" === (n = "Object" === n && e.constructor ? e.constructor.name : n) || "Set" === n ? Array.from(e) : "Arguments" === n || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n) ? W(e, t) : void 0
                }
            }(e)) || t && e && "number" == typeof e.length) return i && (e = i), n = 0, {
                s: t = function () {
                }, n: function () {
                    return n >= e.length ? {done: !0} : {done: !1, value: e[n++]}
                }, e: function (e) {
                    throw e
                }, f: t
            };
            throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
        }
        var o, r = !0, u = !1;
        return {
            s: function () {
                i = i.call(e)
            }, n: function () {
                var e = i.next();
                return r = e.done, e
            }, e: function (e) {
                u = !0, o = e
            }, f: function () {
                try {
                    r || null == i.return || i.return()
                } finally {
                    if (u) throw o
                }
            }
        }
    }

    var s = !1, t = {};

    function H(e) {
        t[e] = !1
    }

    function K() {
        for (var e in t) if (t[e]) return s = !0;
        return s = !1
    }

    function f() {
        return (new Date).getTime()
    }

    function V(e) {
        var t = f();
        return e(), f() - t
    }

    function q(n, i) {
        function e(t) {
            return function () {
                n && n();
                var e = t.apply(void 0, arguments);
                return i && i(), e
            }
        }

        var t = window.alert, o = window.confirm, r = window.prompt;
        try {
            window.alert = e(t), window.confirm = e(o), window.prompt = e(r)
        } catch (e) {
        }
    }

    function d(e) {
        return -1 !== navigator.userAgent.toLocaleLowerCase().indexOf(e)
    }

    var F = function () {
            try {
                return window.self !== window.top
            } catch (e) {
                return !0
            }
        }(), M = !/(iphone|ipad|ipod|ios|android)/i.test(navigator.userAgent.toLowerCase()), X = d("qqbrowser"),
        B = d("firefox"), N = d("macintosh"), $ = d("edge"), v = $ && !d("chrome") || d("trident") || d("msie"),
        h = d("crios"), G = d("edgios"), Y = d("chrome") || h;

    function J() {
        for (var e = function () {
            for (var e = {}, t = 0; t < 500; t++) e["".concat(t)] = "".concat(t);
            return e
        }(), t = [], n = 0; n < 50; n++) t.push(e);
        return t
    }

    var Q = "", Z = !1;

    function ee() {
        var e = y.ignore;
        if (e) {
            if ("function" == typeof e) return e();
            if (0 !== e.length) {
                var t = location.href;
                if (Q === t) return Z;
                Q = t;
                var n, i = !1, o = U(e);
                try {
                    for (o.s(); !(n = o.n()).done;) {
                        var r = n.value;
                        if ("string" == typeof r) {
                            if (-1 !== t.indexOf(r)) {
                                i = !0;
                                break
                            }
                        } else if (r.test(t)) {
                            i = !0;
                            break
                        }
                    }
                } catch (e) {
                    o.e(e)
                } finally {
                    o.f()
                }
                return Z = i
            }
        }
    }

    var te = 0, ne = 0, ie = [], oe = 0;

    function re(o) {
        function e() {
            l = !0
        }

        function t() {
            l = !1
        }

        var n, i, r, u, c, a, l = !1;

        function f() {
            (a[u] === r ? i : n)()
        }

        q(e, t), n = t, i = e, void 0 !== (a = document).hidden ? (r = "hidden", c = "visibilitychange", u = "visibilityState") : void 0 !== a.mozHidden ? (r = "mozHidden", c = "mozvisibilitychange", u = "mozVisibilityState") : void 0 !== a.msHidden ? (r = "msHidden", c = "msvisibilitychange", u = "msVisibilityState") : void 0 !== a.webkitHidden && (r = "webkitHidden", c = "webkitvisibilitychange", u = "webkitVisibilityState"), a.removeEventListener(c, f, !1), a.addEventListener(c, f, !1), te = window.setInterval(function () {
            if (!(o.isSuspend || l || ee())) {
                var e, t, n = U(ie);
                try {
                    for (n.s(); !(e = n.n()).done;) {
                        var i = e.value;
                        H(i.type), i.detect(oe++)
                    }
                } catch (e) {
                    n.e(e)
                } finally {
                    n.f()
                }
                g(), "function" == typeof y.ondevtoolclose && (t = s, !K() && t && y.ondevtoolclose())
            }
        }, y.interval), ne = setTimeout(function () {
            M || p()
        }, y.stopIntervalTime)
    }

    function p() {
        window.clearInterval(te)
    }

    function ue() {
        if (p(), y.url)
            window.location.href = y.url;
        else {
            try {
                // window.opener = null, window.open("", "_self"), window.close(), alert("我知路难但情坚，爱如初始情已定，最幸福的爱情没有言语，只有彼此心灵的契合。亲爱的，执子之手，与子偕老，愿与你相互守护一辈子。"), window.history.back()
            } catch (e) {
                console.log(e)
            }
            // setTimeout(function () {
            //     window.history.back()
            // }, 500)
        }
    }

    var y = {
        md5: "",
        ondevtoolopen: ue,
        ondevtoolclose: null,
        url: "",
        tkName: "ddtk",
        interval: 200,
        disableMenu: !0,
        stopIntervalTime: 5e3,
        clearIntervalWhenDevOpenTrigger: !1,
        detectors: "all",
        clearLog: !0,
        disableSelect: !1,
        disableCopy: !1,
        disableCut: !1,
        disablePaste: !1,
        ignore: null,
        disableIframeParents: !0
    }, ce = ["detectors", "ondevtoolclose", "ignore"];

    function ae(e) {
        var t, n = 0 < arguments.length && void 0 !== e ? e : {};
        for (t in y) {
            var i = t;
            void 0 === n[i] || o(y[i]) !== o(n[i]) && -1 === ce.indexOf(i) || (y[i] = n[i])
        }
        "function" == typeof y.ondevtoolclose && !0 === y.clearIntervalWhenDevOpenTrigger && (y.clearIntervalWhenDevOpenTrigger = !1, console.warn("【DISABLE-DEVTOOL】clearIntervalWhenDevOpenTrigger 在使用 ondevtoolclose 时无效"))
    }

    var b = window.console || {
        log: function () {
        }, table: function () {
        }, clear: function () {
        }
    }, w = v ? function () {
        return b.log.apply(b, arguments)
    } : b.log, le = v ? function () {
        return b.table.apply(b, arguments)
    } : b.table, fe = v ? function () {
        return b.clear()
    } : b.clear;

    function g() {
        y.clearLog && fe()
    }

    var se = function () {
        return !1
    };

    function m(n) {
        var e, i = 74, o = 73, r = 85, u = 83, c = 123, a = N ? function (e, t) {
            return e.metaKey && e.altKey && (t === o || t === i)
        } : function (e, t) {
            return e.ctrlKey && e.shiftKey && (t === o || t === i)
        }, l = N ? function (e, t) {
            return e.metaKey && e.altKey && t === r || e.metaKey && t === u
        } : function (e, t) {
            return e.ctrlKey && (t === u || t === r)
        };
        n.addEventListener("keydown", function (e) {
            var t = (e = e || n.event).keyCode || e.which;
            if (t === c || a(e, t) || l(e, t)) return de(n, e)
        }, !0), e = n, y.disableMenu && T(e, "contextmenu"), e = n, y.disableSelect && T(e, "selectstart"), e = n, y.disableCopy && T(e, "copy"), e = n, y.disableCut && T(e, "cut"), e = n, y.disablePaste && T(e, "paste")
    }

    function T(t, e) {
        t.addEventListener(e, function (e) {
            return de(t, e)
        })
    }

    function de(e, t) {
        if (!ee() && !se()) return (t = t || e.event).returnValue = !1, t.preventDefault(), !1
    }

    var O = 8;

    function ve(e) {
        for (var t = function (e, t) {
            e[t >> 5] |= 128 << t % 32, e[14 + (t + 64 >>> 9 << 4)] = t;
            for (var n = 1732584193, i = -271733879, o = -1732584194, r = 271733878, u = 0; u < e.length; u += 16) {
                var c = n, a = i, l = o, f = r;
                n = S(n, i, o, r, e[u + 0], 7, -680876936), r = S(r, n, i, o, e[u + 1], 12, -389564586), o = S(o, r, n, i, e[u + 2], 17, 606105819), i = S(i, o, r, n, e[u + 3], 22, -1044525330), n = S(n, i, o, r, e[u + 4], 7, -176418897), r = S(r, n, i, o, e[u + 5], 12, 1200080426), o = S(o, r, n, i, e[u + 6], 17, -1473231341), i = S(i, o, r, n, e[u + 7], 22, -45705983), n = S(n, i, o, r, e[u + 8], 7, 1770035416), r = S(r, n, i, o, e[u + 9], 12, -1958414417), o = S(o, r, n, i, e[u + 10], 17, -42063), i = S(i, o, r, n, e[u + 11], 22, -1990404162), n = S(n, i, o, r, e[u + 12], 7, 1804603682), r = S(r, n, i, o, e[u + 13], 12, -40341101), o = S(o, r, n, i, e[u + 14], 17, -1502002290), i = S(i, o, r, n, e[u + 15], 22, 1236535329), n = k(n, i, o, r, e[u + 1], 5, -165796510), r = k(r, n, i, o, e[u + 6], 9, -1069501632), o = k(o, r, n, i, e[u + 11], 14, 643717713), i = k(i, o, r, n, e[u + 0], 20, -373897302), n = k(n, i, o, r, e[u + 5], 5, -701558691), r = k(r, n, i, o, e[u + 10], 9, 38016083), o = k(o, r, n, i, e[u + 15], 14, -660478335), i = k(i, o, r, n, e[u + 4], 20, -405537848), n = k(n, i, o, r, e[u + 9], 5, 568446438), r = k(r, n, i, o, e[u + 14], 9, -1019803690), o = k(o, r, n, i, e[u + 3], 14, -187363961), i = k(i, o, r, n, e[u + 8], 20, 1163531501), n = k(n, i, o, r, e[u + 13], 5, -1444681467), r = k(r, n, i, o, e[u + 2], 9, -51403784), o = k(o, r, n, i, e[u + 7], 14, 1735328473), i = k(i, o, r, n, e[u + 12], 20, -1926607734), n = P(n, i, o, r, e[u + 5], 4, -378558), r = P(r, n, i, o, e[u + 8], 11, -2022574463), o = P(o, r, n, i, e[u + 11], 16, 1839030562), i = P(i, o, r, n, e[u + 14], 23, -35309556), n = P(n, i, o, r, e[u + 1], 4, -1530992060), r = P(r, n, i, o, e[u + 4], 11, 1272893353), o = P(o, r, n, i, e[u + 7], 16, -155497632), i = P(i, o, r, n, e[u + 10], 23, -1094730640), n = P(n, i, o, r, e[u + 13], 4, 681279174), r = P(r, n, i, o, e[u + 0], 11, -358537222), o = P(o, r, n, i, e[u + 3], 16, -722521979), i = P(i, o, r, n, e[u + 6], 23, 76029189), n = P(n, i, o, r, e[u + 9], 4, -640364487), r = P(r, n, i, o, e[u + 12], 11, -421815835), o = P(o, r, n, i, e[u + 15], 16, 530742520), i = P(i, o, r, n, e[u + 2], 23, -995338651), n = I(n, i, o, r, e[u + 0], 6, -198630844), r = I(r, n, i, o, e[u + 7], 10, 1126891415), o = I(o, r, n, i, e[u + 14], 15, -1416354905), i = I(i, o, r, n, e[u + 5], 21, -57434055), n = I(n, i, o, r, e[u + 12], 6, 1700485571), r = I(r, n, i, o, e[u + 3], 10, -1894986606), o = I(o, r, n, i, e[u + 10], 15, -1051523), i = I(i, o, r, n, e[u + 1], 21, -2054922799), n = I(n, i, o, r, e[u + 8], 6, 1873313359), r = I(r, n, i, o, e[u + 15], 10, -30611744), o = I(o, r, n, i, e[u + 6], 15, -1560198380), i = I(i, o, r, n, e[u + 13], 21, 1309151649), n = I(n, i, o, r, e[u + 4], 6, -145523070), r = I(r, n, i, o, e[u + 11], 10, -1120210379), o = I(o, r, n, i, e[u + 2], 15, 718787259), i = I(i, o, r, n, e[u + 9], 21, -343485551), n = j(n, c), i = j(i, a), o = j(o, l), r = j(r, f)
            }
            return Array(n, i, o, r)
        }(function (e) {
            for (var t = Array(), n = (1 << O) - 1, i = 0; i < e.length * O; i += O) t[i >> 5] |= (e.charCodeAt(i / O) & n) << i % 32;
            return t
        }(e), e.length * O), n = "0123456789abcdef", i = "", o = 0; o < 4 * t.length; o++) i += n.charAt(t[o >> 2] >> o % 4 * 8 + 4 & 15) + n.charAt(t[o >> 2] >> o % 4 * 8 & 15);
        return i
    }

    function D(e, t, n, i, o, r) {
        return j((t = j(j(t, e), j(i, r))) << o | t >>> 32 - o, n)
    }

    function S(e, t, n, i, o, r, u) {
        return D(t & n | ~t & i, e, t, o, r, u)
    }

    function k(e, t, n, i, o, r, u) {
        return D(t & i | n & ~i, e, t, o, r, u)
    }

    function P(e, t, n, i, o, r, u) {
        return D(t ^ n ^ i, e, t, o, r, u)
    }

    function I(e, t, n, i, o, r, u) {
        return D(n ^ (t | ~i), e, t, o, r, u)
    }

    function j(e, t) {
        var n = (65535 & e) + (65535 & t);
        return (e >> 16) + (t >> 16) + (n >> 16) << 16 | 65535 & n
    }

    (v = x = x || {})[v.Unknown = -1] = "Unknown", v[v.RegToString = 0] = "RegToString", v[v.DefineId = 1] = "DefineId", v[v.Size = 2] = "Size", v[v.DateToString = 3] = "DateToString", v[v.FuncToString = 4] = "FuncToString", v[v.Debugger = 5] = "Debugger", v[v.Performance = 6] = "Performance", v[v.DebugLib = 7] = "DebugLib";
    var x, A = function () {
        function n(e) {
            var t = e.type, e = e.enabled, e = void 0 === e || e;
            i(this, n), this.type = x.Unknown, this.enabled = !0, this.type = t, this.enabled = e, this.enabled && (t = this, ie.push(t), this.init())
        }

        return u(n, [{
            key: "onDevToolOpen", value: function () {
                var e;
                console.warn("You ar not allow to use DEVTOOL! 【type = ".concat(this.type, "】")), y.clearIntervalWhenDevOpenTrigger && p(), window.clearTimeout(ne), y.ondevtoolopen(this.type, ue), e = this.type, t[e] = !0
            }
        }, {
            key: "init", value: function () {
            }
        }]), n
    }(), v = function () {
        n(t, A);
        var e = l(t);

        function t() {
            return i(this, t), e.call(this, {type: x.RegToString, enabled: X || B})
        }

        return u(t, [{
            key: "init", value: function () {
                var t = this;
                this.lastTime = 0, this.reg = /./, w(this.reg), this.reg.toString = function () {
                    var e;
                    return X ? (e = (new Date).getTime(), t.lastTime && e - t.lastTime < 100 ? t.onDevToolOpen() : t.lastTime = e) : B && t.onDevToolOpen(), ""
                }
            }
        }, {
            key: "detect", value: function () {
                w(this.reg)
            }
        }]), t
    }(), he = function () {
        n(t, A);
        var e = l(t);

        function t() {
            return i(this, t), e.call(this, {type: x.DefineId})
        }

        return u(t, [{
            key: "init", value: function () {
                var e = this;
                this.div = document.createElement("div"), this.div.__defineGetter__("id", function () {
                    e.onDevToolOpen()
                }), Object.defineProperty(this.div, "id", {
                    get: function () {
                        e.onDevToolOpen()
                    }
                })
            }
        }, {
            key: "detect", value: function () {
                w(this.div)
            }
        }]), t
    }(), pe = function () {
        n(t, A);
        var e = l(t);

        function t() {
            return i(this, t), e.call(this, {type: x.Size, enabled: !F && !$})
        }

        return u(t, [{
            key: "init", value: function () {
                var e = this;
                this.checkWindowSizeUneven(), window.addEventListener("resize", function () {
                    setTimeout(function () {
                        e.checkWindowSizeUneven()
                    }, 100)
                }, !0)
            }
        }, {
            key: "detect", value: function () {
            }
        }, {
            key: "checkWindowSizeUneven", value: function () {
                var e = function () {
                    if (ye(window.devicePixelRatio)) return window.devicePixelRatio;
                    var e = window.screen;
                    return !(ye(e) || !e.deviceXDPI || !e.logicalXDPI) && e.deviceXDPI / e.logicalXDPI
                }();
                if (!1 !== e) {
                    var t = 200 < window.outerWidth - window.innerWidth * e,
                        e = 300 < window.outerHeight - window.innerHeight * e;
                    if (t || e) return this.onDevToolOpen(), !1;
                    H(this.type)
                }
                return !0
            }
        }]), t
    }();

    function ye(e) {
        return null != e
    }

    var _, be = function () {
            n(t, A);
            var e = l(t);

            function t() {
                return i(this, t), e.call(this, {type: x.DateToString, enabled: !h})
            }

            return u(t, [{
                key: "init", value: function () {
                    var e = this;
                    this.count = 0, this.date = new Date, this.date.toString = function () {
                        return e.count++, ""
                    }
                }
            }, {
                key: "detect", value: function () {
                    this.count = 0, w(this.date), g(), 2 <= this.count && this.onDevToolOpen()
                }
            }]), t
        }(), we = function () {
            n(t, A);
            var e = l(t);

            function t() {
                return i(this, t), e.call(this, {type: x.FuncToString, enabled: !h && !G})
            }

            return u(t, [{
                key: "init", value: function () {
                    var e = this;
                    this.count = 0, this.func = function () {
                    }, this.func.toString = function () {
                        return e.count++, ""
                    }
                }
            }, {
                key: "detect", value: function () {
                    this.count = 0, w(this.func), g(), 2 <= this.count && this.onDevToolOpen()
                }
            }]), t
        }(), ge = function () {
            n(t, A);
            var e = l(t);

            function t() {
                return i(this, t), e.call(this, {type: x.Debugger, enabled: h || G})
            }

            return u(t, [{
                key: "detect", value: function () {
                    var e = f();
                    100 < f() - e && this.onDevToolOpen()
                }
            }]), t
        }(), me = function () {
            n(t, A);
            var e = l(t);

            function t() {
                return i(this, t), e.call(this, {type: x.Performance, enabled: Y})
            }

            return u(t, [{
                key: "init", value: function () {
                    this.maxPrintTime = 0, this.largeObjectArray = J()
                }
            }, {
                key: "detect", value: function () {
                    var e = this, t = V(function () {
                        le(e.largeObjectArray)
                    }), n = V(function () {
                        w(e.largeObjectArray)
                    });
                    if (this.maxPrintTime = Math.max(this.maxPrintTime, n), g(), 0 === t || 0 === this.maxPrintTime) return !1;
                    t > 10 * this.maxPrintTime && this.onDevToolOpen()
                }
            }]), t
        }(), Te = function () {
            n(t, A);
            var e = l(t);

            function t() {
                return i(this, t), e.call(this, {type: x.DebugLib})
            }

            return u(t, [{
                key: "init", value: function () {
                }
            }, {
                key: "detect", value: function () {
                    var e;
                    (!0 === (null == (e = null == (e = window.eruda) ? void 0 : e._devTools) ? void 0 : e._isShow) || window._vcOrigConsole && window.document.querySelector("#__vconsole.vc-toggle")) && this.onDevToolOpen()
                }
            }]), t
        }(),
        Oe = (e(_ = {}, x.RegToString, v), e(_, x.DefineId, he), e(_, x.Size, pe), e(_, x.DateToString, be), e(_, x.FuncToString, we), e(_, x.Debugger, ge), e(_, x.Performance, me), e(_, x.DebugLib, Te), _);
    var De, E, L, R, C = Object.assign(function (e) {
        if (ae(e), !function () {
            if (y.md5) if (ve(function (e) {
                var t = window.location.search, n = window.location.hash;
                if ("" !== (t = "" === t && "" !== n ? "?".concat(n.split("?")[1]) : t) && void 0 !== t) {
                    n = new RegExp("(^|&)" + e + "=([^&]*)(&|$)", "i"), e = t.substr(1).match(n);
                    if (null != e) return unescape(e[2])
                }
                return ""
            }(y.tkName)) === y.md5) return 1;
            return
        }()) {
            C.isRunning = !0, re(C);
            var t = C, n = (se = function () {
                return t.isSuspend
            }, window.top), i = window.parent;
            if (m(window), y.disableIframeParents && n && i && n !== window) {
                for (; i !== n;) m(i), i = i.parent;
                m(n)
            }
            ("all" === y.detectors ? Object.keys(Oe) : y.detectors).forEach(function (e) {
                new Oe[e]
            })
        }
    }, {isRunning: !1, isSuspend: !1, md5: ve, version: "0.3.2", DetectorType: x, isDevToolOpened: K});
    return "undefined" != typeof document && (De = document.querySelector("[disable-devtool-auto]")) && (E = ["disable-menu", "disable-select", "disable-copy", "disable-cut", "disable-paste", "clear-log"], L = ["interval"], R = {}, ["md5", "url", "tk-name", "detectors"].concat(E, L).forEach(function (e) {
        var t = De.getAttribute(e);
        null !== t && (-1 !== L.indexOf(e) ? t = parseInt(t) : -1 !== E.indexOf(e) ? t = "false" !== t : "detector" === e && "all" !== t && (t = t.split(" ")), R[function (e) {
            if (-1 === e.indexOf("-")) return e;
            var t = !1;
            return e.split("").map(function (e) {
                return "-" === e ? (t = !0, "") : t ? (t = !1, e.toUpperCase()) : e
            }).join("")
        }(e)] = t)
    }), C(R)), C
});