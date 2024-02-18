var p = function (t, n) {
    p = Object.setPrototypeOf || {
            __proto__: []
        } instanceof Array && function (t, n) {
            t.__proto__ = n
        }
        || function (t, n) {
            for (var e in n)
                if (n.hasOwnProperty(e))
                    t[e] = n[e]
        };
    return p(t, n)
}

function d(t, n) {
    p(t, n);

    function e() {
        this.constructor = t
    }

    t.prototype = n === null ? Object.create(n) : (e.prototype = n.prototype,
        new e)
}

var gt = function (e) {
    d(r, e);

    function r(t) {
        var n = e.call(this) || this;
        if (t)
            if (typeof t === "string")
                n.parseKey(t);
            else if (r.hasPrivateKeyProperty(t) || r.hasPublicKeyProperty(t))
                n.parsePropertiesFrom(t);
        return n
    }

    r.prototype.parseKey = function (t) {
        try {
            var n = 0;
            var e = 0;
            var r = /^\s*(?:[0-9A-Fa-f][0-9A-Fa-f]\s*)+$/;
            var i = r.test(t) ? g.decode(t) : b.unarmor(t);
            var o = O.decode(i);
            if (o.sub.length === 3)
                o = o.sub[2].sub[0];
            if (o.sub.length === 9) {
                n = o.sub[1].getHexStringValue();
                this.n = V(n, 16);
                e = o.sub[2].getHexStringValue();
                this.e = parseInt(e, 16);
                var u = o.sub[3].getHexStringValue();
                this.d = V(u, 16);
                var a = o.sub[4].getHexStringValue();
                this.p = V(a, 16);
                var c = o.sub[5].getHexStringValue();
                this.q = V(c, 16);
                var f = o.sub[6].getHexStringValue();
                this.dmp1 = V(f, 16);
                var s = o.sub[7].getHexStringValue();
                this.dmq1 = V(s, 16);
                var l = o.sub[8].getHexStringValue();
                this.coeff = V(l, 16)
            } else if (o.sub.length === 2) {
                var h = o.sub[1];
                var p = h.sub[0];
                n = p.sub[0].getHexStringValue();
                this.n = V(n, 16);
                e = p.sub[1].getHexStringValue();
                this.e = parseInt(e, 16)
            } else
                return false;
            return true
        } catch (t) {
            return false
        }
    }
    ;
    r.prototype.getPrivateBaseKey = function () {
        var t = {
            array: [new dt.asn1.DERInteger({
                int: 0
            }), new dt.asn1.DERInteger({
                bigint: this.n
            }), new dt.asn1.DERInteger({
                int: this.e
            }), new dt.asn1.DERInteger({
                bigint: this.d
            }), new dt.asn1.DERInteger({
                bigint: this.p
            }), new dt.asn1.DERInteger({
                bigint: this.q
            }), new dt.asn1.DERInteger({
                bigint: this.dmp1
            }), new dt.asn1.DERInteger({
                bigint: this.dmq1
            }), new dt.asn1.DERInteger({
                bigint: this.coeff
            })]
        };
        var n = new dt.asn1.DERSequence(t);
        return n.getEncodedHex()
    }
    ;
    r.prototype.getPrivateBaseKeyB64 = function () {
        return l(this.getPrivateBaseKey())
    }
    ;
    r.prototype.getPublicBaseKey = function () {
        var t = new dt.asn1.DERSequence({
            array: [new dt.asn1.DERObjectIdentifier({
                oid: "1.2.840.113549.1.1.1"
            }), new dt.asn1.DERNull]
        });
        var n = new dt.asn1.DERSequence({
            array: [new dt.asn1.DERInteger({
                bigint: this.n
            }), new dt.asn1.DERInteger({
                int: this.e
            })]
        });
        var e = new dt.asn1.DERBitString({
            hex: "00" + n.getEncodedHex()
        });
        var r = new dt.asn1.DERSequence({
            array: [t, e]
        });
        return r.getEncodedHex()
    }
    ;
    r.prototype.getPublicBaseKeyB64 = function () {
        return l(this.getPublicBaseKey())
    }
    ;
    r.wordwrap = function (t, n) {
        n = n || 64;
        if (!t)
            return t;
        var e = "(.{1," + n + "})( +|$\n?)|(.{1," + n + "})";
        return t.match(RegExp(e, "g")).join("\n")
    }
    ;
    r.prototype.getPrivateKey = function () {
        var t = "-----BEGIN RSA PRIVATE KEY-----\n";
        t += r.wordwrap(this.getPrivateBaseKeyB64()) + "\n";
        t += "-----END RSA PRIVATE KEY-----";
        return t
    }
    ;
    r.prototype.getPublicKey = function () {
        var t = "-----BEGIN PUBLIC KEY-----\n";
        t += r.wordwrap(this.getPublicBaseKeyB64()) + "\n";
        t += "-----END PUBLIC KEY-----";
        return t
    }
    ;
    r.hasPublicKeyProperty = function (t) {
        t = t || {};
        return t.hasOwnProperty("n") && t.hasOwnProperty("e")
    }
    ;
    r.hasPrivateKeyProperty = function (t) {
        t = t || {};
        return t.hasOwnProperty("n") && t.hasOwnProperty("e") && t.hasOwnProperty("d") && t.hasOwnProperty("p") && t.hasOwnProperty("q") && t.hasOwnProperty("dmp1") && t.hasOwnProperty("dmq1") && t.hasOwnProperty("coeff")
    }
    ;
    r.prototype.parsePropertiesFrom = function (t) {
        this.n = t.n;
        this.e = t.e;
        if (t.hasOwnProperty("d")) {
            this.d = t.d;
            this.p = t.p;
            this.q = t.q;
            this.dmp1 = t.dmp1;
            this.dmq1 = t.dmq1;
            this.coeff = t.coeff
        }
    }
    ;
    return r
}
// var t = new a.a.prototype.$jsEncrypt;
var t = function t(t) {
    t = t || {};
    this.default_key_size = parseInt(t.default_key_size, 10) || 1024;
    this.default_public_exponent = t.default_public_exponent || "010001";
    this.log = t.log || false;
    this.key = null
};
var PublicKey = `-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDlXTJX5BgW2/oJRf3kTo7XZ3q7
aOnqN832+hkKe/xjKLKHnMTv+td/0Zsw1VkczWvodtLKsjJnrjiIx+dRIjLz2qYC
WagGNroXGeh0AQm+GarLqkpsxQpgu7p9HIgukF1lkUKkGlKLHk7WdOYMDEsvWpF/
BprA0vZPz1SeTjmllQIDAQAB
-----END PUBLIC KEY-----`;
// t.setPublicKey(PublicKey);
t.setPublicKey = new gt(PublicKey);
hashtoken = t.encrypt((new Date).getTime().toString());

console.log(hashtoken)
