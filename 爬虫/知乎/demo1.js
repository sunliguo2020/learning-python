t2 = '2.0'

function ed(tt, te, tr, ti) {
    var ta = tr.zse93
        , tu = tr.dc0
        , tc = tr.xZst81
        , tf = t4(tt)
        , td = t6(te)
        , tp = [ta, tf, tu, t8(td) && td, tc].filter(Boolean).join("+");
    return {
        source: tp,
        signature: (0,
            tJ(ti).encrypt)(ty()(tp))
    }
}

function tT() {
    if ("undefined" == typeof Reflect || !Reflect.construct || Reflect.construct.sham)
        return !1;
    if ("function" == typeof Proxy)
        return !0;
    try {
        return Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function () {
        })),
            !0
    } catch (tt) {
        return !1
    }
}
//te:url
te = '/api/v4/members/d53b74e344eed04badd1167d0fd5fe83?include=allow_message%2Cis_followed%2Cis_following%2Cis_org%2Cis_blocking%2Cemployments%2Canswer_count%2Cfollower_count%2Carticles_count%2Cgender%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics'
tT = ed(te, tf.body, {
    zse93: tb,
    dc0: tE,
    xZst81: tC
}, tA)


tO = tT.signature
xzse = t2 + tO

console.log(xzse)