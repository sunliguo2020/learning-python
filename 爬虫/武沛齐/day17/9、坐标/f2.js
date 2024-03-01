function _0x41dc48(_0x289f0f) {

    _0x289f0f = _0x289f0f || _0x11dabc["event"];
    var _0xe41ea4 = _0x289f0f["srcElement"] || _0x289f0f["target"]
        , _0x311abd = this["_data"]
        , _0x226da4 = _0x311abd["selectData"]
        , _0x3710ef = _0x311abd['selectPosData']
        , _0xd3e4df = _0x311abd['trueWidth']
        , _0x30fbb2 = _0x311abd["trueHeight"]
        , _0x128b5e = this["_config"]["mode"]
        , _0x2d4e0e = this['getMainDom']()
        , _0x170354 = _0x2d4e0e["imageEl"]
        , _0x28ed43 = this['getMousePos'](_0x289f0f)

        , _0x4351e1 = _0x2460cd[_0x1d0195["lVKke"]]['getBoundingClientRect'](_0x170354)

        , _0x52aa32 = +new Date()
        , _0x5a1fbf = _0x4351e1['x']
        , _0x1e9886 = _0x4351e1['y']

        , _0x5ab598 = void (0x35a * -0x7 + -0x17c7 + 0x2f3d)
        , _0x4c0a1f = (_0x28ed43['x'] - _0x5a1fbf - (-0x1 * 0x2da + 0x19cf + 0xb73 * -0x2)) / _0xd3e4df
        , _0x27bb65 = void (-0x22b3 + 0x22e9 + 0x6 * -0x9)

        , _0x42ca39 = _0x1d0195["rlnuS"](_0x28ed43['x'] - _0x5a1fbf, _0xd3e4df);

    this['preventDefaultHandler'](_0x289f0f);
    _0x4c0a1f * (-0xeea + 0x1194 + -0x2a9 * 0x1) != _0x4c0a1f && (_0x4c0a1f = -0x1d76 + 0x23 * -0x9a + 0xca1 * 0x4);
    _0x1d0195["bSGXS"](_0x42ca39 * (-0x214d + 0x2b * -0xd + 0x237d), _0x42ca39) && (_0x42ca39 = -0x22f9 * -0x1 + -0x1 * 0x528 + 0x1dd1 * -0x1);
    _0x5ab598 = [_0x4c0a1f, _0x1d0195['VuVFS'](_0x28ed43['y'] - _0x1e9886, 0x2 * 0x10ee + -0xa53 * 0x3 + 0x16a * -0x2) / _0x30fbb2, _0x52aa32],


        // 鼠标点击信息
        // _0x42ca39
        _0x27bb65 = [_0x42ca39, _0x1d0195["IXgiz"](_0x28ed43['y'], _0x1e9886) / _0x30fbb2, _0x52aa32];

        this["_data"]["selectPosData"]["push"](_0x5ab598),
        //要求的值
        this["_data"]["selectData"]["push"](_0x27bb65),
        this['updateAnswerHtml']();
    switch (_0x128b5e) {
        case "select":
        case _0x1d0195['wXeDh']:
        case 'seq_select':
            if (_0x3710ef["length"] == 0x22e2 + 0x22a8 + -0x16 * 0x329) {
                var _0x1b07f1 = _0x1d0195["iSGeA"]["split"]('|')
                    , _0x708ea5 = 0x1d6f + 0xd * 0x4d + 0x8 * -0x42b;
                while (!![]) {
                    switch (_0x1b07f1[_0x708ea5++]) {
                        case '0':
                            this["_data"]['endTime'] = +new Date();
                            continue;
                        case '1':
                            return;
                        case '2':
                            this['_data']['mouseData'] = _0x226da4;
                            continue;
                        case '3':
                            this["checkApi"]();
                            continue;
                        case '4':
                            this['clearEvent']();
                            continue;
                    }
                    break;
                }
            }
            break;
        case "spatial_select":
            if (_0x1d0195["dwvzD"](_0x3710ef["length"], -0x91a + -0x2212 + 0x2b2d * 0x1)) {
                var _0x14aef1 = '1|3|4|2|0'["split"]('|')
                    , _0x326b17 = 0x1bcb + 0xe0b + -0x29d6;
                while (!![]) {
                    switch (_0x14aef1[_0x326b17++]) {
                        case '0':
                            return;
                        case '1':
                            this["_data"][_0x1d0195["japAq"]] = _0x226da4;
                            continue;
                        case '2':
                            this['clearEvent']();
                            continue;
                        case '3':
                            this["_data"][_0x1d0195["Cgncz"]] = +new Date();
                            continue;
                        case '4':
                            this["checkApi"]();
                            continue;
                    }
                    break;
                }
            }
            break;
    }
}