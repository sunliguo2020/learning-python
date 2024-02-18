const { JSDOM } = require('jsdom');
const { window } = new JSDOM();
const navigator = {
  userAgent: 'node.js'
};
global.window = window;
global.navigator = navigator;

const JSEncrypt = require('jsencrypt');


// 加密函数
function encryptMessage(message, publicKey) {
  const encrypt = new JSEncrypt();
  encrypt.setPublicKey(publicKey);
  return encrypt.encrypt(message);
}

// 模拟从步骤 2 中获得的公钥
const publicKeyForJSEncrypt = `MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDlXTJX5BgW2/oJRf3kTo7XZ3q7aOnqN832+hkKe/xjKLKHnMTv+td/0Zsw1VkczWvodtLKsjJnrjiIx+dRIjLz2qYCWagGNroXGeh0AQm+GarLqkpsxQpgu7p9HIgukF1lkUKkGlKLHk7WdOYMDEsvWpF/BprA0vZPz1SeTjmllQIDAQAB`; // 这里应该是从步骤 2 中获得的公钥字符串
const messageToEncrypt = (new Date).getTime().toString();

console.log(messageToEncrypt)
const encryptedMessage = encryptMessage(messageToEncrypt, publicKeyForJSEncrypt);
console.log('Encrypted Message:', encryptedMessage);