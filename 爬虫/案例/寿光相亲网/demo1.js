function l(t) {
    var n;
    var e;
    var r = "";
    for (n = 0; n + 3 <= t.length; n += 3) {
        e = parseInt(t.substring(n, n + 3), 16);
        r += a.charAt(e >> 6) + a.charAt(e & 63)
    }
    if (n + 1 == t.length) {
        e = parseInt(t.substring(n, n + 1), 16);
        r += a.charAt(e << 2)
    } else if (n + 2 == t.length) {
        e = parseInt(t.substring(n, n + 2), 16);
        r += a.charAt(e >> 2) + a.charAt((e & 3) << 4)
    }
    while ((r.length & 3) > 0)
        r += s;
    return r
}

function ct(t, n) {
    if (n < t.length + 11) {
        console.error("Message too long for RSA");
        return null
    }
    var e = [];
    var r = t.length - 1;
    while (r >= 0 && n > 0) {
        var i = t.charCodeAt(r--);
        if (i < 128)
            e[--n] = i;
        else if (i > 127 && i < 2048) {
            e[--n] = i & 63 | 128;
            e[--n] = i >> 6 | 192
        } else {
            e[--n] = i & 63 | 128;
            e[--n] = i >> 6 & 63 | 128;
            e[--n] = i >> 12 | 224
        }
    }
    e[--n] = 0;
    var o = new ut;
    var u = [];
    while (n > 2) {
        u[0] = 0;
        while (u[0] == 0)
            o.nextBytes(u);
        e[--n] = u[0]
    }
    e[--n] = 2;
    e[--n] = 0;
    return new P(e)
}

function encrypt(t) {
    var n = ct(t, this.n.bitLength() + 7 >> 3);
    if (n == null)
        return null;
    var e = this.doPublic(n);
    if (e == null)
        return null;
    var r = e.toString(16);
    if ((r.length & 1) == 0)
        return r;
    else
        return "0" + r
}

t = {}
t.encrypt = function (t) {

    return l(encrypt(t))

}

console.log(t.encrypt())
var hashtoken = t.encrypt((new Date).getTime().toString());


console.log(hashtoken)