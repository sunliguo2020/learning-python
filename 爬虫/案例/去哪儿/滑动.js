window = global;

const jsdom = require("jsdom");
const {JSDOM} = jsdom;

const html = `<!DOCTYPE html><p>Hello world</p>`;
const dom = new JSDOM(html, {
    url: "https://user.qunar.com/passport/login.jsp",
    referrer: "https://www.qunar.com/",
    contentType: "text/html"
});
document = dom.window.document;

window = global;
Object.assign(global, {
    location: {
        hash: "",
        host: "user.qunar.com",
        hostname: "user.qunar.com",
        href: "https://user.qunar.com/passport/login.jsp",
        origin: "https://user.qunar.com",
        pathname: "/passport/login.jsp",
        port: "",
        protocol: "https:",
        search: "",
    },
    navigator: {
        appCodeName: "Mozilla",
        appName: "Netscape",
        appVersion: "5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
        cookieEnabled: true,
        deviceMemory: 8,
        doNotTrack: null,
        hardwareConcurrency: 4,
        language: "zh-CN",
        languages: ["zh-CN", "zh"],
        maxTouchPoints: 0,
        onLine: true,
        platform: "MacIntel",
        product: "Gecko",
        productSub: "20030107",
        userAgent: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
        vendor: "Google Inc.",
        vendorSub: "",
        webdriver: false
    }
});


window.sliderInfo =
    {
        "openTime": 1712585804945,
        "startTime": 1712585808497,
        "endTime": 1712585808967,
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "uid": "0000ea80306c5af20058a1eb",
        "track": [
            "8500;82.00;281.00;0.00",
            "8550;86.00;281.00;4.00",
            "8574;94.00;281.00;12.00",
            "8602;130.00;281.00;48.00",
            "8622;170.00;281.00;88.00",
            "8648;252.00;281.00;170.00",
            "8671;330.00;281.00;248.00",
            "8690;373.00;281.00;291.00",
            "8715;422.00;281.00;340.00",
            "8736;444.00;281.00;362.00",
            "8757;447.00;281.00;365.00",
            "8779;449.00;281.00;367.00",
            "8790;451.00;281.00;369.00",
            "8812;454.00;281.00;372.00",
            "8833;460.00;281.00;378.00",
            "8854;465.00;281.00;383.00",
            "8874;474.00;280.00;392.00",
            "8895;478.00;280.00;396.00",
            "8916;486.00;280.00;404.00",
            "8938;498.00;280.00;416.00",
            "8959;509.00;280.00;427.00"
        ],
        "acc": [],
        "ori": [],
        "deviceMotion": [
            {
                "isTrusted": true
            },
            {
                "isTrusted": true
            },
            {
                "isTrusted": true
            },
            {
                "isTrusted": true
            },
            {
                "isTrusted": true
            },
            {
                "isTrusted": true
            }
        ]
    }
// console.log(sliderInfo)

const CryptoJS = require("crypto-js");
d = CryptoJS

function encryption() {
    var e = JSON.stringify(this.sliderInfo);
    // console.log(e)
    return d.AES.encrypt(d.enc.Utf8.parse(e), d.enc.Utf8.parse("227V2xYeHTARSh1R"), {
        mode: d.mode.ECB,
        padding: d.pad.Pkcs7
    }).toString()
}
// console.log(d.enc.Utf8.parse("227V2xYeHTARSh1R"))
console.log(encryption.call(window))