const CryptoJS  = require('./crypto')

function getToken(player) {
    let key = CryptoJS.enc.Utf8.parse('fipFfVsZsTda94hJNKJfLoaqyqMZFFimwLt')
    const {name, birthday, height, weight} = player
    let base64Name = CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse(name))
    let encrypted = CryptoJS.DES.encrypt(`${base64Name}${birthday}${height}${weight}`, key, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    })
    return encrypted.toString()
}

const player = {
    'name': '凯文-杜兰特',
    'image': 'durant.png',
    'birthday': '1988-09-29',
    'height': '208cm',
    'weight': '108.9KG'
  }

  console.log(getToken(player))