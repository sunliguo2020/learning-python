const jsdom = require("jsdom");
const {JSDOM} = jsdom;
const $ = require("jquery")(new JSDOM(`<!DOCTYPE html><p>Hello world</p>`).window);
window = global;

!function a(b, c, d) {
    // b:模块
    // c:{}
    // d:[20]

    //e 是 a 函数内部的一个闭包函数，它负责加载和执行模块。
    // g 是要加载的模块名，h 是一个可选参数。
    function e(g, h) {
        /*
        * * 如果 `c[g]`（即缓存中）不存在该模块，则继续查找。
        * 首先检查 `b[g]`（可能是模块定义数组）是否存在。
        * 如果不存在，则尝试使用 `require`（如果可用）来加载模块。
        * 如果 `require` 不可用，并且 `f`（可能是另一个加载器或自定义函数）存在，则使用 `f` 来加载模块。
        * 如果两者都不可用，则抛出一个错误，表示找不到模块。
        * 如果 `b[g]` 存在，则创建一个新的模块对象 `k`，并将其添加到缓存 `c[g]` 中。
        * 执行模块定义中的代码（`b[g][0]`），并传入一个回调函数和其他相关参数。
        * 如果模块定义中有依赖（`b[g][1]`），则递归地加载这些依赖。
        *
        * */
        if (!c[g]) {
            if (!b[g]) {
                var i = "function" == typeof require && require;
                if (!h && i)
                    return i(g, !0);
                if (f)
                    return f(g, !0);
                var j = new Error("Cannot find module '" + g + "'");
                throw j.code = "MODULE_NOT_FOUND",
                    j
            }
            var k = c[g] = {
                exports: {}
            };
            b[g][0].call(k.exports, function (a) {
                var c = b[g][1][a];
                return e(c || a)
            }, k, k.exports, a, b, c, d)
        }
        return c[g].exports
    }

    window.loader = e;
    // 遍历d d[0] ... d[d.length-1]  执行e(d[0])
    //这部分代码遍历 d 数组（包含模块定义），并使用加载器 e 来加载和执行每个模块。
    for (var f = "function" == typeof require && require, g = 0; g < d.length; g++)
        e(d[g]);

    return e
}({
    1: [function (a, b, c) {
        !function (d, e, f) {
            "object" == typeof c ? b.exports = c = e(a("./core"), a("./enc-base64"), a("./md5"), a("./evpkdf"), a("./cipher-core")) : "function" == typeof define && define.amd ? define(["./core", "./enc-base64", "./md5", "./evpkdf", "./cipher-core"], e) : e(d.CryptoJS)
        }(this, function (a) {
            return function () {
                var b = a
                    , c = b.lib
                    , d = c.BlockCipher
                    , e = b.algo
                    , f = []
                    , g = []
                    , h = []
                    , i = []
                    , j = []
                    , k = []
                    , l = []
                    , m = []
                    , n = []
                    , o = [];
                !function () {
                    for (var a = [], b = 0; b < 256; b++)
                        a[b] = b < 128 ? b << 1 : b << 1 ^ 283;
                    for (var c = 0, d = 0, b = 0; b < 256; b++) {
                        var e = d ^ d << 1 ^ d << 2 ^ d << 3 ^ d << 4;
                        e = e >>> 8 ^ 255 & e ^ 99,
                            f[c] = e,
                            g[e] = c;
                        var p = a[c]
                            , q = a[p]
                            , r = a[q]
                            , s = 257 * a[e] ^ 16843008 * e;
                        h[c] = s << 24 | s >>> 8,
                            i[c] = s << 16 | s >>> 16,
                            j[c] = s << 8 | s >>> 24,
                            k[c] = s;
                        var s = 16843009 * r ^ 65537 * q ^ 257 * p ^ 16843008 * c;
                        l[e] = s << 24 | s >>> 8,
                            m[e] = s << 16 | s >>> 16,
                            n[e] = s << 8 | s >>> 24,
                            o[e] = s,
                            c ? (c = p ^ a[a[a[r ^ p]]],
                                d ^= a[a[d]]) : c = d = 1
                    }
                }();
                var p = [0, 1, 2, 4, 8, 16, 32, 64, 128, 27, 54]
                    , q = e.AES = d.extend({
                    _doReset: function () {
                        if (!this._nRounds || this._keyPriorReset !== this._key) {
                            for (var a = this._keyPriorReset = this._key, b = a.words, c = a.sigBytes / 4, d = this._nRounds = c + 6, e = 4 * (d + 1), g = this._keySchedule = [], h = 0; h < e; h++)
                                if (h < c)
                                    g[h] = b[h];
                                else {
                                    var i = g[h - 1];
                                    h % c ? c > 6 && h % c == 4 && (i = f[i >>> 24] << 24 | f[i >>> 16 & 255] << 16 | f[i >>> 8 & 255] << 8 | f[255 & i]) : (i = i << 8 | i >>> 24,
                                        i = f[i >>> 24] << 24 | f[i >>> 16 & 255] << 16 | f[i >>> 8 & 255] << 8 | f[255 & i],
                                        i ^= p[h / c | 0] << 24),
                                        g[h] = g[h - c] ^ i
                                }
                            for (var j = this._invKeySchedule = [], k = 0; k < e; k++) {
                                var h = e - k;
                                if (k % 4)
                                    var i = g[h];
                                else
                                    var i = g[h - 4];
                                j[k] = k < 4 || h <= 4 ? i : l[f[i >>> 24]] ^ m[f[i >>> 16 & 255]] ^ n[f[i >>> 8 & 255]] ^ o[f[255 & i]]
                            }
                        }
                    },
                    encryptBlock: function (a, b) {
                        this._doCryptBlock(a, b, this._keySchedule, h, i, j, k, f)
                    },
                    decryptBlock: function (a, b) {
                        var c = a[b + 1];
                        a[b + 1] = a[b + 3],
                            a[b + 3] = c,
                            this._doCryptBlock(a, b, this._invKeySchedule, l, m, n, o, g);
                        var c = a[b + 1];
                        a[b + 1] = a[b + 3],
                            a[b + 3] = c
                    },
                    _doCryptBlock: function (a, b, c, d, e, f, g, h) {
                        for (var i = this._nRounds, j = a[b] ^ c[0], k = a[b + 1] ^ c[1], l = a[b + 2] ^ c[2], m = a[b + 3] ^ c[3], n = 4, o = 1; o < i; o++) {
                            var p = d[j >>> 24] ^ e[k >>> 16 & 255] ^ f[l >>> 8 & 255] ^ g[255 & m] ^ c[n++]
                                , q = d[k >>> 24] ^ e[l >>> 16 & 255] ^ f[m >>> 8 & 255] ^ g[255 & j] ^ c[n++]
                                , r = d[l >>> 24] ^ e[m >>> 16 & 255] ^ f[j >>> 8 & 255] ^ g[255 & k] ^ c[n++]
                                , s = d[m >>> 24] ^ e[j >>> 16 & 255] ^ f[k >>> 8 & 255] ^ g[255 & l] ^ c[n++];
                            j = p,
                                k = q,
                                l = r,
                                m = s
                        }
                        var p = (h[j >>> 24] << 24 | h[k >>> 16 & 255] << 16 | h[l >>> 8 & 255] << 8 | h[255 & m]) ^ c[n++]
                            ,
                            q = (h[k >>> 24] << 24 | h[l >>> 16 & 255] << 16 | h[m >>> 8 & 255] << 8 | h[255 & j]) ^ c[n++]
                            ,
                            r = (h[l >>> 24] << 24 | h[m >>> 16 & 255] << 16 | h[j >>> 8 & 255] << 8 | h[255 & k]) ^ c[n++]
                            ,
                            s = (h[m >>> 24] << 24 | h[j >>> 16 & 255] << 16 | h[k >>> 8 & 255] << 8 | h[255 & l]) ^ c[n++];
                        a[b] = p,
                            a[b + 1] = q,
                            a[b + 2] = r,
                            a[b + 3] = s
                    },
                    keySize: 8
                });
                b.AES = d._createHelper(q)
            }(),
                a.AES
        })
    }
        , {
            "./cipher-core": 2,
            "./core": 3,
            "./enc-base64": 4,
            "./evpkdf": 6,
            "./md5": 8
        }],
    2: [function (a, b, c) {
        !function (d, e, f) {
            "object" == typeof c ? b.exports = c = e(a("./core"), a("./evpkdf")) : "function" == typeof define && define.amd ? define(["./core", "./evpkdf"], e) : e(d.CryptoJS)
        }(this, function (a) {
            a.lib.Cipher || function (b) {
                var c = a
                    , d = c.lib
                    , e = d.Base
                    , f = d.WordArray
                    , g = d.BufferedBlockAlgorithm
                    , h = c.enc
                    , i = (h.Utf8,
                    h.Base64)
                    , j = c.algo
                    , k = j.EvpKDF
                    , l = d.Cipher = g.extend({
                    cfg: e.extend(),
                    createEncryptor: function (a, b) {
                        return this.create(this._ENC_XFORM_MODE, a, b)
                    },
                    createDecryptor: function (a, b) {
                        return this.create(this._DEC_XFORM_MODE, a, b)
                    },
                    init: function (a, b, c) {
                        this.cfg = this.cfg.extend(c),
                            this._xformMode = a,
                            this._key = b,
                            this.reset()
                    },
                    reset: function () {
                        g.reset.call(this),
                            this._doReset()
                    },
                    process: function (a) {
                        return this._append(a),
                            this._process()
                    },
                    finalize: function (a) {
                        return a && this._append(a),
                            this._doFinalize()
                    },
                    keySize: 4,
                    ivSize: 4,
                    _ENC_XFORM_MODE: 1,
                    _DEC_XFORM_MODE: 2,
                    _createHelper: function () {
                        function a(a) {
                            return "string" == typeof a ? x : u
                        }

                        return function (b) {
                            return {
                                encrypt: function (c, d, e) {
                                    return a(d).encrypt(b, c, d, e)
                                },
                                decrypt: function (c, d, e) {
                                    return a(d).decrypt(b, c, d, e)
                                }
                            }
                        }
                    }()
                })
                    , m = (d.StreamCipher = l.extend({
                    _doFinalize: function () {
                        return this._process(!0)
                    },
                    blockSize: 1
                }),
                    c.mode = {})
                    , n = d.BlockCipherMode = e.extend({
                    createEncryptor: function (a, b) {
                        return this.Encryptor.create(a, b)
                    },
                    createDecryptor: function (a, b) {
                        return this.Decryptor.create(a, b)
                    },
                    init: function (a, b) {
                        this._cipher = a,
                            this._iv = b
                    }
                })
                    , o = m.CBC = function () {
                    function a(a, c, d) {
                        var e = this._iv;
                        if (e) {
                            var f = e;
                            this._iv = b
                        } else
                            var f = this._prevBlock;
                        for (var g = 0; g < d; g++)
                            a[c + g] ^= f[g]
                    }

                    var c = n.extend();
                    return c.Encryptor = c.extend({
                        processBlock: function (b, c) {
                            var d = this._cipher
                                , e = d.blockSize;
                            a.call(this, b, c, e),
                                d.encryptBlock(b, c),
                                this._prevBlock = b.slice(c, c + e)
                        }
                    }),
                        c.Decryptor = c.extend({
                            processBlock: function (b, c) {
                                var d = this._cipher
                                    , e = d.blockSize
                                    , f = b.slice(c, c + e);
                                d.decryptBlock(b, c),
                                    a.call(this, b, c, e),
                                    this._prevBlock = f
                            }
                        }),
                        c
                }()
                    , p = c.pad = {}
                    , q = p.Pkcs7 = {
                    pad: function (a, b) {
                        for (var c = 4 * b, d = c - a.sigBytes % c, e = d << 24 | d << 16 | d << 8 | d, g = [], h = 0; h < d; h += 4)
                            g.push(e);
                        var i = f.create(g, d);
                        a.concat(i)
                    },
                    unpad: function (a) {
                        var b = 255 & a.words[a.sigBytes - 1 >>> 2];
                        a.sigBytes -= b
                    }
                }
                    , r = (d.BlockCipher = l.extend({
                    cfg: l.cfg.extend({
                        mode: o,
                        padding: q
                    }),
                    reset: function () {
                        l.reset.call(this);
                        var a = this.cfg
                            , b = a.iv
                            , c = a.mode;
                        if (this._xformMode == this._ENC_XFORM_MODE)
                            var d = c.createEncryptor;
                        else {
                            var d = c.createDecryptor;
                            this._minBufferSize = 1
                        }
                        this._mode && this._mode.__creator == d ? this._mode.init(this, b && b.words) : (this._mode = d.call(c, this, b && b.words),
                            this._mode.__creator = d)
                    },
                    _doProcessBlock: function (a, b) {
                        this._mode.processBlock(a, b)
                    },
                    _doFinalize: function () {
                        var a = this.cfg.padding;
                        if (this._xformMode == this._ENC_XFORM_MODE) {
                            a.pad(this._data, this.blockSize);
                            var b = this._process(!0)
                        } else {
                            var b = this._process(!0);
                            a.unpad(b)
                        }
                        return b
                    },
                    blockSize: 4
                }),
                    d.CipherParams = e.extend({
                        init: function (a) {
                            this.mixIn(a)
                        },
                        toString: function (a) {
                            return (a || this.formatter).stringify(this)
                        }
                    }))
                    , s = c.format = {}
                    , t = s.OpenSSL = {
                    stringify: function (a) {
                        var b = a.ciphertext
                            , c = a.salt;
                        if (c)
                            var d = f.create([1398893684, 1701076831]).concat(c).concat(b);
                        else
                            var d = b;
                        return d.toString(i)
                    },
                    parse: function (a) {
                        var b = i.parse(a)
                            , c = b.words;
                        if (1398893684 == c[0] && 1701076831 == c[1]) {
                            var d = f.create(c.slice(2, 4));
                            c.splice(0, 4),
                                b.sigBytes -= 16
                        }
                        return r.create({
                            ciphertext: b,
                            salt: d
                        })
                    }
                }
                    , u = d.SerializableCipher = e.extend({
                    cfg: e.extend({
                        format: t
                    }),
                    encrypt: function (a, b, c, d) {
                        d = this.cfg.extend(d);
                        var e = a.createEncryptor(c, d)
                            , f = e.finalize(b)
                            , g = e.cfg;
                        return r.create({
                            ciphertext: f,
                            key: c,
                            iv: g.iv,
                            algorithm: a,
                            mode: g.mode,
                            padding: g.padding,
                            blockSize: a.blockSize,
                            formatter: d.format
                        })
                    },
                    decrypt: function (a, b, c, d) {
                        return d = this.cfg.extend(d),
                            b = this._parse(b, d.format),
                            a.createDecryptor(c, d).finalize(b.ciphertext)
                    },
                    _parse: function (a, b) {
                        return "string" == typeof a ? b.parse(a, this) : a
                    }
                })
                    , v = c.kdf = {}
                    , w = v.OpenSSL = {
                    execute: function (a, b, c, d) {
                        d || (d = f.random(8));
                        var e = k.create({
                            keySize: b + c
                        }).compute(a, d)
                            , g = f.create(e.words.slice(b), 4 * c);
                        return e.sigBytes = 4 * b,
                            r.create({
                                key: e,
                                iv: g,
                                salt: d
                            })
                    }
                }
                    , x = d.PasswordBasedCipher = u.extend({
                    cfg: u.cfg.extend({
                        kdf: w
                    }),
                    encrypt: function (a, b, c, d) {
                        d = this.cfg.extend(d);
                        var e = d.kdf.execute(c, a.keySize, a.ivSize);
                        d.iv = e.iv;
                        var f = u.encrypt.call(this, a, b, e.key, d);
                        return f.mixIn(e),
                            f
                    },
                    decrypt: function (a, b, c, d) {
                        d = this.cfg.extend(d),
                            b = this._parse(b, d.format);
                        var e = d.kdf.execute(c, a.keySize, a.ivSize, b.salt);
                        return d.iv = e.iv,
                            u.decrypt.call(this, a, b, e.key, d)
                    }
                })
            }()
        })
    }
        , {
            "./core": 3,
            "./evpkdf": 6
        }],
    3: [function (a, b, c) {
        !function (a, d) {
            "object" == typeof c ? b.exports = c = d() : "function" == typeof define && define.amd ? define([], d) : a.CryptoJS = d()
        }(this, function () {
            var a = a || function (a, b) {
                var c = Object.create || function () {
                    function a() {
                    }

                    return function (b) {
                        var c;
                        return a.prototype = b,
                            c = new a,
                            a.prototype = null,
                            c
                    }
                }()
                    , d = {}
                    , e = d.lib = {}
                    , f = e.Base = function () {
                    return {
                        extend: function (a) {
                            var b = c(this);
                            return a && b.mixIn(a),
                            b.hasOwnProperty("init") && this.init !== b.init || (b.init = function () {
                                    b.$super.init.apply(this, arguments)
                                }
                            ),
                                b.init.prototype = b,
                                b.$super = this,
                                b
                        },
                        create: function () {
                            var a = this.extend();
                            return a.init.apply(a, arguments),
                                a
                        },
                        init: function () {
                        },
                        mixIn: function (a) {
                            for (var b in a)
                                a.hasOwnProperty(b) && (this[b] = a[b]);
                            a.hasOwnProperty("toString") && (this.toString = a.toString)
                        },
                        clone: function () {
                            return this.init.prototype.extend(this)
                        }
                    }
                }()
                    , g = e.WordArray = f.extend({
                    init: function (a, c) {
                        a = this.words = a || [],
                            this.sigBytes = c != b ? c : 4 * a.length
                    },
                    toString: function (a) {
                        return (a || i).stringify(this)
                    },
                    concat: function (a) {
                        var b = this.words
                            , c = a.words
                            , d = this.sigBytes
                            , e = a.sigBytes;
                        if (this.clamp(),
                        d % 4)
                            for (var f = 0; f < e; f++) {
                                var g = c[f >>> 2] >>> 24 - f % 4 * 8 & 255;
                                b[d + f >>> 2] |= g << 24 - (d + f) % 4 * 8
                            }
                        else
                            for (var f = 0; f < e; f += 4)
                                b[d + f >>> 2] = c[f >>> 2];
                        return this.sigBytes += e,
                            this
                    },
                    clamp: function () {
                        var b = this.words
                            , c = this.sigBytes;
                        b[c >>> 2] &= 4294967295 << 32 - c % 4 * 8,
                            b.length = a.ceil(c / 4)
                    },
                    clone: function () {
                        var a = f.clone.call(this);
                        return a.words = this.words.slice(0),
                            a
                    },
                    random: function (b) {
                        for (var c, d = [], e = function (b) {
                            var b = b
                                , c = 987654321
                                , d = 4294967295;
                            return function () {
                                c = 36969 * (65535 & c) + (c >> 16) & d,
                                    b = 18e3 * (65535 & b) + (b >> 16) & d;
                                var e = (c << 16) + b & d;
                                return e /= 4294967296,
                                (e += .5) * (a.random() > .5 ? 1 : -1)
                            }
                        }, f = 0; f < b; f += 4) {
                            var h = e(4294967296 * (c || a.random()));
                            c = 987654071 * h(),
                                d.push(4294967296 * h() | 0)
                        }
                        return new g.init(d, b)
                    }
                })
                    , h = d.enc = {}
                    , i = h.Hex = {
                    stringify: function (a) {
                        for (var b = a.words, c = a.sigBytes, d = [], e = 0; e < c; e++) {
                            var f = b[e >>> 2] >>> 24 - e % 4 * 8 & 255;
                            d.push((f >>> 4).toString(16)),
                                d.push((15 & f).toString(16))
                        }
                        return d.join("")
                    },
                    parse: function (a) {
                        for (var b = a.length, c = [], d = 0; d < b; d += 2)
                            c[d >>> 3] |= parseInt(a.substr(d, 2), 16) << 24 - d % 8 * 4;
                        return new g.init(c, b / 2)
                    }
                }
                    , j = h.Latin1 = {
                    stringify: function (a) {
                        for (var b = a.words, c = a.sigBytes, d = [], e = 0; e < c; e++) {
                            var f = b[e >>> 2] >>> 24 - e % 4 * 8 & 255;
                            d.push(String.fromCharCode(f))
                        }
                        return d.join("")
                    },
                    parse: function (a) {
                        for (var b = a.length, c = [], d = 0; d < b; d++)
                            c[d >>> 2] |= (255 & a.charCodeAt(d)) << 24 - d % 4 * 8;
                        return new g.init(c, b)
                    }
                }
                    , k = h.Utf8 = {
                    stringify: function (a) {
                        try {
                            return decodeURIComponent(escape(j.stringify(a)))
                        } catch (a) {
                            throw new Error("Malformed UTF-8 data")
                        }
                    },
                    parse: function (a) {
                        return j.parse(unescape(encodeURIComponent(a)))
                    }
                }
                    , l = e.BufferedBlockAlgorithm = f.extend({
                    reset: function () {
                        this._data = new g.init,
                            this._nDataBytes = 0
                    },
                    _append: function (a) {
                        "string" == typeof a && (a = k.parse(a)),
                            this._data.concat(a),
                            this._nDataBytes += a.sigBytes
                    },
                    _process: function (b) {
                        var c = this._data
                            , d = c.words
                            , e = c.sigBytes
                            , f = this.blockSize
                            , h = 4 * f
                            , i = e / h;
                        i = b ? a.ceil(i) : a.max((0 | i) - this._minBufferSize, 0);
                        var j = i * f
                            , k = a.min(4 * j, e);
                        if (j) {
                            for (var l = 0; l < j; l += f)
                                this._doProcessBlock(d, l);
                            var m = d.splice(0, j);
                            c.sigBytes -= k
                        }
                        return new g.init(m, k)
                    },
                    clone: function () {
                        var a = f.clone.call(this);
                        return a._data = this._data.clone(),
                            a
                    },
                    _minBufferSize: 0
                })
                    , m = (e.Hasher = l.extend({
                    cfg: f.extend(),
                    init: function (a) {
                        this.cfg = this.cfg.extend(a),
                            this.reset()
                    },
                    reset: function () {
                        l.reset.call(this),
                            this._doReset()
                    },
                    update: function (a) {
                        return this._append(a),
                            this._process(),
                            this
                    },
                    finalize: function (a) {
                        return a && this._append(a),
                            this._doFinalize()
                    },
                    blockSize: 16,
                    _createHelper: function (a) {
                        return function (b, c) {
                            return new a.init(c).finalize(b)
                        }
                    },
                    _createHmacHelper: function (a) {
                        return function (b, c) {
                            return new m.HMAC.init(a, c).finalize(b)
                        }
                    }
                }),
                    d.algo = {});
                return d
            }(Math);
            return a
        })
    }
        , {}],
    4: [function (a, b, c) {
        !function (d, e) {
            "object" == typeof c ? b.exports = c = e(a("./core")) : "function" == typeof define && define.amd ? define(["./core"], e) : e(d.CryptoJS)
        }(this, function (a) {
            return function () {
                function b(a, b, c) {
                    for (var d = [], f = 0, g = 0; g < b; g++)
                        if (g % 4) {
                            var h = c[a.charCodeAt(g - 1)] << g % 4 * 2
                                , i = c[a.charCodeAt(g)] >>> 6 - g % 4 * 2;
                            d[f >>> 2] |= (h | i) << 24 - f % 4 * 8,
                                f++
                        }
                    return e.create(d, f)
                }

                var c = a
                    , d = c.lib
                    , e = d.WordArray
                    , f = c.enc;
                f.Base64 = {
                    stringify: function (a) {
                        var b = a.words
                            , c = a.sigBytes
                            , d = this._map;
                        a.clamp();
                        for (var e = [], f = 0; f < c; f += 3)
                            for (var g = b[f >>> 2] >>> 24 - f % 4 * 8 & 255, h = b[f + 1 >>> 2] >>> 24 - (f + 1) % 4 * 8 & 255, i = b[f + 2 >>> 2] >>> 24 - (f + 2) % 4 * 8 & 255, j = g << 16 | h << 8 | i, k = 0; k < 4 && f + .75 * k < c; k++)
                                e.push(d.charAt(j >>> 6 * (3 - k) & 63));
                        var l = d.charAt(64);
                        if (l)
                            for (; e.length % 4;)
                                e.push(l);
                        return e.join("")
                    },
                    parse: function (a) {
                        var c = a.length
                            , d = this._map
                            , e = this._reverseMap;
                        if (!e) {
                            e = this._reverseMap = [];
                            for (var f = 0; f < d.length; f++)
                                e[d.charCodeAt(f)] = f
                        }
                        var g = d.charAt(64);
                        if (g) {
                            var h = a.indexOf(g);
                            -1 !== h && (c = h)
                        }
                        return b(a, c, e)
                    },
                    _map: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
                }
            }(),
                a.enc.Base64
        })
    }
        , {
            "./core": 3
        }],
    5: [function (a, b, c) {
        !function (d, e) {
            "object" == typeof c ? b.exports = c = e(a("./core")) : "function" == typeof define && define.amd ? define(["./core"], e) : e(d.CryptoJS)
        }(this, function (a) {
            return a.enc.Utf8
        })
    }
        , {
            "./core": 3
        }],
    6: [function (a, b, c) {
        !function (d, e, f) {
            "object" == typeof c ? b.exports = c = e(a("./core"), a("./sha1"), a("./hmac")) : "function" == typeof define && define.amd ? define(["./core", "./sha1", "./hmac"], e) : e(d.CryptoJS)
        }(this, function (a) {
            return function () {
                var b = a
                    , c = b.lib
                    , d = c.Base
                    , e = c.WordArray
                    , f = b.algo
                    , g = f.MD5
                    , h = f.EvpKDF = d.extend({
                    cfg: d.extend({
                        keySize: 4,
                        hasher: g,
                        iterations: 1
                    }),
                    init: function (a) {
                        this.cfg = this.cfg.extend(a)
                    },
                    compute: function (a, b) {
                        for (var c = this.cfg, d = c.hasher.create(), f = e.create(), g = f.words, h = c.keySize, i = c.iterations; g.length < h;) {
                            j && d.update(j);
                            var j = d.update(a).finalize(b);
                            d.reset();
                            for (var k = 1; k < i; k++)
                                j = d.finalize(j),
                                    d.reset();
                            f.concat(j)
                        }
                        return f.sigBytes = 4 * h,
                            f
                    }
                });
                b.EvpKDF = function (a, b, c) {
                    return h.create(c).compute(a, b)
                }
            }(),
                a.EvpKDF
        })
    }
        , {
            "./core": 3,
            "./hmac": 7,
            "./sha1": 10
        }],
    7: [function (a, b, c) {
        !function (d, e) {
            "object" == typeof c ? b.exports = c = e(a("./core")) : "function" == typeof define && define.amd ? define(["./core"], e) : e(d.CryptoJS)
        }(this, function (a) {
            !function () {
                var b = a
                    , c = b.lib
                    , d = c.Base
                    , e = b.enc
                    , f = e.Utf8
                    , g = b.algo;
                g.HMAC = d.extend({
                    init: function (a, b) {
                        a = this._hasher = new a.init,
                        "string" == typeof b && (b = f.parse(b));
                        var c = a.blockSize
                            , d = 4 * c;
                        b.sigBytes > d && (b = a.finalize(b)),
                            b.clamp();
                        for (var e = this._oKey = b.clone(), g = this._iKey = b.clone(), h = e.words, i = g.words, j = 0; j < c; j++)
                            h[j] ^= 1549556828,
                                i[j] ^= 909522486;
                        e.sigBytes = g.sigBytes = d,
                            this.reset()
                    },
                    reset: function () {
                        var a = this._hasher;
                        a.reset(),
                            a.update(this._iKey)
                    },
                    update: function (a) {
                        return this._hasher.update(a),
                            this
                    },
                    finalize: function (a) {
                        var b = this._hasher
                            , c = b.finalize(a);
                        return b.reset(),
                            b.finalize(this._oKey.clone().concat(c))
                    }
                })
            }()
        })
    }
        , {
            "./core": 3
        }],
    8: [function (a, b, c) {
        !function (d, e) {
            "object" == typeof c ? b.exports = c = e(a("./core")) : "function" == typeof define && define.amd ? define(["./core"], e) : e(d.CryptoJS)
        }(this, function (a) {
            return function (b) {
                function c(a, b, c, d, e, f, g) {
                    var h = a + (b & c | ~b & d) + e + g;
                    return (h << f | h >>> 32 - f) + b
                }

                function d(a, b, c, d, e, f, g) {
                    var h = a + (b & d | c & ~d) + e + g;
                    return (h << f | h >>> 32 - f) + b
                }

                function e(a, b, c, d, e, f, g) {
                    var h = a + (b ^ c ^ d) + e + g;
                    return (h << f | h >>> 32 - f) + b
                }

                function f(a, b, c, d, e, f, g) {
                    var h = a + (c ^ (b | ~d)) + e + g;
                    return (h << f | h >>> 32 - f) + b
                }

                var g = a
                    , h = g.lib
                    , i = h.WordArray
                    , j = h.Hasher
                    , k = g.algo
                    , l = [];
                !function () {
                    for (var a = 0; a < 64; a++)
                        l[a] = 4294967296 * b.abs(b.sin(a + 1)) | 0
                }();
                var m = k.MD5 = j.extend({
                    _doReset: function () {
                        this._hash = new i.init([1732584193, 4023233417, 2562383102, 271733878])
                    },
                    _doProcessBlock: function (a, b) {
                        for (var g = 0; g < 16; g++) {
                            var h = b + g
                                , i = a[h];
                            a[h] = 16711935 & (i << 8 | i >>> 24) | 4278255360 & (i << 24 | i >>> 8)
                        }
                        var j = this._hash.words
                            , k = a[b + 0]
                            , m = a[b + 1]
                            , n = a[b + 2]
                            , o = a[b + 3]
                            , p = a[b + 4]
                            , q = a[b + 5]
                            , r = a[b + 6]
                            , s = a[b + 7]
                            , t = a[b + 8]
                            , u = a[b + 9]
                            , v = a[b + 10]
                            , w = a[b + 11]
                            , x = a[b + 12]
                            , y = a[b + 13]
                            , z = a[b + 14]
                            , A = a[b + 15]
                            , B = j[0]
                            , C = j[1]
                            , D = j[2]
                            , E = j[3];
                        B = c(B, C, D, E, k, 7, l[0]),
                            E = c(E, B, C, D, m, 12, l[1]),
                            D = c(D, E, B, C, n, 17, l[2]),
                            C = c(C, D, E, B, o, 22, l[3]),
                            B = c(B, C, D, E, p, 7, l[4]),
                            E = c(E, B, C, D, q, 12, l[5]),
                            D = c(D, E, B, C, r, 17, l[6]),
                            C = c(C, D, E, B, s, 22, l[7]),
                            B = c(B, C, D, E, t, 7, l[8]),
                            E = c(E, B, C, D, u, 12, l[9]),
                            D = c(D, E, B, C, v, 17, l[10]),
                            C = c(C, D, E, B, w, 22, l[11]),
                            B = c(B, C, D, E, x, 7, l[12]),
                            E = c(E, B, C, D, y, 12, l[13]),
                            D = c(D, E, B, C, z, 17, l[14]),
                            C = c(C, D, E, B, A, 22, l[15]),
                            B = d(B, C, D, E, m, 5, l[16]),
                            E = d(E, B, C, D, r, 9, l[17]),
                            D = d(D, E, B, C, w, 14, l[18]),
                            C = d(C, D, E, B, k, 20, l[19]),
                            B = d(B, C, D, E, q, 5, l[20]),
                            E = d(E, B, C, D, v, 9, l[21]),
                            D = d(D, E, B, C, A, 14, l[22]),
                            C = d(C, D, E, B, p, 20, l[23]),
                            B = d(B, C, D, E, u, 5, l[24]),
                            E = d(E, B, C, D, z, 9, l[25]),
                            D = d(D, E, B, C, o, 14, l[26]),
                            C = d(C, D, E, B, t, 20, l[27]),
                            B = d(B, C, D, E, y, 5, l[28]),
                            E = d(E, B, C, D, n, 9, l[29]),
                            D = d(D, E, B, C, s, 14, l[30]),
                            C = d(C, D, E, B, x, 20, l[31]),
                            B = e(B, C, D, E, q, 4, l[32]),
                            E = e(E, B, C, D, t, 11, l[33]),
                            D = e(D, E, B, C, w, 16, l[34]),
                            C = e(C, D, E, B, z, 23, l[35]),
                            B = e(B, C, D, E, m, 4, l[36]),
                            E = e(E, B, C, D, p, 11, l[37]),
                            D = e(D, E, B, C, s, 16, l[38]),
                            C = e(C, D, E, B, v, 23, l[39]),
                            B = e(B, C, D, E, y, 4, l[40]),
                            E = e(E, B, C, D, k, 11, l[41]),
                            D = e(D, E, B, C, o, 16, l[42]),
                            C = e(C, D, E, B, r, 23, l[43]),
                            B = e(B, C, D, E, u, 4, l[44]),
                            E = e(E, B, C, D, x, 11, l[45]),
                            D = e(D, E, B, C, A, 16, l[46]),
                            C = e(C, D, E, B, n, 23, l[47]),
                            B = f(B, C, D, E, k, 6, l[48]),
                            E = f(E, B, C, D, s, 10, l[49]),
                            D = f(D, E, B, C, z, 15, l[50]),
                            C = f(C, D, E, B, q, 21, l[51]),
                            B = f(B, C, D, E, x, 6, l[52]),
                            E = f(E, B, C, D, o, 10, l[53]),
                            D = f(D, E, B, C, v, 15, l[54]),
                            C = f(C, D, E, B, m, 21, l[55]),
                            B = f(B, C, D, E, t, 6, l[56]),
                            E = f(E, B, C, D, A, 10, l[57]),
                            D = f(D, E, B, C, r, 15, l[58]),
                            C = f(C, D, E, B, y, 21, l[59]),
                            B = f(B, C, D, E, p, 6, l[60]),
                            E = f(E, B, C, D, w, 10, l[61]),
                            D = f(D, E, B, C, n, 15, l[62]),
                            C = f(C, D, E, B, u, 21, l[63]),
                            j[0] = j[0] + B | 0,
                            j[1] = j[1] + C | 0,
                            j[2] = j[2] + D | 0,
                            j[3] = j[3] + E | 0
                    },
                    _doFinalize: function () {
                        var a = this._data
                            , c = a.words
                            , d = 8 * this._nDataBytes
                            , e = 8 * a.sigBytes;
                        c[e >>> 5] |= 128 << 24 - e % 32;
                        var f = b.floor(d / 4294967296)
                            , g = d;
                        c[15 + (e + 64 >>> 9 << 4)] = 16711935 & (f << 8 | f >>> 24) | 4278255360 & (f << 24 | f >>> 8),
                            c[14 + (e + 64 >>> 9 << 4)] = 16711935 & (g << 8 | g >>> 24) | 4278255360 & (g << 24 | g >>> 8),
                            a.sigBytes = 4 * (c.length + 1),
                            this._process();
                        for (var h = this._hash, i = h.words, j = 0; j < 4; j++) {
                            var k = i[j];
                            i[j] = 16711935 & (k << 8 | k >>> 24) | 4278255360 & (k << 24 | k >>> 8)
                        }
                        return h
                    },
                    clone: function () {
                        var a = j.clone.call(this);
                        return a._hash = this._hash.clone(),
                            a
                    }
                });
                g.MD5 = j._createHelper(m),
                    g.HmacMD5 = j._createHmacHelper(m)
            }(Math),
                a.MD5
        })
    }
        , {
            "./core": 3
        }],
    9: [function (a, b, c) {
        !function (d, e, f) {
            "object" == typeof c ? b.exports = c = e(a("./core"), a("./cipher-core")) : "function" == typeof define && define.amd ? define(["./core", "./cipher-core"], e) : e(d.CryptoJS)
        }(this, function (a) {
            return a.mode.ECB = function () {
                var b = a.lib.BlockCipherMode.extend();
                return b.Encryptor = b.extend({
                    processBlock: function (a, b) {
                        this._cipher.encryptBlock(a, b)
                    }
                }),
                    b.Decryptor = b.extend({
                        processBlock: function (a, b) {
                            this._cipher.decryptBlock(a, b)
                        }
                    }),
                    b
            }(),
                a.mode.ECB
        })
    }
        , {
            "./cipher-core": 2,
            "./core": 3
        }],
    10: [function (a, b, c) {
        !function (d, e) {
            "object" == typeof c ? b.exports = c = e(a("./core")) : "function" == typeof define && define.amd ? define(["./core"], e) : e(d.CryptoJS)
        }(this, function (a) {
            return function () {
                var b = a
                    , c = b.lib
                    , d = c.WordArray
                    , e = c.Hasher
                    , f = b.algo
                    , g = []
                    , h = f.SHA1 = e.extend({
                    _doReset: function () {
                        this._hash = new d.init([1732584193, 4023233417, 2562383102, 271733878, 3285377520])
                    },
                    _doProcessBlock: function (a, b) {
                        for (var c = this._hash.words, d = c[0], e = c[1], f = c[2], h = c[3], i = c[4], j = 0; j < 80; j++) {
                            if (j < 16)
                                g[j] = 0 | a[b + j];
                            else {
                                var k = g[j - 3] ^ g[j - 8] ^ g[j - 14] ^ g[j - 16];
                                g[j] = k << 1 | k >>> 31
                            }
                            var l = (d << 5 | d >>> 27) + i + g[j];
                            l += j < 20 ? 1518500249 + (e & f | ~e & h) : j < 40 ? 1859775393 + (e ^ f ^ h) : j < 60 ? (e & f | e & h | f & h) - 1894007588 : (e ^ f ^ h) - 899497514,
                                i = h,
                                h = f,
                                f = e << 30 | e >>> 2,
                                e = d,
                                d = l
                        }
                        c[0] = c[0] + d | 0,
                            c[1] = c[1] + e | 0,
                            c[2] = c[2] + f | 0,
                            c[3] = c[3] + h | 0,
                            c[4] = c[4] + i | 0
                    },
                    _doFinalize: function () {
                        var a = this._data
                            , b = a.words
                            , c = 8 * this._nDataBytes
                            , d = 8 * a.sigBytes;
                        return b[d >>> 5] |= 128 << 24 - d % 32,
                            b[14 + (d + 64 >>> 9 << 4)] = Math.floor(c / 4294967296),
                            b[15 + (d + 64 >>> 9 << 4)] = c,
                            a.sigBytes = 4 * b.length,
                            this._process(),
                            this._hash
                    },
                    clone: function () {
                        var a = e.clone.call(this);
                        return a._hash = this._hash.clone(),
                            a
                    }
                });
                b.SHA1 = e._createHelper(h),
                    b.HmacSHA1 = e._createHmacHelper(h)
            }(),
                a.SHA1
        })
    }
        , {
            "./core": 3
        }],
    11: [function (a, b, c) {
        var d = a("login-form")
            , e = a("user-register-dialog");
        $(function () {
            d.init(),
                $("#btn-user-register").on("click", function (a) {
                    a.preventDefault(),
                        e.open()
                }),
                $("#phone-btn-user-register").on("click", function (a) {
                    a.preventDefault(),
                        e.open()
                }),
                $("#pwdlogin").on("click", function (a) {
                    $("#login-form").show(),
                        $("#pwdlogin").css("background", "#f8931e"),
                        $("#phone-login-form").hide(),
                        $("#smslogin").css("background", "#d2d1d1"),
                        $("#wx-qrcode").hide(),
                        $("#wxlogin").css("background", "#d2d1d1")
                }),
                $("#wxlogin").on("click", function (a) {
                    "" === $("#wxLoginCode").html() && function () {
                        var a = new Date;
                        $(".copyright-end-time").text(a.getFullYear()),
                            window.wxLoginInst = new WxLogin({
                                self_redirect: !0,
                                id: "wxLoginCode",
                                appid: XSMConfig.appid,
                                scope: "snsapi_login",
                                redirect_uri: XSMConfig.redirect_uri,
                                state: "",
                                style: "",
                                href: "data:text/css;base64,LmltcG93ZXJCb3ggLnFyY29kZSB7d2lkdGg6IDIwMHB4O30NCi5pbXBvd2VyQm94IC50aXRsZSB7dGV4dC1hbGlnbjogY2VudGVyO30NCi5pbXBvd2VyQm94IC5pbmZvIHtkaXNwbGF5OiBub25lO30NCi5zdGF0dXNfaWNvbiB7ZGlzcGxheTogbm9uZX0NCi5pbXBvd2VyQm94IC5zdGF0dXMge3RleHQtYWxpZ246IGNlbnRlcjt9"
                            })
                    }(),
                        $("#wx-qrcode").show(),
                        $("#wxlogin").css("background", "#f8931e"),
                        $("#login-form").hide(),
                        $("#pwdlogin").css("background", "#d2d1d1"),
                        $("#phone-login-form").hide(),
                        $("#smslogin").css("background", "#d2d1d1")
                }),
                $("#smslogin").on("click", function (a) {
                    $("#phone-login-form").show(),
                        $("#smslogin").css("background", "#f8931e"),
                        $("#login-form").hide(),
                        $("#pwdlogin").css("background", "#d2d1d1"),
                        $("#wx-qrcode").hide(),
                        $("#wxlogin").css("background", "#d2d1d1")
                })
        })
    }
        , {
            "login-form": 12,
            "user-register-dialog": 23
        }],
    12: [function (a, b, c) {
        function d(a) {
            a.focus(),
                H.hidePlaceholder(a[0])
        }

        function e() {
            var a = L.userName();
            if ("" == a)
                return Q = !1,
                    G.alert("请输入用户名！").done(function () {
                        d(y)
                    }),
                    !1;
            var b = L.password();
            if ("" == b)
                return Q = !1,
                    G.alert("请输入密码！").done(function () {
                        d(z)
                    }),
                    !1;
            var c = I.getValue();
            if (I.isActive() && !c)
                return Q = !1,
                    G.alert("请输入验证码！").done(function () {
                        I.focus()
                    }),
                    !1;
            u();
            var e = b;
            b = F(F(b) + c);
            var g = {
                protocol: location.protocol,
                loginIndex: location.href
            };
            return g.j_mmrm = a,
                g.j_mcmm = b,
                g.j_valcode = c,
                P.j_mmrm = a,
                P.j_mcmm = F(F(e) + ""),
                E.getCookie("usercomcookieId").done(function (b) {
                    b && "null" !== b && (b = b.split(",")[0]) !== a.toUpperCase() && (g.j_puserId = b,
                        P.j_puserId = b,
                        E.getCookie("myguid1234567890").done(function (a) {
                            g.j_guid = a,
                                P.j_guid = a
                        }))
                }).always(function () {
                    J.login(g).done(f).fail(q)
                }),
                !1
        }

        function f(a) {
            var b = v(decodeURIComponent(a));
            b.documentElement && "xsm" == b.documentElement.nodeName || (b = a.replace(/\n/g, ""),
            -1 === b.indexOf("<xml>") && (b = b.replace("<xsm ", "<xml><xsm ")),
            -1 === b.indexOf("</xml>") && (b = b.replace("</xsm>", "</xsm></xml>")));
            var c = $(b).find("xsm");
            if (S = c,
            null == c[0])
                return void r("服务器返回数据错误，请与管理员联系！");
            var d = c.attr("code")
                , e = c.attr("msg")
                , i = c.find("userType").text()
                , j = c.find("comId").text();
            if ("0000" == d) {
                var l = c.find("passwordStatus").text();
                if ("1" == l) {
                    var e = "您的密码已超过90天未修改，请及时修改密码！"
                        , o = g(e);
                    G.prompt(o, m),
                        "1000" == i ? J.checkModifyForced().done(function (a) {
                            a && a.data && ($("#nextModify").css("display", "none"),
                                $("#modify").css("margin-right", "0px"))
                        }) : ($("#nextModify").css("display", "none"),
                            $("#modify").css("margin-right", "0px"))
                } else if ("2" == l) {
                    var e = "您的密码过于简单，请前往密码修改页面按照要求设置复杂密码！"
                        , o = g(e);
                    G.prompt(o, m),
                    "1000" == i && 0 != j.indexOf("1444") || ($("#nextModify").css("display", "none"),
                        $("#modify").css("margin-right", "0px"))
                } else
                    n(c)
            } else if ("9201" == d) {
                var o = g(e);
                G.prompt(o, m),
                    $("#nextModify").remove(),
                    $("#modify").css("margin-right", "0px")
            } else if (new RegExp("^02").test(d))
                "0200" === d || "0231" === d ? h(c) : k();
            else if ("0300" == d)
                O.init({
                    random: c.find("random").text(),
                    previousURL: c.find("appUrl").text()
                }),
                    O.createQRURL().done(function (a) {
                        O.showDialog(a.base64, O.stopCheckLoginStatus),
                            O.checkLoginStatus(function (a) {
                                O.stopCheckLoginStatus(),
                                    J.loginForQR(a).done(f).fail(function () {
                                        J.deleteSessionForQR(),
                                            q(e)
                                    })
                            }, function (a) {
                                O.stopCheckLoginStatus(),
                                    J.deleteSessionForQR(),
                                    q(a)
                            })
                    }).fail(function (a) {
                        J.deleteSessionForQR(),
                            q(a)
                    });
            else {
                var p = c.find("NEED_CODE").text();
                "1" == p && I.activeValidate(),
                    r(e ? e : "数据错误：" + b)
            }
        }

        function g(a) {
            return '<span style="font-weight:bold;display:block;text-align:center;font-size:24px;">密码安全风险提醒</span>尊敬的用户：<p><span style="color:red;font-weight:bold;font-size: 20px;">' + "为避免账户风险，建议您务必将密码设置为复杂密码！" + '</span><p><p>您的中烟新商盟卷烟订货商务平台账号、密码是您身份标识、鉴别的重要信息。</p><p>一、请您务必将密码设置为复杂密码，密码长度不少于8位，包含字母和数字。</p><p>二、请您在中烟新商盟卷烟订货商务平台“我的新商盟“页面中，将邮箱填写完整，当密码忘记时，可以通过系统自主找回密码。</p><p>三、请您定期修改密码，保护账户安全。</p><p>四、请保护好您的账号和密码，不要随意透露给任何人，对可疑的电子邮件、短信、电话等方式索要账号和密码的行为要提高警惕、谨慎确认，若有任何疑问，请立即致电您的客户经理。</p><p style="text-align:right;padding-right: 1em;">中烟新商盟卷烟订货商务平台</p>'
        }

        function h(a) {
            var b = a.find("phone").text()
                , c = a.find("sendTime").text()
                , d = a.find("expiredSecond").text()
                , e = a.find("remainingSecond").text() ? a.find("remainingSecond").text() : d;
            G.sms('<span style="font-weight:bold;display:block;text-align:center;font-size:22px;">为了您更安全的使用新商盟，现对您的登录进行手机短信验证</span><hr style="height: 0px;height: 3px;border:none;border-top: 3px double #737473;"><p style="color:#666;font-weight:bold;margin-top: 20px"><span >新商盟已于 <span style="color: red;margin: 0 3px" id="sendTime">' + M.getHMfromDateTimeStr(c) + '</span> 向您的手机 <span id="monbile" style="color: red;margin: 0 3px">' + b + '</span> 发送登录验证码，请及时录入</span><p><p span style="color:#666;font-weight:bold">验证码<span style="color: red;margin: 0 3px" id="expiryLength">' + M.second2Datetime(d) + '</span>内有效， <span id="countDownSpan" style="color: red;margin: 0 3px"></span><span>后可点击重新获取</span><span style="display:none;cursor: pointer;color: #0000CD;margin: 0 1px"  id="getNextSMS"> 重新获取</span></p><p style="margin-top: 20px">短信验证码：<input id="SMSCode" style="width: 186px;height: 20px;line-height: 20px;"/><span style="color: red;margin: 0 28px;display: none;font-weight:bold" id="validateMessage"></span></p>', i),
                R.callback = function (a) {
                    a.text("验证码已失效。").next().text("").next().show().unbind("click").bind("click", j),
                        $("#SMSCode").val("验证码已失效，请重新获取").attr("disabled", !0),
                        $("#validateMessage").text("")
                }
                ,
                R.timelong = e,
                M.timecountdown($("#countDownSpan"), R)
        }

        function i(a) {
            if ("smsValidate" == a.type) {
                if ($("#SMSCode").attr("disabled"))
                    return void $("#validateMessage").hide().show("normal").text("验证码已失效!");
                if ($.trim($("#SMSCode").val()).length < 1)
                    return void $("#validateMessage").hide().show("normal").text("验证码不能为空!");
                if (6 != $.trim($("#SMSCode").val()).length)
                    return void $("#validateMessage").hide().show("normal").text("验证码必须为六位!");
                var b = {
                    j_mmrm: L.userName(),
                    j_valcode: $.trim($("#SMSCode").val())
                };
                J.validateSms(b).done(function (a) {
                    var b = l(a);
                    null == b[0] && k(),
                        "0000" === b.attr("code") ? n(b) : $("#validateMessage").hide().show("normal").text("验证错误，重新输入!")
                }).fail(function (a) {
                    k()
                })
            } else
                "close" == a.type && J.deleteSession(b).always(function (a) {
                })
        }

        function j() {
            var a = {
                j_mmrm: L.userName()
            };
            J.regetSMS(a).done(function (a) {
                var b = l(a);
                null == b[0] && k(),
                    "0200" === b.attr("code") || "0231" === b.attr("code") ? h(b) : k()
            }).fail(function () {
                k()
            })
        }

        function k() {
            G.error("连接短信平台服务器失败，请检查您的网络或与客户经理联系。").done(function () {
                d(z)
            })
        }

        function l(a) {
            var b = v(decodeURIComponent(a));
            return b.documentElement && "xsm" == b.documentElement.nodeName || (b = data.replace(/\n/g, ""),
            -1 === b.indexOf("<xml>") && (b = b.replace("<xsm ", "<xml><xsm ")),
            -1 === b.indexOf("</xml>") && (b = b.replace("</xsm>", "</xsm></xml>"))),
                $(b).find("xsm")
        }

        function m(a) {
            if ("go" == a.type) {
                var b = L.userName();
                b = N.encrypt(b),
                    b = encodeURIComponent(encodeURIComponent(b));
                var c = XSMConfig.st + "/users/selfservice/toChangePassword?mmxmId=" + b;
                window.location.href = c
            } else
                "close" == a.type && n(S)
        }

        function n(a) {
            L.rememberUser() ? E.setCookiefroUn("index_userid", L.userName()) : E.setCookiefroUn("index_userid", ""),
                E.getCookie("myguid1234567890").done(function (a) {
                    a || E.setMyguidCookie(D.getGUID())
                }).fail(function () {
                    E.setMyguidCookie(D.getGUID())
                }).always(function () {
                    o(a)
                })
        }

        function o(a) {
            var b = a.find("domainUrl").text()
                , c = a.find("userId").text()
                , d = a.find("comId").text();
            E.setCookie("usercomcookieId", c + "," + d);
            var e = K.getUrl();
            e && (b = e),
                I.unactiveValidate();
            var f = t(b);
            Q ? (J.getNoCgtUrl(d).done(function (a) {
                "0000" === a.CODE && a.NO_CGT_URL ? window.location.href = a.NO_CGT_URL : (setTimeout(f, 3e3),
                    G.alert("您所在的地市尚未开通非烟订货业务<br />将为您跳转新商盟首页").done(f))
            }).fail(function () {
                setTimeout(f, 3e3),
                    G.alert("获取非烟系统信息失败<br />将为您跳转新商盟首页").done(f)
            }),
                Q = !1) : -1 != b.indexOf("xsm2/xsm.html") ? p(XSMConfig.login + "/users/logout?web=true").done(function () {
                J.loginSt(P).done(function () {
                    window.location.href = b
                })
            }) : window.location.href = b
        }

        function p(a) {
            var b = $.Deferred();
            return $.ajax({
                url: a,
                dataType: "jsonp",
                type: "POST",
                jsonp: "jsonp"
            }).always(function () {
                b.resolve()
            }),
                b.promise()
        }

        function q(a) {
            r(a || "登录失败，无法连接到登录服务器，请检查您的网络或与客户经理联系。")
        }

        function r(a) {
            var b;
            if ("object" == typeof a) {
                b = [];
                for (var c in a)
                    a.hasOwnProperty(c) && b.push(c + ":" + a[c]);
                b = b.join("\n")
            } else
                b = a;
            Q = !1,
                s(b)
        }

        function s(a) {
            if (-1 != a.indexOf("hn_")) {
                var b = "http://96368.hntobacco.com";
                G.alert("您所在烟草公司已启用统一订单平台订货，初始账号密码与新商盟保持一致，系统地址为：" + b + "，有任何问题请与您的客户经理联系！").done(function () {
                    location.href = b
                })
            } else
                a.indexOf("loginWarnning.jsp") > -1 ? location.href = XSMConfig.login + "/jsp/loginWarnning.jsp" : G.error(a).done(function () {
                    z.val(""),
                        $("#mcmm1").val(""),
                        d($("#mcmm1"))
                })
        }

        function t(a) {
            return function () {
                location.href = a
            }
        }

        function u() {
            E.clearCookie("/"),
                E.clearCookie("/app/"),
                E.clearCookie("/", ".xinshangmeng.com"),
                E.clearCookie("/", ".preview.xinshangmeng.com"),
                E.clearCookie("/", ".test.xinshangmeng.com"),
                E.clearCookie("/", ".dynamic.xinshangmeng.com")
        }

        function v(a) {
            var b;
            return $.browser.msie ? (b = new ActiveXObject("Microsoft.XMLDOM"),
                b.async = !1,
                b.loadXML(a)) : b = (new DOMParser).parseFromString(a, "text/xml"),
                b
        }

        function w(a, b) {
            var c = $(a.currentTarget)
                , d = b || 5
                , e = c.text();
            c.text(d + " 秒").prop("disabled", !0).addClass("disabled");
            var f = setInterval(function () {
                1 === d ? (c.text(e).prop("disabled", !1).removeClass("disabled"),
                    clearInterval(f)) : c.text(--d + " 秒")
            }, 1e3)
        }

        function x(a) {
            var b = a.secretUserId
                , c = (a.mobile,
                a.comId)
                , d = a.ecPath;
            "https:" == window.location.protocol && (d = d.replace("http:", "https:").replace(":80", "")),
                $.ajax({
                    type: "get",
                    url: d + "/sms/ecSms/sendSmsByUserIdAndVerifiedType",
                    dataType: "jsonp",
                    data: {
                        userId: b,
                        verifiedType: 50,
                        comId: c,
                        key: "SMS_LOGIN"
                    }
                }).done(function (a) {
                    "0000" === a.code ? G.success(a.msg) : G.error(a.msg)
                })
        }

        var y, z, A, B, C, D = a("utils"), E = D.Cookie, F = a("md5").hex_md5, G = a("msgbox"), H = a("placeholder"),
            I = a("validate-code"), J = a("web-utils"), K = a("redirect"), L = a("form-store"), M = a("count-down"),
            N = a("xsm-aes"), O = a("qr"), P = {
                protocol: location.protocol,
                loginIndex: location.href
            }, Q = !1, R = {
                timelong: 30,
                format: "minute分second秒",
                callback: function (a) {
                    return !1
                }
            };
        c.init = function () {
            H.init(),
                I.init();
            var a = $("#login-form");
            y = $("#username"),
                z = $("#mcmm");
            var b;
            E.getCookie("isSpWxsm").done(function (a) {
                b = a,
                    A = a,
                    "1" === a ? $("#wxlogin").css("display", "block") : $("#wxlogin").css("display", "none")
            }),
                E.getCookie("isSpDxdl").done(function (a) {
                    B = a,
                        "1" === a ? $("#smslogin").css("display", "block") : $("#smslogin").css("display", "none"),
                        "1" === b || "1" === B ? $("#pwdlogin").css("display", "block") : $("#pwdlogin").css("display", "none")
                }),
                E.getCookie("isSpDxdlpw").done(function (a) {
                    C = a,
                        "1" === a ? ($(".pwshow").show(),
                            $("#login-form-phone-box").addClass("validate-code-box-show")) : ($(".pwshow").hide(),
                            $("#login-form-phone-box").removeClass("validate-code-box-show"))
                }),
                K.getUserId().done(function (a) {
                    a ? (L.userName(a),
                        H.hidePlaceholder(y[0]),
                        d(z)) : E.getCookie("index_userid").done(function (a) {
                        a ? (L.userName(a),
                            H.hidePlaceholder(y[0]),
                            L.rememberUser(!0),
                            d(z)) : d(y)
                    })
                }),
                a.submit(e),
                $("#btn-no-cgt-login").click(function (b) {
                    b.preventDefault(),
                        w(b),
                        Q = !0,
                        a.submit()
                }),
                $("#phone-btn-no-cgt-login").click(function (b) {
                    b.preventDefault(),
                        w(b),
                        Q = !0,
                        a.submit()
                }),
                a.find(".link-find-mcmm").attr("href", XSMConfig.st + "/users/resetpwd/start?protocol=" + location.protocol)
        }
        ;
        var S;
        $("#get-phone-validate-code").click(function () {
            var a = $("#get-phone-validate-code")
                , b = 60
                , c = b || 5
                , e = a.text()
                , f = L.userNamePhone();
            if ("" == f)
                return Q = !1,
                    G.alert("请输入用户名！").done(function () {
                        d(y)
                    }),
                    !1;
            var f = L.userNamePhone();
            $.ajax({
                type: "get",
                url: XSMConfig.st + "/users/resetpwd/getLoginPhoneByUserId/" + f,
                dataType: "jsonp"
            }).done(function (a) {
                if (a && a.isSpDxdl && a.isSpDxdl != '1') {
                    G.alert("您所在的地市不支持手机登录！");
                    return;
                }
                if (a && a.mobile) {
                    a.mobile;
                    x(a)
                } else
                    "0000" === a.code && "" === a.mobile ? G.alert("您的账号没有维护手机号！") : "0000" === a.code ? G.alert(a.msg) : G.error(a.msg)
            }),
                a.text(c + " 秒").prop("disabled", !0).addClass("disabled");
            var g = setInterval(function () {
                1 === c ? (a.text(e).prop("disabled", !1).removeClass("disabled"),
                    clearInterval(g)) : a.text(--c + " 秒")
            }, 1e3)
        }),
            $("#phone-btn-login").click(function () {
                var a = L.userNamePhone();
                if ("" == a)
                    return Q = !1,
                        G.alert("请输入用户名！").done(function () {
                            d(y)
                        }),
                        !1;
                if ("1" === C) {
                    var b = L.passwordPhone();
                    if ("" == b)
                        return Q = !1,
                            G.alert("请输入密码！").done(function () {
                                d(z)
                            }),
                            !1
                }
                var c = $("#phone-validate-code").val();
                if (I.isActive() && !c)
                    return Q = !1,
                        G.alert("请输入验证码！"),
                        !1;
                u();
                var e = {
                    protocol: location.protocol,
                    loginIndex: location.href
                };
                e.j_mmrm = a,
                    e.j_valcode = c,
                "1" === C && (e.j_mcmm = F(F(b) + "")),
                    $.ajax({
                        url: XSMConfig.login + "/users/dologin/sms",
                        type: "post",
                        dataType: "jsonp",
                        jsonp: "jsonp",
                        data: e
                    }).done(f).fail(q)
            })
    }
        , {
            "count-down": 13,
            "form-store": 14,
            md5: 20,
            msgbox: 21,
            placeholder: 22,
            qr: 15,
            redirect: 16,
            utils: 26,
            "validate-code": 17,
            "web-utils": 18,
            "xsm-aes": 19
        }],
    13: [function (a, b, c) {
        c.timecountdown = function (a, b) {
            function c() {
                var c = setInterval(function () {
                    b.timelong > 0 ? (a.text(d()),
                        b.timelong--) : (clearInterval(c),
                        b.callback(a))
                }, 1e3)
            }

            function d() {
                var a = 0
                    , c = 0
                    , d = 0
                    , e = parseInt(b.timelong) % 60;
                (d = parseInt(b.timelong / 60)) > 60 && (d = parseInt(b.timelong / 60) % 60,
                (c = parseInt(parseInt(b.timelong / 60) / 60)) > 24 && (c = parseInt(parseInt(b.timelong / 60) / 60) % 24,
                    a = parseInt(parseInt(parseInt(b.timelong / 60) / 60) / 24)));
                var f = b.format;
                return -1 != f.indexOf("day") && (f = f.replace("day", a)),
                -1 != f.indexOf("hour") && (f = f.replace("hour", c)),
                -1 != f.indexOf("minute") && (f = f.replace("minute", d)),
                -1 != f.indexOf("second") && (f = f.replace("second", e)),
                    f
            }

            b = jQuery.extend({
                timelong: 60,
                format: "day天hour时minute分second秒",
                callback: function () {
                    return !1
                }
            }, b || {}),
                c()
        }
            ,
            c.getHMfromDateTimeStr = function (a) {
                return a && a.length >= 14 ? a.substring(8, 10) + ":" + a.substring(10, 12) + ":" + a.substring(12, 14) : "unkown"
            }
            ,
            c.second2Datetime = function (a) {
                if (a && !isNaN(Number(a))) {
                    var b = Number(a);
                    return (Math.floor(b / 60) > 0 ? Math.floor(b / 60) + "分" : "") + (b % 60 > 0 ? b % 60 + "秒" : "")
                }
                return "unkown"
            }
    }
        , {}],
    14: [function (a, b, c) {
        function d(a) {
            return function (b) {
                var c = $(a);
                if (void 0 === b)
                    return $.trim(c.val());
                c.val($.trim(b))
            }
        }

        function e(a) {
            return function (b) {
                var c = $(a);
                if (void 0 === b)
                    return c.prop("checked");
                c.prop("checked", b)
            }
        }

        c.userName = d("#username"),
            c.password = d("#mcmm"),
            c.rememberUser = e("#remember-user"),
            c.userNamePhone = d("#phone-username"),
            c.passwordPhone = d("#phone-mcmm"),
            c.rememberUserPhone = e("#phone-remember-user")
    }
        , {}],
    15: [function (a, b, c) {
        function d() {
            clearInterval(i),
                clearTimeout(j),
                i = null,
                j = null
        }

        var e = a("msgbox")
            , f = a("web-utils")
            , g = ""
            , h = ""
            , i = null
            , j = null;
        c.init = function (a) {
            g = a.previousURL || "",
                h = a.random || ""
        }
            ,
            c.showDialog = function (a, b) {
                e.qrPrompt('<span style="font-weight:bold;display:block;text-align:center;font-size:22px;">为了您更安全的使用新商盟，现对您的登录进行安全验证</span><hr style="height: 0px;height: 3px;border:none;border-top: 3px double #737473;"><p style="text-align: center;"><div style="text-align: center;"><img style="margin-top: 10px; width: 200px; height: 200px;" id="qr-img" src="' + a + '" /><div style="color: #999;">请使用<span style="color: red;margin: 0 4px;">微信</span>扫描二维码进行安全验证</div></div></p><p style="margin-top: 10px; text-align: center;"><span style="color: red;display: none;font-weight:bold" id="qrErrorMessage"></span></p>', b, {
                    cancelBtnText: "返回登录页"
                })
            }
            ,
            c.createQRURL = function () {
                var a = $.Deferred();
                return f.getQR(g, h).done(function (b) {
                    "0000" === b.code ? a.resolve({
                        base64: "data:image/png;base64," + b.data,
                        expiredSecond: b.expiredSecond
                    }) : a.reject(b.msg)
                }).fail(function () {
                    a.reject()
                }),
                    a.promise()
            }
            ,
            c.checkLoginStatus = function (a, b) {
                i = setInterval(function () {
                    f.checkLoginForQR(g, h).done(function (c) {
                        if ("0000" === c.code)
                            "function" == typeof a && a({
                                un: c.username,
                                random: c.random
                            });
                        else {
                            if (j)
                                return;
                            j = setTimeout(function () {
                                "function" == typeof b && b(c.msg)
                            }, 18e5)
                        }
                    }).fail(d)
                }, 5e3)
            }
            ,
            c.stopCheckLoginStatus = d
    }
        , {
            msgbox: 21,
            "web-utils": 18
        }],
    16: [function (a, b, c) {
        function d() {
            for (var a, b = {}, c = location.search.substr(1).split("&"), d = 0; a = c[d++];) {
                var e = a.indexOf("=");
                if (e > 0) {
                    var f = a.substr(0, e)
                        , g = a.substr(e + 1);
                    g = decodeURIComponent(g),
                        b[f] = g
                }
            }
            return b
        }

        var e = a("utils").Cookie;
        c.getUserId = function () {
            var a = $.Deferred();
            return d().user_id ? a.resolve(d().user_id) : e.getCookie("userId").done(function (b) {
                a.resolve(b)
            }).fail(function () {
                a.resolve(null)
            }),
                a.promise()
        }
            ,
            c.getUrl = function () {
                return d().redirect_url
            }
    }
        , {
            utils: 26
        }],
    17: [function (a, b, c) {
        function d(a) {
            var b = $(a.currentTarget);
            b.val(b.val().replace(/\D/g, ""))
        }

        function e() {
            $(p).val("")
        }

        function f() {
            return $(p).val()
        }

        function g() {
            var a = $(p);
            a.focus(),
                n.hidePlaceholder(a[0])
        }

        function h() {
            var a = XSMConfig.login + "/users/forlogin/img?width=80&height=30&" + (new Date).getTime();
            $(q).attr("src", a)
        }

        function i() {
            return o
        }

        function j() {
            l.show().closest("form").addClass("validate-code-box-show"),
                e(),
                o = !0
        }

        function k() {
            l.hide().closest("form").removeClass("validate-code-box-show"),
                o = !1
        }

        var l, m = a("utils").Cookie, n = a("placeholder"), o = !1, p = "#validate-code-text", q = "#validate-code-img",
            r = "need_code";
        c.init = function () {
            l = $(".validate-code-box"),
                m.getCookie(r).done(function (a) {
                    "1" == a && (j(),
                        h())
                }),
                l.on("keypress change", p, d).on("click", ".btn-refresh", h)
        }
            ,
            c.getValue = f,
            c.focus = g,
            c.isActive = i,
            c.unactiveValidate = function () {
                k(),
                    m.delCookiefroUn(r)
            }
            ,
            c.activeValidate = function () {
                j(),
                    h(),
                    m.setCookiefroUn(r, "1")
            }
    }
        , {
            placeholder: 22,
            utils: 26
        }],
    18: [function (a, b, c) {
        c.login = function (a) {
            return $.ajax({
                url: XSMConfig.login + "/users/dologin/dfaup",
                type: "post",
                dataType: "jsonp",
                jsonp: "jsonp",
                data: a
            })
        }
            ,
            c.smsLogin = function (a) {
                return $.ajax({
                    url: XSMConfig.login + "/users/dologin/sms",
                    type: "post",
                    dataType: "jsonp",
                    jsonp: "jsonp",
                    data: a
                })
            }
            ,
            c.loginSt = function (a) {
                return $.ajax({
                    url: XSMConfig.st + "/users/dologin/up",
                    type: "post",
                    dataType: "jsonp",
                    jsonp: "jsonp",
                    data: a
                })
            }
            ,
            c.getNoCgtUrl = function (a) {
                return $.ajax({
                    url: XSMConfig.home + "/inter/comConfig.do?method=getNoCgtUrl&comId=" + a,
                    dataType: "jsonp",
                    jsonp: "jsonp"
                })
            }
            ,
            c.regetSMS = function (a) {
                return $.ajax({
                    url: XSMConfig.login + "/users/forlogin/dualfactor",
                    type: "post",
                    async: !1,
                    dataType: "jsonp",
                    jsonp: "jsonp",
                    data: a
                })
            }
            ,
            c.validateSms = function (a) {
                return $.ajax({
                    url: XSMConfig.login + "/users/dologin/dualfactor",
                    type: "post",
                    async: !1,
                    dataType: "jsonp",
                    jsonp: "jsonp",
                    data: a
                })
            }
            ,
            c.deleteSession = function (a) {
                return $.ajax({
                    url: XSMConfig.login + "/users/forlogin/dualfactorcancel",
                    type: "post",
                    async: !0,
                    dataType: "jsonp",
                    jsonp: "jsonp",
                    data: a
                })
            }
            ,
            c.deleteSessionForQR = function () {
                return $.ajax({
                    url: XSMConfig.login + "/users/forlogin/isqrcacancel",
                    async: !0,
                    dataType: "jsonp",
                    jsonp: "jsonp"
                })
            }
            ,
            c.checkModifyForced = function () {
                return $.ajax({
                    url: XSMConfig.login + "/member/user/userInfo.do?method=checkModifyForced",
                    type: "GET",
                    dataType: "jsonp",
                    jsonp: "callbackparam"
                })
            }
            ,
            c.checkLoginForQR = function (a, b) {
                return $.ajax({
                    url: a + "/MAuthServer/qrcode/isLogin.do",
                    dataType: "jsonp",
                    jsonp: "jsonp",
                    data: {
                        random: b,
                        t: +new Date
                    }
                })
            }
            ,
            c.getQR = function (a, b) {
                return $.ajax({
                    url: a + "/MAuthServer/web/getChatQrcode.do",
                    dataType: "jsonp",
                    jsonp: "jsonp",
                    data: {
                        random: b
                    }
                })
            }
            ,
            c.loginForQR = function (a) {
                return $.ajax({
                    url: XSMConfig.login + "/users/dologin/isqrca",
                    dataType: "jsonp",
                    type: "POST",
                    jsonp: "jsonp",
                    data: a
                })
            }
    }
        , {}],
    19: [function (a, b, c) {
        var d = a("crypto-js/aes")
            , e = a("crypto-js/enc-utf8")
            , f = a("crypto-js/enc-base64")
            , g = a("crypto-js/mode-ecb")
            , h = e.parse("Wa2cgI0e8nE8CJb1");
        c.encrypt = function (a) {
            var b = e.parse(a)
                , c = d.encrypt(b, h, {
                mode: g
            });
            return f.stringify(c.ciphertext)
        }
            ,
            c.decrypt = function (a) {
                var b = f.parse(a)
                    , c = f.stringify(b);
                return d.decrypt(c, h, {
                    mode: g
                }).toString(e).toString()
            }
    }
        , {
            "crypto-js/aes": 1,
            "crypto-js/enc-base64": 4,
            "crypto-js/enc-utf8": 5,
            "crypto-js/mode-ecb": 9
        }],
    20: [function (a, b, c) {
        function d(a) {
            return n(e(o(m(a + "{1#2$3%4(5)6@7!poeeww$3%4(5)djjkkldss}")), 32))
        }

        function e(a, b) {
            for (var c = 1732584193, d = -271733879, e = -1732584194, f = 271733878, l = 0; l < a.length; l += 16) {
                var m = c
                    , n = d
                    , o = e
                    , p = f;
                c = g(c, d, e, f, a[l + 0], 7, -680876936),
                    f = g(f, c, d, e, a[l + 1], 12, -389564586),
                    e = g(e, f, c, d, a[l + 2], 17, 606105819),
                    d = g(d, e, f, c, a[l + 3], 22, -1044525330),
                    c = g(c, d, e, f, a[l + 4], 7, -176418897),
                    f = g(f, c, d, e, a[l + 5], 12, 1200080426),
                    e = g(e, f, c, d, a[l + 6], 17, -1473231341),
                    d = g(d, e, f, c, a[l + 7], 22, -45705983),
                    c = g(c, d, e, f, a[l + 8], 7, 1770035416),
                    f = g(f, c, d, e, a[l + 9], 12, -1958414417),
                    e = g(e, f, c, d, a[l + 10], 17, -42063),
                    d = g(d, e, f, c, a[l + 11], 22, -1990404162),
                    c = g(c, d, e, f, a[l + 12], 7, 1804603682),
                    f = g(f, c, d, e, a[l + 13], 12, -40341101),
                    e = g(e, f, c, d, a[l + 14], 17, -1502002290),
                    d = g(d, e, f, c, a[l + 15], 22, 1236535329),
                    c = h(c, d, e, f, a[l + 1], 5, -165796510),
                    f = h(f, c, d, e, a[l + 6], 9, -1069501632),
                    e = h(e, f, c, d, a[l + 11], 14, 643717713),
                    d = h(d, e, f, c, a[l + 0], 20, -373897302),
                    c = h(c, d, e, f, a[l + 5], 5, -701558691),
                    f = h(f, c, d, e, a[l + 10], 9, 38016083),
                    e = h(e, f, c, d, a[l + 15], 14, -660478335),
                    d = h(d, e, f, c, a[l + 4], 20, -405537848),
                    c = h(c, d, e, f, a[l + 9], 5, 568446438),
                    f = h(f, c, d, e, a[l + 14], 9, -1019803690),
                    e = h(e, f, c, d, a[l + 3], 14, -187363961),
                    d = h(d, e, f, c, a[l + 8], 20, 1163531501),
                    c = h(c, d, e, f, a[l + 13], 5, -1444681467),
                    f = h(f, c, d, e, a[l + 2], 9, -51403784),
                    e = h(e, f, c, d, a[l + 7], 14, 1735328473),
                    d = h(d, e, f, c, a[l + 12], 20, -1926607734),
                    c = i(c, d, e, f, a[l + 5], 4, -378558),
                    f = i(f, c, d, e, a[l + 8], 11, -2022574463),
                    e = i(e, f, c, d, a[l + 11], 16, 1839030562),
                    d = i(d, e, f, c, a[l + 14], 23, -35309556),
                    c = i(c, d, e, f, a[l + 1], 4, -1530992060),
                    f = i(f, c, d, e, a[l + 4], 11, 1272893353),
                    e = i(e, f, c, d, a[l + 7], 16, -155497632),
                    d = i(d, e, f, c, a[l + 10], 23, -1094730640),
                    c = i(c, d, e, f, a[l + 13], 4, 681279174),
                    f = i(f, c, d, e, a[l + 0], 11, -358537222),
                    e = i(e, f, c, d, a[l + 3], 16, -722521979),
                    d = i(d, e, f, c, a[l + 6], 23, 76029189),
                    c = i(c, d, e, f, a[l + 9], 4, -640364487),
                    f = i(f, c, d, e, a[l + 12], 11, -421815835),
                    e = i(e, f, c, d, a[l + 15], 16, 530742520),
                    d = i(d, e, f, c, a[l + 2], 23, -995338651),
                    c = j(c, d, e, f, a[l + 0], 6, -198630844),
                    f = j(f, c, d, e, a[l + 7], 10, 1126891415),
                    e = j(e, f, c, d, a[l + 14], 15, -1416354905),
                    d = j(d, e, f, c, a[l + 5], 21, -57434055),
                    c = j(c, d, e, f, a[l + 12], 6, 1700485571),
                    f = j(f, c, d, e, a[l + 3], 10, -1894986606),
                    e = j(e, f, c, d, a[l + 10], 15, -1051523),
                    d = j(d, e, f, c, a[l + 1], 21, -2054922799),
                    c = j(c, d, e, f, a[l + 8], 6, 1873313359),
                    f = j(f, c, d, e, a[l + 15], 10, -30611744),
                    e = j(e, f, c, d, a[l + 6], 15, -1560198380),
                    d = j(d, e, f, c, a[l + 13], 21, 1309151649),
                    c = j(c, d, e, f, a[l + 4], 6, -145523070),
                    f = j(f, c, d, e, a[l + 11], 10, -1120210379),
                    e = j(e, f, c, d, a[l + 2], 15, 718787259),
                    d = j(d, e, f, c, a[l + 9], 21, -343485551),
                    c = k(c, m),
                    d = k(d, n),
                    e = k(e, o),
                    f = k(f, p)
            }
            return new Array(c, d, e, f)
        }

        function f(a, b, c, d, e, f) {
            return k(l(k(k(b, a), k(d, f)), e), c)
        }

        function g(a, b, c, d, e, g, h) {
            return f(b & c | ~b & d, a, b, e, g, h)
        }

        function h(a, b, c, d, e, g, h) {
            return f(b & d | c & ~d, a, b, e, g, h)
        }

        function i(a, b, c, d, e, g, h) {
            return f(b ^ c ^ d, a, b, e, g, h)
        }

        function j(a, b, c, d, e, g, h) {
            return f(c ^ (b | ~d), a, b, e, g, h)
        }

        function k(a, b) {
            var c = (65535 & a) + (65535 & b);
            return (a >> 16) + (b >> 16) + (c >> 16) << 16 | 65535 & c
        }

        function l(a, b) {
            return a << b | a >>> 32 - b
        }

        function m(a) {
            for (var b = a.length, c = new Array(b), d = 0; d < b; d++) {
                var e = a.charCodeAt(d);
                c[d] = 255 & e
            }
            return c
        }

        function n(a) {
            for (var b = "0123456789abcdef", c = "", d = 0; d < 4 * a.length; d++)
                c += b.charAt(a[d >> 2] >> d % 4 * 8 + 4 & 15) + b.charAt(a[d >> 2] >> d % 4 * 8 & 15);
            return c
        }

        function o(a) {
            for (var b = 1 + (a.length + 8 >> 6), c = new Array(16 * b), d = 0; d < 16 * b; d++)
                c[d] = 0;
            for (var e = 0; e < a.length; e++)
                c[e >> 2] |= (255 & a[e]) << e % 4 * 8;
            return c[e >> 2] |= 128 << e % 4 * 8,
                c[16 * b - 2] = 8 * a.length,
                c
        }

        c.hex_md5 = d;
        window.d = d;
    }
        , {}],
    21: [function (a, b, c) {
        function d(a, b, c) {
            var d = h[a] || "";
            return c && "object" == typeof c ? d.replace("{message}", b).replace("{confirmBtnText}", c.confirmBtnText || "去修改密码").replace("{cancelBtnText}", c.cancelBtnText || "不，下次修改") : d.replace("{message}", b).replace("{confirmBtnText}", "去修改密码").replace("{cancelBtnText}", "不，下次修改")
        }

        function e(a, b, c, e) {
            return g.html(d(a, b, e)).show(),
            "prompt" != a && "qrPrompt" != a || g.one("go", c),
                g.one("close", c),
                {
                    done: function (b) {
                        return "prompt" != a && "qrPrompt" != a || g.one("go", b),
                            g.one("close", b),
                            this
                    }
                }
        }

        function f() {
            g.hide()
        }

        var g = $('<div class="xsm-ui"></div>').appendTo("body").hide();
        g.on("click", ".xsm-ui-btn-close", function () {
            g.hide().trigger("close")
        }),
            g.on("click", ".xsm-ui-btn-go", function () {
                g.hide().trigger("go")
            });
        var h = {
            cover: '<div class="xsm-ui-mask"></div>',
            notice: '<div class="xsm-ui-mask"></div><div class="xsm-ui-window xsm-ui-window-show"><div class="xsm-ui-message xsm-ui-notice">{message}</div><div class="xsm-ui-control"><a class="xsm-ui-btn-close">确定</a></div></div>',
            success: '<div class="xsm-ui-mask"></div><div class="xsm-ui-window"><div class="xsm-ui-message xsm-ui-success">{message}</div><div class="xsm-ui-control"><a class="xsm-ui-btn-close">确定</a></div></div>',
            error: '<div class="xsm-ui-mask"></div><div class="xsm-ui-window"><div class="xsm-ui-message xsm-ui-error">{message}</div><div class="xsm-ui-control"><a class="xsm-ui-btn-close">确定</a></div></div>',
            prompt: '<div class="xsm-ui-mask"></div><div class="xsm-ui-window-prompt xsm-ui-window-show"><div class="xsm-ui-message-prompt">{message}</div><div class="xsm-ui-control"><a id="modify" class="xsm-ui-btn-go">{confirmBtnText}</a><a id="nextModify" class="xsm-ui-btn-close">{cancelBtnText}</a></div></div>',
            qrPrompt: '<div class="xsm-ui-mask"></div><div class="xsm-ui-window-prompt xsm-ui-window-show"><div class="xsm-ui-message-prompt">{message}</div><div class="xsm-ui-control"><a id="nextModify" class="xsm-ui-btn-close">{cancelBtnText}</a></div></div>'
        };
        h.alert = h.notice;
        for (var i, j = {}, k = ["alert", "notice", "success", "error", "cover", "prompt", "qrPrompt"], l = 0; i = k[l++];)
            j[i] = function (a) {
                return function (b, c, d) {
                    return e(a, b, c, d)
                }
            }(i);
        j.close = j.removeCover = f,
            b.exports = j
    }
        , {}],
    22: [function (a, b, c) {
        function d(a) {
            var b = a.getAttribute("placeholder")
                , c = a[k];
            b && !c && (c = document.createElement("span"),
                c.innerHTML = b,
                c.className = j,
                c.onclick = function () {
                    try {
                        a.focus()
                    } catch (a) {
                    }
                }
                ,
                a.parentNode.insertBefore(c, a),
                a[k] = c,
            a.value && i(a))
        }

        function e(a) {
            var b = g(a);
            (b && "INPUT" === b.tagName || "TEXTAREA" === b.tagName) && (b.value ? i(b) : h(b))
        }

        function f(a) {
            var b = g(a);
            (b && "INPUT" === b.tagName || "TEXTAREA" === b.tagName) && i(b)
        }

        function g(a) {
            var a = a || window.event;
            return a.target || a.srcElement
        }

        function h(a) {
            a && a[k] && (a[k].style.display = "")
        }

        function i(a) {
            a && a[k] && (a[k].style.display = "none")
        }

        var j = "placeholder-hint"
            , k = "__hint__";
        c.init = function () {
            if (!("placeholder" in document.createElement("input"))) {
                document.addEventListener ? (document.addEventListener("focus", f, !0),
                    document.addEventListener("blur", e, !0)) : (document.attachEvent("onfocusin", f),
                    document.attachEvent("onfocusout", e));
                for (var a, b = document.getElementsByTagName("input"), c = 0; a = b[c++];)
                    d(a)
            }
        }
            ,
            c.showPlaceholder = h,
            c.hidePlaceholder = i
    }
        , {}],
    23: [function (a, b, c) {
        function d() {
            q || (m = $(p.mask).hide().appendTo("body"),
                n = $(p.dialog).hide().appendTo("body"),
                $(s).change(j),
                n.on("click", ".btn-close", f).on("click", ".btn-confirm", l),
                i().done(function (a) {
                    r = a,
                        $(s).html(g(r))
                }),
                q = !0)
        }

        function e() {
            m.show(),
                n.show()
        }

        function f() {
            m.hide(),
                n.hide()
        }

        function g(a) {
            for (var b, c = 0, d = [u]; b = a[c++];)
                d.push('<option value="' + b.id + '">' + b.name + "</option>");
            return d.join("")
        }

        function h(a) {
            for (var b, c = 0, d = [u]; b = a[c++];)
                d.push('<option value="' + b.page + '">' + b.name + "</option>");
            return d.join("")
        }

        function i() {
            return $.getJSON(v)
        }

        function j() {
            var a = $(s).val()
                , b = k(a);
            b ? $(t).html(h(b)) : $(t).html(u)
        }

        function k(a) {
            for (var b, c = 0; b = r[c++];)
                if (b.id === a)
                    return b.cities;
            return null
        }

        function l() {
            var a = $(t).val();
            a ? location.href = a : o.alert("您尚未选定所在地区，请先选择")
        }

        var m, n, o = a("msgbox"), p = a("./templates"), q = !1, r = null, s = "#J_register_com",
            t = "#J_register_city", u = '<option value="" selected>未选择</option>', v = "compress/redirectlogin.json";
        c.open = function () {
            d(),
                e()
        }
    }
        , {
            "./templates": 24,
            msgbox: 21
        }],
    24: [function (a, b, c) {
        c.mask = '<div class="user-register-dialog-mask"></div>',
            c.dialog = '<div class="user-register-dialog"><div class="head">新用户注册<a class="btn-close">×</a></div><div class="body">您的零售店所在的地区：<select id="J_register_com" placeholder="省公司"><option value="" selected>未选择</option></select>省<select id="J_register_city" placeholder="地市"><option value="" selected>未选择</option></select>市</div><div class="foot"><ul><li>仅新开通网上订货的零售户需要进行注册。</li><li>新商盟用户使用原有帐号密码登录，无需注册。</li><li>广州市零售户，已经使用网上订货系统的，直接使用原有帐号及密码登录即可；新使用网上订货系统的，请选择所在地区进行注册。</li></ul><div class="cmds"><button class="btn-confirm">注册</button></div></div></div>'
    }
        , {}],
    25: [function (a, b, c) {
        function d(a, b) {
            $.ajax({
                type: "GET",
                url: XSMConfig.login + "/cookieTool?method=setCookieAjax",
                dataType: "jsonp",
                data: {
                    cookieName: k.encrypt(a),
                    cookieValue: k.encrypt(b),
                    domain: k.encrypt(".xinshangmeng.com"),
                    maxAge: k.encrypt(2592e3)
                }
            })
        }

        function e(a) {
            $.ajax({
                type: "GET",
                url: XSMConfig.login + "/cookieTool?method=setCookieAjax",
                dataType: "jsonp",
                data: {
                    cookieName: k.encrypt(a),
                    cookieValue: k.encrypt(""),
                    domain: k.encrypt(".xinshangmeng.com"),
                    maxAge: k.encrypt(0)
                }
            })
        }

        function f(a, b) {
            $.ajax({
                type: "GET",
                url: XSMConfig.login + "/cookieTool?method=setCookieAjax",
                dataType: "jsonp",
                data: {
                    cookieName: k.encrypt(a),
                    cookieValue: k.encrypt(b),
                    path: k.encrypt("/"),
                    domain: k.encrypt(".xinshangmeng.com"),
                    maxAge: k.encrypt(2592e3)
                }
            })
        }

        function g(a) {
            var b = $.Deferred();
            return $.ajax({
                type: "GET",
                url: XSMConfig.login + "/cookieTool?method=getCookieAjax",
                dataType: "jsonp",
                timeout: 5e3,
                data: {
                    cookieName: k.encrypt(a)
                }
            }).done(function (a) {
                a && "000" === a.code ? b.resolve(k.decrypt(a.data)) : b.reject()
            }).always(function () {
                b.reject()
            }),
                b.promise()
        }

        function h(a) {
            $.ajax({
                type: "GET",
                url: XSMConfig.login + "/cookieTool?method=setCookieAjax",
                dataType: "jsonp",
                data: {
                    cookieName: k.encrypt(a),
                    cookieValue: k.encrypt(value),
                    path: k.encrypt("/"),
                    domain: k.encrypt(".xinshangmeng.com"),
                    maxAge: k.encrypt(0)
                }
            })
        }

        function i(a) {
            $.ajax({
                type: "GET",
                url: XSMConfig.login + "/cookieTool?method=setCookieAjax",
                dataType: "jsonp",
                data: {
                    cookieName: k.encrypt("myguid1234567890"),
                    cookieValue: k.encrypt(a),
                    path: k.encrypt("/"),
                    domain: k.encrypt(".xinshangmeng.com"),
                    maxAge: k.encrypt(31536e4)
                }
            })
        }

        function j(a, b) {
            $.ajax({
                type: "GET",
                url: XSMConfig.login + "/cookieTool?method=clearCookieAjax",
                dataType: "jsonp",
                exceptName: "myguid1234567890",
                data: {
                    domain: k.encrypt(b || document.domain),
                    path: k.encrypt(a)
                }
            })
        }

        var k = a("./xsm-aes");
        c.setCookiefroUn = d,
            c.setMyguidCookie = i,
            c.delCookiefroUn = e,
            c.setCookie = f,
            c.getCookie = g,
            c.delCookie = h,
            c.clearCookie = j
    }
        , {
            "./xsm-aes": 27
        }],
    26: [function (a, b, c) {
        var d = a("./cookie");
        c.getGUID = function () {
            for (var a = "", b = 32; b--;)
                a += Math.floor(16 * Math.random()).toString(16);
            return a
        }
            ,
            c.Cookie = d
    }
        , {
            "./cookie": 25
        }],
    27: [function (a, b, c) {
        arguments[4][19][0].apply(c, arguments)
    }
        , {
            "crypto-js/aes": 1,
            "crypto-js/enc-base64": 4,
            "crypto-js/enc-utf8": 5,
            "crypto-js/mode-ecb": 9,
            dup: 19
        }]
}, {}, [20]);

// d 为标准md5
console.log(d(d(123456)+''));
