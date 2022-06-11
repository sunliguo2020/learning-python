const jsdom = require("jsdom");
const {JSDOM} = jsdom;

const resourceLoader = new jsdom.ResourceLoader({
    userAgent: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36"
});

const html = `<!DOCTYPE html><p>Hello world</p>`;
const dom = new JSDOM(html, {
    url: "https://www.toutiao.com",
    referrer: "https://example.com/",
    contentType: "text/html",
    resources: resourceLoader,
});

window = dom.window;

console.log(window);

window.x = 123;
console.log(window.x);
