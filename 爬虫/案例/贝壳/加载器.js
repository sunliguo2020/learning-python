const jsdom = require("jsdom");
const {JSDOM} = jsdom;
var dom = new JSDOM(`<!DOCTYPE html><html lang="cn"><head></head><body></body></html>`, {url: 'https://www.zhihu.com/search'});
var window = dom.window;
// var window = global;

var document = window.document;
var navigator = window.navigator
var location = window.location
var history = window.history
var screen = window.screen
var alert = window.alert

var helaoshi;
var laohe;

!function (n) {
    var i = {};

    function r(t) {
        if (i[t])
            return i[t].exports;
        var e = i[t] = {
            i: t,
            l: !1,
            exports: {}
        };
        // console.log("n",n);
        console.log("t", t);

        return n[t].call(e.exports, e, e.exports, r),
            e.l = !0,
            e.exports
    }

    r.m = n,  //r.m 模块列表输出
        r.c = i, // r.c 字典形式模块输出
        r.d = function (t, e, n) {
            r.o(t, e) || Object.defineProperty(t, e, {
                enumerable: !0,
                get: n
            })
        }
        ,
        r.r = function (t) {
            "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(t, Symbol.toStringTag, {
                value: "Module"
            }),
                Object.defineProperty(t, "__esModule", {
                    value: !0
                })
        }
        ,
        r.t = function (e, t) {
            if (1 & t && (e = r(e)),
            8 & t)
                return e;
            if (4 & t && "object" == typeof e && e && e.__esModule)
                return e;
            var n = Object.create(null);
            if (r.r(n),
                Object.defineProperty(n, "default", {
                    enumerable: !0,
                    value: e
                }),
            2 & t && "string" != typeof e)
                for (var i in e)
                    r.d(n, i, function (t) {
                        return e[t]
                    }
                        .bind(null, i));
            return n
        }
        ,
        r.n = function (t) {
            var e = t && t.__esModule ? function () {
                        return t.default
                    }
                    : function () {
                        return t
                    }
            ;
            return r.d(e, "a", e),
                e
        }
        ,
        r.o = function (t, e) {
            return Object.prototype.hasOwnProperty.call(t, e)
        }
        ,
        r.p = "/",
        // r(r.s = 21) //加载器执行
        laohe = r;
}({
    62: function (t, e, n) {
        "use strict";
        n.r(e);

        function i(t) {
            var o = this;
            this.refreshTicket = function () {
                o.getTicket(),
                o.interval && clearInterval(o.interval),
                    o.interval = setInterval(function () {
                        o.getTicket()
                    }, 6e5)
            }
                ,
                this.getTicket = function () {
                    var t = {
                        service: o.service,
                        version: o.serviceVersion
                    };
                    return new Promise(function (r) {
                            Object(u.fetch)({
                                url: "" + o.domain + l.APIEndpoint.init,
                                method: "POST",
                                data: t
                            }).then(function (t) {
                                var e = null;
                                if (t.data.success) {
                                    var n = t.data.publicKey.key;
                                    o.ec.setPublicKey(n),
                                        o.loginTicketId = t.data.loginTicketId,
                                        o.publicKey = n,
                                        o.encodeVersion = t.data.publicKey.version;
                                    var i = t.data.authenticationMethods.customer.filter(function (t) {
                                        return "qrcode" === t.type
                                    });
                                    0 < i.length && (e = i[0].initialOptions)
                                } else
                                    Object(c.sendFee)({
                                        detail: t,
                                        errorName: "passport-init-error"
                                    });
                                r(e)
                            })
                        }
                    )
                }
                ,
                this.getRiskInfo = function (t) {
                    var e = {
                        name: "",
                        version: ""
                    }
                        , n = "";
                    try {
                        var i = new s.a;
                        e = i.getOS(),
                            n = i.getUA()
                    } catch (t) {
                        Object(c.sendFee)({
                            detail: {
                                error: t
                            },
                            errorName: "ua-parser-error"
                        })
                    }
                    var r = {
                        ua: n,
                        clientSource: "pc",
                        os: e.name,
                        osVersion: e.version
                    };
                    return Object.assign({}, r, t)
                }
                ,
                this.passwordLogin = function (t, e) {
                    t.encodeVersion = o.encodeVersion;
                    var n = {};
                    e && (n = o.getRiskInfo(Object.assign({}, e.clickPos, e.riskData))),
                    o.publicKey && (t.password = o.ec.encrypt(t.password));
                    var i = {
                        service: o.service,
                        mainAuthMethodName: l.mainAuthMethodName.PASSWORD,
                        accountSystem: o.accountSystem,
                        credential: t,
                        context: Object.assign({}, n),
                        loginTicketId: o.loginTicketId,
                        version: o.serviceVersion
                    };
                    return window.srcId && (i.srcId = window.srcId),
                    t.code && (i.mfaAuthMethodName = l.allianceMethods.security),
                    e.ticketMaxAge && (i.ticketMaxAge = e.ticketMaxAge),
                        new Promise(function (e, n) {
                                Object(u.fetch)({
                                    url: "" + o.domain + l.APIEndpoint.auth,
                                    method: "POST",
                                    data: i
                                }).then(function (t) {
                                    e(t),
                                        o.sign = t.data.sign,
                                        o.tgt = t.data.serviceTicket.id
                                }).catch(function (t) {
                                    Object(c.sendFee)({
                                        detail: {
                                            error: t,
                                            data: i
                                        },
                                        errorName: "passport-auth-error"
                                    }),
                                        n(t)
                                })
                            }
                        )
                }
                ,
                this.smsLogin = function (t, e) {
                    var n = {};
                    e && (n = o.getRiskInfo(Object.assign({}, e.clickPos, e.riskData)));
                    var i = {
                        service: o.service,
                        mainAuthMethodName: l.mainAuthMethodName.PHONE,
                        mfaAuthMethodName: l.allianceMethods.security,
                        accountSystem: o.accountSystem,
                        credential: t,
                        context: Object.assign({}, n),
                        loginTicketId: o.loginTicketId,
                        version: o.serviceVersion
                    };
                    return window.srcId && (i.srcId = window.srcId),
                    e.ticketMaxAge && (i.ticketMaxAge = e.ticketMaxAge),
                        new Promise(function (e, n) {
                                Object(u.fetch)({
                                    url: "" + o.domain + l.APIEndpoint.auth,
                                    method: "POST",
                                    data: i
                                }).then(function (t) {
                                    e(t),
                                        o.sign = t.data.sign,
                                        o.tgt = t.data.serviceTicket.id
                                }).catch(function (t) {
                                    Object(c.sendFee)({
                                        detail: {
                                            error: t,
                                            data: i
                                        },
                                        errorName: "passport-smslogin-error"
                                    }),
                                        n(t)
                                })
                            }
                        )
                }
                ,
                this.qrLogin = function (t, e) {
                    var n = {};
                    e && (n = o.getRiskInfo(Object.assign({}, e.riskData)));
                    var i = {
                        service: o.service,
                        mainAuthMethodName: l.mainAuthMethodName.QR,
                        accountSystem: o.accountSystem,
                        credential: t,
                        context: Object.assign({}, n),
                        loginTicketId: o.loginTicketId,
                        version: o.serviceVersion
                    };
                    return window.srcId && (i.srcId = window.srcId),
                        new Promise(function (e, n) {
                                Object(u.fetch)({
                                    url: "" + o.domain + l.APIEndpoint.auth,
                                    method: "POST",
                                    data: i
                                }).then(function (t) {
                                    e(t),
                                        o.sign = t.data.sign,
                                        o.tgt = t.data.serviceTicket.id
                                }).catch(function (t) {
                                    Object(c.sendFee)({
                                        detail: {
                                            error: t,
                                            data: i
                                        },
                                        errorName: "passport-qrlogin-error"
                                    }),
                                        n(t)
                                })
                            }
                        )
                }
                ,
                this.register = function (t, e) {
                    t.encodeVersion = o.encodeVersion;
                    var n = {};
                    e.clickPos && (n = o.getRiskInfo(Object.assign({}, e.clickPos))),
                    o.publicKey && (t.password = o.ec.encrypt(t.password));
                    var i = {
                        service: o.service,
                        accountSystem: o.accountSystem,
                        context: Object.assign({}, n),
                        displayName: Object(u.maskPhoneNumber)(t.phoneNum),
                        registerMethodName: "security-code",
                        credential: t
                    };
                    return window.srcId && (i.srcId = window.srcId),
                        new Promise(function (e, n) {
                                Object(u.fetch)({
                                    url: "" + o.domain + l.APIEndpoint.register,
                                    method: "POST",
                                    data: i
                                }).then(function (t) {
                                    e(t)
                                }).catch(function (t) {
                                    Object(c.sendFee)({
                                        detail: {
                                            error: t,
                                            data: i
                                        },
                                        errorName: "passport-register-error"
                                    }),
                                        n(t)
                                })
                            }
                        )
                }
                ,
                this.sendSMS = function (t, e) {
                    t.ticketId = o.loginTicketId,
                        t.captchaScene = l.scene,
                        t.captchaToken = o.captcha.token;
                    var n = {
                        accountSystem: o.accountSystem,
                        smsType: l.smsTypeEnum.sms,
                        sceneKey: e || l.SceneKey.WHEN_LOGIN,
                        credential: t,
                        context: {},
                        version: o.serviceVersion,
                        service: o.service
                    };
                    return o.smsService && (n.service = o.smsService),
                        new Promise(function (t, e) {
                                Object(u.fetch)({
                                    url: "" + o.domain + l.APIEndpoint.sms,
                                    method: "POST",
                                    data: n
                                }).then(t).catch(function (t) {
                                    Object(c.sendFee)({
                                        detail: {
                                            error: t,
                                            data: n
                                        },
                                        errorName: "passport-sendSMS-error"
                                    }),
                                        e(t)
                                })
                            }
                        )
                }
                ,
                this.sendVoice = function (t, e) {
                    t.ticketId = o.loginTicketId;
                    var n = {
                        accountSystem: o.accountSystem,
                        smsType: l.smsTypeEnum.voice,
                        sceneKey: e || l.SceneKey.WHEN_LOGIN,
                        credential: t,
                        context: {},
                        version: o.serviceVersion
                    };
                    return new Promise(function (t, e) {
                            Object(u.fetch)({
                                url: "" + o.domain + l.APIEndpoint.sms,
                                method: "POST",
                                data: n
                            }).then(t).catch(function (t) {
                                Object(c.sendFee)({
                                    detail: {
                                        error: t,
                                        data: n
                                    },
                                    errorName: "passport-sendVoice-error"
                                }),
                                    e(t)
                            })
                        }
                    )
                }
                ,
                this.setCaptcha = function (e) {
                    return h(o, void 0, void 0, function () {
                        return d(this, function (t) {
                            switch (t.label) {
                                case 0:
                                    return [4, this.captcha.add(e)];
                                case 1:
                                    return t.sent(),
                                        [2]
                            }
                        })
                    })
                }
                ,
                this.removeCaptcha = function () {
                    return h(o, void 0, void 0, function () {
                        return d(this, function (t) {
                            switch (t.label) {
                                case 0:
                                    return [4, this.captcha.remove()];
                                case 1:
                                    return t.sent(),
                                        [2]
                            }
                        })
                    })
                }
                ,
                this.getUserInfo = function (r) {
                    return h(o, void 0, void 0, function () {
                        var i = this;
                        return d(this, function (t) {
                            return [2, new Promise(function (e, n) {
                                    Object(u.fetch)({
                                        url: "" + i.domain + l.APIEndpoint.getinfo,
                                        method: "GET",
                                        params: {
                                            service: i.service,
                                            ticket: r.data.serviceTicket.id
                                        }
                                    }).then(function (t) {
                                        e(t)
                                    }).catch(function (t) {
                                        Object(c.sendFee)({
                                            detail: {
                                                error: t,
                                                data: {
                                                    service: i.service,
                                                    ticket: r.data.serviceTicket.id
                                                }
                                            },
                                            errorName: "passport-getUserInfo-error"
                                        }),
                                            n(t)
                                    })
                                }
                            )]
                        })
                    })
                }
                ,
                this.logout = function (i) {
                    return new Promise(function (e, n) {
                            Object(u.fetch)({
                                url: "" + o.domain + l.APIEndpoint.logout,
                                method: "POST",
                                data: {
                                    context: {
                                        sign: i && i.context && i.context.sign ? i.context.sign : o.sign
                                    },
                                    tgt: i && i.tgt ? i.tgt : o.tgt
                                }
                            }).then(function (t) {
                                e(t)
                            }).catch(function (t) {
                                Object(c.sendFee)({
                                    detail: {
                                        error: t,
                                        data: {
                                            service: o.service,
                                            tgt: i && i.tgt ? i.tgt : o.tgt
                                        }
                                    },
                                    errorName: "passport-logout-error"
                                }),
                                    n(t)
                            })
                        }
                    )
                }
                ,
                this.destroy = function () {
                    clearInterval(o.interval),
                        o.interval = void 0
                }
                ,
                this.createQr = function (t) {
                    return void 0 === t && (t = {
                        type: "wx_official_account",
                        sceneId: 0,
                        sceneStr: ""
                    }),
                        new Promise(function (e, n) {
                                Object(u.fetch)({
                                    url: "" + o.domain + l.APIEndpoint.qr,
                                    method: "POST",
                                    data: {
                                        service: o.service,
                                        type: t.type,
                                        data: {
                                            sceneId: t.sceneId,
                                            sceneStr: t.sceneStr
                                        }
                                    }
                                }).then(function (t) {
                                    e(t)
                                }).catch(function (t) {
                                    n(t)
                                })
                            }
                        )
                }
                ,
                this.pollingQr = function (t) {
                    return new Promise(function (e, n) {
                            Object(u.fetch)({
                                url: "" + o.domain + l.APIEndpoint.polling,
                                method: "GET",
                                params: t
                            }).then(function (t) {
                                e(t)
                            }).catch(function (t) {
                                n(t)
                            })
                        }
                    )
                }
                ,
                this.pollingQrForCustomer = function (t) {
                    return new Promise(function (e, n) {
                            Object(u.fetch)({
                                url: "" + o.domain + l.APIEndpoint.pollingCustomer,
                                method: "GET",
                                params: t
                            }).then(function (t) {
                                e(t)
                            }).catch(function (t) {
                                n(t)
                            })
                        }
                    )
                }
                ,
                this.ec = new a.a,
                laohe = this,
                this.service = t.service,
                this.smsService = t.smsService,
                this.serviceVersion = t.version,
                this.qrCodeOptions = {
                    id: "",
                    qrCodeContent: ""
                },
                this.loginTicketId = "",
                this.publicKey = "",
                this.encodeVersion = "",
                this.sign = "",
                this.tgt = "",
                this.env = t.env,
                this.accountSystem = l.accountSystem.customer,
                this.domain = l.APIDomainKe[t.env],
            "lianjia" === u.plat && (this.domain = l.APIDomainLianjia[t.env]),
                this.captcha = t.captchaInstance,
            this.service && this.env && this.serviceVersion && this.refreshTicket()
        }

        var r = n(6)
            , a = n.n(r)
            , o = n(20)
            , s = n.n(o)
            , c = n(2)
            , l = n(0)
            , u = n(1)
            , h = function (t, a, s, c) {
            return new (s = s || Promise)(function (e, n) {
                    function i(t) {
                        try {
                            o(c.next(t))
                        } catch (t) {
                            n(t)
                        }
                    }

                    function r(t) {
                        try {
                            o(c.throw(t))
                        } catch (t) {
                            n(t)
                        }
                    }

                    function o(t) {
                        t.done ? e(t.value) : function (e) {
                            return e instanceof s ? e : new s(function (t) {
                                    t(e)
                                }
                            )
                        }(t.value).then(i, r)
                    }

                    o((c = c.apply(t, a || [])).next())
                }
            )
        }
            , d = function (n, i) {
            var r, o, a, t, s = {
                label: 0,
                sent: function () {
                    if (1 & a[0])
                        throw a[1];
                    return a[1]
                },
                trys: [],
                ops: []
            };
            return t = {
                next: e(0),
                throw: e(1),
                return: e(2)
            },
            "function" == typeof Symbol && (t[Symbol.iterator] = function () {
                    return this
                }
            ),
                t;

            function e(e) {
                return function (t) {
                    return function (e) {
                        if (r)
                            throw new TypeError("Generator is already executing.");
                        for (; s;)
                            try {
                                if (r = 1,
                                o && (a = 2 & e[0] ? o.return : e[0] ? o.throw || ((a = o.return) && a.call(o),
                                    0) : o.next) && !(a = a.call(o, e[1])).done)
                                    return a;
                                switch (o = 0,
                                a && (e = [2 & e[0], a.value]),
                                    e[0]) {
                                    case 0:
                                    case 1:
                                        a = e;
                                        break;
                                    case 4:
                                        return s.label++,
                                            {
                                                value: e[1],
                                                done: !1
                                            };
                                    case 5:
                                        s.label++,
                                            o = e[1],
                                            e = [0];
                                        continue;
                                    case 7:
                                        e = s.ops.pop(),
                                            s.trys.pop();
                                        continue;
                                    default:
                                        if (!(a = 0 < (a = s.trys).length && a[a.length - 1]) && (6 === e[0] || 2 === e[0])) {
                                            s = 0;
                                            continue
                                        }
                                        if (3 === e[0] && (!a || e[1] > a[0] && e[1] < a[3])) {
                                            s.label = e[1];
                                            break
                                        }
                                        if (6 === e[0] && s.label < a[1]) {
                                            s.label = a[1],
                                                a = e;
                                            break
                                        }
                                        if (a && s.label < a[2]) {
                                            s.label = a[2],
                                                s.ops.push(e);
                                            break
                                        }
                                        a[2] && s.ops.pop(),
                                            s.trys.pop();
                                        continue
                                }
                                e = i.call(n, s)
                            } catch (t) {
                                e = [6, t],
                                    o = 0
                            } finally {
                                r = a = 0
                            }
                        if (5 & e[0])
                            throw e[1];
                        return {
                            value: e[0] ? e[1] : void 0,
                            done: !0
                        }
                    }([e, t])
                }
            }
        };
        e.default = i
    },
    6: function (t, e, n) {
        !function (t) {
            "use strict";
            var e = "0123456789abcdefghijklmnopqrstuvwxyz";

            function c(t) {
                return e.charAt(t)
            }

            function n(t, e) {
                return t & e
            }

            function l(t, e) {
                return t | e
            }

            function i(t, e) {
                return t ^ e
            }

            function r(t, e) {
                return t & ~e
            }

            function o(t) {
                if (0 == t)
                    return -1;
                var e = 0;
                return 0 == (65535 & t) && (t >>= 16,
                    e += 16),
                0 == (255 & t) && (t >>= 8,
                    e += 8),
                0 == (15 & t) && (t >>= 4,
                    e += 4),
                0 == (3 & t) && (t >>= 2,
                    e += 2),
                0 == (1 & t) && ++e,
                    e
            }

            function a(t) {
                for (var e = 0; 0 != t;)
                    t &= t - 1,
                        ++e;
                return e
            }

            var s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

            function u(t) {
                var e, n, i = "";
                for (e = 0; e + 3 <= t.length; e += 3)
                    n = parseInt(t.substring(e, e + 3), 16),
                        i += s.charAt(n >> 6) + s.charAt(63 & n);
                for (e + 1 == t.length ? (n = parseInt(t.substring(e, e + 1), 16),
                    i += s.charAt(n << 2)) : e + 2 == t.length && (n = parseInt(t.substring(e, e + 2), 16),
                    i += s.charAt(n >> 2) + s.charAt((3 & n) << 4)); 0 < (3 & i.length);)
                    i += "=";
                return i
            }

            function h(t) {
                var e, n = "", i = 0, r = 0;
                for (e = 0; e < t.length && "=" != t.charAt(e); ++e) {
                    var o = s.indexOf(t.charAt(e));
                    o < 0 || (i = 0 == i ? (n += c(o >> 2),
                        r = 3 & o,
                        1) : 1 == i ? (n += c(r << 2 | o >> 4),
                        r = 15 & o,
                        2) : 2 == i ? (n += c(r),
                        n += c(o >> 2),
                        r = 3 & o,
                        3) : (n += c(r << 2 | o >> 4),
                        n += c(15 & o),
                        0))
                }
                return 1 == i && (n += c(r << 2)),
                    n
            }

            var d, f = function (t, e) {
                return (f = Object.setPrototypeOf || {
                            __proto__: []
                        } instanceof Array && function (t, e) {
                            t.__proto__ = e
                        }
                        || function (t, e) {
                            for (var n in e)
                                e.hasOwnProperty(n) && (t[n] = e[n])
                        }
                )(t, e)
            };
            var p, g = {
                    decode: function (t) {
                        var e;
                        if (void 0 === d) {
                            var n = "0123456789ABCDEF"
                                , i = " \f\n\r\t \u2028\u2029";
                            for (d = {},
                                     e = 0; e < 16; ++e)
                                d[n.charAt(e)] = e;
                            for (n = n.toLowerCase(),
                                     e = 10; e < 16; ++e)
                                d[n.charAt(e)] = e;
                            for (e = 0; e < i.length; ++e)
                                d[i.charAt(e)] = -1
                        }
                        var r = []
                            , o = 0
                            , a = 0;
                        for (e = 0; e < t.length; ++e) {
                            var s = t.charAt(e);
                            if ("=" == s)
                                break;
                            if (-1 != (s = d[s])) {
                                if (void 0 === s)
                                    throw new Error("Illegal character at offset " + e);
                                o |= s,
                                    2 <= ++a ? (r[r.length] = o,
                                        a = o = 0) : o <<= 4
                            }
                        }
                        if (a)
                            throw new Error("Hex encoding incomplete: 4 bits missing");
                        return r
                    }
                }, m = {
                    decode: function (t) {
                        var e;
                        if (void 0 === p) {
                            var n = "= \f\n\r\t \u2028\u2029";
                            for (p = Object.create(null),
                                     e = 0; e < 64; ++e)
                                p["ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charAt(e)] = e;
                            for (e = 0; e < n.length; ++e)
                                p[n.charAt(e)] = -1
                        }
                        var i = []
                            , r = 0
                            , o = 0;
                        for (e = 0; e < t.length; ++e) {
                            var a = t.charAt(e);
                            if ("=" == a)
                                break;
                            if (-1 != (a = p[a])) {
                                if (void 0 === a)
                                    throw new Error("Illegal character at offset " + e);
                                r |= a,
                                    4 <= ++o ? (i[i.length] = r >> 16,
                                        i[i.length] = r >> 8 & 255,
                                        i[i.length] = 255 & r,
                                        o = r = 0) : r <<= 6
                            }
                        }
                        switch (o) {
                            case 1:
                                throw new Error("Base64 encoding incomplete: at least 2 bits missing");
                            case 2:
                                i[i.length] = r >> 10;
                                break;
                            case 3:
                                i[i.length] = r >> 16,
                                    i[i.length] = r >> 8 & 255
                        }
                        return i
                    },
                    re: /-----BEGIN [^-]+-----([A-Za-z0-9+\/=\s]+)-----END [^-]+-----|begin-base64[^\n]+\n([A-Za-z0-9+\/=\s]+)====/,
                    unarmor: function (t) {
                        var e = m.re.exec(t);
                        if (e)
                            if (e[1])
                                t = e[1];
                            else {
                                if (!e[2])
                                    throw new Error("RegExp out of sync");
                                t = e[2]
                            }
                        return m.decode(t)
                    }
                }, v = 1e13, y = function () {
                    function t(t) {
                        this.buf = [+t || 0]
                    }

                    return t.prototype.mulAdd = function (t, e) {
                        var n, i, r = this.buf, o = r.length;
                        for (n = 0; n < o; ++n)
                            (i = r[n] * t + e) < v ? e = 0 : i -= (e = 0 | i / v) * v,
                                r[n] = i;
                        0 < e && (r[n] = e)
                    }
                        ,
                        t.prototype.sub = function (t) {
                            var e, n, i = this.buf, r = i.length;
                            for (e = 0; e < r; ++e)
                                n = i[e] - t,
                                    t = n < 0 ? (n += v,
                                        1) : 0,
                                    i[e] = n;
                            for (; 0 === i[i.length - 1];)
                                i.pop()
                        }
                        ,
                        t.prototype.toString = function (t) {
                            if (10 != (t || 10))
                                throw new Error("only base 10 is supported");
                            for (var e = this.buf, n = e[e.length - 1].toString(), i = e.length - 2; 0 <= i; --i)
                                n += (v + e[i]).toString().substring(1);
                            return n
                        }
                        ,
                        t.prototype.valueOf = function () {
                            for (var t = this.buf, e = 0, n = t.length - 1; 0 <= n; --n)
                                e = e * v + t[n];
                            return e
                        }
                        ,
                        t.prototype.simplify = function () {
                            var t = this.buf;
                            return 1 == t.length ? t[0] : this
                        }
                        ,
                        t
                }(), b = "…",
                w = /^(\d\d)(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])([01]\d|2[0-3])(?:([0-5]\d)(?:([0-5]\d)(?:[.,](\d{1,3}))?)?)?(Z|[-+](?:[0]\d|1[0-2])([0-5]\d)?)?$/,
                _ = /^(\d\d\d\d)(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])([01]\d|2[0-3])(?:([0-5]\d)(?:([0-5]\d)(?:[.,](\d{1,3}))?)?)?(Z|[-+](?:[0]\d|1[0-2])([0-5]\d)?)?$/;

            function x(t, e) {
                return t.length > e && (t = t.substring(0, e) + b),
                    t
            }

            var T, D = function () {
                    function n(t, e) {
                        this.hexDigits = "0123456789ABCDEF",
                            t instanceof n ? (this.enc = t.enc,
                                this.pos = t.pos) : (this.enc = t,
                                this.pos = e)
                    }

                    return n.prototype.get = function (t) {
                        if (void 0 === t && (t = this.pos++),
                        t >= this.enc.length)
                            throw new Error("Requesting byte offset " + t + " on a stream of length " + this.enc.length);
                        return "string" == typeof this.enc ? this.enc.charCodeAt(t) : this.enc[t]
                    }
                        ,
                        n.prototype.hexByte = function (t) {
                            return this.hexDigits.charAt(t >> 4 & 15) + this.hexDigits.charAt(15 & t)
                        }
                        ,
                        n.prototype.hexDump = function (t, e, n) {
                            for (var i = "", r = t; r < e; ++r)
                                if (i += this.hexByte(this.get(r)),
                                !0 !== n)
                                    switch (15 & r) {
                                        case 7:
                                            i += "  ";
                                            break;
                                        case 15:
                                            i += "\n";
                                            break;
                                        default:
                                            i += " "
                                    }
                            return i
                        }
                        ,
                        n.prototype.isASCII = function (t, e) {
                            for (var n = t; n < e; ++n) {
                                var i = this.get(n);
                                if (i < 32 || 176 < i)
                                    return !1
                            }
                            return !0
                        }
                        ,
                        n.prototype.parseStringISO = function (t, e) {
                            for (var n = "", i = t; i < e; ++i)
                                n += String.fromCharCode(this.get(i));
                            return n
                        }
                        ,
                        n.prototype.parseStringUTF = function (t, e) {
                            for (var n = "", i = t; i < e;) {
                                var r = this.get(i++);
                                n += r < 128 ? String.fromCharCode(r) : 191 < r && r < 224 ? String.fromCharCode((31 & r) << 6 | 63 & this.get(i++)) : String.fromCharCode((15 & r) << 12 | (63 & this.get(i++)) << 6 | 63 & this.get(i++))
                            }
                            return n
                        }
                        ,
                        n.prototype.parseStringBMP = function (t, e) {
                            for (var n, i, r = "", o = t; o < e;)
                                n = this.get(o++),
                                    i = this.get(o++),
                                    r += String.fromCharCode(n << 8 | i);
                            return r
                        }
                        ,
                        n.prototype.parseTime = function (t, e, n) {
                            var i = this.parseStringISO(t, e)
                                , r = (n ? w : _).exec(i);
                            return r ? (n && (r[1] = +r[1],
                                r[1] += +r[1] < 70 ? 2e3 : 1900),
                                i = r[1] + "-" + r[2] + "-" + r[3] + " " + r[4],
                            r[5] && (i += ":" + r[5],
                            r[6] && (i += ":" + r[6],
                            r[7] && (i += "." + r[7]))),
                            r[8] && (i += " UTC",
                            "Z" != r[8] && (i += r[8],
                            r[9] && (i += ":" + r[9]))),
                                i) : "Unrecognized time: " + i
                        }
                        ,
                        n.prototype.parseInteger = function (t, e) {
                            for (var n, i = this.get(t), r = 127 < i, o = r ? 255 : 0, a = ""; i == o && ++t < e;)
                                i = this.get(t);
                            if (0 === (n = e - t))
                                return r ? -1 : 0;
                            if (4 < n) {
                                for (a = i,
                                         n <<= 3; 0 == (128 & (+a ^ o));)
                                    a = +a << 1,
                                        --n;
                                a = "(" + n + " bit)\n"
                            }
                            r && (i -= 256);
                            for (var s = new y(i), c = t + 1; c < e; ++c)
                                s.mulAdd(256, this.get(c));
                            return a + s.toString()
                        }
                        ,
                        n.prototype.parseBitString = function (t, e, n) {
                            for (var i = this.get(t), r = (e - t - 1 << 3) - i, o = "(" + r + " bit)\n", a = "", s = t + 1; s < e; ++s) {
                                for (var c = this.get(s), l = s == e - 1 ? i : 0, u = 7; l <= u; --u)
                                    a += c >> u & 1 ? "1" : "0";
                                if (a.length > n)
                                    return o + x(a, n)
                            }
                            return o + a
                        }
                        ,
                        n.prototype.parseOctetString = function (t, e, n) {
                            if (this.isASCII(t, e))
                                return x(this.parseStringISO(t, e), n);
                            var i = e - t
                                , r = "(" + i + " byte)\n";
                            (n /= 2) < i && (e = t + n);
                            for (var o = t; o < e; ++o)
                                r += this.hexByte(this.get(o));
                            return n < i && (r += b),
                                r
                        }
                        ,
                        n.prototype.parseOID = function (t, e, n) {
                            for (var i = "", r = new y, o = 0, a = t; a < e; ++a) {
                                var s = this.get(a);
                                if (r.mulAdd(128, 127 & s),
                                    o += 7,
                                    !(128 & s)) {
                                    if ("" === i)
                                        if ((r = r.simplify()) instanceof y)
                                            r.sub(80),
                                                i = "2." + r.toString();
                                        else {
                                            var c = r < 80 ? r < 40 ? 0 : 1 : 2;
                                            i = c + "." + (r - 40 * c)
                                        }
                                    else
                                        i += "." + r.toString();
                                    if (i.length > n)
                                        return x(i, n);
                                    r = new y,
                                        o = 0
                                }
                            }
                            return 0 < o && (i += ".incomplete"),
                                i
                        }
                        ,
                        n
                }(), E = function () {
                    function u(t, e, n, i, r) {
                        if (!(i instanceof S))
                            throw new Error("Invalid tag value.");
                        this.stream = t,
                            this.header = e,
                            this.length = n,
                            this.tag = i,
                            this.sub = r
                    }

                    return u.prototype.typeName = function () {
                        switch (this.tag.tagClass) {
                            case 0:
                                switch (this.tag.tagNumber) {
                                    case 0:
                                        return "EOC";
                                    case 1:
                                        return "BOOLEAN";
                                    case 2:
                                        return "INTEGER";
                                    case 3:
                                        return "BIT_STRING";
                                    case 4:
                                        return "OCTET_STRING";
                                    case 5:
                                        return "NULL";
                                    case 6:
                                        return "OBJECT_IDENTIFIER";
                                    case 7:
                                        return "ObjectDescriptor";
                                    case 8:
                                        return "EXTERNAL";
                                    case 9:
                                        return "REAL";
                                    case 10:
                                        return "ENUMERATED";
                                    case 11:
                                        return "EMBEDDED_PDV";
                                    case 12:
                                        return "UTF8String";
                                    case 16:
                                        return "SEQUENCE";
                                    case 17:
                                        return "SET";
                                    case 18:
                                        return "NumericString";
                                    case 19:
                                        return "PrintableString";
                                    case 20:
                                        return "TeletexString";
                                    case 21:
                                        return "VideotexString";
                                    case 22:
                                        return "IA5String";
                                    case 23:
                                        return "UTCTime";
                                    case 24:
                                        return "GeneralizedTime";
                                    case 25:
                                        return "GraphicString";
                                    case 26:
                                        return "VisibleString";
                                    case 27:
                                        return "GeneralString";
                                    case 28:
                                        return "UniversalString";
                                    case 30:
                                        return "BMPString"
                                }
                                return "Universal_" + this.tag.tagNumber.toString();
                            case 1:
                                return "Application_" + this.tag.tagNumber.toString();
                            case 2:
                                return "[" + this.tag.tagNumber.toString() + "]";
                            case 3:
                                return "Private_" + this.tag.tagNumber.toString()
                        }
                    }
                        ,
                        u.prototype.content = function (t) {
                            if (void 0 === this.tag)
                                return null;
                            void 0 === t && (t = 1 / 0);
                            var e = this.posContent()
                                , n = Math.abs(this.length);
                            if (!this.tag.isUniversal())
                                return null !== this.sub ? "(" + this.sub.length + " elem)" : this.stream.parseOctetString(e, e + n, t);
                            switch (this.tag.tagNumber) {
                                case 1:
                                    return 0 === this.stream.get(e) ? "false" : "true";
                                case 2:
                                    return this.stream.parseInteger(e, e + n);
                                case 3:
                                    return this.sub ? "(" + this.sub.length + " elem)" : this.stream.parseBitString(e, e + n, t);
                                case 4:
                                    return this.sub ? "(" + this.sub.length + " elem)" : this.stream.parseOctetString(e, e + n, t);
                                case 6:
                                    return this.stream.parseOID(e, e + n, t);
                                case 16:
                                case 17:
                                    return null !== this.sub ? "(" + this.sub.length + " elem)" : "(no elem)";
                                case 12:
                                    return x(this.stream.parseStringUTF(e, e + n), t);
                                case 18:
                                case 19:
                                case 20:
                                case 21:
                                case 22:
                                case 26:
                                    return x(this.stream.parseStringISO(e, e + n), t);
                                case 30:
                                    return x(this.stream.parseStringBMP(e, e + n), t);
                                case 23:
                                case 24:
                                    return this.stream.parseTime(e, e + n, 23 == this.tag.tagNumber)
                            }
                            return null
                        }
                        ,
                        u.prototype.toString = function () {
                            return this.typeName() + "@" + this.stream.pos + "[header:" + this.header + ",length:" + this.length + ",sub:" + (null === this.sub ? "null" : this.sub.length) + "]"
                        }
                        ,
                        u.prototype.toPrettyString = function (t) {
                            void 0 === t && (t = "");
                            var e = t + this.typeName() + " @" + this.stream.pos;
                            if (0 <= this.length && (e += "+"),
                                e += this.length,
                                this.tag.tagConstructed ? e += " (constructed)" : !this.tag.isUniversal() || 3 != this.tag.tagNumber && 4 != this.tag.tagNumber || null === this.sub || (e += " (encapsulates)"),
                                e += "\n",
                            null !== this.sub) {
                                t += "  ";
                                for (var n = 0, i = this.sub.length; n < i; ++n)
                                    e += this.sub[n].toPrettyString(t)
                            }
                            return e
                        }
                        ,
                        u.prototype.posStart = function () {
                            return this.stream.pos
                        }
                        ,
                        u.prototype.posContent = function () {
                            return this.stream.pos + this.header
                        }
                        ,
                        u.prototype.posEnd = function () {
                            return this.stream.pos + this.header + Math.abs(this.length)
                        }
                        ,
                        u.prototype.toHexString = function () {
                            return this.stream.hexDump(this.posStart(), this.posEnd(), !0)
                        }
                        ,
                        u.decodeLength = function (t) {
                            var e = t.get()
                                , n = 127 & e;
                            if (n == e)
                                return n;
                            if (6 < n)
                                throw new Error("Length over 48 bits not supported at position " + (t.pos - 1));
                            if (0 == n)
                                return null;
                            for (var i = e = 0; i < n; ++i)
                                e = 256 * e + t.get();
                            return e
                        }
                        ,
                        u.prototype.getHexStringValue = function () {
                            var t = this.toHexString()
                                , e = 2 * this.header
                                , n = 2 * this.length;
                            return t.substr(e, n)
                        }
                        ,
                        u.decode = function (t) {
                            var i;
                            i = t instanceof D ? t : new D(t, 0);
                            var e = new D(i)
                                , n = new S(i)
                                , r = u.decodeLength(i)
                                , o = i.pos
                                , a = o - e.pos
                                , s = null
                                , c = function () {
                                var t = [];
                                if (null !== r) {
                                    for (var e = o + r; i.pos < e;)
                                        t[t.length] = u.decode(i);
                                    if (i.pos != e)
                                        throw new Error("Content size is not correct for container starting at offset " + o)
                                } else
                                    try {
                                        for (; ;) {
                                            var n = u.decode(i);
                                            if (n.tag.isEOC())
                                                break;
                                            t[t.length] = n
                                        }
                                        r = o - i.pos
                                    } catch (t) {
                                        throw new Error("Exception while decoding undefined length content: " + t)
                                    }
                                return t
                            };
                            if (n.tagConstructed)
                                s = c();
                            else if (n.isUniversal() && (3 == n.tagNumber || 4 == n.tagNumber))
                                try {
                                    if (3 == n.tagNumber && 0 != i.get())
                                        throw new Error("BIT STRINGs with unused bits cannot encapsulate.");
                                    s = c();
                                    for (var l = 0; l < s.length; ++l)
                                        if (s[l].tag.isEOC())
                                            throw new Error("EOC is not supposed to be actual content.")
                                } catch (t) {
                                    s = null
                                }
                            if (null === s) {
                                if (null === r)
                                    throw new Error("We can't skip over an invalid tag with undefined length at offset " + o);
                                i.pos = o + Math.abs(r)
                            }
                            return new u(e, a, r, n, s)
                        }
                        ,
                        u
                }(), S = function () {
                    function t(t) {
                        var e = t.get();
                        if (this.tagClass = e >> 6,
                            this.tagConstructed = 0 != (32 & e),
                            this.tagNumber = 31 & e,
                        31 == this.tagNumber) {
                            for (var n = new y; e = t.get(),
                                n.mulAdd(128, 127 & e),
                            128 & e;)
                                ;
                            this.tagNumber = n.simplify()
                        }
                    }

                    return t.prototype.isUniversal = function () {
                        return 0 === this.tagClass
                    }
                        ,
                        t.prototype.isEOC = function () {
                            return 0 === this.tagClass && 0 === this.tagNumber
                        }
                        ,
                        t
                }(),
                A = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997],
                M = (1 << 26) / A[A.length - 1], k = function () {
                    function b(t, e, n) {
                        null != t && ("number" == typeof t ? this.fromNumber(t, e, n) : null == e && "string" != typeof t ? this.fromString(t, 256) : this.fromString(t, e))
                    }

                    return b.prototype.toString = function (t) {
                        if (this.s < 0)
                            return "-" + this.negate().toString(t);
                        var e;
                        if (16 == t)
                            e = 4;
                        else if (8 == t)
                            e = 3;
                        else if (2 == t)
                            e = 1;
                        else if (32 == t)
                            e = 5;
                        else {
                            if (4 != t)
                                return this.toRadix(t);
                            e = 2
                        }
                        var n, i = (1 << e) - 1, r = !1, o = "", a = this.t, s = this.DB - a * this.DB % e;
                        if (0 < a--)
                            for (s < this.DB && 0 < (n = this[a] >> s) && (r = !0,
                                o = c(n)); 0 <= a;)
                                s < e ? (n = (this[a] & (1 << s) - 1) << e - s,
                                    n |= this[--a] >> (s += this.DB - e)) : (n = this[a] >> (s -= e) & i,
                                s <= 0 && (s += this.DB,
                                    --a)),
                                0 < n && (r = !0),
                                r && (o += c(n));
                        return r ? o : "0"
                    }
                        ,
                        b.prototype.negate = function () {
                            var t = O();
                            return b.ZERO.subTo(this, t),
                                t
                        }
                        ,
                        b.prototype.abs = function () {
                            return this.s < 0 ? this.negate() : this
                        }
                        ,
                        b.prototype.compareTo = function (t) {
                            var e = this.s - t.s;
                            if (0 != e)
                                return e;
                            var n = this.t;
                            if (0 != (e = n - t.t))
                                return this.s < 0 ? -e : e;
                            for (; 0 <= --n;)
                                if (0 != (e = this[n] - t[n]))
                                    return e;
                            return 0
                        }
                        ,
                        b.prototype.bitLength = function () {
                            return this.t <= 0 ? 0 : this.DB * (this.t - 1) + U(this[this.t - 1] ^ this.s & this.DM)
                        }
                        ,
                        b.prototype.mod = function (t) {
                            var e = O();
                            return this.abs().divRemTo(t, null, e),
                            this.s < 0 && 0 < e.compareTo(b.ZERO) && t.subTo(e, e),
                                e
                        }
                        ,
                        b.prototype.modPowInt = function (t, e) {
                            var n;
                            return n = t < 256 || e.isEven() ? new I(e) : new C(e),
                                this.exp(t, n)
                        }
                        ,
                        b.prototype.clone = function () {
                            var t = O();
                            return this.copyTo(t),
                                t
                        }
                        ,
                        b.prototype.intValue = function () {
                            if (this.s < 0) {
                                if (1 == this.t)
                                    return this[0] - this.DV;
                                if (0 == this.t)
                                    return -1
                            } else {
                                if (1 == this.t)
                                    return this[0];
                                if (0 == this.t)
                                    return 0
                            }
                            return (this[1] & (1 << 32 - this.DB) - 1) << this.DB | this[0]
                        }
                        ,
                        b.prototype.byteValue = function () {
                            return 0 == this.t ? this.s : this[0] << 24 >> 24
                        }
                        ,
                        b.prototype.shortValue = function () {
                            return 0 == this.t ? this.s : this[0] << 16 >> 16
                        }
                        ,
                        b.prototype.signum = function () {
                            return this.s < 0 ? -1 : this.t <= 0 || 1 == this.t && this[0] <= 0 ? 0 : 1
                        }
                        ,
                        b.prototype.toByteArray = function () {
                            var t = this.t
                                , e = [];
                            e[0] = this.s;
                            var n, i = this.DB - t * this.DB % 8, r = 0;
                            if (0 < t--)
                                for (i < this.DB && (n = this[t] >> i) != (this.s & this.DM) >> i && (e[r++] = n | this.s << this.DB - i); 0 <= t;)
                                    i < 8 ? (n = (this[t] & (1 << i) - 1) << 8 - i,
                                        n |= this[--t] >> (i += this.DB - 8)) : (n = this[t] >> (i -= 8) & 255,
                                    i <= 0 && (i += this.DB,
                                        --t)),
                                    0 != (128 & n) && (n |= -256),
                                    0 == r && (128 & this.s) != (128 & n) && ++r,
                                    (0 < r || n != this.s) && (e[r++] = n);
                            return e
                        }
                        ,
                        b.prototype.equals = function (t) {
                            return 0 == this.compareTo(t)
                        }
                        ,
                        b.prototype.min = function (t) {
                            return this.compareTo(t) < 0 ? this : t
                        }
                        ,
                        b.prototype.max = function (t) {
                            return 0 < this.compareTo(t) ? this : t
                        }
                        ,
                        b.prototype.and = function (t) {
                            var e = O();
                            return this.bitwiseTo(t, n, e),
                                e
                        }
                        ,
                        b.prototype.or = function (t) {
                            var e = O();
                            return this.bitwiseTo(t, l, e),
                                e
                        }
                        ,
                        b.prototype.xor = function (t) {
                            var e = O();
                            return this.bitwiseTo(t, i, e),
                                e
                        }
                        ,
                        b.prototype.andNot = function (t) {
                            var e = O();
                            return this.bitwiseTo(t, r, e),
                                e
                        }
                        ,
                        b.prototype.not = function () {
                            for (var t = O(), e = 0; e < this.t; ++e)
                                t[e] = this.DM & ~this[e];
                            return t.t = this.t,
                                t.s = ~this.s,
                                t
                        }
                        ,
                        b.prototype.shiftLeft = function (t) {
                            var e = O();
                            return t < 0 ? this.rShiftTo(-t, e) : this.lShiftTo(t, e),
                                e
                        }
                        ,
                        b.prototype.shiftRight = function (t) {
                            var e = O();
                            return t < 0 ? this.lShiftTo(-t, e) : this.rShiftTo(t, e),
                                e
                        }
                        ,
                        b.prototype.getLowestSetBit = function () {
                            for (var t = 0; t < this.t; ++t)
                                if (0 != this[t])
                                    return t * this.DB + o(this[t]);
                            return this.s < 0 ? this.t * this.DB : -1
                        }
                        ,
                        b.prototype.bitCount = function () {
                            for (var t = 0, e = this.s & this.DM, n = 0; n < this.t; ++n)
                                t += a(this[n] ^ e);
                            return t
                        }
                        ,
                        b.prototype.testBit = function (t) {
                            var e = Math.floor(t / this.DB);
                            return e >= this.t ? 0 != this.s : 0 != (this[e] & 1 << t % this.DB)
                        }
                        ,
                        b.prototype.setBit = function (t) {
                            return this.changeBit(t, l)
                        }
                        ,
                        b.prototype.clearBit = function (t) {
                            return this.changeBit(t, r)
                        }
                        ,
                        b.prototype.flipBit = function (t) {
                            return this.changeBit(t, i)
                        }
                        ,
                        b.prototype.add = function (t) {
                            var e = O();
                            return this.addTo(t, e),
                                e
                        }
                        ,
                        b.prototype.subtract = function (t) {
                            var e = O();
                            return this.subTo(t, e),
                                e
                        }
                        ,
                        b.prototype.multiply = function (t) {
                            var e = O();
                            return this.multiplyTo(t, e),
                                e
                        }
                        ,
                        b.prototype.divide = function (t) {
                            var e = O();
                            return this.divRemTo(t, e, null),
                                e
                        }
                        ,
                        b.prototype.remainder = function (t) {
                            var e = O();
                            return this.divRemTo(t, null, e),
                                e
                        }
                        ,
                        b.prototype.divideAndRemainder = function (t) {
                            var e = O()
                                , n = O();
                            return this.divRemTo(t, e, n),
                                [e, n]
                        }
                        ,
                        b.prototype.modPow = function (t, e) {
                            var n, i, r = t.bitLength(), o = z(1);
                            if (r <= 0)
                                return o;
                            n = r < 18 ? 1 : r < 48 ? 3 : r < 144 ? 4 : r < 768 ? 5 : 6,
                                i = r < 8 ? new I(e) : e.isEven() ? new j(e) : new C(e);
                            var a = []
                                , s = 3
                                , c = n - 1
                                , l = (1 << n) - 1;
                            if (a[1] = i.convert(this),
                            1 < n) {
                                var u = O();
                                for (i.sqrTo(a[1], u); s <= l;)
                                    a[s] = O(),
                                        i.mulTo(u, a[s - 2], a[s]),
                                        s += 2
                            }
                            var h, d, f = t.t - 1, p = !0, g = O();
                            for (r = U(t[f]) - 1; 0 <= f;) {
                                for (c <= r ? h = t[f] >> r - c & l : (h = (t[f] & (1 << r + 1) - 1) << c - r,
                                0 < f && (h |= t[f - 1] >> this.DB + r - c)),
                                         s = n; 0 == (1 & h);)
                                    h >>= 1,
                                        --s;
                                if ((r -= s) < 0 && (r += this.DB,
                                    --f),
                                    p)
                                    a[h].copyTo(o),
                                        p = !1;
                                else {
                                    for (; 1 < s;)
                                        i.sqrTo(o, g),
                                            i.sqrTo(g, o),
                                            s -= 2;
                                    0 < s ? i.sqrTo(o, g) : (d = o,
                                        o = g,
                                        g = d),
                                        i.mulTo(g, a[h], o)
                                }
                                for (; 0 <= f && 0 == (t[f] & 1 << r);)
                                    i.sqrTo(o, g),
                                        d = o,
                                        o = g,
                                        g = d,
                                    --r < 0 && (r = this.DB - 1,
                                        --f)
                            }
                            return i.revert(o)
                        }
                        ,
                        b.prototype.modInverse = function (t) {
                            var e = t.isEven();
                            if (this.isEven() && e || 0 == t.signum())
                                return b.ZERO;
                            for (var n = t.clone(), i = this.clone(), r = z(1), o = z(0), a = z(0), s = z(1); 0 != n.signum();) {
                                for (; n.isEven();)
                                    n.rShiftTo(1, n),
                                        e ? (r.isEven() && o.isEven() || (r.addTo(this, r),
                                            o.subTo(t, o)),
                                            r.rShiftTo(1, r)) : o.isEven() || o.subTo(t, o),
                                        o.rShiftTo(1, o);
                                for (; i.isEven();)
                                    i.rShiftTo(1, i),
                                        e ? (a.isEven() && s.isEven() || (a.addTo(this, a),
                                            s.subTo(t, s)),
                                            a.rShiftTo(1, a)) : s.isEven() || s.subTo(t, s),
                                        s.rShiftTo(1, s);
                                0 <= n.compareTo(i) ? (n.subTo(i, n),
                                e && r.subTo(a, r),
                                    o.subTo(s, o)) : (i.subTo(n, i),
                                e && a.subTo(r, a),
                                    s.subTo(o, s))
                            }
                            return 0 != i.compareTo(b.ONE) ? b.ZERO : 0 <= s.compareTo(t) ? s.subtract(t) : s.signum() < 0 ? (s.addTo(t, s),
                                s.signum() < 0 ? s.add(t) : s) : s
                        }
                        ,
                        b.prototype.pow = function (t) {
                            return this.exp(t, new N)
                        }
                        ,
                        b.prototype.gcd = function (t) {
                            var e = this.s < 0 ? this.negate() : this.clone()
                                , n = t.s < 0 ? t.negate() : t.clone();
                            if (e.compareTo(n) < 0) {
                                var i = e;
                                e = n,
                                    n = i
                            }
                            var r = e.getLowestSetBit()
                                , o = n.getLowestSetBit();
                            if (o < 0)
                                return e;
                            for (r < o && (o = r),
                                 0 < o && (e.rShiftTo(o, e),
                                     n.rShiftTo(o, n)); 0 < e.signum();)
                                0 < (r = e.getLowestSetBit()) && e.rShiftTo(r, e),
                                0 < (r = n.getLowestSetBit()) && n.rShiftTo(r, n),
                                    0 <= e.compareTo(n) ? (e.subTo(n, e),
                                        e.rShiftTo(1, e)) : (n.subTo(e, n),
                                        n.rShiftTo(1, n));
                            return 0 < o && n.lShiftTo(o, n),
                                n
                        }
                        ,
                        b.prototype.isProbablePrime = function (t) {
                            var e, n = this.abs();
                            if (1 == n.t && n[0] <= A[A.length - 1]) {
                                for (e = 0; e < A.length; ++e)
                                    if (n[0] == A[e])
                                        return !0;
                                return !1
                            }
                            if (n.isEven())
                                return !1;
                            for (e = 1; e < A.length;) {
                                for (var i = A[e], r = e + 1; r < A.length && i < M;)
                                    i *= A[r++];
                                for (i = n.modInt(i); e < r;)
                                    if (i % A[e++] == 0)
                                        return !1
                            }
                            return n.millerRabin(t)
                        }
                        ,
                        b.prototype.copyTo = function (t) {
                            for (var e = this.t - 1; 0 <= e; --e)
                                t[e] = this[e];
                            t.t = this.t,
                                t.s = this.s
                        }
                        ,
                        b.prototype.fromInt = function (t) {
                            this.t = 1,
                                this.s = t < 0 ? -1 : 0,
                                0 < t ? this[0] = t : t < -1 ? this[0] = t + this.DV : this.t = 0
                        }
                        ,
                        b.prototype.fromString = function (t, e) {
                            var n;
                            if (16 == e)
                                n = 4;
                            else if (8 == e)
                                n = 3;
                            else if (256 == e)
                                n = 8;
                            else if (2 == e)
                                n = 1;
                            else if (32 == e)
                                n = 5;
                            else {
                                if (4 != e)
                                    return void this.fromRadix(t, e);
                                n = 2
                            }
                            this.t = 0,
                                this.s = 0;
                            for (var i = t.length, r = !1, o = 0; 0 <= --i;) {
                                var a = 8 == n ? 255 & +t[i] : q(t, i);
                                a < 0 ? "-" == t.charAt(i) && (r = !0) : (r = !1,
                                    0 == o ? this[this.t++] = a : o + n > this.DB ? (this[this.t - 1] |= (a & (1 << this.DB - o) - 1) << o,
                                        this[this.t++] = a >> this.DB - o) : this[this.t - 1] |= a << o,
                                (o += n) >= this.DB && (o -= this.DB))
                            }
                            8 == n && 0 != (128 & +t[0]) && (this.s = -1,
                            0 < o && (this[this.t - 1] |= (1 << this.DB - o) - 1 << o)),
                                this.clamp(),
                            r && b.ZERO.subTo(this, this)
                        }
                        ,
                        b.prototype.clamp = function () {
                            for (var t = this.s & this.DM; 0 < this.t && this[this.t - 1] == t;)
                                --this.t
                        }
                        ,
                        b.prototype.dlShiftTo = function (t, e) {
                            var n;
                            for (n = this.t - 1; 0 <= n; --n)
                                e[n + t] = this[n];
                            for (n = t - 1; 0 <= n; --n)
                                e[n] = 0;
                            e.t = this.t + t,
                                e.s = this.s
                        }
                        ,
                        b.prototype.drShiftTo = function (t, e) {
                            for (var n = t; n < this.t; ++n)
                                e[n - t] = this[n];
                            e.t = Math.max(this.t - t, 0),
                                e.s = this.s
                        }
                        ,
                        b.prototype.lShiftTo = function (t, e) {
                            for (var n = t % this.DB, i = this.DB - n, r = (1 << i) - 1, o = Math.floor(t / this.DB), a = this.s << n & this.DM, s = this.t - 1; 0 <= s; --s)
                                e[s + o + 1] = this[s] >> i | a,
                                    a = (this[s] & r) << n;
                            for (var s = o - 1; 0 <= s; --s)
                                e[s] = 0;
                            e[o] = a,
                                e.t = this.t + o + 1,
                                e.s = this.s,
                                e.clamp()
                        }
                        ,
                        b.prototype.rShiftTo = function (t, e) {
                            e.s = this.s;
                            var n = Math.floor(t / this.DB);
                            if (n >= this.t)
                                e.t = 0;
                            else {
                                var i = t % this.DB
                                    , r = this.DB - i
                                    , o = (1 << i) - 1;
                                e[0] = this[n] >> i;
                                for (var a = n + 1; a < this.t; ++a)
                                    e[a - n - 1] |= (this[a] & o) << r,
                                        e[a - n] = this[a] >> i;
                                0 < i && (e[this.t - n - 1] |= (this.s & o) << r),
                                    e.t = this.t - n,
                                    e.clamp()
                            }
                        }
                        ,
                        b.prototype.subTo = function (t, e) {
                            for (var n = 0, i = 0, r = Math.min(t.t, this.t); n < r;)
                                i += this[n] - t[n],
                                    e[n++] = i & this.DM,
                                    i >>= this.DB;
                            if (t.t < this.t) {
                                for (i -= t.s; n < this.t;)
                                    i += this[n],
                                        e[n++] = i & this.DM,
                                        i >>= this.DB;
                                i += this.s
                            } else {
                                for (i += this.s; n < t.t;)
                                    i -= t[n],
                                        e[n++] = i & this.DM,
                                        i >>= this.DB;
                                i -= t.s
                            }
                            e.s = i < 0 ? -1 : 0,
                                i < -1 ? e[n++] = this.DV + i : 0 < i && (e[n++] = i),
                                e.t = n,
                                e.clamp()
                        }
                        ,
                        b.prototype.multiplyTo = function (t, e) {
                            var n = this.abs()
                                , i = t.abs()
                                , r = n.t;
                            for (e.t = r + i.t; 0 <= --r;)
                                e[r] = 0;
                            for (r = 0; r < i.t; ++r)
                                e[r + n.t] = n.am(0, i[r], e, r, 0, n.t);
                            e.s = 0,
                                e.clamp(),
                            this.s != t.s && b.ZERO.subTo(e, e)
                        }
                        ,
                        b.prototype.squareTo = function (t) {
                            for (var e = this.abs(), n = t.t = 2 * e.t; 0 <= --n;)
                                t[n] = 0;
                            for (n = 0; n < e.t - 1; ++n) {
                                var i = e.am(n, e[n], t, 2 * n, 0, 1);
                                (t[n + e.t] += e.am(n + 1, 2 * e[n], t, 2 * n + 1, i, e.t - n - 1)) >= e.DV && (t[n + e.t] -= e.DV,
                                    t[n + e.t + 1] = 1)
                            }
                            0 < t.t && (t[t.t - 1] += e.am(n, e[n], t, 2 * n, 0, 1)),
                                t.s = 0,
                                t.clamp()
                        }
                        ,
                        b.prototype.divRemTo = function (t, e, n) {
                            var i = t.abs();
                            if (!(i.t <= 0)) {
                                var r = this.abs();
                                if (r.t < i.t)
                                    return null != e && e.fromInt(0),
                                        void (null != n && this.copyTo(n));
                                null == n && (n = O());
                                var o = O()
                                    , a = this.s
                                    , s = t.s
                                    , c = this.DB - U(i[i.t - 1]);
                                0 < c ? (i.lShiftTo(c, o),
                                    r.lShiftTo(c, n)) : (i.copyTo(o),
                                    r.copyTo(n));
                                var l = o.t
                                    , u = o[l - 1];
                                if (0 != u) {
                                    var h = u * (1 << this.F1) + (1 < l ? o[l - 2] >> this.F2 : 0)
                                        , d = this.FV / h
                                        , f = (1 << this.F1) / h
                                        , p = 1 << this.F2
                                        , g = n.t
                                        , m = g - l
                                        , v = null == e ? O() : e;
                                    for (o.dlShiftTo(m, v),
                                         0 <= n.compareTo(v) && (n[n.t++] = 1,
                                             n.subTo(v, n)),
                                             b.ONE.dlShiftTo(l, v),
                                             v.subTo(o, o); o.t < l;)
                                        o[o.t++] = 0;
                                    for (; 0 <= --m;) {
                                        var y = n[--g] == u ? this.DM : Math.floor(n[g] * d + (n[g - 1] + p) * f);
                                        if ((n[g] += o.am(0, y, n, m, 0, l)) < y)
                                            for (o.dlShiftTo(m, v),
                                                     n.subTo(v, n); n[g] < --y;)
                                                n.subTo(v, n)
                                    }
                                    null != e && (n.drShiftTo(l, e),
                                    a != s && b.ZERO.subTo(e, e)),
                                        n.t = l,
                                        n.clamp(),
                                    0 < c && n.rShiftTo(c, n),
                                    a < 0 && b.ZERO.subTo(n, n)
                                }
                            }
                        }
                        ,
                        b.prototype.invDigit = function () {
                            if (this.t < 1)
                                return 0;
                            var t = this[0];
                            if (0 == (1 & t))
                                return 0;
                            var e = 3 & t;
                            return 0 < (e = (e = (e = (e = e * (2 - (15 & t) * e) & 15) * (2 - (255 & t) * e) & 255) * (2 - ((65535 & t) * e & 65535)) & 65535) * (2 - t * e % this.DV) % this.DV) ? this.DV - e : -e
                        }
                        ,
                        b.prototype.isEven = function () {
                            return 0 == (0 < this.t ? 1 & this[0] : this.s)
                        }
                        ,
                        b.prototype.exp = function (t, e) {
                            if (4294967295 < t || t < 1)
                                return b.ONE;
                            var n = O()
                                , i = O()
                                , r = e.convert(this)
                                , o = U(t) - 1;
                            for (r.copyTo(n); 0 <= --o;)
                                if (e.sqrTo(n, i),
                                0 < (t & 1 << o))
                                    e.mulTo(i, r, n);
                                else {
                                    var a = n;
                                    n = i,
                                        i = a
                                }
                            return e.revert(n)
                        }
                        ,
                        b.prototype.chunkSize = function (t) {
                            return Math.floor(Math.LN2 * this.DB / Math.log(t))
                        }
                        ,
                        b.prototype.toRadix = function (t) {
                            if (null == t && (t = 10),
                            0 == this.signum() || t < 2 || 36 < t)
                                return "0";
                            var e = this.chunkSize(t)
                                , n = Math.pow(t, e)
                                , i = z(n)
                                , r = O()
                                , o = O()
                                , a = "";
                            for (this.divRemTo(i, r, o); 0 < r.signum();)
                                a = (n + o.intValue()).toString(t).substr(1) + a,
                                    r.divRemTo(i, r, o);
                            return o.intValue().toString(t) + a
                        }
                        ,
                        b.prototype.fromRadix = function (t, e) {
                            this.fromInt(0),
                            null == e && (e = 10);
                            for (var n = this.chunkSize(e), i = Math.pow(e, n), r = !1, o = 0, a = 0, s = 0; s < t.length; ++s) {
                                var c = q(t, s);
                                c < 0 ? "-" == t.charAt(s) && 0 == this.signum() && (r = !0) : (a = e * a + c,
                                ++o >= n && (this.dMultiply(i),
                                    this.dAddOffset(a, 0),
                                    a = o = 0))
                            }
                            0 < o && (this.dMultiply(Math.pow(e, o)),
                                this.dAddOffset(a, 0)),
                            r && b.ZERO.subTo(this, this)
                        }
                        ,
                        b.prototype.fromNumber = function (t, e, n) {
                            if ("number" == typeof e)
                                if (t < 2)
                                    this.fromInt(1);
                                else
                                    for (this.fromNumber(t, n),
                                         this.testBit(t - 1) || this.bitwiseTo(b.ONE.shiftLeft(t - 1), l, this),
                                         this.isEven() && this.dAddOffset(1, 0); !this.isProbablePrime(e);)
                                        this.dAddOffset(2, 0),
                                        this.bitLength() > t && this.subTo(b.ONE.shiftLeft(t - 1), this);
                            else {
                                var i = []
                                    , r = 7 & t;
                                i.length = 1 + (t >> 3),
                                    e.nextBytes(i),
                                    0 < r ? i[0] &= (1 << r) - 1 : i[0] = 0,
                                    this.fromString(i, 256)
                            }
                        }
                        ,
                        b.prototype.bitwiseTo = function (t, e, n) {
                            var i, r, o = Math.min(t.t, this.t);
                            for (i = 0; i < o; ++i)
                                n[i] = e(this[i], t[i]);
                            if (t.t < this.t) {
                                for (r = t.s & this.DM,
                                         i = o; i < this.t; ++i)
                                    n[i] = e(this[i], r);
                                n.t = this.t
                            } else {
                                for (r = this.s & this.DM,
                                         i = o; i < t.t; ++i)
                                    n[i] = e(r, t[i]);
                                n.t = t.t
                            }
                            n.s = e(this.s, t.s),
                                n.clamp()
                        }
                        ,
                        b.prototype.changeBit = function (t, e) {
                            var n = b.ONE.shiftLeft(t);
                            return this.bitwiseTo(n, e, n),
                                n
                        }
                        ,
                        b.prototype.addTo = function (t, e) {
                            for (var n = 0, i = 0, r = Math.min(t.t, this.t); n < r;)
                                i += this[n] + t[n],
                                    e[n++] = i & this.DM,
                                    i >>= this.DB;
                            if (t.t < this.t) {
                                for (i += t.s; n < this.t;)
                                    i += this[n],
                                        e[n++] = i & this.DM,
                                        i >>= this.DB;
                                i += this.s
                            } else {
                                for (i += this.s; n < t.t;)
                                    i += t[n],
                                        e[n++] = i & this.DM,
                                        i >>= this.DB;
                                i += t.s
                            }
                            e.s = i < 0 ? -1 : 0,
                                0 < i ? e[n++] = i : i < -1 && (e[n++] = this.DV + i),
                                e.t = n,
                                e.clamp()
                        }
                        ,
                        b.prototype.dMultiply = function (t) {
                            this[this.t] = this.am(0, t - 1, this, 0, 0, this.t),
                                ++this.t,
                                this.clamp()
                        }
                        ,
                        b.prototype.dAddOffset = function (t, e) {
                            if (0 != t) {
                                for (; this.t <= e;)
                                    this[this.t++] = 0;
                                for (this[e] += t; this[e] >= this.DV;)
                                    this[e] -= this.DV,
                                    ++e >= this.t && (this[this.t++] = 0),
                                        ++this[e]
                            }
                        }
                        ,
                        b.prototype.multiplyLowerTo = function (t, e, n) {
                            var i = Math.min(this.t + t.t, e);
                            for (n.s = 0,
                                     n.t = i; 0 < i;)
                                n[--i] = 0;
                            for (var r = n.t - this.t; i < r; ++i)
                                n[i + this.t] = this.am(0, t[i], n, i, 0, this.t);
                            for (var r = Math.min(t.t, e); i < r; ++i)
                                this.am(0, t[i], n, i, 0, e - i);
                            n.clamp()
                        }
                        ,
                        b.prototype.multiplyUpperTo = function (t, e, n) {
                            --e;
                            var i = n.t = this.t + t.t - e;
                            for (n.s = 0; 0 <= --i;)
                                n[i] = 0;
                            for (i = Math.max(e - this.t, 0); i < t.t; ++i)
                                n[this.t + i - e] = this.am(e - i, t[i], n, 0, 0, this.t + i - e);
                            n.clamp(),
                                n.drShiftTo(1, n)
                        }
                        ,
                        b.prototype.modInt = function (t) {
                            if (t <= 0)
                                return 0;
                            var e = this.DV % t
                                , n = this.s < 0 ? t - 1 : 0;
                            if (0 < this.t)
                                if (0 == e)
                                    n = this[0] % t;
                                else
                                    for (var i = this.t - 1; 0 <= i; --i)
                                        n = (e * n + this[i]) % t;
                            return n
                        }
                        ,
                        b.prototype.millerRabin = function (t) {
                            var e = this.subtract(b.ONE)
                                , n = e.getLowestSetBit();
                            if (n <= 0)
                                return !1;
                            var i = e.shiftRight(n);
                            A.length < (t = t + 1 >> 1) && (t = A.length);
                            for (var r = O(), o = 0; o < t; ++o) {
                                r.fromInt(A[Math.floor(Math.random() * A.length)]);
                                var a = r.modPow(i, this);
                                if (0 != a.compareTo(b.ONE) && 0 != a.compareTo(e)) {
                                    for (var s = 1; s++ < n && 0 != a.compareTo(e);)
                                        if (0 == (a = a.modPowInt(2, this)).compareTo(b.ONE))
                                            return !1;
                                    if (0 != a.compareTo(e))
                                        return !1
                                }
                            }
                            return !0
                        }
                        ,
                        b.prototype.square = function () {
                            var t = O();
                            return this.squareTo(t),
                                t
                        }
                        ,
                        b.prototype.gcda = function (t, e) {
                            var n = this.s < 0 ? this.negate() : this.clone()
                                , i = t.s < 0 ? t.negate() : t.clone();
                            if (n.compareTo(i) < 0) {
                                var r = n;
                                n = i,
                                    i = r
                            }
                            var o = n.getLowestSetBit()
                                , a = i.getLowestSetBit();
                            if (a < 0)
                                e(n);
                            else {
                                o < a && (a = o),
                                0 < a && (n.rShiftTo(a, n),
                                    i.rShiftTo(a, i));
                                var s = function () {
                                    0 < (o = n.getLowestSetBit()) && n.rShiftTo(o, n),
                                    0 < (o = i.getLowestSetBit()) && i.rShiftTo(o, i),
                                        0 <= n.compareTo(i) ? (n.subTo(i, n),
                                            n.rShiftTo(1, n)) : (i.subTo(n, i),
                                            i.rShiftTo(1, i)),
                                        0 < n.signum() ? setTimeout(s, 0) : (0 < a && i.lShiftTo(a, i),
                                            setTimeout(function () {
                                                e(i)
                                            }, 0))
                                };
                                setTimeout(s, 10)
                            }
                        }
                        ,
                        b.prototype.fromNumberAsync = function (t, e, n, i) {
                            if ("number" == typeof e)
                                if (t < 2)
                                    this.fromInt(1);
                                else {
                                    this.fromNumber(t, n),
                                    this.testBit(t - 1) || this.bitwiseTo(b.ONE.shiftLeft(t - 1), l, this),
                                    this.isEven() && this.dAddOffset(1, 0);
                                    var r = this
                                        , o = function () {
                                        r.dAddOffset(2, 0),
                                        r.bitLength() > t && r.subTo(b.ONE.shiftLeft(t - 1), r),
                                            r.isProbablePrime(e) ? setTimeout(function () {
                                                i()
                                            }, 0) : setTimeout(o, 0)
                                    };
                                    setTimeout(o, 0)
                                }
                            else {
                                var a = []
                                    , s = 7 & t;
                                a.length = 1 + (t >> 3),
                                    e.nextBytes(a),
                                    0 < s ? a[0] &= (1 << s) - 1 : a[0] = 0,
                                    this.fromString(a, 256)
                            }
                        }
                        ,
                        b
                }(), N = function () {
                    function t() {
                    }

                    return t.prototype.convert = function (t) {
                        return t
                    }
                        ,
                        t.prototype.revert = function (t) {
                            return t
                        }
                        ,
                        t.prototype.mulTo = function (t, e, n) {
                            t.multiplyTo(e, n)
                        }
                        ,
                        t.prototype.sqrTo = function (t, e) {
                            t.squareTo(e)
                        }
                        ,
                        t
                }(), I = function () {
                    function t(t) {
                        this.m = t
                    }

                    return t.prototype.convert = function (t) {
                        return t.s < 0 || 0 <= t.compareTo(this.m) ? t.mod(this.m) : t
                    }
                        ,
                        t.prototype.revert = function (t) {
                            return t
                        }
                        ,
                        t.prototype.reduce = function (t) {
                            t.divRemTo(this.m, null, t)
                        }
                        ,
                        t.prototype.mulTo = function (t, e, n) {
                            t.multiplyTo(e, n),
                                this.reduce(n)
                        }
                        ,
                        t.prototype.sqrTo = function (t, e) {
                            t.squareTo(e),
                                this.reduce(e)
                        }
                        ,
                        t
                }(), C = function () {
                    function t(t) {
                        this.m = t,
                            this.mp = t.invDigit(),
                            this.mpl = 32767 & this.mp,
                            this.mph = this.mp >> 15,
                            this.um = (1 << t.DB - 15) - 1,
                            this.mt2 = 2 * t.t
                    }

                    return t.prototype.convert = function (t) {
                        var e = O();
                        return t.abs().dlShiftTo(this.m.t, e),
                            e.divRemTo(this.m, null, e),
                        t.s < 0 && 0 < e.compareTo(k.ZERO) && this.m.subTo(e, e),
                            e
                    }
                        ,
                        t.prototype.revert = function (t) {
                            var e = O();
                            return t.copyTo(e),
                                this.reduce(e),
                                e
                        }
                        ,
                        t.prototype.reduce = function (t) {
                            for (; t.t <= this.mt2;)
                                t[t.t++] = 0;
                            for (var e = 0; e < this.m.t; ++e) {
                                var n = 32767 & t[e]
                                    , i = n * this.mpl + ((n * this.mph + (t[e] >> 15) * this.mpl & this.um) << 15) & t.DM;
                                for (n = e + this.m.t,
                                         t[n] += this.m.am(0, i, t, e, 0, this.m.t); t[n] >= t.DV;)
                                    t[n] -= t.DV,
                                        t[++n]++
                            }
                            t.clamp(),
                                t.drShiftTo(this.m.t, t),
                            0 <= t.compareTo(this.m) && t.subTo(this.m, t)
                        }
                        ,
                        t.prototype.mulTo = function (t, e, n) {
                            t.multiplyTo(e, n),
                                this.reduce(n)
                        }
                        ,
                        t.prototype.sqrTo = function (t, e) {
                            t.squareTo(e),
                                this.reduce(e)
                        }
                        ,
                        t
                }(), j = function () {
                    function t(t) {
                        this.m = t,
                            this.r2 = O(),
                            this.q3 = O(),
                            k.ONE.dlShiftTo(2 * t.t, this.r2),
                            this.mu = this.r2.divide(t)
                    }

                    return t.prototype.convert = function (t) {
                        if (t.s < 0 || t.t > 2 * this.m.t)
                            return t.mod(this.m);
                        if (t.compareTo(this.m) < 0)
                            return t;
                        var e = O();
                        return t.copyTo(e),
                            this.reduce(e),
                            e
                    }
                        ,
                        t.prototype.revert = function (t) {
                            return t
                        }
                        ,
                        t.prototype.reduce = function (t) {
                            for (t.drShiftTo(this.m.t - 1, this.r2),
                                 t.t > this.m.t + 1 && (t.t = this.m.t + 1,
                                     t.clamp()),
                                     this.mu.multiplyUpperTo(this.r2, this.m.t + 1, this.q3),
                                     this.m.multiplyLowerTo(this.q3, this.m.t + 1, this.r2); t.compareTo(this.r2) < 0;)
                                t.dAddOffset(1, this.m.t + 1);
                            for (t.subTo(this.r2, t); 0 <= t.compareTo(this.m);)
                                t.subTo(this.m, t)
                        }
                        ,
                        t.prototype.mulTo = function (t, e, n) {
                            t.multiplyTo(e, n),
                                this.reduce(n)
                        }
                        ,
                        t.prototype.sqrTo = function (t, e) {
                            t.squareTo(e),
                                this.reduce(e)
                        }
                        ,
                        t
                }();

            function O() {
                return new k(null)
            }

            function L(t, e) {
                return new k(t, e)
            }

            T = "Microsoft Internet Explorer" == navigator.appName ? (k.prototype.am = function (t, e, n, i, r, o) {
                var a = 32767 & e
                    , s = e >> 15;
                for (; 0 <= --o;) {
                    var c = 32767 & this[t]
                        , l = this[t++] >> 15
                        , u = s * c + l * a;
                    c = a * c + ((32767 & u) << 15) + n[i] + (1073741823 & r),
                        r = (c >>> 30) + (u >>> 15) + s * l + (r >>> 30),
                        n[i++] = 1073741823 & c
                }
                return r
            }
                ,
                30) : "Netscape" != navigator.appName ? (k.prototype.am = function (t, e, n, i, r, o) {
                for (; 0 <= --o;) {
                    var a = e * this[t++] + n[i] + r;
                    r = Math.floor(a / 67108864),
                        n[i++] = 67108863 & a
                }
                return r
            }
                ,
                26) : (k.prototype.am = function (t, e, n, i, r, o) {
                var a = 16383 & e
                    , s = e >> 14;
                for (; 0 <= --o;) {
                    var c = 16383 & this[t]
                        , l = this[t++] >> 14
                        , u = s * c + l * a;
                    c = a * c + ((16383 & u) << 14) + n[i] + r,
                        r = (c >> 28) + (u >> 14) + s * l,
                        n[i++] = 268435455 & c
                }
                return r
            }
                ,
                28),
                k.prototype.DB = T,
                k.prototype.DM = (1 << T) - 1,
                k.prototype.DV = 1 << T;
            k.prototype.FV = Math.pow(2, 52),
                k.prototype.F1 = 52 - T,
                k.prototype.F2 = 2 * T - 52;
            var R, P, B = [];
            for (R = "0".charCodeAt(0),
                     P = 0; P <= 9; ++P)
                B[R++] = P;
            for (R = "a".charCodeAt(0),
                     P = 10; P < 36; ++P)
                B[R++] = P;
            for (R = "A".charCodeAt(0),
                     P = 10; P < 36; ++P)
                B[R++] = P;

            function q(t, e) {
                var n = B[t.charCodeAt(e)];
                return null == n ? -1 : n
            }

            function z(t) {
                var e = O();
                return e.fromInt(t),
                    e
            }

            function U(t) {
                var e, n = 1;
                return 0 != (e = t >>> 16) && (t = e,
                    n += 16),
                0 != (e = t >> 8) && (t = e,
                    n += 8),
                0 != (e = t >> 4) && (t = e,
                    n += 4),
                0 != (e = t >> 2) && (t = e,
                    n += 2),
                0 != (e = t >> 1) && (t = e,
                    n += 1),
                    n
            }

            k.ZERO = z(0),
                k.ONE = z(1);
            var V = function () {
                function t() {
                    this.i = 0,
                        this.j = 0,
                        this.S = []
                }

                return t.prototype.init = function (t) {
                    var e, n, i;
                    for (e = 0; e < 256; ++e)
                        this.S[e] = e;
                    for (e = n = 0; e < 256; ++e)
                        n = n + this.S[e] + t[e % t.length] & 255,
                            i = this.S[e],
                            this.S[e] = this.S[n],
                            this.S[n] = i;
                    this.i = 0,
                        this.j = 0
                }
                    ,
                    t.prototype.next = function () {
                        var t;
                        return this.i = this.i + 1 & 255,
                            this.j = this.j + this.S[this.i] & 255,
                            t = this.S[this.i],
                            this.S[this.i] = this.S[this.j],
                            this.S[this.j] = t,
                            this.S[t + this.S[this.i] & 255]
                    }
                    ,
                    t
            }();
            var H, F, K = 256, Y = null;
            if (null == Y) {
                Y = [];
                var Q = void (F = 0);
                if (window.crypto && window.crypto.getRandomValues) {
                    var W = new Uint32Array(256);
                    for (window.crypto.getRandomValues(W),
                             Q = 0; Q < W.length; ++Q)
                        Y[F++] = 255 & W[Q]
                }
                var G = function (t) {
                    if (this.count = this.count || 0,
                    256 <= this.count || K <= F)
                        window.removeEventListener ? window.removeEventListener("mousemove", G, !1) : window.detachEvent && window.detachEvent("onmousemove", G);
                    else
                        try {
                            var e = t.x + t.y;
                            Y[F++] = 255 & e,
                                this.count += 1
                        } catch (t) {
                        }
                };
                window.addEventListener ? window.addEventListener("mousemove", G, !1) : window.attachEvent && window.attachEvent("onmousemove", G)
            }

            function Z() {
                if (null == H) {
                    for (H = new V; F < K;) {
                        var t = Math.floor(65536 * Math.random());
                        Y[F++] = 255 & t
                    }
                    for (H.init(Y),
                             F = 0; F < Y.length; ++F)
                        Y[F] = 0;
                    F = 0
                }
                return H.next()
            }

            var X = function () {
                function t() {
                }

                return t.prototype.nextBytes = function (t) {
                    for (var e = 0; e < t.length; ++e)
                        t[e] = Z()
                }
                    ,
                    t
            }();
            var J = function () {
                function t() {
                    this.n = null,
                        this.e = 0,
                        this.d = null,
                        this.p = null,
                        this.q = null,
                        this.dmp1 = null,
                        this.dmq1 = null,
                        this.coeff = null
                }

                return t.prototype.doPublic = function (t) {
                    return t.modPowInt(this.e, this.n)
                }
                    ,
                    t.prototype.doPrivate = function (t) {
                        if (null == this.p || null == this.q)
                            return t.modPow(this.d, this.n);
                        for (var e = t.mod(this.p).modPow(this.dmp1, this.p), n = t.mod(this.q).modPow(this.dmq1, this.q); e.compareTo(n) < 0;)
                            e = e.add(this.p);
                        return e.subtract(n).multiply(this.coeff).mod(this.p).multiply(this.q).add(n)
                    }
                    ,
                    t.prototype.setPublic = function (t, e) {
                        null != t && null != e && 0 < t.length && 0 < e.length && (this.n = L(t, 16),
                            this.e = parseInt(e, 16))
                    }
                    ,
                    t.prototype.encrypt = function (t) {
                        var e = function (t, e) {
                            if (e < t.length + 11)
                                return null;
                            var n = []
                                , i = t.length - 1;
                            for (; 0 <= i && 0 < e;) {
                                var r = t.charCodeAt(i--);
                                r < 128 ? n[--e] = r : 127 < r && r < 2048 ? (n[--e] = 63 & r | 128,
                                    n[--e] = r >> 6 | 192) : (n[--e] = 63 & r | 128,
                                    n[--e] = r >> 6 & 63 | 128,
                                    n[--e] = r >> 12 | 224)
                            }
                            n[--e] = 0;
                            var o = new X
                                , a = [];
                            for (; 2 < e;) {
                                for (a[0] = 0; 0 == a[0];)
                                    o.nextBytes(a);
                                n[--e] = a[0]
                            }
                            return n[--e] = 2,
                                n[--e] = 0,
                                new k(n)
                        }(t, this.n.bitLength() + 7 >> 3);
                        if (null == e)
                            return null;
                        var n = this.doPublic(e);
                        if (null == n)
                            return null;
                        var i = n.toString(16);
                        return 0 == (1 & i.length) ? i : "0" + i
                    }
                    ,
                    t.prototype.setPrivate = function (t, e, n) {
                        null != t && null != e && 0 < t.length && 0 < e.length && (this.n = L(t, 16),
                            this.e = parseInt(e, 16),
                            this.d = L(n, 16))
                    }
                    ,
                    t.prototype.setPrivateEx = function (t, e, n, i, r, o, a, s) {
                        null != t && null != e && 0 < t.length && 0 < e.length && (this.n = L(t, 16),
                            this.e = parseInt(e, 16),
                            this.d = L(n, 16),
                            this.p = L(i, 16),
                            this.q = L(r, 16),
                            this.dmp1 = L(o, 16),
                            this.dmq1 = L(a, 16),
                            this.coeff = L(s, 16))
                    }
                    ,
                    t.prototype.generate = function (t, e) {
                        var n = new X
                            , i = t >> 1;
                        this.e = parseInt(e, 16);
                        for (var r = new k(e, 16); ;) {
                            for (; this.p = new k(t - i, 1, n),
                                   0 != this.p.subtract(k.ONE).gcd(r).compareTo(k.ONE) || !this.p.isProbablePrime(10);)
                                ;
                            for (; this.q = new k(i, 1, n),
                                   0 != this.q.subtract(k.ONE).gcd(r).compareTo(k.ONE) || !this.q.isProbablePrime(10);)
                                ;
                            if (this.p.compareTo(this.q) <= 0) {
                                var o = this.p;
                                this.p = this.q,
                                    this.q = o
                            }
                            var a = this.p.subtract(k.ONE)
                                , s = this.q.subtract(k.ONE)
                                , c = a.multiply(s);
                            if (0 == c.gcd(r).compareTo(k.ONE)) {
                                this.n = this.p.multiply(this.q),
                                    this.d = r.modInverse(c),
                                    this.dmp1 = this.d.mod(a),
                                    this.dmq1 = this.d.mod(s),
                                    this.coeff = this.q.modInverse(this.p);
                                break
                            }
                        }
                    }
                    ,
                    t.prototype.decrypt = function (t) {
                        var e = L(t, 16)
                            , n = this.doPrivate(e);
                        return null == n ? null : function (t, e) {
                            var n = t.toByteArray()
                                , i = 0;
                            for (; i < n.length && 0 == n[i];)
                                ++i;
                            if (n.length - i != e - 1 || 2 != n[i])
                                return null;
                            ++i;
                            for (; 0 != n[i];)
                                if (++i >= n.length)
                                    return null;
                            var r = "";
                            for (; ++i < n.length;) {
                                var o = 255 & n[i];
                                o < 128 ? r += String.fromCharCode(o) : 191 < o && o < 224 ? (r += String.fromCharCode((31 & o) << 6 | 63 & n[i + 1]),
                                    ++i) : (r += String.fromCharCode((15 & o) << 12 | (63 & n[i + 1]) << 6 | 63 & n[i + 2]),
                                    i += 2)
                            }
                            return r
                        }(n, this.n.bitLength() + 7 >> 3)
                    }
                    ,
                    t.prototype.generateAsync = function (t, e, r) {
                        var o = new X
                            , a = t >> 1;
                        this.e = parseInt(e, 16);
                        var s = new k(e, 16)
                            , c = this
                            , l = function () {
                            var e = function () {
                                if (c.p.compareTo(c.q) <= 0) {
                                    var t = c.p;
                                    c.p = c.q,
                                        c.q = t
                                }
                                var e = c.p.subtract(k.ONE)
                                    , n = c.q.subtract(k.ONE)
                                    , i = e.multiply(n);
                                0 == i.gcd(s).compareTo(k.ONE) ? (c.n = c.p.multiply(c.q),
                                    c.d = s.modInverse(i),
                                    c.dmp1 = c.d.mod(e),
                                    c.dmq1 = c.d.mod(n),
                                    c.coeff = c.q.modInverse(c.p),
                                    setTimeout(function () {
                                        r()
                                    }, 0)) : setTimeout(l, 0)
                            }
                                , n = function () {
                                c.q = O(),
                                    c.q.fromNumberAsync(a, 1, o, function () {
                                        c.q.subtract(k.ONE).gcda(s, function (t) {
                                            0 == t.compareTo(k.ONE) && c.q.isProbablePrime(10) ? setTimeout(e, 0) : setTimeout(n, 0)
                                        })
                                    })
                            }
                                , i = function () {
                                c.p = O(),
                                    c.p.fromNumberAsync(t - a, 1, o, function () {
                                        c.p.subtract(k.ONE).gcda(s, function (t) {
                                            0 == t.compareTo(k.ONE) && c.p.isProbablePrime(10) ? setTimeout(n, 0) : setTimeout(i, 0)
                                        })
                                    })
                            };
                            setTimeout(i, 0)
                        };
                        setTimeout(l, 0)
                    }
                    ,
                    t.prototype.sign = function (t, e, n) {
                        var i = function (t) {
                            return $[t] || ""
                        }(n)
                            , r = i + e(t).toString()
                            , o = function (t, e) {
                            if (e < t.length + 22)
                                return null;
                            for (var n = e - t.length - 6, i = "", r = 0; r < n; r += 2)
                                i += "ff";
                            return L("0001" + i + "00" + t, 16)
                        }(r, this.n.bitLength() / 4);
                        if (null == o)
                            return null;
                        var a = this.doPrivate(o);
                        if (null == a)
                            return null;
                        var s = a.toString(16);
                        return 0 == (1 & s.length) ? s : "0" + s
                    }
                    ,
                    t.prototype.verify = function (t, e, n) {
                        var i = L(e, 16)
                            , r = this.doPublic(i);
                        if (null == r)
                            return null;
                        var o = r.toString(16).replace(/^1f+00/, "")
                            , a = function (t) {
                            for (var e in $)
                                if ($.hasOwnProperty(e)) {
                                    var n = $[e]
                                        , i = n.length;
                                    if (t.substr(0, i) == n)
                                        return t.substr(i)
                                }
                            return t
                        }(o);
                        return a == n(t).toString()
                    }
                    ,
                    t
            }();
            var $ = {
                md2: "3020300c06082a864886f70d020205000410",
                md5: "3020300c06082a864886f70d020505000410",
                sha1: "3021300906052b0e03021a05000414",
                sha224: "302d300d06096086480165030402040500041c",
                sha256: "3031300d060960864801650304020105000420",
                sha384: "3041300d060960864801650304020205000430",
                sha512: "3051300d060960864801650304020305000440",
                ripemd160: "3021300906052b2403020105000414"
            };
            var tt = {};
            tt.lang = {
                extend: function (t, e, n) {
                    if (!e || !t)
                        throw new Error("YAHOO.lang.extend failed, please check that all dependencies are included.");
                    var i = function () {
                    };
                    if (i.prototype = e.prototype,
                        t.prototype = new i,
                        (t.prototype.constructor = t).superclass = e.prototype,
                    e.prototype.constructor == Object.prototype.constructor && (e.prototype.constructor = e),
                        n) {
                        var r;
                        for (r in n)
                            t.prototype[r] = n[r];
                        var o = function () {
                        }
                            , a = ["toString", "valueOf"];
                        try {
                            /MSIE/.test(navigator.userAgent) && (o = function (t, e) {
                                    for (r = 0; r < a.length; r += 1) {
                                        var n = a[r]
                                            , i = e[n];
                                        "function" == typeof i && i != Object.prototype[n] && (t[n] = i)
                                    }
                                }
                            )
                        } catch (t) {
                        }
                        o(t.prototype, n)
                    }
                }
            };
            var et = {};
            void 0 !== et.asn1 && et.asn1 || (et.asn1 = {}),
                et.asn1.ASN1Util = new function () {
                    this.integerToByteHex = function (t) {
                        var e = t.toString(16);
                        return e.length % 2 == 1 && (e = "0" + e),
                            e
                    }
                        ,
                        this.bigIntToMinTwosComplementsHex = function (t) {
                            var e = t.toString(16);
                            if ("-" != e.substr(0, 1))
                                e.length % 2 == 1 ? e = "0" + e : e.match(/^[0-7]/) || (e = "00" + e);
                            else {
                                var n = e.substr(1)
                                    , i = n.length;
                                i % 2 == 1 ? i += 1 : e.match(/^[0-7]/) || (i += 2);
                                for (var r = "", o = 0; o < i; o++)
                                    r += "f";
                                var a = new k(r, 16)
                                    , s = a.xor(t).add(k.ONE);
                                e = s.toString(16).replace(/^-/, "")
                            }
                            return e
                        }
                        ,
                        this.getPEMStringFromHex = function (t, e) {
                            return hextopem(t, e)
                        }
                        ,
                        this.newObject = function (t) {
                            var e = et
                                , n = e.asn1
                                , i = n.DERBoolean
                                , r = n.DERInteger
                                , o = n.DERBitString
                                , a = n.DEROctetString
                                , s = n.DERNull
                                , c = n.DERObjectIdentifier
                                , l = n.DEREnumerated
                                , u = n.DERUTF8String
                                , h = n.DERNumericString
                                , d = n.DERPrintableString
                                , f = n.DERTeletexString
                                , p = n.DERIA5String
                                , g = n.DERUTCTime
                                , m = n.DERGeneralizedTime
                                , v = n.DERSequence
                                , y = n.DERSet
                                , b = n.DERTaggedObject
                                , w = n.ASN1Util.newObject
                                , _ = Object.keys(t);
                            if (1 != _.length)
                                throw "key of param shall be only one.";
                            var x = _[0];
                            if (-1 == ":bool:int:bitstr:octstr:null:oid:enum:utf8str:numstr:prnstr:telstr:ia5str:utctime:gentime:seq:set:tag:".indexOf(":" + x + ":"))
                                throw "undefined key: " + x;
                            if ("bool" == x)
                                return new i(t[x]);
                            if ("int" == x)
                                return new r(t[x]);
                            if ("bitstr" == x)
                                return new o(t[x]);
                            if ("octstr" == x)
                                return new a(t[x]);
                            if ("null" == x)
                                return new s(t[x]);
                            if ("oid" == x)
                                return new c(t[x]);
                            if ("enum" == x)
                                return new l(t[x]);
                            if ("utf8str" == x)
                                return new u(t[x]);
                            if ("numstr" == x)
                                return new h(t[x]);
                            if ("prnstr" == x)
                                return new d(t[x]);
                            if ("telstr" == x)
                                return new f(t[x]);
                            if ("ia5str" == x)
                                return new p(t[x]);
                            if ("utctime" == x)
                                return new g(t[x]);
                            if ("gentime" == x)
                                return new m(t[x]);
                            if ("seq" == x) {
                                for (var T = t[x], D = [], E = 0; E < T.length; E++) {
                                    var S = w(T[E]);
                                    D.push(S)
                                }
                                return new v({
                                    array: D
                                })
                            }
                            if ("set" == x) {
                                for (var T = t[x], D = [], E = 0; E < T.length; E++) {
                                    var S = w(T[E]);
                                    D.push(S)
                                }
                                return new y({
                                    array: D
                                })
                            }
                            if ("tag" == x) {
                                var A = t[x];
                                if ("[object Array]" === Object.prototype.toString.call(A) && 3 == A.length) {
                                    var M = w(A[2]);
                                    return new b({
                                        tag: A[0],
                                        explicit: A[1],
                                        obj: M
                                    })
                                }
                                var k = {};
                                if (void 0 !== A.explicit && (k.explicit = A.explicit),
                                void 0 !== A.tag && (k.tag = A.tag),
                                void 0 === A.obj)
                                    throw "obj shall be specified for 'tag'.";
                                return k.obj = w(A.obj),
                                    new b(k)
                            }
                        }
                        ,
                        this.jsonToASN1HEX = function (t) {
                            var e = this.newObject(t);
                            return e.getEncodedHex()
                        }
                }
                ,
                et.asn1.ASN1Util.oidHexToInt = function (t) {
                    for (var e = "", n = parseInt(t.substr(0, 2), 16), i = Math.floor(n / 40), r = n % 40, e = i + "." + r, o = "", a = 2; a < t.length; a += 2) {
                        var s = parseInt(t.substr(a, 2), 16)
                            , c = ("00000000" + s.toString(2)).slice(-8);
                        if (o += c.substr(1, 7),
                        "0" == c.substr(0, 1)) {
                            var l = new k(o, 2);
                            e = e + "." + l.toString(10),
                                o = ""
                        }
                    }
                    return e
                }
                ,
                et.asn1.ASN1Util.oidIntToHex = function (t) {
                    var c = function (t) {
                        var e = t.toString(16);
                        return 1 == e.length && (e = "0" + e),
                            e
                    }
                        , e = function (t) {
                        var e = ""
                            , n = new k(t, 10)
                            , i = n.toString(2)
                            , r = 7 - i.length % 7;
                        7 == r && (r = 0);
                        for (var o = "", a = 0; a < r; a++)
                            o += "0";
                        i = o + i;
                        for (var a = 0; a < i.length - 1; a += 7) {
                            var s = i.substr(a, 7);
                            a != i.length - 7 && (s = "1" + s),
                                e += c(parseInt(s, 2))
                        }
                        return e
                    };
                    if (!t.match(/^[0-9.]+$/))
                        throw "malformed oid string: " + t;
                    var n = ""
                        , i = t.split(".")
                        , r = 40 * parseInt(i[0]) + parseInt(i[1]);
                    n += c(r),
                        i.splice(0, 2);
                    for (var o = 0; o < i.length; o++)
                        n += e(i[o]);
                    return n
                }
                ,
                et.asn1.ASN1Object = function () {
                    this.getLengthHexFromValue = function () {
                        if (void 0 === this.hV || null == this.hV)
                            throw "this.hV is null or undefined.";
                        if (this.hV.length % 2 == 1)
                            throw "value hex must be even length: n=" + "".length + ",v=" + this.hV;
                        var t = this.hV.length / 2
                            , e = t.toString(16);
                        if (e.length % 2 == 1 && (e = "0" + e),
                        t < 128)
                            return e;
                        var n = e.length / 2;
                        if (15 < n)
                            throw "ASN.1 length too long to represent by 8x: n = " + t.toString(16);
                        var i = 128 + n;
                        return i.toString(16) + e
                    }
                        ,
                        this.getEncodedHex = function () {
                            return null != this.hTLV && !this.isModified || (this.hV = this.getFreshValueHex(),
                                this.hL = this.getLengthHexFromValue(),
                                this.hTLV = this.hT + this.hL + this.hV,
                                this.isModified = !1),
                                this.hTLV
                        }
                        ,
                        this.getValueHex = function () {
                            return this.getEncodedHex(),
                                this.hV
                        }
                        ,
                        this.getFreshValueHex = function () {
                            return ""
                        }
                }
                ,
                et.asn1.DERAbstractString = function (t) {
                    et.asn1.DERAbstractString.superclass.constructor.call(this),
                        this.getString = function () {
                            return this.s
                        }
                        ,
                        this.setString = function (t) {
                            this.hTLV = null,
                                this.isModified = !0,
                                this.s = t,
                                this.hV = stohex(this.s)
                        }
                        ,
                        this.setStringHex = function (t) {
                            this.hTLV = null,
                                this.isModified = !0,
                                this.s = null,
                                this.hV = t
                        }
                        ,
                        this.getFreshValueHex = function () {
                            return this.hV
                        }
                        ,
                    void 0 !== t && ("string" == typeof t ? this.setString(t) : void 0 !== t.str ? this.setString(t.str) : void 0 !== t.hex && this.setStringHex(t.hex))
                }
                ,
                tt.lang.extend(et.asn1.DERAbstractString, et.asn1.ASN1Object),
                et.asn1.DERAbstractTime = function (t) {
                    et.asn1.DERAbstractTime.superclass.constructor.call(this),
                        this.localDateToUTC = function (t) {
                            utc = t.getTime() + 6e4 * t.getTimezoneOffset();
                            var e = new Date(utc);
                            return e
                        }
                        ,
                        this.formatDate = function (t, e, n) {
                            var i = this.zeroPadding
                                , r = this.localDateToUTC(t)
                                , o = String(r.getFullYear());
                            "utc" == e && (o = o.substr(2, 2));
                            var a = i(String(r.getMonth() + 1), 2)
                                , s = i(String(r.getDate()), 2)
                                , c = i(String(r.getHours()), 2)
                                , l = i(String(r.getMinutes()), 2)
                                , u = i(String(r.getSeconds()), 2)
                                , h = o + a + s + c + l + u;
                            if (!0 === n) {
                                var d = r.getMilliseconds();
                                if (0 != d) {
                                    var f = i(String(d), 3);
                                    f = f.replace(/[0]+$/, ""),
                                        h = h + "." + f
                                }
                            }
                            return h + "Z"
                        }
                        ,
                        this.zeroPadding = function (t, e) {
                            return t.length >= e ? t : new Array(e - t.length + 1).join("0") + t
                        }
                        ,
                        this.getString = function () {
                            return this.s
                        }
                        ,
                        this.setString = function (t) {
                            this.hTLV = null,
                                this.isModified = !0,
                                this.s = t,
                                this.hV = stohex(t)
                        }
                        ,
                        this.setByDateValue = function (t, e, n, i, r, o) {
                            var a = new Date(Date.UTC(t, e - 1, n, i, r, o, 0));
                            this.setByDate(a)
                        }
                        ,
                        this.getFreshValueHex = function () {
                            return this.hV
                        }
                }
                ,
                tt.lang.extend(et.asn1.DERAbstractTime, et.asn1.ASN1Object),
                et.asn1.DERAbstractStructured = function (t) {
                    et.asn1.DERAbstractString.superclass.constructor.call(this),
                        this.setByASN1ObjectArray = function (t) {
                            this.hTLV = null,
                                this.isModified = !0,
                                this.asn1Array = t
                        }
                        ,
                        this.appendASN1Object = function (t) {
                            this.hTLV = null,
                                this.isModified = !0,
                                this.asn1Array.push(t)
                        }
                        ,
                        this.asn1Array = new Array,
                    void 0 !== t && void 0 !== t.array && (this.asn1Array = t.array)
                }
                ,
                tt.lang.extend(et.asn1.DERAbstractStructured, et.asn1.ASN1Object),
                et.asn1.DERBoolean = function () {
                    et.asn1.DERBoolean.superclass.constructor.call(this),
                        this.hT = "01",
                        this.hTLV = "0101ff"
                }
                ,
                tt.lang.extend(et.asn1.DERBoolean, et.asn1.ASN1Object),
                et.asn1.DERInteger = function (t) {
                    et.asn1.DERInteger.superclass.constructor.call(this),
                        this.hT = "02",
                        this.setByBigInteger = function (t) {
                            this.hTLV = null,
                                this.isModified = !0,
                                this.hV = et.asn1.ASN1Util.bigIntToMinTwosComplementsHex(t)
                        }
                        ,
                        this.setByInteger = function (t) {
                            var e = new k(String(t), 10);
                            this.setByBigInteger(e)
                        }
                        ,
                        this.setValueHex = function (t) {
                            this.hV = t
                        }
                        ,
                        this.getFreshValueHex = function () {
                            return this.hV
                        }
                        ,
                    void 0 !== t && (void 0 !== t.bigint ? this.setByBigInteger(t.bigint) : void 0 !== t.int ? this.setByInteger(t.int) : "number" == typeof t ? this.setByInteger(t) : void 0 !== t.hex && this.setValueHex(t.hex))
                }
                ,
                tt.lang.extend(et.asn1.DERInteger, et.asn1.ASN1Object),
                et.asn1.DERBitString = function (t) {
                    if (void 0 !== t && void 0 !== t.obj) {
                        var e = et.asn1.ASN1Util.newObject(t.obj);
                        t.hex = "00" + e.getEncodedHex()
                    }
                    et.asn1.DERBitString.superclass.constructor.call(this),
                        this.hT = "03",
                        this.setHexValueIncludingUnusedBits = function (t) {
                            this.hTLV = null,
                                this.isModified = !0,
                                this.hV = t
                        }
                        ,
                        this.setUnusedBitsAndHexValue = function (t, e) {
                            if (t < 0 || 7 < t)
                                throw "unused bits shall be from 0 to 7: u = " + t;
                            var n = "0" + t;
                            this.hTLV = null,
                                this.isModified = !0,
                                this.hV = n + e
                        }
                        ,
                        this.setByBinaryString = function (t) {
                            var e = 8 - (t = t.replace(/0+$/, "")).length % 8;
                            8 == e && (e = 0);
                            for (var n = 0; n <= e; n++)
                                t += "0";
                            for (var i = "", n = 0; n < t.length - 1; n += 8) {
                                var r = t.substr(n, 8)
                                    , o = parseInt(r, 2).toString(16);
                                1 == o.length && (o = "0" + o),
                                    i += o
                            }
                            this.hTLV = null,
                                this.isModified = !0,
                                this.hV = "0" + e + i
                        }
                        ,
                        this.setByBooleanArray = function (t) {
                            for (var e = "", n = 0; n < t.length; n++)
                                1 == t[n] ? e += "1" : e += "0";
                            this.setByBinaryString(e)
                        }
                        ,
                        this.newFalseArray = function (t) {
                            for (var e = new Array(t), n = 0; n < t; n++)
                                e[n] = !1;
                            return e
                        }
                        ,
                        this.getFreshValueHex = function () {
                            return this.hV
                        }
                        ,
                    void 0 !== t && ("string" == typeof t && t.toLowerCase().match(/^[0-9a-f]+$/) ? this.setHexValueIncludingUnusedBits(t) : void 0 !== t.hex ? this.setHexValueIncludingUnusedBits(t.hex) : void 0 !== t.bin ? this.setByBinaryString(t.bin) : void 0 !== t.array && this.setByBooleanArray(t.array))
                }
                ,
                tt.lang.extend(et.asn1.DERBitString, et.asn1.ASN1Object),
                et.asn1.DEROctetString = function (t) {
                    if (void 0 !== t && void 0 !== t.obj) {
                        var e = et.asn1.ASN1Util.newObject(t.obj);
                        t.hex = e.getEncodedHex()
                    }
                    et.asn1.DEROctetString.superclass.constructor.call(this, t),
                        this.hT = "04"
                }
                ,
                tt.lang.extend(et.asn1.DEROctetString, et.asn1.DERAbstractString),
                et.asn1.DERNull = function () {
                    et.asn1.DERNull.superclass.constructor.call(this),
                        this.hT = "05",
                        this.hTLV = "0500"
                }
                ,
                tt.lang.extend(et.asn1.DERNull, et.asn1.ASN1Object),
                et.asn1.DERObjectIdentifier = function (t) {
                    var c = function (t) {
                        var e = t.toString(16);
                        return 1 == e.length && (e = "0" + e),
                            e
                    }
                        , o = function (t) {
                        var e = ""
                            , n = new k(t, 10)
                            , i = n.toString(2)
                            , r = 7 - i.length % 7;
                        7 == r && (r = 0);
                        for (var o = "", a = 0; a < r; a++)
                            o += "0";
                        i = o + i;
                        for (var a = 0; a < i.length - 1; a += 7) {
                            var s = i.substr(a, 7);
                            a != i.length - 7 && (s = "1" + s),
                                e += c(parseInt(s, 2))
                        }
                        return e
                    };
                    et.asn1.DERObjectIdentifier.superclass.constructor.call(this),
                        this.hT = "06",
                        this.setValueHex = function (t) {
                            this.hTLV = null,
                                this.isModified = !0,
                                this.s = null,
                                this.hV = t
                        }
                        ,
                        this.setValueOidString = function (t) {
                            if (!t.match(/^[0-9.]+$/))
                                throw "malformed oid string: " + t;
                            var e = ""
                                , n = t.split(".")
                                , i = 40 * parseInt(n[0]) + parseInt(n[1]);
                            e += c(i),
                                n.splice(0, 2);
                            for (var r = 0; r < n.length; r++)
                                e += o(n[r]);
                            this.hTLV = null,
                                this.isModified = !0,
                                this.s = null,
                                this.hV = e
                        }
                        ,
                        this.setValueName = function (t) {
                            var e = et.asn1.x509.OID.name2oid(t);
                            if ("" === e)
                                throw "DERObjectIdentifier oidName undefined: " + t;
                            this.setValueOidString(e)
                        }
                        ,
                        this.getFreshValueHex = function () {
                            return this.hV
                        }
                        ,
                    void 0 !== t && ("string" == typeof t ? t.match(/^[0-2].[0-9.]+$/) ? this.setValueOidString(t) : this.setValueName(t) : void 0 !== t.oid ? this.setValueOidString(t.oid) : void 0 !== t.hex ? this.setValueHex(t.hex) : void 0 !== t.name && this.setValueName(t.name))
                }
                ,
                tt.lang.extend(et.asn1.DERObjectIdentifier, et.asn1.ASN1Object),
                et.asn1.DEREnumerated = function (t) {
                    et.asn1.DEREnumerated.superclass.constructor.call(this),
                        this.hT = "0a",
                        this.setByBigInteger = function (t) {
                            this.hTLV = null,
                                this.isModified = !0,
                                this.hV = et.asn1.ASN1Util.bigIntToMinTwosComplementsHex(t)
                        }
                        ,
                        this.setByInteger = function (t) {
                            var e = new k(String(t), 10);
                            this.setByBigInteger(e)
                        }
                        ,
                        this.setValueHex = function (t) {
                            this.hV = t
                        }
                        ,
                        this.getFreshValueHex = function () {
                            return this.hV
                        }
                        ,
                    void 0 !== t && (void 0 !== t.int ? this.setByInteger(t.int) : "number" == typeof t ? this.setByInteger(t) : void 0 !== t.hex && this.setValueHex(t.hex))
                }
                ,
                tt.lang.extend(et.asn1.DEREnumerated, et.asn1.ASN1Object),
                et.asn1.DERUTF8String = function (t) {
                    et.asn1.DERUTF8String.superclass.constructor.call(this, t),
                        this.hT = "0c"
                }
                ,
                tt.lang.extend(et.asn1.DERUTF8String, et.asn1.DERAbstractString),
                et.asn1.DERNumericString = function (t) {
                    et.asn1.DERNumericString.superclass.constructor.call(this, t),
                        this.hT = "12"
                }
                ,
                tt.lang.extend(et.asn1.DERNumericString, et.asn1.DERAbstractString),
                et.asn1.DERPrintableString = function (t) {
                    et.asn1.DERPrintableString.superclass.constructor.call(this, t),
                        this.hT = "13"
                }
                ,
                tt.lang.extend(et.asn1.DERPrintableString, et.asn1.DERAbstractString),
                et.asn1.DERTeletexString = function (t) {
                    et.asn1.DERTeletexString.superclass.constructor.call(this, t),
                        this.hT = "14"
                }
                ,
                tt.lang.extend(et.asn1.DERTeletexString, et.asn1.DERAbstractString),
                et.asn1.DERIA5String = function (t) {
                    et.asn1.DERIA5String.superclass.constructor.call(this, t),
                        this.hT = "16"
                }
                ,
                tt.lang.extend(et.asn1.DERIA5String, et.asn1.DERAbstractString),
                et.asn1.DERUTCTime = function (t) {
                    et.asn1.DERUTCTime.superclass.constructor.call(this, t),
                        this.hT = "17",
                        this.setByDate = function (t) {
                            this.hTLV = null,
                                this.isModified = !0,
                                this.date = t,
                                this.s = this.formatDate(this.date, "utc"),
                                this.hV = stohex(this.s)
                        }
                        ,
                        this.getFreshValueHex = function () {
                            return void 0 === this.date && void 0 === this.s && (this.date = new Date,
                                this.s = this.formatDate(this.date, "utc"),
                                this.hV = stohex(this.s)),
                                this.hV
                        }
                        ,
                    void 0 !== t && (void 0 !== t.str ? this.setString(t.str) : "string" == typeof t && t.match(/^[0-9]{12}Z$/) ? this.setString(t) : void 0 !== t.hex ? this.setStringHex(t.hex) : void 0 !== t.date && this.setByDate(t.date))
                }
                ,
                tt.lang.extend(et.asn1.DERUTCTime, et.asn1.DERAbstractTime),
                et.asn1.DERGeneralizedTime = function (t) {
                    et.asn1.DERGeneralizedTime.superclass.constructor.call(this, t),
                        this.hT = "18",
                        this.withMillis = !1,
                        this.setByDate = function (t) {
                            this.hTLV = null,
                                this.isModified = !0,
                                this.date = t,
                                this.s = this.formatDate(this.date, "gen", this.withMillis),
                                this.hV = stohex(this.s)
                        }
                        ,
                        this.getFreshValueHex = function () {
                            return void 0 === this.date && void 0 === this.s && (this.date = new Date,
                                this.s = this.formatDate(this.date, "gen", this.withMillis),
                                this.hV = stohex(this.s)),
                                this.hV
                        }
                        ,
                    void 0 !== t && (void 0 !== t.str ? this.setString(t.str) : "string" == typeof t && t.match(/^[0-9]{14}Z$/) ? this.setString(t) : void 0 !== t.hex ? this.setStringHex(t.hex) : void 0 !== t.date && this.setByDate(t.date),
                    !0 === t.millis && (this.withMillis = !0))
                }
                ,
                tt.lang.extend(et.asn1.DERGeneralizedTime, et.asn1.DERAbstractTime),
                et.asn1.DERSequence = function (t) {
                    et.asn1.DERSequence.superclass.constructor.call(this, t),
                        this.hT = "30",
                        this.getFreshValueHex = function () {
                            for (var t = "", e = 0; e < this.asn1Array.length; e++) {
                                var n = this.asn1Array[e];
                                t += n.getEncodedHex()
                            }
                            return this.hV = t,
                                this.hV
                        }
                }
                ,
                tt.lang.extend(et.asn1.DERSequence, et.asn1.DERAbstractStructured),
                et.asn1.DERSet = function (t) {
                    et.asn1.DERSet.superclass.constructor.call(this, t),
                        this.hT = "31",
                        this.sortFlag = !0,
                        this.getFreshValueHex = function () {
                            for (var t = new Array, e = 0; e < this.asn1Array.length; e++) {
                                var n = this.asn1Array[e];
                                t.push(n.getEncodedHex())
                            }
                            return 1 == this.sortFlag && t.sort(),
                                this.hV = t.join(""),
                                this.hV
                        }
                        ,
                    void 0 !== t && void 0 !== t.sortflag && 0 == t.sortflag && (this.sortFlag = !1)
                }
                ,
                tt.lang.extend(et.asn1.DERSet, et.asn1.DERAbstractStructured),
                et.asn1.DERTaggedObject = function (t) {
                    et.asn1.DERTaggedObject.superclass.constructor.call(this),
                        this.hT = "a0",
                        this.hV = "",
                        this.isExplicit = !0,
                        this.asn1Object = null,
                        this.setASN1Object = function (t, e, n) {
                            this.hT = e,
                                this.isExplicit = t,
                                this.asn1Object = n,
                                this.isExplicit ? (this.hV = this.asn1Object.getEncodedHex(),
                                    this.hTLV = null,
                                    this.isModified = !0) : (this.hV = null,
                                    this.hTLV = n.getEncodedHex(),
                                    this.hTLV = this.hTLV.replace(/^../, e),
                                    this.isModified = !1)
                        }
                        ,
                        this.getFreshValueHex = function () {
                            return this.hV
                        }
                        ,
                    void 0 !== t && (void 0 !== t.tag && (this.hT = t.tag),
                    void 0 !== t.explicit && (this.isExplicit = t.explicit),
                    void 0 !== t.obj && (this.asn1Object = t.obj,
                        this.setASN1Object(this.isExplicit, this.hT, this.asn1Object)))
                }
                ,
                tt.lang.extend(et.asn1.DERTaggedObject, et.asn1.ASN1Object);
            var nt = function (n) {
                function i(t) {
                    var e = n.call(this) || this;
                    return t && ("string" == typeof t ? e.parseKey(t) : (i.hasPrivateKeyProperty(t) || i.hasPublicKeyProperty(t)) && e.parsePropertiesFrom(t)),
                        e
                }

                return function (t, e) {
                    function n() {
                        this.constructor = t
                    }

                    f(t, e),
                        t.prototype = null === e ? Object.create(e) : (n.prototype = e.prototype,
                            new n)
                }(i, n),
                    i.prototype.parseKey = function (t) {
                        try {
                            var e = 0
                                , n = 0
                                , i = /^\s*(?:[0-9A-Fa-f][0-9A-Fa-f]\s*)+$/.test(t) ? g.decode(t) : m.unarmor(t)
                                , r = E.decode(i);
                            if (3 === r.sub.length && (r = r.sub[2].sub[0]),
                            9 === r.sub.length) {
                                e = r.sub[1].getHexStringValue(),
                                    this.n = L(e, 16),
                                    n = r.sub[2].getHexStringValue(),
                                    this.e = parseInt(n, 16);
                                var o = r.sub[3].getHexStringValue();
                                this.d = L(o, 16);
                                var a = r.sub[4].getHexStringValue();
                                this.p = L(a, 16);
                                var s = r.sub[5].getHexStringValue();
                                this.q = L(s, 16);
                                var c = r.sub[6].getHexStringValue();
                                this.dmp1 = L(c, 16);
                                var l = r.sub[7].getHexStringValue();
                                this.dmq1 = L(l, 16);
                                var u = r.sub[8].getHexStringValue();
                                this.coeff = L(u, 16)
                            } else {
                                if (2 !== r.sub.length)
                                    return !1;
                                var h = r.sub[1]
                                    , d = h.sub[0];
                                e = d.sub[0].getHexStringValue(),
                                    this.n = L(e, 16),
                                    n = d.sub[1].getHexStringValue(),
                                    this.e = parseInt(n, 16)
                            }
                            return !0
                        } catch (t) {
                            return !1
                        }
                    }
                    ,
                    i.prototype.getPrivateBaseKey = function () {
                        var t = {
                            array: [new et.asn1.DERInteger({
                                int: 0
                            }), new et.asn1.DERInteger({
                                bigint: this.n
                            }), new et.asn1.DERInteger({
                                int: this.e
                            }), new et.asn1.DERInteger({
                                bigint: this.d
                            }), new et.asn1.DERInteger({
                                bigint: this.p
                            }), new et.asn1.DERInteger({
                                bigint: this.q
                            }), new et.asn1.DERInteger({
                                bigint: this.dmp1
                            }), new et.asn1.DERInteger({
                                bigint: this.dmq1
                            }), new et.asn1.DERInteger({
                                bigint: this.coeff
                            })]
                        }
                            , e = new et.asn1.DERSequence(t);
                        return e.getEncodedHex()
                    }
                    ,
                    i.prototype.getPrivateBaseKeyB64 = function () {
                        return u(this.getPrivateBaseKey())
                    }
                    ,
                    i.prototype.getPublicBaseKey = function () {
                        var t = new et.asn1.DERSequence({
                            array: [new et.asn1.DERObjectIdentifier({
                                oid: "1.2.840.113549.1.1.1"
                            }), new et.asn1.DERNull]
                        })
                            , e = new et.asn1.DERSequence({
                            array: [new et.asn1.DERInteger({
                                bigint: this.n
                            }), new et.asn1.DERInteger({
                                int: this.e
                            })]
                        })
                            , n = new et.asn1.DERBitString({
                            hex: "00" + e.getEncodedHex()
                        })
                            , i = new et.asn1.DERSequence({
                            array: [t, n]
                        });
                        return i.getEncodedHex()
                    }
                    ,
                    i.prototype.getPublicBaseKeyB64 = function () {
                        return u(this.getPublicBaseKey())
                    }
                    ,
                    i.wordwrap = function (t, e) {
                        if (e = e || 64,
                            !t)
                            return t;
                        var n = "(.{1," + e + "})( +|$\n?)|(.{1," + e + "})";
                        return t.match(RegExp(n, "g")).join("\n")
                    }
                    ,
                    i.prototype.getPrivateKey = function () {
                        var t = "-----BEGIN RSA PRIVATE KEY-----\n";
                        return t += i.wordwrap(this.getPrivateBaseKeyB64()) + "\n",
                            t += "-----END RSA PRIVATE KEY-----"
                    }
                    ,
                    i.prototype.getPublicKey = function () {
                        var t = "-----BEGIN PUBLIC KEY-----\n";
                        return t += i.wordwrap(this.getPublicBaseKeyB64()) + "\n",
                            t += "-----END PUBLIC KEY-----"
                    }
                    ,
                    i.hasPublicKeyProperty = function (t) {
                        return (t = t || {}).hasOwnProperty("n") && t.hasOwnProperty("e")
                    }
                    ,
                    i.hasPrivateKeyProperty = function (t) {
                        return (t = t || {}).hasOwnProperty("n") && t.hasOwnProperty("e") && t.hasOwnProperty("d") && t.hasOwnProperty("p") && t.hasOwnProperty("q") && t.hasOwnProperty("dmp1") && t.hasOwnProperty("dmq1") && t.hasOwnProperty("coeff")
                    }
                    ,
                    i.prototype.parsePropertiesFrom = function (t) {
                        this.n = t.n,
                            this.e = t.e,
                        t.hasOwnProperty("d") && (this.d = t.d,
                            this.p = t.p,
                            this.q = t.q,
                            this.dmp1 = t.dmp1,
                            this.dmq1 = t.dmq1,
                            this.coeff = t.coeff)
                    }
                    ,
                    i
            }(J)
                , it = function () {
                function t(t) {
                    t = t || {},
                        this.default_key_size = parseInt(t.default_key_size, 10) || 1024,
                        this.default_public_exponent = t.default_public_exponent || "010001",
                        this.log = t.log || !1,
                        this.key = null
                }

                return t.prototype.setKey = function (t) {
                    this.log && this.key,
                        this.key = new nt(t)
                }
                    ,
                    t.prototype.setPrivateKey = function (t) {
                        this.setKey(t)
                    }
                    ,
                    t.prototype.setPublicKey = function (t) {
                        this.setKey(t)
                    }
                    ,
                    t.prototype.decrypt = function (t) {
                        try {
                            return this.getKey().decrypt(h(t))
                        } catch (t) {
                            return !1
                        }
                    }
                    ,
                    t.prototype.encrypt = function (t) {
                        try {
                            return u(this.getKey().encrypt(t))
                        } catch (t) {
                            return !1
                        }
                    }
                    ,
                    t.prototype.sign = function (t, e, n) {
                        try {
                            return u(this.getKey().sign(t, e, n))
                        } catch (t) {
                            return !1
                        }
                    }
                    ,
                    t.prototype.verify = function (t, e, n) {
                        try {
                            return this.getKey().verify(t, h(e), n)
                        } catch (t) {
                            return !1
                        }
                    }
                    ,
                    t.prototype.getKey = function (t) {
                        if (!this.key) {
                            if (this.key = new nt,
                            t && "[object Function]" === {}.toString.call(t))
                                return void this.key.generateAsync(this.default_key_size, this.default_public_exponent, t);
                            this.key.generate(this.default_key_size, this.default_public_exponent)
                        }
                        return this.key
                    }
                    ,
                    t.prototype.getPrivateKey = function () {
                        return this.getKey().getPrivateKey()
                    }
                    ,
                    t.prototype.getPrivateKeyB64 = function () {
                        return this.getKey().getPrivateBaseKeyB64()
                    }
                    ,
                    t.prototype.getPublicKey = function () {
                        return this.getKey().getPublicKey()
                    }
                    ,
                    t.prototype.getPublicKeyB64 = function () {
                        return this.getKey().getPublicBaseKeyB64()
                    }
                    ,
                    t.version = "3.0.0-rc.1",
                    t
            }();
            window.JSEncrypt = it,
                t.JSEncrypt = it,
                t.default = it,
                Object.defineProperty(t, "__esModule", {
                    value: !0
                })
        }(e)
    },
    20: function (H, F, K) {
        var Y;
        !function (r, h) {
            "use strict";

            function t(t) {
                for (var e = {}, n = 0; n < t.length; n++)
                    e[t[n].toUpperCase()] = t[n];
                return e
            }

            function o(t, e) {
                return typeof t == l && -1 !== P(e).indexOf(P(t))
            }

            function a(t, e) {
                if (typeof t == l)
                    return t = t.replace(/^\s\s*/, "").replace(/\s\s*$/, ""),
                        typeof e == c ? t : t.substring(0, 255)
            }

            function s(t, e) {
                for (var n, i, r, o, a, s, c = 0; c < e.length && !a;) {
                    var l = e[c]
                        , u = e[c + 1];
                    for (n = i = 0; n < l.length && !a;)
                        if (a = l[n++].exec(t))
                            for (r = 0; r < u.length; r++)
                                s = a[++i],
                                    typeof (o = u[r]) == f && 0 < o.length ? 2 === o.length ? typeof o[1] == d ? this[o[0]] = o[1].call(this, s) : this[o[0]] = o[1] : 3 === o.length ? typeof o[1] != d || o[1].exec && o[1].test ? this[o[0]] = s ? s.replace(o[1], o[2]) : h : this[o[0]] = s ? o[1].call(this, s, o[2]) : h : 4 === o.length && (this[o[0]] = s ? o[3].call(this, s.replace(o[1], o[2])) : h) : this[o] = s || h;
                    c += 2
                }
            }

            function e(t, e) {
                for (var n in e)
                    if (typeof e[n] == f && 0 < e[n].length) {
                        for (var i = 0; i < e[n].length; i++)
                            if (o(e[n][i], t))
                                return "?" === n ? h : n
                    } else if (o(e[n], t))
                        return "?" === n ? h : n;
                return t
            }

            var d = "function"
                , c = "undefined"
                , f = "object"
                , l = "string"
                , u = "model"
                , p = "name"
                , g = "type"
                , m = "vendor"
                , v = "version"
                , y = "architecture"
                , n = "console"
                , i = "mobile"
                , b = "tablet"
                , w = "smarttv"
                , _ = "wearable"
                , x = "embedded"
                , T = "Amazon"
                , D = "Apple"
                , E = "BlackBerry"
                , S = "Browser"
                , A = "Chrome"
                , M = "Firefox"
                , k = "Google"
                , N = "Microsoft"
                , I = "Motorola"
                , C = "Opera"
                , j = "Samsung"
                , O = "Sony"
                , L = "Zebra"
                , R = "Facebook"
                , P = function (t) {
                return t.toLowerCase()
            }
                , B = {
                ME: "4.90",
                "NT 3.11": "NT3.51",
                "NT 4.0": "NT4.0",
                2e3: "NT 5.0",
                XP: ["NT 5.1", "NT 5.2"],
                Vista: "NT 6.0",
                7: "NT 6.1",
                8: "NT 6.2",
                8.1: "NT 6.3",
                10: ["NT 6.4", "NT 10.0"],
                RT: "ARM"
            }
                , q = {
                browser: [[/\b(?:crmo|crios)\/([\w\.]+)/i], [v, [p, "Chrome"]], [/edg(?:e|ios|a)?\/([\w\.]+)/i], [v, [p, "Edge"]], [/(opera mini)\/([-\w\.]+)/i, /(opera [mobiletab]{3,6})\b.+version\/([-\w\.]+)/i, /(opera)(?:.+version\/|[\/ ]+)([\w\.]+)/i], [p, v], [/opios[\/ ]+([\w\.]+)/i], [v, [p, C + " Mini"]], [/\bopr\/([\w\.]+)/i], [v, [p, C]], [/(kindle)\/([\w\.]+)/i, /(lunascape|maxthon|netfront|jasmine|blazer)[\/ ]?([\w\.]*)/i, /(avant |iemobile|slim)(?:browser)?[\/ ]?([\w\.]*)/i, /(ba?idubrowser)[\/ ]?([\w\.]+)/i, /(?:ms|\()(ie) ([\w\.]+)/i, /(flock|rockmelt|midori|epiphany|silk|skyfire|ovibrowser|bolt|iron|vivaldi|iridium|phantomjs|bowser|quark|qupzilla|falkon|rekonq|puffin|brave|whale|qqbrowserlite|qq)\/([-\w\.]+)/i, /(weibo)__([\d\.]+)/i], [p, v], [/(?:\buc? ?browser|(?:juc.+)ucweb)[\/ ]?([\w\.]+)/i], [v, [p, "UC" + S]], [/\bqbcore\/([\w\.]+)/i], [v, [p, "WeChat(Win) Desktop"]], [/micromessenger\/([\w\.]+)/i], [v, [p, "WeChat"]], [/konqueror\/([\w\.]+)/i], [v, [p, "Konqueror"]], [/trident.+rv[: ]([\w\.]{1,9})\b.+like gecko/i], [v, [p, "IE"]], [/yabrowser\/([\w\.]+)/i], [v, [p, "Yandex"]], [/(avast|avg)\/([\w\.]+)/i], [[p, /(.+)/, "$1 Secure " + S], v], [/\bfocus\/([\w\.]+)/i], [v, [p, M + " Focus"]], [/\bopt\/([\w\.]+)/i], [v, [p, C + " Touch"]], [/coc_coc\w+\/([\w\.]+)/i], [v, [p, "Coc Coc"]], [/dolfin\/([\w\.]+)/i], [v, [p, "Dolphin"]], [/coast\/([\w\.]+)/i], [v, [p, C + " Coast"]], [/miuibrowser\/([\w\.]+)/i], [v, [p, "MIUI " + S]], [/fxios\/([-\w\.]+)/i], [v, [p, M]], [/\bqihu|(qi?ho?o?|360)browser/i], [[p, "360 " + S]], [/(oculus|samsung|sailfish)browser\/([\w\.]+)/i], [[p, /(.+)/, "$1 " + S], v], [/(comodo_dragon)\/([\w\.]+)/i], [[p, /_/g, " "], v], [/(electron)\/([\w\.]+) safari/i, /(tesla)(?: qtcarbrowser|\/(20\d\d\.[-\w\.]+))/i, /m?(qqbrowser|baiduboxapp|2345Explorer)[\/ ]?([\w\.]+)/i], [p, v], [/(metasr)[\/ ]?([\w\.]+)/i, /(lbbrowser)/i], [p], [/((?:fban\/fbios|fb_iab\/fb4a)(?!.+fbav)|;fbav\/([\w\.]+);)/i], [[p, R], v], [/safari (line)\/([\w\.]+)/i, /\b(line)\/([\w\.]+)\/iab/i, /(chromium|instagram)[\/ ]([-\w\.]+)/i], [p, v], [/\bgsa\/([\w\.]+) .*safari\//i], [v, [p, "GSA"]], [/headlesschrome(?:\/([\w\.]+)| )/i], [v, [p, A + " Headless"]], [/ wv\).+(chrome)\/([\w\.]+)/i], [[p, A + " WebView"], v], [/droid.+ version\/([\w\.]+)\b.+(?:mobile safari|safari)/i], [v, [p, "Android " + S]], [/(chrome|omniweb|arora|[tizenoka]{5} ?browser)\/v?([\w\.]+)/i], [p, v], [/version\/([\w\.]+) .*mobile\/\w+ (safari)/i], [v, [p, "Mobile Safari"]], [/version\/([\w\.]+) .*(mobile ?safari|safari)/i], [v, p], [/webkit.+?(mobile ?safari|safari)(\/[\w\.]+)/i], [p, [v, e, {
                    "1.0": "/8",
                    1.2: "/1",
                    1.3: "/3",
                    "2.0": "/412",
                    "2.0.2": "/416",
                    "2.0.3": "/417",
                    "2.0.4": "/419",
                    "?": "/"
                }]], [/(webkit|khtml)\/([\w\.]+)/i], [p, v], [/(navigator|netscape\d?)\/([-\w\.]+)/i], [[p, "Netscape"], v], [/mobile vr; rv:([\w\.]+)\).+firefox/i], [v, [p, M + " Reality"]], [/ekiohf.+(flow)\/([\w\.]+)/i, /(swiftfox)/i, /(icedragon|iceweasel|camino|chimera|fennec|maemo browser|minimo|conkeror|klar)[\/ ]?([\w\.\+]+)/i, /(seamonkey|k-meleon|icecat|iceape|firebird|phoenix|palemoon|basilisk|waterfox)\/([-\w\.]+)$/i, /(firefox)\/([\w\.]+)/i, /(mozilla)\/([\w\.]+) .+rv\:.+gecko\/\d+/i, /(polaris|lynx|dillo|icab|doris|amaya|w3m|netsurf|sleipnir|obigo|mosaic|(?:go|ice|up)[\. ]?browser)[-\/ ]?v?([\w\.]+)/i, /(links) \(([\w\.]+)/i], [p, v]],
                cpu: [[/(?:(amd|x(?:(?:86|64)[-_])?|wow|win)64)[;\)]/i], [[y, "amd64"]], [/(ia32(?=;))/i], [[y, P]], [/((?:i[346]|x)86)[;\)]/i], [[y, "ia32"]], [/\b(aarch64|arm(v?8e?l?|_?64))\b/i], [[y, "arm64"]], [/\b(arm(?:v[67])?ht?n?[fl]p?)\b/i], [[y, "armhf"]], [/windows (ce|mobile); ppc;/i], [[y, "arm"]], [/((?:ppc|powerpc)(?:64)?)(?: mac|;|\))/i], [[y, /ower/, "", P]], [/(sun4\w)[;\)]/i], [[y, "sparc"]], [/((?:avr32|ia64(?=;))|68k(?=\))|\barm(?=v(?:[1-7]|[5-7]1)l?|;|eabi)|(?=atmel )avr|(?:irix|mips|sparc)(?:64)?\b|pa-risc)/i], [[y, P]]],
                device: [[/\b(sch-i[89]0\d|shw-m380s|sm-[pt]\w{2,4}|gt-[pn]\d{2,4}|sgh-t8[56]9|nexus 10)/i], [u, [m, j], [g, b]], [/\b((?:s[cgp]h|gt|sm)-\w+|galaxy nexus)/i, /samsung[- ]([-\w]+)/i, /sec-(sgh\w+)/i], [u, [m, j], [g, i]], [/\((ip(?:hone|od)[\w ]*);/i], [u, [m, D], [g, i]], [/\((ipad);[-\w\),; ]+apple/i, /applecoremedia\/[\w\.]+ \((ipad)/i, /\b(ipad)\d\d?,\d\d?[;\]].+ios/i], [u, [m, D], [g, b]], [/\b((?:ag[rs][23]?|bah2?|sht?|btv)-a?[lw]\d{2})\b(?!.+d\/s)/i], [u, [m, "Huawei"], [g, b]], [/(?:huawei|honor)([-\w ]+)[;\)]/i, /\b(nexus 6p|\w{2,4}-[atu]?[ln][01259x][012359][an]?)\b(?!.+d\/s)/i], [u, [m, "Huawei"], [g, i]], [/\b(poco[\w ]+)(?: bui|\))/i, /\b; (\w+) build\/hm\1/i, /\b(hm[-_ ]?note?[_ ]?(?:\d\w)?) bui/i, /\b(redmi[\-_ ]?(?:note|k)?[\w_ ]+)(?: bui|\))/i, /\b(mi[-_ ]?(?:a\d|one|one[_ ]plus|note lte|max)?[_ ]?(?:\d?\w?)[_ ]?(?:plus|se|lite)?)(?: bui|\))/i], [[u, /_/g, " "], [m, "Xiaomi"], [g, i]], [/\b(mi[-_ ]?(?:pad)(?:[\w_ ]+))(?: bui|\))/i], [[u, /_/g, " "], [m, "Xiaomi"], [g, b]], [/; (\w+) bui.+ oppo/i, /\b(cph[12]\d{3}|p(?:af|c[al]|d\w|e[ar])[mt]\d0|x9007|a101op)\b/i], [u, [m, "OPPO"], [g, i]], [/vivo (\w+)(?: bui|\))/i, /\b(v[12]\d{3}\w?[at])(?: bui|;)/i], [u, [m, "Vivo"], [g, i]], [/\b(rmx[12]\d{3})(?: bui|;|\))/i], [u, [m, "Realme"], [g, i]], [/\b(milestone|droid(?:[2-4x]| (?:bionic|x2|pro|razr))?:?( 4g)?)\b[\w ]+build\//i, /\bmot(?:orola)?[- ](\w*)/i, /((?:moto[\w\(\) ]+|xt\d{3,4}|nexus 6)(?= bui|\)))/i], [u, [m, I], [g, i]], [/\b(mz60\d|xoom[2 ]{0,2}) build\//i], [u, [m, I], [g, b]], [/((?=lg)?[vl]k\-?\d{3}) bui| 3\.[-\w; ]{10}lg?-([06cv9]{3,4})/i], [u, [m, "LG"], [g, b]], [/(lm(?:-?f100[nv]?|-[\w\.]+)(?= bui|\))|nexus [45])/i, /\blg[-e;\/ ]+((?!browser|netcast|android tv)\w+)/i, /\blg-?([\d\w]+) bui/i], [u, [m, "LG"], [g, i]], [/(ideatab[-\w ]+)/i, /lenovo ?(s[56]000[-\w]+|tab(?:[\w ]+)|yt[-\d\w]{6}|tb[-\d\w]{6})/i], [u, [m, "Lenovo"], [g, b]], [/(?:maemo|nokia).*(n900|lumia \d+)/i, /nokia[-_ ]?([-\w\.]*)/i], [[u, /_/g, " "], [m, "Nokia"], [g, i]], [/(pixel c)\b/i], [u, [m, k], [g, b]], [/droid.+; (pixel[\daxl ]{0,6})(?: bui|\))/i], [u, [m, k], [g, i]], [/droid.+ ([c-g]\d{4}|so[-gl]\w+|xq-a\w[4-7][12])(?= bui|\).+chrome\/(?![1-6]{0,1}\d\.))/i], [u, [m, O], [g, i]], [/sony tablet [ps]/i, /\b(?:sony)?sgp\w+(?: bui|\))/i], [[u, "Xperia Tablet"], [m, O], [g, b]], [/ (kb2005|in20[12]5|be20[12][59])\b/i, /(?:one)?(?:plus)? (a\d0\d\d)(?: b|\))/i], [u, [m, "OnePlus"], [g, i]], [/(alexa)webm/i, /(kf[a-z]{2}wi)( bui|\))/i, /(kf[a-z]+)( bui|\)).+silk\//i], [u, [m, T], [g, b]], [/((?:sd|kf)[0349hijorstuw]+)( bui|\)).+silk\//i], [[u, /(.+)/g, "Fire Phone $1"], [m, T], [g, i]], [/(playbook);[-\w\),; ]+(rim)/i], [u, m, [g, b]], [/\b((?:bb[a-f]|st[hv])100-\d)/i, /\(bb10; (\w+)/i], [u, [m, E], [g, i]], [/(?:\b|asus_)(transfo[prime ]{4,10} \w+|eeepc|slider \w+|nexus 7|padfone|p00[cj])/i], [u, [m, "ASUS"], [g, b]], [/ (z[bes]6[027][012][km][ls]|zenfone \d\w?)\b/i], [u, [m, "ASUS"], [g, i]], [/(nexus 9)/i], [u, [m, "HTC"], [g, b]], [/(htc)[-;_ ]{1,2}([\w ]+(?=\)| bui)|\w+)/i, /(zte)[- ]([\w ]+?)(?: bui|\/|\))/i, /(alcatel|geeksphone|nexian|panasonic|sony)[-_ ]?([-\w]*)/i], [m, [u, /_/g, " "], [g, i]], [/droid.+; ([ab][1-7]-?[0178a]\d\d?)/i], [u, [m, "Acer"], [g, b]], [/droid.+; (m[1-5] note) bui/i, /\bmz-([-\w]{2,})/i], [u, [m, "Meizu"], [g, i]], [/\b(sh-?[altvz]?\d\d[a-ekm]?)/i], [u, [m, "Sharp"], [g, i]], [/(blackberry|benq|palm(?=\-)|sonyericsson|acer|asus|dell|meizu|motorola|polytron)[-_ ]?([-\w]*)/i, /(hp) ([\w ]+\w)/i, /(asus)-?(\w+)/i, /(microsoft); (lumia[\w ]+)/i, /(lenovo)[-_ ]?([-\w]+)/i, /(jolla)/i, /(oppo) ?([\w ]+) bui/i], [m, u, [g, i]], [/(archos) (gamepad2?)/i, /(hp).+(touchpad(?!.+tablet)|tablet)/i, /(kindle)\/([\w\.]+)/i, /(nook)[\w ]+build\/(\w+)/i, /(dell) (strea[kpr\d ]*[\dko])/i, /(le[- ]+pan)[- ]+(\w{1,9}) bui/i, /(trinity)[- ]*(t\d{3}) bui/i, /(gigaset)[- ]+(q\w{1,9}) bui/i, /(vodafone) ([\w ]+)(?:\)| bui)/i], [m, u, [g, b]], [/(surface duo)/i], [u, [m, N], [g, b]], [/droid [\d\.]+; (fp\du?)(?: b|\))/i], [u, [m, "Fairphone"], [g, i]], [/(u304aa)/i], [u, [m, "AT&T"], [g, i]], [/\bsie-(\w*)/i], [u, [m, "Siemens"], [g, i]], [/\b(rct\w+) b/i], [u, [m, "RCA"], [g, b]], [/\b(venue[\d ]{2,7}) b/i], [u, [m, "Dell"], [g, b]], [/\b(q(?:mv|ta)\w+) b/i], [u, [m, "Verizon"], [g, b]], [/\b(?:barnes[& ]+noble |bn[rt])([\w\+ ]*) b/i], [u, [m, "Barnes & Noble"], [g, b]], [/\b(tm\d{3}\w+) b/i], [u, [m, "NuVision"], [g, b]], [/\b(k88) b/i], [u, [m, "ZTE"], [g, b]], [/\b(nx\d{3}j) b/i], [u, [m, "ZTE"], [g, i]], [/\b(gen\d{3}) b.+49h/i], [u, [m, "Swiss"], [g, i]], [/\b(zur\d{3}) b/i], [u, [m, "Swiss"], [g, b]], [/\b((zeki)?tb.*\b) b/i], [u, [m, "Zeki"], [g, b]], [/\b([yr]\d{2}) b/i, /\b(dragon[- ]+touch |dt)(\w{5}) b/i], [[m, "Dragon Touch"], u, [g, b]], [/\b(ns-?\w{0,9}) b/i], [u, [m, "Insignia"], [g, b]], [/\b((nxa|next)-?\w{0,9}) b/i], [u, [m, "NextBook"], [g, b]], [/\b(xtreme\_)?(v(1[045]|2[015]|[3469]0|7[05])) b/i], [[m, "Voice"], u, [g, i]], [/\b(lvtel\-)?(v1[12]) b/i], [[m, "LvTel"], u, [g, i]], [/\b(ph-1) /i], [u, [m, "Essential"], [g, i]], [/\b(v(100md|700na|7011|917g).*\b) b/i], [u, [m, "Envizen"], [g, b]], [/\b(trio[-\w\. ]+) b/i], [u, [m, "MachSpeed"], [g, b]], [/\btu_(1491) b/i], [u, [m, "Rotor"], [g, b]], [/(shield[\w ]+) b/i], [u, [m, "Nvidia"], [g, b]], [/(sprint) (\w+)/i], [m, u, [g, i]], [/(kin\.[onetw]{3})/i], [[u, /\./g, " "], [m, N], [g, i]], [/droid.+; (cc6666?|et5[16]|mc[239][23]x?|vc8[03]x?)\)/i], [u, [m, L], [g, b]], [/droid.+; (ec30|ps20|tc[2-8]\d[kx])\)/i], [u, [m, L], [g, i]], [/(ouya)/i, /(nintendo) ([wids3utch]+)/i], [m, u, [g, n]], [/droid.+; (shield) bui/i], [u, [m, "Nvidia"], [g, n]], [/(playstation [345portablevi]+)/i], [u, [m, O], [g, n]], [/\b(xbox(?: one)?(?!; xbox))[\); ]/i], [u, [m, N], [g, n]], [/smart-tv.+(samsung)/i], [m, [g, w]], [/hbbtv.+maple;(\d+)/i], [[u, /^/, "SmartTV"], [m, j], [g, w]], [/(nux; netcast.+smarttv|lg (netcast\.tv-201\d|android tv))/i], [[m, "LG"], [g, w]], [/(apple) ?tv/i], [m, [u, D + " TV"], [g, w]], [/crkey/i], [[u, A + "cast"], [m, k], [g, w]], [/droid.+aft(\w)( bui|\))/i], [u, [m, T], [g, w]], [/\(dtv[\);].+(aquos)/i], [u, [m, "Sharp"], [g, w]], [/\b(roku)[\dx]*[\)\/]((?:dvp-)?[\d\.]*)/i, /hbbtv\/\d+\.\d+\.\d+ +\([\w ]*; *(\w[^;]*);([^;]*)/i], [[m, a], [u, a], [g, w]], [/\b(android tv|smart[- ]?tv|opera tv|tv; rv:)\b/i], [[g, w]], [/((pebble))app/i], [m, u, [g, _]], [/droid.+; (glass) \d/i], [u, [m, k], [g, _]], [/droid.+; (wt63?0{2,3})\)/i], [u, [m, L], [g, _]], [/(quest( 2)?)/i], [u, [m, R], [g, _]], [/(tesla)(?: qtcarbrowser|\/[-\w\.]+)/i], [m, [g, x]], [/droid .+?; ([^;]+?)(?: bui|\) applew).+? mobile safari/i], [u, [g, i]], [/droid .+?; ([^;]+?)(?: bui|\) applew).+?(?! mobile) safari/i], [u, [g, b]], [/\b((tablet|tab)[;\/]|focus\/\d(?!.+mobile))/i], [[g, b]], [/(phone|mobile(?:[;\/]| safari)|pda(?=.+windows ce))/i], [[g, i]], [/(android[-\w\. ]{0,9});.+buil/i], [u, [m, "Generic"]]],
                engine: [[/windows.+ edge\/([\w\.]+)/i], [v, [p, "EdgeHTML"]], [/webkit\/537\.36.+chrome\/(?!27)([\w\.]+)/i], [v, [p, "Blink"]], [/(presto)\/([\w\.]+)/i, /(webkit|trident|netfront|netsurf|amaya|lynx|w3m|goanna)\/([\w\.]+)/i, /ekioh(flow)\/([\w\.]+)/i, /(khtml|tasman|links)[\/ ]\(?([\w\.]+)/i, /(icab)[\/ ]([23]\.[\d\.]+)/i], [p, v], [/rv\:([\w\.]{1,9})\b.+(gecko)/i], [v, p]],
                os: [[/microsoft (windows) (vista|xp)/i], [p, v], [/(windows) nt 6\.2; (arm)/i, /(windows (?:phone(?: os)?|mobile))[\/ ]?([\d\.\w ]*)/i, /(windows)[\/ ]?([ntce\d\. ]+\w)(?!.+xbox)/i], [p, [v, e, B]], [/(win(?=3|9|n)|win 9x )([nt\d\.]+)/i], [[p, "Windows"], [v, e, B]], [/ip[honead]{2,4}\b(?:.*os ([\w]+) like mac|; opera)/i, /cfnetwork\/.+darwin/i], [[v, /_/g, "."], [p, "iOS"]], [/(mac os x) ?([\w\. ]*)/i, /(macintosh|mac_powerpc\b)(?!.+haiku)/i], [[p, "Mac OS"], [v, /_/g, "."]], [/droid ([\w\.]+)\b.+(android[- ]x86)/i], [v, p], [/(android|webos|qnx|bada|rim tablet os|maemo|meego|sailfish)[-\/ ]?([\w\.]*)/i, /(blackberry)\w*\/([\w\.]*)/i, /(tizen|kaios)[\/ ]([\w\.]+)/i, /\((series40);/i], [p, v], [/\(bb(10);/i], [v, [p, E]], [/(?:symbian ?os|symbos|s60(?=;)|series60)[-\/ ]?([\w\.]*)/i], [v, [p, "Symbian"]], [/mozilla\/[\d\.]+ \((?:mobile|tablet|tv|mobile; [\w ]+); rv:.+ gecko\/([\w\.]+)/i], [v, [p, M + " OS"]], [/web0s;.+rt(tv)/i, /\b(?:hp)?wos(?:browser)?\/([\w\.]+)/i], [v, [p, "webOS"]], [/crkey\/([\d\.]+)/i], [v, [p, A + "cast"]], [/(cros) [\w]+ ([\w\.]+\w)/i], [[p, "Chromium OS"], v], [/(nintendo|playstation) ([wids345portablevuch]+)/i, /(xbox); +xbox ([^\);]+)/i, /\b(joli|palm)\b ?(?:os)?\/?([\w\.]*)/i, /(mint)[\/\(\) ]?(\w*)/i, /(mageia|vectorlinux)[; ]/i, /([kxln]?ubuntu|debian|suse|opensuse|gentoo|arch(?= linux)|slackware|fedora|mandriva|centos|pclinuxos|red ?hat|zenwalk|linpus|raspbian|plan 9|minix|risc os|contiki|deepin|manjaro|elementary os|sabayon|linspire)(?: gnu\/linux)?(?: enterprise)?(?:[- ]linux)?(?:-gnu)?[-\/ ]?(?!chrom|package)([-\w\.]*)/i, /(hurd|linux) ?([\w\.]*)/i, /(gnu) ?([\w\.]*)/i, /\b([-frentopcghs]{0,5}bsd|dragonfly)[\/ ]?(?!amd|[ix346]{1,2}86)([\w\.]*)/i, /(haiku) (\w+)/i], [p, v], [/(sunos) ?([\w\.\d]*)/i], [[p, "Solaris"], v], [/((?:open)?solaris)[-\/ ]?([\w\.]*)/i, /(aix) ((\d)(?=\.|\)| )[\w\.])*/i, /\b(beos|os\/2|amigaos|morphos|openvms|fuchsia|hp-ux)/i, /(unix) ?([\w\.]*)/i], [p, v]]
            }
                , z = function (t, e) {
                if (typeof t == f && (e = t,
                    t = h),
                    !(this instanceof z))
                    return new z(t, e).getResult();
                var n = t || (typeof r != c && r.navigator && r.navigator.userAgent ? r.navigator.userAgent : "")
                    , i = e ? function (t, e) {
                    var n = {};
                    for (var i in t)
                        e[i] && e[i].length % 2 == 0 ? n[i] = e[i].concat(t[i]) : n[i] = t[i];
                    return n
                }(q, e) : q;
                return this.getBrowser = function () {
                    var t = {};
                    return t[p] = h,
                        t[v] = h,
                        s.call(t, n, i.browser),
                        t.major = function (t) {
                            return typeof t == l ? t.replace(/[^\d\.]/g, "").split(".")[0] : h
                        }(t.version),
                        t
                }
                    ,
                    this.getCPU = function () {
                        var t = {};
                        return t[y] = h,
                            s.call(t, n, i.cpu),
                            t
                    }
                    ,
                    this.getDevice = function () {
                        var t = {};
                        return t[m] = h,
                            t[u] = h,
                            t[g] = h,
                            s.call(t, n, i.device),
                            t
                    }
                    ,
                    this.getEngine = function () {
                        var t = {};
                        return t[p] = h,
                            t[v] = h,
                            s.call(t, n, i.engine),
                            t
                    }
                    ,
                    this.getOS = function () {
                        var t = {};
                        return t[p] = h,
                            t[v] = h,
                            s.call(t, n, i.os),
                            t
                    }
                    ,
                    this.getResult = function () {
                        return {
                            ua: this.getUA(),
                            browser: this.getBrowser(),
                            engine: this.getEngine(),
                            os: this.getOS(),
                            device: this.getDevice(),
                            cpu: this.getCPU()
                        }
                    }
                    ,
                    this.getUA = function () {
                        return n
                    }
                    ,
                    this.setUA = function (t) {
                        return n = typeof t == l && 255 < t.length ? a(t, 255) : t,
                            this
                    }
                    ,
                    this.setUA(n),
                    this
            };
            z.VERSION = "1.0.2",
                z.BROWSER = t([p, v, "major"]),
                z.CPU = t([y]),
                z.DEVICE = t([u, m, g, n, i, w, b, _, x]),
                z.ENGINE = z.OS = t([p, v]),
                typeof F != c ? (typeof H != c && H.exports && (F = H.exports = z),
                    F.UAParser = z) : K(63) ? (Y = function () {
                    return z
                }
                    .call(F, K, F, H)) === h || (H.exports = Y) : typeof r != c && (r.UAParser = z);
            var U = typeof r != c && (r.jQuery || r.Zepto);
            if (U && !U.ua) {
                var V = new z;
                U.ua = V.getResult(),
                    U.ua.get = function () {
                        return V.getUA()
                    }
                    ,
                    U.ua.set = function (t) {
                        V.setUA(t);
                        var e = V.getResult();
                        for (var n in e)
                            U.ua[n] = e[n]
                    }
            }
        }("object" == typeof window ? window : this)
    },
    2: function (t, e, n) {
        "use strict";
        n.r(e),
            n.d(e, "makeParam", function () {
                return o
            }),
            n.d(e, "sendFee", function () {
                return i
            });
        var o = function (e) {
            var n = "";
            try {
                n = JSON.stringify(e.detail)
            } catch (t) {
                n = Object.prototype.toString.call(e.detail)
            }
            return {
                type: "error",
                common: {
                    pid: e.pid,
                    uuid: e.uuid,
                    ucid: e.ucid,
                    is_test: "test" === e.env,
                    record: {
                        time_on_page: !0,
                        performance: !0,
                        js_error: !0,
                        js_error_report_config: {
                            ERROR_RUNTIME: !0,
                            ERROR_SCRIPT: !0,
                            ERROR_STYLE: !0,
                            ERROR_IMAGE: !0,
                            ERROR_AUDIO: !0,
                            ERROR_VIDEO: !0,
                            ERROR_CONSOLE: !0,
                            ERROR_TRY_CATCH: !0
                        }
                    },
                    version: "1.0.0",
                    timestamp: Date.now(),
                    runtime_version: e.version,
                    sdk_version: "1.3.0",
                    page_type: e.pageUrl || "/"
                },
                code: 8,
                extra: {
                    desc: n
                },
                detail: {
                    error_no: e.errorName || "unknown_error",
                    url: e.pageUrl || "",
                    http_code: 0,
                    during_ms: 0,
                    request_size_b: 0,
                    response_size_b: 0
                }
            }
        }
            , i = function (t) {
            var e = t.errorName
                , n = t.detail
                , i = o({
                detail: n,
                env: /test/.test(window.location.href) ? "test" : "prod",
                errorName: e,
                pid: "pc_login_sdk",
                ucid: 1,
                uuid: "",
                version: "1.2.0"
            })
                , r = "https://dig.lianjia.com/fee.gif?d=" + encodeURIComponent(JSON.stringify(i));
            try {
                new Image(0, 0).src = r
            } catch (t) {
            }
        }
    },
    0: function (t, e, n) {
        "use strict";
        n.r(e),
            n.d(e, "scene", function () {
                return q
            }),
            n.d(e, "withCredentialDomain", function () {
                return z
            }),
            n.d(e, "APIEndpoint", function () {
                return i
            }),
            n.d(e, "PasswordAPIEndpoint", function () {
                return o
            }),
            n.d(e, "captchaDomain", function () {
                return s
            }),
            n.d(e, "captchaJSAddr", function () {
                return l
            }),
            n.d(e, "riskJSAddr", function () {
                return h
            }),
            n.d(e, "APIDomainKe", function () {
                return f
            }),
            n.d(e, "APIDomainDeyoulife", function () {
                return g
            }),
            n.d(e, "APIDomainLianjia", function () {
                return v
            }),
            n.d(e, "mainAuthMethodName", function () {
                return b
            }),
            n.d(e, "TitleEnum", function () {
                return _
            }),
            n.d(e, "allianceMethods", function () {
                return T
            }),
            n.d(e, "SupportedIdentityCheckMethodsEnum", function () {
                return E
            }),
            n.d(e, "accountSystem", function () {
                return A
            }),
            n.d(e, "smsTypeEnum", function () {
                return k
            }),
            n.d(e, "SceneKey", function () {
                return I
            }),
            n.d(e, "AuthStatus", function () {
                return j
            }),
            n.d(e, "Gender", function () {
                return L
            }),
            n.d(e, "Views", function () {
                return P
            }),
            n.d(e, "adImages", function () {
                return U
            });
        var i, r, o, a, s, c, l, u, h, d, f, p, g, m, v, y, b, w, _, x, T, D, E, S, A, M, k, N, I, C, j, O, L, R, P, B,
            q = ["0x6c", "0x6f", "0x67", "0x69", "0x6e", "0x5f", "0x73", "0x6c", "0x69", "0x64", "0x65", "0x72"].map(function (t) {
                return String.fromCharCode(Number(t))
            }).reduce(function (t, e) {
                return t + e
            }), z = ["ke.com", "lianjia.com", "deyoulife.com"];
        (r = i = i || {}).init = "/authentication/initialize",
            r.auth = "/authentication/authenticate",
            r.sms = "/authentication/mfa/sms",
            r.getinfo = "/serviceValidate",
            r.register = "/registration/register",
            r.logout = "/authentication/destroy",
            r.userLogout = "/logout",
            r.qr = "/qrcode",
            r.polling = "/qrcode/status",
            r.pollingCustomer = "/authentication/qrcode/c/query",
            (a = o = o || {}).init = "/authentication/password/initialize",
            a.change = "/authentication/password",
            a.reset = "/authentication/reset-password",
            a.validate = "/authentication/password/action/validate",
            (c = s = s || {}).dev = "//test3-captcha.lianjia.com",
            c.test = "//test3-captcha.lianjia.com",
            c.prod = "https://captcha.lianjia.com",
            c.preview = "https://captcha.lianjia.com",
            (u = l = l || {}).dev = "//test-s1.ljcdn.com/test-captcha-js-sdk-v2/captcha.js",
            u.test = "//test-s1.ljcdn.com/test-captcha-js-sdk-v2/captcha.js",
            u.prod = "https://s1.ljcdn.com/captcha-js-sdk-v2/captcha.js",
            u.preview = "https://s1.ljcdn.com/captcha-js-sdk-v2/captcha.js",
            (d = h = h || {}).dev = "//test-s1.ljcdn.lianjia.com/risk-control/static/keRiskControl.js",
            d.test = "//test-s1.ljcdn.lianjia.com/risk-control/static/keRiskControl.js",
            d.prod = "//s1.ljcdn.com/risk-control/static/keRiskControl.js",
            d.preview = "//s1.ljcdn.com/risk-control/static/keRiskControl.js",
            (p = f = f || {}).dev = "http://alps-passport.login-dev.tta.test.ke.com",
            p.test = "https://test-clogin.ke.com",
            p.prod = "https://clogin.ke.com",
            p.preview = "https://clogin.ke.com",
            (m = g = g || {}).dev = "http://alps-passport.login-dev.tta.test.ke.com",
            m.test = "https://test-clogin.ke.com",
            m.prod = "https://clogin.ke.com",
            m.preview = "https://clogin.ke.com",
            (y = v = v || {}).dev = "http://alps-passport.login-dev.tta.test.ke.com",
            y.test = "https://test-clogin.lianjia.com",
            y.prod = "https://clogin.lianjia.com",
            y.preview = "https://clogin.lianjia.com",
            (w = b = b || {}).PASSWORD = "username-password",
            w.QR = "qrcode",
            w.PHONE = "phone-code",
            (x = _ = _ || {})["username-password"] = "账号密码登录",
            x.qrcode = "二维码登录",
            x["phone-code"] = "短信验证码登录",
            (D = T = T || {}).security = "security-code",
            D.shield = "shield-code",
            (S = E = E || {}).id_num = "id-num",
            S.security_code = "security-code",
            S.old_password = "old-password",
            S.security_code_id_num = "security-code&id-num",
            (M = A = A || {}).commerceSeller = "commerce-seller",
            M.customer = "customer",
            M.employee = "employee",
            M.guangsha = "guangsha",
            M.rentSaas = "rent-saas",
            (N = k = k || {}).sms = "sms",
            N.voice = "voice",
            (C = I = I || {}).DEFAULT = "DEFAULT",
            C.WHEN_LOGIN = "WHEN_LOGIN",
            C.WHEN_VALIDATE_PASSWORD = "WHEN_VALIDATE_PASSWORD",
            C.WHEN_REGISTER = "WHEN_REGISTER",
            C.WHEN_RESET_PASSWORD = "WHEN_RESET_PASSWORD",
            C.WHEN_LOGOUT = "WHEN_LOGOUT",
            C.WHEN_SEND_SMS = "WHEN_SEND_SMS",
            C.WHEN_RESET_PASSWORD_SEND_SMS = "WHEN_RESET_PASSWORD_SEND_SMS",
            (O = j = j || {}).PASS = "PASS",
            O.WARN = "WARN",
            (R = L = L || {}).MALE = "MALE",
            R.FEMALE = "FEMALE",
            (B = P = P || {})[B.passwordlogin = 0] = "passwordlogin",
            B[B.smslogin = 1] = "smslogin",
            B[B.resetpassword = 2] = "resetpassword",
            B[B.register = 3] = "register",
            e.default = {
                scene: q,
                APIEndpoint: i,
                PasswordAPIEndpoint: o,
                captchaDomain: s,
                captchaJSAddr: l,
                mainAuthMethodName: b,
                TitleEnum: _,
                allianceMethods: T,
                accountSystem: A,
                Gender: L,
                SceneKey: I,
                AuthStatus: j,
                APIDomainKe: f,
                APIDomainLianjia: v,
                Views: P
            };
        var U = {
            ke: "https://file.ljcdn.com/nebula/ad_ke_1700530046970.png",
            lianjia: "https://file.ljcdn.com/nebula/ad_lianjia_1700530046973.png"
        }
    },
    1: function (t, e, n) {
        "use strict";
        n.r(e),
            n.d(e, "loadScriptWithPromise", function () {
                return d
            }),
            n.d(e, "commonValidator", function () {
                return f
            }),
            n.d(e, "triggerInput", function () {
                return p
            }),
            n.d(e, "maskPhoneNumber", function () {
                return g
            }),
            n.d(e, "ulog", function () {
                return m
            }),
            n.d(e, "fetch", function () {
                return v
            }),
            n.d(e, "Xml2Json", function () {
                return y
            }),
            n.d(e, "parseUserInfo", function () {
                return b
            }),
            n.d(e, "cookie", function () {
                return w
            }),
            n.d(e, "getEnv", function () {
                return _
            }),
            n.d(e, "parseURL", function () {
                return x
            }),
            n.d(e, "env", function () {
                return T
            }),
            n.d(e, "plat", function () {
                return D
            }),
            n.d(e, "withCredential", function () {
                return E
            }),
            n.d(e, "getQuery", function () {
                return S
            });
        var i = n(8)
            , o = n.n(i)
            , r = n(5)
            , s = n.n(r);
        s.a.defaults.withCredentials = !0;

        function a(t) {
            var e = document.createElement("b");
            return e.innerHTML = "\x3c!--[if IE " + t + "]><i></i><![endif]--\x3e",
            1 === e.getElementsByTagName("i").length
        }

        function c(a) {
            return window.XDomainRequest ? new Promise(function (e, n) {
                    var t = a.method || "GET"
                        , i = a.timeout || 3e4
                        , r = a.data || a.params || {};
                    r instanceof Object && (r = JSON.stringify(r));
                    var o = new window.XDomainRequest;
                    o.open(t, a.url),
                        o.timeout = i,
                        o.onload = function () {
                            try {
                                var t = JSON.parse(o.responseText);
                                return e(t.data)
                            } catch (t) {
                                n(t)
                            }
                            return n({})
                        }
                        ,
                        o.onprogress = function () {
                        }
                        ,
                        o.ontimeout = function () {
                            return n("XDomainRequest timeout")
                        }
                        ,
                        o.onerror = function () {
                            return n("XDomainRequest error")
                        }
                        ,
                        setTimeout(function () {
                            o.send(r)
                        }, 0)
                }
            ) : s()(a)
        }

        var l, u, h, d = function (r) {
                return new Promise(function (t, e) {
                        var n = o()(r);
                        if (document.querySelector("#md5" + n))
                            return t(!0);
                        var i = document.createElement("script");
                        i.src = r,
                            i.id = "md5" + n,
                            i.addEventListener("load", function () {
                                t(!0)
                            }),
                            document.head.appendChild(i)
                    }
                )
            }, f = {
                mail: function (t) {
                    return /.*\@.+\..+/.test(t)
                },
                mobile: function (t) {
                    return /1\d{10}/.test(t)
                },
                pasword: function (t) {
                    return /(?!^[0-9]+$)(?!^[A-Za-z]+$)(?!^[_\-+=(){},.;!~'@#$%^&*]+$).{8,}/.test(t)
                }
            }, p = function (t, e) {
                var n = document.querySelector(t);
                Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set.call(n, e);
                var i = new Event("input", {
                    bubbles: !0
                });
                n.dispatchEvent(i)
            }, g = function (t) {
                return t.slice(0, 3) + "****" + t.slice(7, t.length)
            }, m = function () {
            }, v = function (t) {
                return (t.url && function (t) {
                    var e = /^(https?):\/\/([a-zA-Z\.\-\_]+)\/?(:\d+)?/.exec(t)
                        , n = /^(https?):\/\/([a-zA-Z\.\-\_]+)\/?(:\d+)?/.exec(window.location.href)
                        , i = !1;
                    return null !== e && null !== n && (i = e[1] === n[1] && e[2] === n[2] && e[3] === n[3]),
                        i
                }(t.url) && (a(9) || a(8) || a(7) || a(6) || a(5) || a(4)) ? c : s.a)(t)
            }, y = function t(e) {
                var n = {};
                if (e.nodeType === Node.ELEMENT_NODE) {
                    var i = e.attributes;
                    if (0 < i.length)
                        for (var r = 0; r < i.length; r++)
                            n["@" + i[r].nodeName] = i[r].value
                } else
                    e.nodeType === Node.TEXT_NODE && (n = "" === e.nodeValue.replace(/[\ +\r\n]/g, "") ? "" : e.nodeValue);
                if (e.hasChildNodes())
                    for (var o = e.childNodes, a = 0; a < o.length; a++) {
                        var s = o[a].nodeName;
                        if (void 0 === n[s]) {
                            "" !== (l = t(o[a])) && (n[s] = l)
                        } else {
                            if (void 0 === n[s].push) {
                                var c = n[s];
                                n[s] = [],
                                    n[s].push(c)
                            }
                            var l;
                            "" !== (l = t(o[a])) && n[s].push(l)
                        }
                    }
                return n
            }, b = function (t) {
                return {
                    username: t["cas:serviceResponse"]["cas:authenticationSuccess"]["cas:attributes"]["cas:displayName"]["#text"],
                    ucid: t["cas:serviceResponse"]["cas:authenticationSuccess"]["cas:attributes"]["cas:ucid"]["#text"]
                }
            }, w = {
                set: function (t, e, n) {
                    var i = new Date;
                    i.setTime(i.getTime() + 24 * n * 60 * 60 * 1e3);
                    var r = "expires=" + i.toUTCString();
                    document.cookie = t + "=" + e + ";" + r + ";path=/"
                },
                get: function (t) {
                    for (var e = t + "=", n = document.cookie.split(";"), i = 0; i < n.length; i++) {
                        for (var r = n[i]; " " == r.charAt(0);)
                            r = r.substring(1);
                        if (0 == r.indexOf(e))
                            return r.substring(e.length, r.length)
                    }
                    return ""
                }
            }, _ = function (t) {
                var e = x(window.location.href);
                return /dev/.test(t) || /^http:\/\/localhost/.test(e.url) || "127.0.0.1" === e.host ? "dev" : /test/.test(t) ? "test" : "prod"
            }, x = function (t) {
                if (!t)
                    return null;
                var e = ["url", "origin", "scheme", "slash", "host", "port", "path", "query", "hash"]
                    ,
                    n = /^((?:([A-Za-z]+)?:?(\/{0,3}))?([0-9.\-A-Za-z]+\.[0-9A-Za-z]+)?(?::(\d+))?)(?:\/([^?#]*))?(?:\?([^#]*))?(?:#(.*))?$/.exec(t)
                    , i = {};
                if (null !== n)
                    for (var r = 0, o = e.length; r < o; r += 1)
                        i[e[r]] = n[r] || "";
                return i
            }, T = (l = x(window.location.href).host,
                _(l)), D = (u = x(window.location.href).host,
                /lianjia/.test(u) ? "lianjia" : "ke"), E = (h = x(window.location.href).host,
                !!(/^(.*\.)?lianjia\.com/.test(h) || /^(.*\.)?ke\.com/.test(h) || /^(.*\.)?deyoulife\.com/.test(h))),
            S = function (t, e) {
                var n = new RegExp("(^|&)" + t + "=([^&]*)(&|$)", "i")
                    , i = e.split("?")[1].match(n);
                return null != i ? i[2] : null
            };
        "prod" !== T && (window.fillValueToEl || (window.fillValueToEl = function (t, e) {
                return p(e, t)
            }
        )),
            e.default = {
                loadScriptWithPromise: d,
                md5: o.a,
                triggerInput: p,
                commonValidator: f,
                maskPhoneNumber: g,
                ulog: m,
                fetch: v,
                parseUserInfo: b,
                cookie: w,
                getQuery: S
            }
    },
    8: function (t, e, n) {
        var v, y, b, w, _;
        v = n(42),
            y = n(11).utf8,
            b = n(43),
            w = n(11).bin,
            (_ = function (t, e) {
                    t.constructor == String ? t = e && "binary" === e.encoding ? w.stringToBytes(t) : y.stringToBytes(t) : b(t) ? t = Array.prototype.slice.call(t, 0) : Array.isArray(t) || (t = t.toString());
                    for (var n = v.bytesToWords(t), i = 8 * t.length, r = 1732584193, o = -271733879, a = -1732584194, s = 271733878, c = 0; c < n.length; c++)
                        n[c] = 16711935 & (n[c] << 8 | n[c] >>> 24) | 4278255360 & (n[c] << 24 | n[c] >>> 8);
                    n[i >>> 5] |= 128 << i % 32,
                        n[14 + (64 + i >>> 9 << 4)] = i;
                    var l = _._ff
                        , u = _._gg
                        , h = _._hh
                        , d = _._ii;
                    for (c = 0; c < n.length; c += 16) {
                        var f = r
                            , p = o
                            , g = a
                            , m = s;
                        o = d(o = d(o = d(o = d(o = h(o = h(o = h(o = h(o = u(o = u(o = u(o = u(o = l(o = l(o = l(o = l(o, a = l(a, s = l(s, r = l(r, o, a, s, n[c + 0], 7, -680876936), o, a, n[c + 1], 12, -389564586), r, o, n[c + 2], 17, 606105819), s, r, n[c + 3], 22, -1044525330), a = l(a, s = l(s, r = l(r, o, a, s, n[c + 4], 7, -176418897), o, a, n[c + 5], 12, 1200080426), r, o, n[c + 6], 17, -1473231341), s, r, n[c + 7], 22, -45705983), a = l(a, s = l(s, r = l(r, o, a, s, n[c + 8], 7, 1770035416), o, a, n[c + 9], 12, -1958414417), r, o, n[c + 10], 17, -42063), s, r, n[c + 11], 22, -1990404162), a = l(a, s = l(s, r = l(r, o, a, s, n[c + 12], 7, 1804603682), o, a, n[c + 13], 12, -40341101), r, o, n[c + 14], 17, -1502002290), s, r, n[c + 15], 22, 1236535329), a = u(a, s = u(s, r = u(r, o, a, s, n[c + 1], 5, -165796510), o, a, n[c + 6], 9, -1069501632), r, o, n[c + 11], 14, 643717713), s, r, n[c + 0], 20, -373897302), a = u(a, s = u(s, r = u(r, o, a, s, n[c + 5], 5, -701558691), o, a, n[c + 10], 9, 38016083), r, o, n[c + 15], 14, -660478335), s, r, n[c + 4], 20, -405537848), a = u(a, s = u(s, r = u(r, o, a, s, n[c + 9], 5, 568446438), o, a, n[c + 14], 9, -1019803690), r, o, n[c + 3], 14, -187363961), s, r, n[c + 8], 20, 1163531501), a = u(a, s = u(s, r = u(r, o, a, s, n[c + 13], 5, -1444681467), o, a, n[c + 2], 9, -51403784), r, o, n[c + 7], 14, 1735328473), s, r, n[c + 12], 20, -1926607734), a = h(a, s = h(s, r = h(r, o, a, s, n[c + 5], 4, -378558), o, a, n[c + 8], 11, -2022574463), r, o, n[c + 11], 16, 1839030562), s, r, n[c + 14], 23, -35309556), a = h(a, s = h(s, r = h(r, o, a, s, n[c + 1], 4, -1530992060), o, a, n[c + 4], 11, 1272893353), r, o, n[c + 7], 16, -155497632), s, r, n[c + 10], 23, -1094730640), a = h(a, s = h(s, r = h(r, o, a, s, n[c + 13], 4, 681279174), o, a, n[c + 0], 11, -358537222), r, o, n[c + 3], 16, -722521979), s, r, n[c + 6], 23, 76029189), a = h(a, s = h(s, r = h(r, o, a, s, n[c + 9], 4, -640364487), o, a, n[c + 12], 11, -421815835), r, o, n[c + 15], 16, 530742520), s, r, n[c + 2], 23, -995338651), a = d(a, s = d(s, r = d(r, o, a, s, n[c + 0], 6, -198630844), o, a, n[c + 7], 10, 1126891415), r, o, n[c + 14], 15, -1416354905), s, r, n[c + 5], 21, -57434055), a = d(a, s = d(s, r = d(r, o, a, s, n[c + 12], 6, 1700485571), o, a, n[c + 3], 10, -1894986606), r, o, n[c + 10], 15, -1051523), s, r, n[c + 1], 21, -2054922799), a = d(a, s = d(s, r = d(r, o, a, s, n[c + 8], 6, 1873313359), o, a, n[c + 15], 10, -30611744), r, o, n[c + 6], 15, -1560198380), s, r, n[c + 13], 21, 1309151649), a = d(a, s = d(s, r = d(r, o, a, s, n[c + 4], 6, -145523070), o, a, n[c + 11], 10, -1120210379), r, o, n[c + 2], 15, 718787259), s, r, n[c + 9], 21, -343485551),
                            r = r + f >>> 0,
                            o = o + p >>> 0,
                            a = a + g >>> 0,
                            s = s + m >>> 0
                    }
                    return v.endian([r, o, a, s])
                }
            )._ff = function (t, e, n, i, r, o, a) {
                var s = t + (e & n | ~e & i) + (r >>> 0) + a;
                return (s << o | s >>> 32 - o) + e
            }
            ,
            _._gg = function (t, e, n, i, r, o, a) {
                var s = t + (e & i | n & ~i) + (r >>> 0) + a;
                return (s << o | s >>> 32 - o) + e
            }
            ,
            _._hh = function (t, e, n, i, r, o, a) {
                var s = t + (e ^ n ^ i) + (r >>> 0) + a;
                return (s << o | s >>> 32 - o) + e
            }
            ,
            _._ii = function (t, e, n, i, r, o, a) {
                var s = t + (n ^ (e | ~i)) + (r >>> 0) + a;
                return (s << o | s >>> 32 - o) + e
            }
            ,
            _._blocksize = 16,
            _._digestsize = 16,
            t.exports = function (t, e) {
                if (null == t)
                    throw new Error("Illegal argument " + t);
                var n = v.wordsToBytes(_(t, e));
                return e && e.asBytes ? n : e && e.asString ? w.bytesToString(n) : v.bytesToHex(n)
            }
    },
    42: function (t, e) {
        var o, n;
        o = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",
            n = {
                rotl: function (t, e) {
                    return t << e | t >>> 32 - e
                },
                rotr: function (t, e) {
                    return t << 32 - e | t >>> e
                },
                endian: function (t) {
                    if (t.constructor == Number)
                        return 16711935 & n.rotl(t, 8) | 4278255360 & n.rotl(t, 24);
                    for (var e = 0; e < t.length; e++)
                        t[e] = n.endian(t[e]);
                    return t
                },
                randomBytes: function (t) {
                    for (var e = []; 0 < t; t--)
                        e.push(Math.floor(256 * Math.random()));
                    return e
                },
                bytesToWords: function (t) {
                    for (var e = [], n = 0, i = 0; n < t.length; n++,
                        i += 8)
                        e[i >>> 5] |= t[n] << 24 - i % 32;
                    return e
                },
                wordsToBytes: function (t) {
                    for (var e = [], n = 0; n < 32 * t.length; n += 8)
                        e.push(t[n >>> 5] >>> 24 - n % 32 & 255);
                    return e
                },
                bytesToHex: function (t) {
                    for (var e = [], n = 0; n < t.length; n++)
                        e.push((t[n] >>> 4).toString(16)),
                            e.push((15 & t[n]).toString(16));
                    return e.join("")
                },
                hexToBytes: function (t) {
                    for (var e = [], n = 0; n < t.length; n += 2)
                        e.push(parseInt(t.substr(n, 2), 16));
                    return e
                },
                bytesToBase64: function (t) {
                    for (var e = [], n = 0; n < t.length; n += 3)
                        for (var i = t[n] << 16 | t[n + 1] << 8 | t[n + 2], r = 0; r < 4; r++)
                            8 * n + 6 * r <= 8 * t.length ? e.push(o.charAt(i >>> 6 * (3 - r) & 63)) : e.push("=");
                    return e.join("")
                },
                base64ToBytes: function (t) {
                    t = t.replace(/[^A-Z0-9+\/]/gi, "");
                    for (var e = [], n = 0, i = 0; n < t.length; i = ++n % 4)
                        0 != i && e.push((o.indexOf(t.charAt(n - 1)) & Math.pow(2, -2 * i + 8) - 1) << 2 * i | o.indexOf(t.charAt(n)) >>> 6 - 2 * i);
                    return e
                }
            },
            t.exports = n
    },
    11: function (t, e) {
        var n = {
            utf8: {
                stringToBytes: function (t) {
                    return n.bin.stringToBytes(unescape(encodeURIComponent(t)))
                },
                bytesToString: function (t) {
                    return decodeURIComponent(escape(n.bin.bytesToString(t)))
                }
            },
            bin: {
                stringToBytes: function (t) {
                    for (var e = [], n = 0; n < t.length; n++)
                        e.push(255 & t.charCodeAt(n));
                    return e
                },
                bytesToString: function (t) {
                    for (var e = [], n = 0; n < t.length; n++)
                        e.push(String.fromCharCode(t[n]));
                    return e.join("")
                }
            }
        };
        t.exports = n
    },
    43: function (t, e) {
        function n(t) {
            return !!t.constructor && "function" == typeof t.constructor.isBuffer && t.constructor.isBuffer(t)
        }

        t.exports = function (t) {
            return null != t && (n(t) || function (t) {
                return "function" == typeof t.readFloatLE && "function" == typeof t.slice && n(t.slice(0, 0))
            }(t) || !!t._isBuffer)
        }
    },
    5: function (t, e, n) {
        t.exports = n(44)
    },
    44: function (t, e, n) {
        "use strict";
        var i = n(3)
            , r = n(12)
            , o = n(46)
            , a = n(18);

        function s(t) {
            var e = new o(t)
                , n = r(o.prototype.request, e);
            return i.extend(n, o.prototype, e),
                i.extend(n, e),
                n
        }

        var c = s(n(15));
        c.Axios = o,
            c.create = function (t) {
                return s(a(c.defaults, t))
            }
            ,
            c.Cancel = n(19),
            c.CancelToken = n(59),
            c.isCancel = n(14),
            c.all = function (t) {
                return Promise.all(t)
            }
            ,
            c.spread = n(60),
            t.exports = c,
            t.exports.default = c
    },
    3: function (t, e, n) {
        "use strict";
        var r = n(12)
            , i = n(45)
            , o = Object.prototype.toString;

        function a(t) {
            return "[object Array]" === o.call(t)
        }

        function s(t) {
            return null !== t && "object" == typeof t
        }

        function c(t) {
            return "[object Function]" === o.call(t)
        }

        function l(t, e) {
            if (null != t)
                if ("object" != typeof t && (t = [t]),
                    a(t))
                    for (var n = 0, i = t.length; n < i; n++)
                        e.call(null, t[n], n, t);
                else
                    for (var r in t)
                        Object.prototype.hasOwnProperty.call(t, r) && e.call(null, t[r], r, t)
        }

        t.exports = {
            isArray: a,
            isArrayBuffer: function (t) {
                return "[object ArrayBuffer]" === o.call(t)
            },
            isBuffer: i,
            isFormData: function (t) {
                return "undefined" != typeof FormData && t instanceof FormData
            },
            isArrayBufferView: function (t) {
                return "undefined" != typeof ArrayBuffer && ArrayBuffer.isView ? ArrayBuffer.isView(t) : t && t.buffer && t.buffer instanceof ArrayBuffer
            },
            isString: function (t) {
                return "string" == typeof t
            },
            isNumber: function (t) {
                return "number" == typeof t
            },
            isObject: s,
            isUndefined: function (t) {
                return void 0 === t
            },
            isDate: function (t) {
                return "[object Date]" === o.call(t)
            },
            isFile: function (t) {
                return "[object File]" === o.call(t)
            },
            isBlob: function (t) {
                return "[object Blob]" === o.call(t)
            },
            isFunction: c,
            isStream: function (t) {
                return s(t) && c(t.pipe)
            },
            isURLSearchParams: function (t) {
                return "undefined" != typeof URLSearchParams && t instanceof URLSearchParams
            },
            isStandardBrowserEnv: function () {
                return ("undefined" == typeof navigator || "ReactNative" !== navigator.product && "NativeScript" !== navigator.product && "NS" !== navigator.product) && ("undefined" != typeof window && "undefined" != typeof document)
            },
            forEach: l,
            merge: function n() {
                var i = {};

                function t(t, e) {
                    "object" == typeof i[e] && "object" == typeof t ? i[e] = n(i[e], t) : i[e] = t
                }

                for (var e = 0, r = arguments.length; e < r; e++)
                    l(arguments[e], t);
                return i
            },
            deepMerge: function n() {
                var i = {};

                function t(t, e) {
                    "object" == typeof i[e] && "object" == typeof t ? i[e] = n(i[e], t) : i[e] = "object" == typeof t ? n({}, t) : t
                }

                for (var e = 0, r = arguments.length; e < r; e++)
                    l(arguments[e], t);
                return i
            },
            extend: function (n, t, i) {
                return l(t, function (t, e) {
                    n[e] = i && "function" == typeof t ? r(t, i) : t
                }),
                    n
            },
            trim: function (t) {
                return t.replace(/^\s*/, "").replace(/\s*$/, "")
            }
        }
    },
    12: function (t, e, n) {
        "use strict";
        t.exports = function (n, i) {
            return function () {
                for (var t = new Array(arguments.length), e = 0; e < t.length; e++)
                    t[e] = arguments[e];
                return n.apply(i, t)
            }
        }
    },
    45: function (t, e) {
        t.exports = function (t) {
            return null != t && null != t.constructor && "function" == typeof t.constructor.isBuffer && t.constructor.isBuffer(t)
        }
    },
    46: function (t, e, n) {
        "use strict";
        var r = n(3)
            , i = n(13)
            , o = n(47)
            , a = n(48)
            , s = n(18);

        function c(t) {
            this.defaults = t,
                this.interceptors = {
                    request: new o,
                    response: new o
                }
        }

        c.prototype.request = function (t, e) {
            "string" == typeof t ? (t = e || {}).url = arguments[0] : t = t || {},
                (t = s(this.defaults, t)).method = t.method ? t.method.toLowerCase() : "get";
            var n = [a, void 0]
                , i = Promise.resolve(t);
            for (this.interceptors.request.forEach(function (t) {
                n.unshift(t.fulfilled, t.rejected)
            }),
                     this.interceptors.response.forEach(function (t) {
                         n.push(t.fulfilled, t.rejected)
                     }); n.length;)
                i = i.then(n.shift(), n.shift());
            return i
        }
            ,
            c.prototype.getUri = function (t) {
                return t = s(this.defaults, t),
                    i(t.url, t.params, t.paramsSerializer).replace(/^\?/, "")
            }
            ,
            r.forEach(["delete", "get", "head", "options"], function (n) {
                c.prototype[n] = function (t, e) {
                    return this.request(r.merge(e || {}, {
                        method: n,
                        url: t
                    }))
                }
            }),
            r.forEach(["post", "put", "patch"], function (i) {
                c.prototype[i] = function (t, e, n) {
                    return this.request(r.merge(n || {}, {
                        method: i,
                        url: t,
                        data: e
                    }))
                }
            }),
            t.exports = c
    },
    13: function (t, e, n) {
        "use strict";
        var a = n(3);

        function s(t) {
            return encodeURIComponent(t).replace(/%40/gi, "@").replace(/%3A/gi, ":").replace(/%24/g, "$").replace(/%2C/gi, ",").replace(/%20/g, "+").replace(/%5B/gi, "[").replace(/%5D/gi, "]")
        }

        t.exports = function (t, e, n) {
            if (!e)
                return t;
            var i;
            if (n)
                i = n(e);
            else if (a.isURLSearchParams(e))
                i = e.toString();
            else {
                var r = [];
                a.forEach(e, function (t, e) {
                    null != t && (a.isArray(t) ? e += "[]" : t = [t],
                        a.forEach(t, function (t) {
                            a.isDate(t) ? t = t.toISOString() : a.isObject(t) && (t = JSON.stringify(t)),
                                r.push(s(e) + "=" + s(t))
                        }))
                }),
                    i = r.join("&")
            }
            if (i) {
                var o = t.indexOf("#");
                -1 !== o && (t = t.slice(0, o)),
                    t += (-1 === t.indexOf("?") ? "?" : "&") + i
            }
            return t
        }
    },
    47: function (t, e, n) {
        "use strict";
        var i = n(3);

        function r() {
            this.handlers = []
        }

        r.prototype.use = function (t, e) {
            return this.handlers.push({
                fulfilled: t,
                rejected: e
            }),
            this.handlers.length - 1
        }
            ,
            r.prototype.eject = function (t) {
                this.handlers[t] && (this.handlers[t] = null)
            }
            ,
            r.prototype.forEach = function (e) {
                i.forEach(this.handlers, function (t) {
                    null !== t && e(t)
                })
            }
            ,
            t.exports = r
    },
    48: function (t, e, n) {
        "use strict";
        var i = n(3)
            , r = n(49)
            , o = n(14)
            , a = n(15)
            , s = n(57)
            , c = n(58);

        function l(t) {
            t.cancelToken && t.cancelToken.throwIfRequested()
        }

        t.exports = function (e) {
            return l(e),
            e.baseURL && !s(e.url) && (e.url = c(e.baseURL, e.url)),
                e.headers = e.headers || {},
                e.data = r(e.data, e.headers, e.transformRequest),
                e.headers = i.merge(e.headers.common || {}, e.headers[e.method] || {}, e.headers || {}),
                i.forEach(["delete", "get", "head", "post", "put", "patch", "common"], function (t) {
                    delete e.headers[t]
                }),
                (e.adapter || a.adapter)(e).then(function (t) {
                    return l(e),
                        t.data = r(t.data, t.headers, e.transformResponse),
                        t
                }, function (t) {
                    return o(t) || (l(e),
                    t && t.response && (t.response.data = r(t.response.data, t.response.headers, e.transformResponse))),
                        Promise.reject(t)
                })
        }
    },
    49: function (t, e, n) {
        "use strict";
        var i = n(3);
        t.exports = function (e, n, t) {
            return i.forEach(t, function (t) {
                e = t(e, n)
            }),
                e
        }
    },
    14: function (t, e, n) {
        "use strict";
        t.exports = function (t) {
            return !(!t || !t.__CANCEL__)
        }
    },
    15: function (s, t, c) {
        "use strict";
        (function (t) {
                var n = c(3)
                    , i = c(51)
                    , e = {
                    "Content-Type": "application/x-www-form-urlencoded"
                };

                function r(t, e) {
                    !n.isUndefined(t) && n.isUndefined(t["Content-Type"]) && (t["Content-Type"] = e)
                }

                var o, a = {
                    adapter: (void 0 !== t && "[object process]" === Object.prototype.toString.call(t) ? o = c(16) : "undefined" != typeof XMLHttpRequest && (o = c(16)),
                        o),
                    transformRequest: [function (t, e) {
                        return i(e, "Accept"),
                            i(e, "Content-Type"),
                            n.isFormData(t) || n.isArrayBuffer(t) || n.isBuffer(t) || n.isStream(t) || n.isFile(t) || n.isBlob(t) ? t : n.isArrayBufferView(t) ? t.buffer : n.isURLSearchParams(t) ? (r(e, "application/x-www-form-urlencoded;charset=utf-8"),
                                t.toString()) : n.isObject(t) ? (r(e, "application/json;charset=utf-8"),
                                JSON.stringify(t)) : t
                    }
                    ],
                    transformResponse: [function (t) {
                        if ("string" == typeof t)
                            try {
                                t = JSON.parse(t)
                            } catch (t) {
                            }
                        return t
                    }
                    ],
                    timeout: 0,
                    xsrfCookieName: "XSRF-TOKEN",
                    xsrfHeaderName: "X-XSRF-TOKEN",
                    maxContentLength: -1,
                    validateStatus: function (t) {
                        return 200 <= t && t < 300
                    }
                };
                a.headers = {
                    common: {
                        Accept: "application/json, text/plain, */*"
                    }
                },
                    n.forEach(["delete", "get", "head"], function (t) {
                        a.headers[t] = {}
                    }),
                    n.forEach(["post", "put", "patch"], function (t) {
                        a.headers[t] = n.merge(e)
                    }),
                    s.exports = a
            }
        ).call(this, c(50))
    },
    50:function(t, e) {
    var n, i, r = t.exports = {};
    function o() {
        throw new Error("setTimeout has not been defined")
    }
    function a() {
        throw new Error("clearTimeout has not been defined")
    }
    function s(e) {
        if (n === setTimeout)
            return setTimeout(e, 0);
        if ((n === o || !n) && setTimeout)
            return n = setTimeout,
            setTimeout(e, 0);
        try {
            return n(e, 0)
        } catch (t) {
            try {
                return n.call(null, e, 0)
            } catch (t) {
                return n.call(this, e, 0)
            }
        }
    }
    !function() {
        try {
            n = "function" == typeof setTimeout ? setTimeout : o
        } catch (t) {
            n = o
        }
        try {
            i = "function" == typeof clearTimeout ? clearTimeout : a
        } catch (t) {
            i = a
        }
    }();
    var c, l = [], u = !1, h = -1;
    function d() {
        u && c && (u = !1,
        c.length ? l = c.concat(l) : h = -1,
        l.length && f())
    }
    function f() {
        if (!u) {
            var t = s(d);
            u = !0;
            for (var e = l.length; e; ) {
                for (c = l,
                l = []; ++h < e; )
                    c && c[h].run();
                h = -1,
                e = l.length
            }
            c = null,
            u = !1,
            function(e) {
                if (i === clearTimeout)
                    return clearTimeout(e);
                if ((i === a || !i) && clearTimeout)
                    return i = clearTimeout,
                    clearTimeout(e);
                try {
                    i(e)
                } catch (t) {
                    try {
                        return i.call(null, e)
                    } catch (t) {
                        return i.call(this, e)
                    }
                }
            }(t)
        }
    }
    function p(t, e) {
        this.fun = t,
        this.array = e
    }
    function g() {}
    r.nextTick = function(t) {
        var e = new Array(arguments.length - 1);
        if (1 < arguments.length)
            for (var n = 1; n < arguments.length; n++)
                e[n - 1] = arguments[n];
        l.push(new p(t,e)),
        1 !== l.length || u || s(f)
    }
    ,
    p.prototype.run = function() {
        this.fun.apply(null, this.array)
    }
    ,
    r.title = "browser",
    r.browser = !0,
    r.env = {},
    r.argv = [],
    r.version = "",
    r.versions = {},
    r.on = g,
    r.addListener = g,
    r.once = g,
    r.off = g,
    r.removeListener = g,
    r.removeAllListeners = g,
    r.emit = g,
    r.prependListener = g,
    r.prependOnceListener = g,
    r.listeners = function(t) {
        return []
    }
    ,
    r.binding = function(t) {
        throw new Error("process.binding is not supported")
    }
    ,
    r.cwd = function() {
        return "/"
    }
    ,
    r.chdir = function(t) {
        throw new Error("process.chdir is not supported")
    }
    ,
    r.umask = function() {
        return 0
    }
},
    51:function(t, e, n) {
    "use strict";
    var r = n(3);
    t.exports = function(n, i) {
        r.forEach(n, function(t, e) {
            e !== i && e.toUpperCase() === i.toUpperCase() && (n[i] = t,
            delete n[e])
        })
    }
},
    57:function(t, e, n) {
    "use strict";
    t.exports = function(t) {
        return /^([a-z][a-z\d\+\-\.]*:)?\/\//i.test(t)
    }
},
    58:function(t, e, n) {
    "use strict";
    t.exports = function(t, e) {
        return e ? t.replace(/\/+$/, "") + "/" + e.replace(/^\/+/, "") : t
    }
},
    18:function(t, e, n) {
    "use strict";
    var r = n(3);
    t.exports = function(e, n) {
        n = n || {};
        var i = {};
        return r.forEach(["url", "method", "params", "data"], function(t) {
            void 0 !== n[t] && (i[t] = n[t])
        }),
        r.forEach(["headers", "auth", "proxy"], function(t) {
            r.isObject(n[t]) ? i[t] = r.deepMerge(e[t], n[t]) : void 0 !== n[t] ? i[t] = n[t] : r.isObject(e[t]) ? i[t] = r.deepMerge(e[t]) : void 0 !== e[t] && (i[t] = e[t])
        }),
        r.forEach(["baseURL", "transformRequest", "transformResponse", "paramsSerializer", "timeout", "withCredentials", "adapter", "responseType", "xsrfCookieName", "xsrfHeaderName", "onUploadProgress", "onDownloadProgress", "maxContentLength", "validateStatus", "maxRedirects", "httpAgent", "httpsAgent", "cancelToken", "socketPath"], function(t) {
            void 0 !== n[t] ? i[t] = n[t] : void 0 !== e[t] && (i[t] = e[t])
        }),
        i
    }
},
    19:function(t, e, n) {
    "use strict";
    function i(t) {
        this.message = t
    }
    i.prototype.toString = function() {
        return "Cancel" + (this.message ? ": " + this.message : "")
    }
    ,
    i.prototype.__CANCEL__ = !0,
    t.exports = i
},
    59:function(t, e, n) {
    "use strict";
    var i = n(19);
    function r(t) {
        if ("function" != typeof t)
            throw new TypeError("executor must be a function.");
        var e;
        this.promise = new Promise(function(t) {
            e = t
        }
        );
        var n = this;
        t(function(t) {
            n.reason || (n.reason = new i(t),
            e(n.reason))
        })
    }
    r.prototype.throwIfRequested = function() {
        if (this.reason)
            throw this.reason
    }
    ,
    r.source = function() {
        var e;
        return {
            token: new r(function(t) {
                e = t
            }
            ),
            cancel: e
        }
    }
    ,
    t.exports = r
},
    60:function(t, e, n) {
    "use strict";
    t.exports = function(e) {
        return function(t) {
            return e.apply(null, t)
        }
    }
}

})

laohe(62)