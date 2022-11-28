

function f(e, t) {
    e = [e[0] >>> 16, 65535 & e[0], e[1] >>> 16, 65535 & e[1]],
        t = [t[0] >>> 16, 65535 & t[0], t[1] >>> 16, 65535 & t[1]];
    var n = [0, 0, 0, 0];
    return n[3] += e[3] + t[3],
        n[2] += n[3] >>> 16,
        n[3] &= 65535,
        n[2] += e[2] + t[2],
        n[1] += n[2] >>> 16,
        n[2] &= 65535,
        n[1] += e[1] + t[1],
        n[0] += n[1] >>> 16,
        n[1] &= 65535,
        n[0] += e[0] + t[0],
        n[0] &= 65535,
        [n[0] << 16 | n[1], n[2] << 16 | n[3]]
}

function d(e, t) {
    e = [e[0] >>> 16, 65535 & e[0], e[1] >>> 16, 65535 & e[1]],
        t = [t[0] >>> 16, 65535 & t[0], t[1] >>> 16, 65535 & t[1]];
    var n = [0, 0, 0, 0];
    return n[3] += e[3] * t[3],
        n[2] += n[3] >>> 16,
        n[3] &= 65535,
        n[2] += e[2] * t[3],
        n[1] += n[2] >>> 16,
        n[2] &= 65535,
        n[2] += e[3] * t[2],
        n[1] += n[2] >>> 16,
        n[2] &= 65535,
        n[1] += e[1] * t[3],
        n[0] += n[1] >>> 16,
        n[1] &= 65535,
        n[1] += e[2] * t[2],
        n[0] += n[1] >>> 16,
        n[1] &= 65535,
        n[1] += e[3] * t[1],
        n[0] += n[1] >>> 16,
        n[1] &= 65535,
        n[0] += e[0] * t[3] + e[1] * t[2] + e[2] * t[1] + e[3] * t[0],
        n[0] &= 65535,
        [n[0] << 16 | n[1], n[2] << 16 | n[3]]
}

function h(e, t) {
    return 32 === (t %= 64) ? [e[1], e[0]] : t < 32 ? [e[0] << t | e[1] >>> 32 - t, e[1] << t | e[0] >>> 32 - t] : (t -= 32,
        [e[1] << t | e[0] >>> 32 - t, e[0] << t | e[1] >>> 32 - t])
}

function p(e, t) {
    return 0 === (t %= 64) ? e : t < 32 ? [e[0] << t | e[1] >>> 32 - t, e[1] << t] : [e[1] << t - 32, 0]
}

function g(e, t) {
    return [e[0] ^ t[0], e[1] ^ t[1]]
}

function m(e) {
    return e = g(e, [0, e[0] >>> 1]),
        e = d(e, [4283543511, 3981806797]),
        e = g(e, [0, e[0] >>> 1]),
        e = d(e, [3301882366, 444984403]),
        e = g(e, [0, e[0] >>> 1])
}

function s(e, t) {
    t = t || 0;
    for (var n = (e = e || "").length % 16, r = e.length - n, o = [0, t], i = [0, t], a = [0, 0], s = [0, 0], c = [2277735313, 289559509], u = [1291169091, 658871167], l = 0; l < r; l += 16)
        a = [255 & e.charCodeAt(l + 4) | (255 & e.charCodeAt(l + 5)) << 8 | (255 & e.charCodeAt(l + 6)) << 16 | (255 & e.charCodeAt(l + 7)) << 24, 255 & e.charCodeAt(l) | (255 & e.charCodeAt(l + 1)) << 8 | (255 & e.charCodeAt(l + 2)) << 16 | (255 & e.charCodeAt(l + 3)) << 24],
            s = [255 & e.charCodeAt(l + 12) | (255 & e.charCodeAt(l + 13)) << 8 | (255 & e.charCodeAt(l + 14)) << 16 | (255 & e.charCodeAt(l + 15)) << 24, 255 & e.charCodeAt(l + 8) | (255 & e.charCodeAt(l + 9)) << 8 | (255 & e.charCodeAt(l + 10)) << 16 | (255 & e.charCodeAt(l + 11)) << 24],
            a = d(a, c),
            a = h(a, 31),
            a = d(a, u),
            o = g(o, a),
            o = h(o, 27),
            o = f(o, i),
            o = f(d(o, [0, 5]), [0, 1390208809]),
            s = d(s, u),
            s = h(s, 33),
            s = d(s, c),
            i = g(i, s),
            i = h(i, 31),
            i = f(i, o),
            i = f(d(i, [0, 5]), [0, 944331445]);
    switch (a = [0, 0],
        s = [0, 0],
        n) {
        case 15:
            s = g(s, p([0, e.charCodeAt(l + 14)], 48));
        case 14:
            s = g(s, p([0, e.charCodeAt(l + 13)], 40));
        case 13:
            s = g(s, p([0, e.charCodeAt(l + 12)], 32));
        case 12:
            s = g(s, p([0, e.charCodeAt(l + 11)], 24));
        case 11:
            s = g(s, p([0, e.charCodeAt(l + 10)], 16));
        case 10:
            s = g(s, p([0, e.charCodeAt(l + 9)], 8));
        case 9:
            s = g(s, [0, e.charCodeAt(l + 8)]),
                s = d(s, u),
                s = h(s, 33),
                s = d(s, c),
                i = g(i, s);
        case 8:
            a = g(a, p([0, e.charCodeAt(l + 7)], 56));
        case 7:
            a = g(a, p([0, e.charCodeAt(l + 6)], 48));
        case 6:
            a = g(a, p([0, e.charCodeAt(l + 5)], 40));
        case 5:
            a = g(a, p([0, e.charCodeAt(l + 4)], 32));
        case 4:
            a = g(a, p([0, e.charCodeAt(l + 3)], 24));
        case 3:
            a = g(a, p([0, e.charCodeAt(l + 2)], 16));
        case 2:
            a = g(a, p([0, e.charCodeAt(l + 1)], 8));
        case 1:
            a = g(a, [0, e.charCodeAt(l)]),
                a = d(a, c),
                a = h(a, 31),
                a = d(a, u),
                o = g(o, a)
    }
    return o = g(o, [0, e.length]),
        i = g(i, [0, e.length]),
        o = f(o, i),
        i = f(i, o),
        o = m(o),
        i = m(i),
        o = f(o, i),
        i = f(i, o),
    ("00000000" + (o[0] >>> 0).toString(16)).slice(-8) + ("00000000" + (o[1] >>> 0).toString(16)).slice(-8) + ("00000000" + (i[0] >>> 0).toString(16)).slice(-8) + ("00000000" + (i[1] >>> 0).toString(16)).slice(-8)
}

