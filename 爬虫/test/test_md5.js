// 首先，确保你已经包含了CryptoJS库
// 你可以通过CDN或者npm安装CryptoJS
// 例如：<script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0/crypto-js.min.js"></script>
CryptoJS = require('crypto-js')
// 使用CryptoJS计算数字1（转换为字符串后）的MD5哈希
var numStr = "1"; // 数字1转换为字符串
var md5HashNumStr = CryptoJS.MD5(numStr).toString();
console.log(md5HashNumStr); // 输出MD5哈希值

// 使用CryptoJS计算字符串"1"的MD5哈希
var str = '1'; // 已经是字符串
var md5HashStr = CryptoJS.MD5(str).toString();
console.log(md5HashStr); // 输出MD5哈希值