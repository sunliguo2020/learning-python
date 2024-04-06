const jsdom = require("jsdom");
const {JSDOM} = jsdom;
const $ = require("jquery")(new JSDOM(`<!DOCTYPE html><p>Hello world</p>`).window);
window = global;


!function(e) {
    function f(data) {
        for (var f, d, n = data[0], o = data[1], l = data[2], i = 0, h = []; i < n.length; i++)
            d = n[i],
            Object.prototype.hasOwnProperty.call(r, d) && r[d] && h.push(r[d][0]),
            r[d] = 0;
        for (f in o)
            Object.prototype.hasOwnProperty.call(o, f) && (e[f] = o[f]);
        for (v && v(data); h.length; )
            h.shift()();
        return t.push.apply(t, l || []),
        c()
    }
    function c() {
        for (var e, i = 0; i < t.length; i++) {
            for (var f = t[i], c = !0, d = 1; d < f.length; d++) {
                var o = f[d];
                0 !== r[o] && (c = !1)
            }
            c && (t.splice(i--, 1),
            e = n(n.s = f[0]))
        }
        return e
    }
    var d = {}
      , r = {
        495: 0
    }
      , t = [];
    function n(f) {
        if (d[f])
            return d[f].exports;
        var c = d[f] = {
            i: f,
            l: !1,
            exports: {}
        };
        console.log('f：',f)
        return e[f].call(c.exports, c, c.exports, n),
        c.l = !0,
        c.exports
    }
    n.e = function(e) {
        var f = []
          , c = r[e];
        if (0 !== c)
            if (c)
                f.push(c[2]);
            else {
                var d = new Promise((function(f, d) {
                    c = r[e] = [f, d]
                }
                ));
                f.push(c[2] = d);
                var t, script = document.createElement("script");
                script.charset = "utf-8",
                script.timeout = 120,
                n.nc && script.setAttribute("nonce", n.nc),
                script.src = function(e) {
                    return n.p + "" + {
                        0: "8980b15",
                        1: "d2b27a7",
                        2: "f5186d9",
                        3: "6ec21e8",
                        4: "037910c",
                        5: "949f52f",
                        6: "5ae912e",
                        7: "9aea062",
                        8: "0b65e47",
                        9: "5e17197",
                        10: "8a7e86f",
                        11: "9eca5c5",
                        12: "996a766",
                        13: "56ac230",
                        14: "731a1b2",
                        15: "d3cad36",
                        16: "7f5f1b4",
                        17: "7456a0f",
                        18: "a54607e",
                        19: "b282bf7",
                        20: "8d80284",
                        21: "af4e0df",
                        22: "8bdc2b3",
                        23: "24187f3",
                        24: "b1c01e1",
                        25: "15cef3e",
                        26: "16b460e",
                        27: "e3b05a3",
                        28: "602a9ec",
                        29: "f1bb8bb",
                        30: "f024521",
                        31: "3858745",
                        32: "0d850f9",
                        33: "62a4cc5",
                        34: "b09f0a3",
                        35: "4155f1f",
                        36: "53891c1",
                        37: "bb19ee3",
                        38: "327deff",
                        39: "7c9f600",
                        40: "6d96302",
                        41: "e70a27a",
                        42: "112ac57",
                        43: "2256a91",
                        44: "8448072",
                        45: "f1fe70a",
                        46: "af80b87",
                        47: "c6b082f",
                        48: "c055255",
                        49: "e95b8d1",
                        50: "070b60c",
                        51: "609f968",
                        52: "e35c3b6",
                        53: "6a17862",
                        54: "47368f5",
                        55: "c6da98b",
                        56: "78fd41b",
                        57: "4861f0e",
                        58: "6139b54",
                        59: "7e15ef9",
                        60: "4711a89",
                        61: "7a017ef",
                        62: "4fa1d67",
                        63: "7f1b3da",
                        64: "94810ff",
                        65: "9fd8f0a",
                        66: "93aae4c",
                        69: "09ece26",
                        70: "145dc57",
                        71: "ca145c4",
                        72: "4bd99fe",
                        73: "add1411",
                        74: "03ab610",
                        75: "7bc8bb1",
                        76: "cfba228",
                        77: "f8c7e40",
                        78: "bc92aad",
                        79: "c7ad040",
                        80: "a0c4e5b",
                        81: "74dde45",
                        82: "c80f182",
                        83: "963889c",
                        84: "c8c54f8",
                        85: "16b5e2d",
                        86: "2a6c089",
                        87: "751fe9d",
                        88: "ff19242",
                        89: "6141d3e",
                        90: "a839e68",
                        91: "2e37ccd",
                        92: "fa13038",
                        93: "1726763",
                        94: "1d5f31a",
                        95: "dda4789",
                        96: "d5a1f43",
                        97: "de03200",
                        98: "22bec5c",
                        99: "ee6a184",
                        100: "38e21af",
                        101: "c744c94",
                        102: "023991a",
                        103: "245bcc2",
                        104: "f5b89a1",
                        105: "463dc37",
                        106: "02d1356",
                        107: "265343c",
                        108: "12a907c",
                        109: "20ee439",
                        110: "6c7de69",
                        111: "89d4bd9",
                        112: "55f8b0d",
                        113: "7185642",
                        114: "b0ff865",
                        115: "24ea2bd",
                        116: "1a6d16b",
                        117: "25dcbb1",
                        118: "05178e0",
                        119: "de28286",
                        120: "cd09723",
                        121: "19ae3bf",
                        122: "5da2121",
                        123: "b94d734",
                        124: "82aec52",
                        125: "22d6fd8",
                        126: "ef33b05",
                        127: "75c2c07",
                        128: "a7fe5d0",
                        129: "9fa0feb",
                        130: "c91362e",
                        131: "22609f1",
                        132: "fb690ce",
                        133: "07d214e",
                        134: "58bd457",
                        135: "8aabbe3",
                        136: "26ced29",
                        137: "46ff2c1",
                        138: "0f2e3b1",
                        139: "01927ff",
                        140: "3976906",
                        141: "2f68768",
                        142: "53e932d",
                        143: "5406679",
                        144: "66886e6",
                        145: "36aa23f",
                        146: "2261409",
                        147: "b86e4ab",
                        148: "9ab705a",
                        149: "2df8477",
                        150: "15cb09b",
                        151: "f38702c",
                        152: "e3d3149",
                        153: "896ac1f",
                        154: "52ddae5",
                        155: "2d463c2",
                        156: "0a08029",
                        157: "a632fb3",
                        158: "64f4eea",
                        159: "02e6166",
                        160: "059012d",
                        161: "73cd3ce",
                        162: "bc30332",
                        163: "756ee74",
                        164: "73db5c1",
                        165: "9f2cdd7",
                        166: "95bb540",
                        167: "cbbbecd",
                        168: "1746d69",
                        169: "84406af",
                        170: "1ca481e",
                        171: "83f1c7c",
                        172: "deb5587",
                        173: "015b864",
                        174: "2583c90",
                        175: "9ada1bc",
                        176: "7ee2ebe",
                        177: "3d545f1",
                        178: "cfb10f1",
                        179: "8d486f4",
                        180: "8a5151a",
                        181: "0d5eaf2",
                        182: "db96209",
                        183: "c4c4ddf",
                        184: "11b87ad",
                        185: "563927d",
                        186: "7127aad",
                        187: "999dbb9",
                        188: "8670352",
                        189: "d495fa1",
                        190: "bb6b6ee",
                        191: "867047f",
                        192: "1b24883",
                        193: "9c82762",
                        194: "696c752",
                        195: "8b8ffc2",
                        196: "803583e",
                        197: "352c4dc",
                        198: "909866a",
                        199: "cf38060",
                        200: "2479af6",
                        201: "7385f33",
                        202: "a30b356",
                        203: "df1fafb",
                        204: "3ba1c3a",
                        205: "1c8f0cb",
                        206: "353a384",
                        207: "405a063",
                        208: "a418fc2",
                        209: "6f6994b",
                        210: "576792d",
                        211: "865dcae",
                        212: "8cbe3a9",
                        213: "50588fd",
                        214: "33792cd",
                        215: "ed365f9",
                        216: "5b0c66f",
                        217: "29873e1",
                        218: "5a0438e",
                        219: "8370044",
                        220: "136db7e",
                        221: "e6254f2",
                        222: "a8caed1",
                        223: "cbae7cd",
                        224: "772a167",
                        225: "50254fc",
                        226: "c1b8a1d",
                        227: "d02edc8",
                        228: "f01d6e5",
                        229: "1b95a7d",
                        230: "df2dba9",
                        231: "50209cd",
                        232: "4788311",
                        233: "881b756",
                        234: "483425b",
                        235: "fe50a37",
                        236: "439653c",
                        237: "e33c680",
                        238: "c500d8b",
                        239: "b437ffb",
                        240: "db0b764",
                        241: "11c104a",
                        242: "8846ba6",
                        243: "0fb4d58",
                        244: "313284c",
                        245: "8141e19",
                        246: "1c2e727",
                        247: "9de77ad",
                        248: "71762e5",
                        249: "df6ae9c",
                        250: "47fce2f",
                        251: "e74b756",
                        252: "2dd5ffd",
                        253: "bffbcb6",
                        254: "7903c4a",
                        255: "00fffd1",
                        256: "113178a",
                        257: "6223f02",
                        258: "50a53c8",
                        259: "bca3ee2",
                        260: "f0b1455",
                        261: "e40052f",
                        262: "3088c53",
                        263: "86eefc6",
                        264: "b7ee19c",
                        265: "0033ef1",
                        266: "0321da4",
                        267: "30021b4",
                        268: "8a33bfa",
                        269: "77c445c",
                        270: "c3beac6",
                        271: "dba732c",
                        272: "f62f1ce",
                        273: "7708860",
                        274: "2bb53b7",
                        275: "6541a6f",
                        276: "bbb2687",
                        277: "27393d7",
                        278: "cb4f16d",
                        279: "8c2b836",
                        280: "7f7335d",
                        281: "5e5bce6",
                        282: "c64c6ee",
                        283: "2d3d0bf",
                        284: "9673a8a",
                        285: "f857f66",
                        286: "56d9223",
                        287: "8d7d40f",
                        288: "802d14c",
                        289: "2d6a5dc",
                        290: "5fcb29b",
                        291: "d519d54",
                        292: "5dca774",
                        293: "c17c2c6",
                        294: "bc50751",
                        295: "833c92e",
                        296: "789a403",
                        297: "982878a",
                        298: "2a786f5",
                        299: "6d0e79d",
                        300: "dd6d374",
                        301: "319e1f8",
                        302: "9f36952",
                        303: "113114f",
                        304: "dddd10a",
                        305: "4b20e09",
                        306: "2bbfa15",
                        307: "bb957ab",
                        308: "12a9bc8",
                        309: "dda4676",
                        310: "e1a31a7",
                        311: "2b352d0",
                        312: "879c3f1",
                        313: "5fb1b30",
                        314: "9f46981",
                        315: "08e5d21",
                        316: "6cd15f0",
                        317: "e91479c",
                        318: "552a356",
                        319: "b49f706",
                        320: "f579dc4",
                        321: "4bebae7",
                        322: "642811b",
                        323: "b8713a5",
                        324: "a02baee",
                        325: "0ef8ef3",
                        326: "c3879b0",
                        327: "a49c876",
                        328: "b2a7ef2",
                        329: "20ac95d",
                        330: "d59233d",
                        331: "7bf5f09",
                        332: "ccd2212",
                        333: "d844706",
                        334: "fddc20a",
                        335: "93e4f99",
                        336: "ae5e982",
                        337: "37ce298",
                        338: "2f6295d",
                        339: "7187f7a",
                        340: "c45993c",
                        341: "604260f",
                        342: "42ae9ae",
                        343: "f53d182",
                        344: "6bde5f2",
                        345: "4bd8611",
                        346: "69d5c64",
                        347: "008f697",
                        348: "1139a03",
                        349: "88a2508",
                        350: "7c7bd30",
                        351: "e886720",
                        352: "fad7f7b",
                        353: "2502f94",
                        354: "1b7dfbd",
                        355: "e14f6ef",
                        356: "24cd19b",
                        357: "ffd18df",
                        358: "f7a3477",
                        359: "4e856b4",
                        360: "c453609",
                        361: "8dc8252",
                        362: "634bdcd",
                        363: "0d23e53",
                        364: "98faf37",
                        365: "a1c6ddf",
                        366: "a36c60b",
                        367: "d3b7dba",
                        368: "dc582c8",
                        369: "6ea0513",
                        370: "772c711",
                        371: "daa3e80",
                        372: "16c3b17",
                        373: "abe248c",
                        374: "49f17a4",
                        375: "5898214",
                        376: "8739a11",
                        377: "3d06d3e",
                        378: "bff90e2",
                        379: "924eeaa",
                        380: "75aaddf",
                        381: "9ea85b7",
                        382: "c3ad459",
                        383: "08682d6",
                        384: "c8fcb8c",
                        385: "7d8188f",
                        386: "384cd82",
                        387: "ad74975",
                        388: "898212c",
                        389: "694e0e1",
                        390: "a10042a",
                        391: "95696fb",
                        392: "5993e0b",
                        393: "5d993be",
                        394: "d12878f",
                        395: "af2a144",
                        396: "b93d849",
                        397: "b1bcfcb",
                        398: "215b588",
                        399: "09cfc62",
                        400: "9716b16",
                        401: "e22b579",
                        402: "c63b136",
                        403: "1aa313d",
                        404: "5967e8e",
                        405: "45cb621",
                        406: "8562dd0",
                        407: "d5b8465",
                        408: "e095e1f",
                        409: "68bc464",
                        410: "8ce3bd8",
                        411: "3dbe8ce",
                        412: "b129f01",
                        413: "4c26f67",
                        414: "b16f507",
                        415: "16770fe",
                        416: "c0d1bc5",
                        417: "73d115b",
                        418: "772d14d",
                        419: "767d06e",
                        420: "e95f614",
                        421: "727d57a",
                        422: "c6d7831",
                        423: "91daca3",
                        424: "18169c3",
                        425: "a08fef5",
                        426: "9b7b5a9",
                        427: "e4a47aa",
                        428: "b77018b",
                        429: "19d9113",
                        430: "90c188f",
                        431: "8d5168f",
                        432: "5a2dc38",
                        433: "717a6d7",
                        434: "b5687b2",
                        435: "52a9ba8",
                        436: "e153902",
                        437: "525cff5",
                        438: "a8ae563",
                        439: "5e61bad",
                        440: "ec976f6",
                        441: "c774bf6",
                        442: "4c6eea9",
                        443: "97b6183",
                        444: "b25d094",
                        445: "3d40f73",
                        446: "e768023",
                        447: "ae0fe60",
                        448: "fcc5715",
                        449: "4581649",
                        450: "58b1b34",
                        451: "8b6fd75",
                        452: "950a81c",
                        453: "c33fc98",
                        454: "e4c9c77",
                        455: "b3fd51b",
                        456: "868a330",
                        457: "d12e368",
                        458: "918a7ba",
                        459: "1ad4654",
                        460: "cbc0f03",
                        461: "d5fc0c9",
                        462: "f0e351e",
                        463: "28dec4e",
                        464: "9c4b6e3",
                        465: "c1ef4bd",
                        466: "f7d1446",
                        467: "857f16f",
                        468: "c892a44",
                        469: "9fe4967",
                        470: "f7f6899",
                        471: "f2be9cb",
                        472: "702145b",
                        473: "cff24b0",
                        474: "bf6caa1",
                        475: "456b81d",
                        476: "e93c932",
                        477: "7a61ef5",
                        478: "d0c74d2",
                        479: "b431bc6",
                        480: "8133cdb",
                        481: "7cb64e0",
                        482: "2ab058a",
                        483: "3e94589",
                        484: "700f0d3",
                        485: "e34fdd4",
                        486: "303e0d2",
                        487: "e4a9473",
                        488: "1122af1",
                        489: "23f68d2",
                        490: "4315d30",
                        491: "24857c3",
                        492: "f35237e",
                        493: "e461504",
                        494: "ae91353",
                        497: "5d539bb",
                        498: "12cd05d",
                        499: "9c6876a",
                        500: "d970040",
                        501: "dc77fd2",
                        502: "3a923f8",
                        503: "f41aea5",
                        504: "98c629e",
                        505: "4aaab87",
                        506: "60d2fad",
                        507: "f659b0a",
                        508: "4b1bc17",
                        509: "06e09ce",
                        510: "a135c44"
                    }[e] + ".js"
                }(e);
                var o = new Error;
                t = function(f) {
                    script.onerror = script.onload = null,
                    clearTimeout(l);
                    var c = r[e];
                    if (0 !== c) {
                        if (c) {
                            var d = f && ("load" === f.type ? "missing" : f.type)
                              , t = f && f.target && f.target.src;
                            o.message = "Loading chunk " + e + " failed.\n(" + d + ": " + t + ")",
                            o.name = "ChunkLoadError",
                            o.type = d,
                            o.request = t,
                            c[1](o)
                        }
                        r[e] = void 0
                    }
                }
                ;
                var l = setTimeout((function() {
                    t({
                        type: "timeout",
                        target: script
                    })
                }
                ), 12e4);
                script.onerror = script.onload = t,
                document.head.appendChild(script)
            }
        return Promise.all(f)
    }
    ,
    n.m = e,
    n.c = d,
    n.d = function(e, f, c) {
        n.o(e, f) || Object.defineProperty(e, f, {
            enumerable: !0,
            get: c
        })
    }
    ,
    n.r = function(e) {
        "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
            value: "Module"
        }),
        Object.defineProperty(e, "__esModule", {
            value: !0
        })
    }
    ,
    n.t = function(e, f) {
        if (1 & f && (e = n(e)),
        8 & f)
            return e;
        if (4 & f && "object" == typeof e && e && e.__esModule)
            return e;
        var c = Object.create(null);
        if (n.r(c),
        Object.defineProperty(c, "default", {
            enumerable: !0,
            value: e
        }),
        2 & f && "string" != typeof e)
            for (var d in e)
                n.d(c, d, function(f) {
                    return e[f]
                }
                .bind(null, d));
        return c
    }
    ,
    n.n = function(e) {
        var f = e && e.__esModule ? function() {
            return e.default
        }
        : function() {
            return e
        }
        ;
        return n.d(f, "a", f),
        f
    }
    ,
    n.o = function(object, e) {
        return Object.prototype.hasOwnProperty.call(object, e)
    }
    ,
    n.p = "/_nuxt/",
    n.oe = function(e) {
        throw console.error(e),
        e
    }
    ;
    var o = window.webpackJsonp = window.webpackJsonp || []
      , l = o.push.bind(o);
    o.push = f,
    o = o.slice();
    for (var i = 0; i < o.length; i++)
        f(o[i]);
    var v = l;
    c();
    window.n = n;
}({
    141: function(e, t, n) {
        "use strict";
        n.d(t, "a", (function() {
            return o
        }
        ));
        // n(97),
        // n(52);
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
});

window.n('141')
// console.log(window.n('141'))
console.log(window.randomStr(12))