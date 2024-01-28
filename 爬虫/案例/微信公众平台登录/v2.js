function vv(A, z, k) {
    "use strict";
    var T;
    ;!(T = function (R, F, p) {
        function _(t, i) {
            var r = (t & 65535) + (i & 65535)
                , f = (t >> 16) + (i >> 16) + (r >> 16);
            return f << 16 | r & 65535
        }

        function x(t, i) {
            return t << i | t >>> 32 - i
        }

        function C(t, i, r, f, j, O) {
            return _(x(_(_(i, t), _(f, O)), j), r)
        }

        function S(t, i, r, f, j, O, $) {
            return C(i & r | ~i & f, t, i, j, O, $)
        }

        function d(t, i, r, f, j, O, $) {
            return C(i & f | r & ~f, t, i, j, O, $)
        }

        function g(t, i, r, f, j, O, $) {
            return C(i ^ r ^ f, t, i, j, O, $)
        }

        function v(t, i, r, f, j, O, $) {
            return C(r ^ (i | ~f), t, i, j, O, $)
        }

        function o(t, i) {
            t[i >> 5] |= 128 << i % 32;
            t[(i + 64 >>> 9 << 4) + 14] = i;
            var r, f, j, O, $, s = 1732584193, c = -271733879, m = -1732584194, n = 271733878;
            for (r = 0; r < t.length; r += 16) {
                f = s;
                j = c;
                O = m;
                $ = n;
                s = S(s, c, m, n, t[r], 7, -680876936);
                n = S(n, s, c, m, t[r + 1], 12, -389564586);
                m = S(m, n, s, c, t[r + 2], 17, 606105819);
                c = S(c, m, n, s, t[r + 3], 22, -1044525330);
                s = S(s, c, m, n, t[r + 4], 7, -176418897);
                n = S(n, s, c, m, t[r + 5], 12, 1200080426);
                m = S(m, n, s, c, t[r + 6], 17, -1473231341);
                c = S(c, m, n, s, t[r + 7], 22, -45705983);
                s = S(s, c, m, n, t[r + 8], 7, 1770035416);
                n = S(n, s, c, m, t[r + 9], 12, -1958414417);
                m = S(m, n, s, c, t[r + 10], 17, -42063);
                c = S(c, m, n, s, t[r + 11], 22, -1990404162);
                s = S(s, c, m, n, t[r + 12], 7, 1804603682);
                n = S(n, s, c, m, t[r + 13], 12, -40341101);
                m = S(m, n, s, c, t[r + 14], 17, -1502002290);
                c = S(c, m, n, s, t[r + 15], 22, 1236535329);
                s = d(s, c, m, n, t[r + 1], 5, -165796510);
                n = d(n, s, c, m, t[r + 6], 9, -1069501632);
                m = d(m, n, s, c, t[r + 11], 14, 643717713);
                c = d(c, m, n, s, t[r], 20, -373897302);
                s = d(s, c, m, n, t[r + 5], 5, -701558691);
                n = d(n, s, c, m, t[r + 10], 9, 38016083);
                m = d(m, n, s, c, t[r + 15], 14, -660478335);
                c = d(c, m, n, s, t[r + 4], 20, -405537848);
                s = d(s, c, m, n, t[r + 9], 5, 568446438);
                n = d(n, s, c, m, t[r + 14], 9, -1019803690);
                m = d(m, n, s, c, t[r + 3], 14, -187363961);
                c = d(c, m, n, s, t[r + 8], 20, 1163531501);
                s = d(s, c, m, n, t[r + 13], 5, -1444681467);
                n = d(n, s, c, m, t[r + 2], 9, -51403784);
                m = d(m, n, s, c, t[r + 7], 14, 1735328473);
                c = d(c, m, n, s, t[r + 12], 20, -1926607734);
                s = g(s, c, m, n, t[r + 5], 4, -378558);
                n = g(n, s, c, m, t[r + 8], 11, -2022574463);
                m = g(m, n, s, c, t[r + 11], 16, 1839030562);
                c = g(c, m, n, s, t[r + 14], 23, -35309556);
                s = g(s, c, m, n, t[r + 1], 4, -1530992060);
                n = g(n, s, c, m, t[r + 4], 11, 1272893353);
                m = g(m, n, s, c, t[r + 7], 16, -155497632);
                c = g(c, m, n, s, t[r + 10], 23, -1094730640);
                s = g(s, c, m, n, t[r + 13], 4, 681279174);
                n = g(n, s, c, m, t[r], 11, -358537222);
                m = g(m, n, s, c, t[r + 3], 16, -722521979);
                c = g(c, m, n, s, t[r + 6], 23, 76029189);
                s = g(s, c, m, n, t[r + 9], 4, -640364487);
                n = g(n, s, c, m, t[r + 12], 11, -421815835);
                m = g(m, n, s, c, t[r + 15], 16, 530742520);
                c = g(c, m, n, s, t[r + 2], 23, -995338651);
                s = v(s, c, m, n, t[r], 6, -198630844);
                n = v(n, s, c, m, t[r + 7], 10, 1126891415);
                m = v(m, n, s, c, t[r + 14], 15, -1416354905);
                c = v(c, m, n, s, t[r + 5], 21, -57434055);
                s = v(s, c, m, n, t[r + 12], 6, 1700485571);
                n = v(n, s, c, m, t[r + 3], 10, -1894986606);
                m = v(m, n, s, c, t[r + 10], 15, -1051523);
                c = v(c, m, n, s, t[r + 1], 21, -2054922799);
                s = v(s, c, m, n, t[r + 8], 6, 1873313359);
                n = v(n, s, c, m, t[r + 15], 10, -30611744);
                m = v(m, n, s, c, t[r + 6], 15, -1560198380);
                c = v(c, m, n, s, t[r + 13], 21, 1309151649);
                s = v(s, c, m, n, t[r + 4], 6, -145523070);
                n = v(n, s, c, m, t[r + 11], 10, -1120210379);
                m = v(m, n, s, c, t[r + 2], 15, 718787259);
                c = v(c, m, n, s, t[r + 9], 21, -343485551);
                s = _(s, f);
                c = _(c, j);
                m = _(m, O);
                n = _(n, $)
            }
            return [s, c, m, n]
        }

        function u(t) {
            var i, r = "";
            for (i = 0; i < t.length * 32; i += 8) {
                r += String.fromCharCode(t[i >> 5] >>> i % 32 & 255)
            }
            return r
        }

        function b(t) {
            var i, r = [];
            r[(t.length >> 2) - 1] = void 0;
            for (i = 0; i < r.length; i += 1) {
                r[i] = 0
            }
            for (i = 0; i < t.length * 8; i += 8) {
                r[i >> 5] |= (t.charCodeAt(i / 8) & 255) << i % 32
            }
            return r
        }

        function L(t) {
            return u(o(b(t), t.length * 8))
        }

        function h(t, i) {
            var r, f = b(t), j = [], O = [], $;
            j[15] = O[15] = void 0;
            if (f.length > 16) {
                f = o(f, t.length * 8)
            }
            for (r = 0; r < 16; r += 1) {
                j[r] = f[r] ^ 909522486;
                O[r] = f[r] ^ 1549556828
            }
            $ = o(j.concat(b(i)), 512 + i.length * 8);
            return u(o(O.concat($), 512 + 128))
        }

        function y(t) {
            var i = "0123456789abcdef", r = "", f, j;
            for (j = 0; j < t.length; j += 1) {
                f = t.charCodeAt(j);
                r += i.charAt(f >>> 4 & 15) + i.charAt(f & 15)
            }
            return r
        }

        function I(t) {
            return unescape(encodeURIComponent(t))
        }

        function E(t) {
            return L(I(t))
        }

        function D(t) {
            return y(E(t))
        }

        function q(t, i) {
            return h(I(t), I(i))
        }

        function l(t, i) {
            return y(q(t, i))
        }

        p.exports = function (t, i, r) {
            if (!i) {
                if (!r) {
                    return D(t)
                } else {
                    return E(t)
                }
            }
            if (!r) {
                return l(i, t)
            } else {
                return q(i, t)
            }
        }
    }
        .call(z, k, z, A),
    T !== void 0 && (A.exports = T))
}