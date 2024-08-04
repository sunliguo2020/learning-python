# -*- coding: utf-8 -*-
"""
 @Time : 2024/4/10 19:18
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import requests

cookies = {
    'QN1': '0000ea80306c5af20058a1eb',
    'QN300': 'organic',
    'QN99': '9350',
    'QunarGlobal': '10.72.48.24_-7e14ca11_18d1673d5ca_6c40|1705490956232',
    '_i': 'ueHd8ZkXXXVXqeqA-RUsWm9c0kRX',
    'QN601': '6db340d059de52e6dcc8f4ee08fc004f',
    'QN48': '0000f5802f105af200600bcb',
    'fid': 'e015c9ee-f271-409b-8d24-1be75cd1b552',
    'ctt_june': '1683616182042##iK3wWRawWUPwawPwa%3Dj%3DaSP%2BED3%3DESgnERj%2BaP3wVPaAaPXNWRiTER3nWRt%2BiK3siK3saKg8WKXNaR2AVKP%2BWUPwaUvt',
    'QN271AC': 'register_pc',
    'QN271RC': '8de1668fd625006f9e3a2f0044f2002e',
    'QN271SL': '8de1668fd625006f9e3a2f0044f2002e',
    'qunar-assist': '{%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}',
    'QN205': 'organic',
    'QN277': 'organic',
    'QN267': '03637566343b49f99e',
    'csrfToken': 'uw9aiIBAKuwyzi8d5Tkq6IInE1zIFh4M',
    'QN163': '0',
    'QN269': 'C6D5F871F72B11EEA52796E0D56CFCE6',
    '_vi': 'j7-HfQSwbpzfCV8qCssQEYqsvWFjzyYE_A6EPucZlGt0gIhcfLzvCjjM4iLw39E-uXrEMvBvb_Wm4F2Orc5Vr_LXn79esEoQYbYUR_EXvdXSz5CAee7ytVfTx0Zkt_pwLo0NRzJOyinufjaWyjeQJlWt7jsBOS8DR8Lo0xgMtdS1',
    'QN271': 'e7511178-6444-4716-a74c-b65ef4820b45',
    'ctf_june': '1683616182042##iK3wWS3%3DWUPwawPwaskIVKETWSPAaRDwa2ihWPEDERgAasgNERjsWPfIW%3D3niK3siK3saKgnaSg%3DWsgNWKXNauPwaUvt',
    'ariaDefaultTheme': 'undefined',
    'cs_june': '0b92240f316f3f2328b75f4f7e10a15474256fe3bdbdd111f99b3bd3e5d61b80f746750334d6f023c8722f6765aa464cbe3e27be81c12e4d339099d1734c7ef2b17c80df7eee7c02a9c1a6a5b97c1179a0f3a9aabdd74a086f7a7a327e96a7bc5a737ae180251ef5be23400b098dd8ca',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'text/plain;charset=UTF-8',
    # 'cookie': 'QN1=0000ea80306c5af20058a1eb; QN300=organic; QN99=9350; QunarGlobal=10.72.48.24_-7e14ca11_18d1673d5ca_6c40|1705490956232; _i=ueHd8ZkXXXVXqeqA-RUsWm9c0kRX; QN601=6db340d059de52e6dcc8f4ee08fc004f; QN48=0000f5802f105af200600bcb; fid=e015c9ee-f271-409b-8d24-1be75cd1b552; ctt_june=1683616182042##iK3wWRawWUPwawPwa%3Dj%3DaSP%2BED3%3DESgnERj%2BaP3wVPaAaPXNWRiTER3nWRt%2BiK3siK3saKg8WKXNaR2AVKP%2BWUPwaUvt; QN271AC=register_pc; QN271RC=8de1668fd625006f9e3a2f0044f2002e; QN271SL=8de1668fd625006f9e3a2f0044f2002e; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; QN205=organic; QN277=organic; QN267=03637566343b49f99e; csrfToken=uw9aiIBAKuwyzi8d5Tkq6IInE1zIFh4M; QN163=0; QN269=C6D5F871F72B11EEA52796E0D56CFCE6; _vi=j7-HfQSwbpzfCV8qCssQEYqsvWFjzyYE_A6EPucZlGt0gIhcfLzvCjjM4iLw39E-uXrEMvBvb_Wm4F2Orc5Vr_LXn79esEoQYbYUR_EXvdXSz5CAee7ytVfTx0Zkt_pwLo0NRzJOyinufjaWyjeQJlWt7jsBOS8DR8Lo0xgMtdS1; QN271=e7511178-6444-4716-a74c-b65ef4820b45; ctf_june=1683616182042##iK3wWS3%3DWUPwawPwaskIVKETWSPAaRDwa2ihWPEDERgAasgNERjsWPfIW%3D3niK3siK3saKgnaSg%3DWsgNWKXNauPwaUvt; ariaDefaultTheme=undefined; cs_june=0b92240f316f3f2328b75f4f7e10a15474256fe3bdbdd111f99b3bd3e5d61b80f746750334d6f023c8722f6765aa464cbe3e27be81c12e4d339099d1734c7ef2b17c80df7eee7c02a9c1a6a5b97c1179a0f3a9aabdd74a086f7a7a327e96a7bc5a737ae180251ef5be23400b098dd8ca',
    'origin': 'https://user.qunar.com',
    'pragma': 'no-cache',
    'referer': 'https://user.qunar.com/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

# data = '{"data":"V1nlNJb+MLQfIW6JxmaEGjBY7/otL3iUR0uQaLw8SXnJodLuX2EMY9Zd8VHWW5SPVq2GZxe37FMpRHtLqE4MVL7Cwu496XPe3CXNVaHS82HbwIYdS4ceo1kLfu+9Hxv4Pf1bQK7GBdkHOn+pynXZ5rf/Cry06pPfR/Hf7BrFSk1rvLNqcTBvq6730+O1VcEkBJTDTx/lnSA+jwK9ypQ44HRjonU347dLl4qbCximrSPRQuBNdBrRqhvabjhMp9D/GJBsICcW13u/6VrdJ1k9i08JA9gofUTN8UR4foGqKgJ86u5W4V97ockfl/+Y0srIpJY1huQuDiaLM/CyIOhOewBn0gNmC6EIrkgeyqH2oCgb0m1uixA3Hot4J96I76IWMcacR1LFZAReZsrJnZV6BO1fIp/COmbAkls0FQMjwAp8l+KxFPHWQgXffkGY6B26lgsTuWaE1vb8qy4eBxVyc6MS0vg0yghiyDjT3i/PLdY5EFIrflhqFTCv/0wddH5dC15zXE9xgqCQ5prvDSU9MHy6a35qM9FDGEfLKlz6VLAso7ZoNpLvMBDq0QAX8nicmypxs71L3mUXtScON+PWa9K+9Ruib9Jjr6ZkXN5jv9mTAQt7vEKXxQBdivxADUY9R3e2W6J3+MOMrUtk+mJi4jBypr8qyRwZcjG4UHDOh64=","orca":2,"appCode":"register_pc","cs":"pc"}'
data = {
    # "data": "V1nlNJb+MLQfIW6JxmaEGjBY7/otL3iUR0uQaLw8SXnJodLuX2EMY9Zd8VHWW5SPVq2GZxe37FMpRHtLqE4MVL7Cwu496XPe3CXNVaHS82HbwIYdS4ceo1kLfu+9Hxv4Pf1bQK7GBdkHOn+pynXZ5rf/Cry06pPfR/Hf7BrFSk1rvLNqcTBvq6730+O1VcEkBJTDTx/lnSA+jwK9ypQ44HRjonU347dLl4qbCximrSPRQuBNdBrRqhvabjhMp9D/GJBsICcW13u/6VrdJ1k9i08JA9gofUTN8UR4foGqKgJ86u5W4V97ockfl/+Y0srIpJY1huQuDiaLM/CyIOhOewBn0gNmC6EIrkgeyqH2oCgb0m1uixA3Hot4J96I76IWMcacR1LFZAReZsrJnZV6BO1fIp/COmbAkls0FQMjwAp8l+KxFPHWQgXffkGY6B26lgsTuWaE1vb8qy4eBxVyc6MS0vg0yghiyDjT3i/PLdY5EFIrflhqFTCv/0wddH5dC15zXE9xgqCQ5prvDSU9MHy6a35qM9FDGEfLKlz6VLAso7ZoNpLvMBDq0QAX8nicmypxs71L3mUXtScON+PWa9K+9Ruib9Jjr6ZkXN5jv9mTAQt7vEKXxQBdivxADUY9R3e2W6J3+MOMrUtk+mJi4jBypr8qyRwZcjG4UHDOh64=",
    "data":"V1nlNJb+MLQfIW6JxmaEGpa7Z+MFcKCAOs1KuppmFOp2O49Q8208ZWJBdbne/Zr1hBFgOH6+zbGDizWSbVxE8USmdQEe2yjX4FR31s6vg33bwIYdS4ceo1kLfu+9Hxv4Pf1bQK7GBdkHOn+pynXZ5rf/Cry06pPfR/Hf7BrFSk1rvLNqcTBvq6730+O1VcEkBJTDTx/lnSA+jwK9ypQ44HRjonU347dLl4qbCximrSPRQuBNdBrRqhvabjhMp9D/GJBsICcW13u/6VrdJ1k9i08JA9gofUTN8UR4foGqKgJ86u5W4V97ockfl/+Y0srIsSp5icCHLAHF0lYO0TQEi6m05cQGZLM/ELH1CWcn/CrvFrcQ50E3CXIibxjAuul7f8WZcaNRVYlreQ4392byNTU77FB8/rxJjvKaizKQmlmOKNhXCZSHmKgYXVrS2R0wv7KqudJvCrhnBn3ltUBKbBK/1qGlvdiEAOebkRR8md3qc7drpztiSrWT2aC2OV3EhcLEaWLGbIFxYEbaaJRUcIDHCCWxPozGm8EekBR80XDPrGGjpDzBjYCdRFwS3CKGqb5e5wcwPjY6mVcf0cqTMyav2NKfPDnjtayY2NB83Wc3CPMliT97+6ACFXNgTdhoAspdm0Fj/HnM+U3onzmvXJ9zxnPPuORZuaplxmgBf+Pr+Ev7GH5dyFjnxvs6WxYJugsjCSHq7pL8Tdr61z8Hy1MDigMZKi3RRY/QQvEaDSUHFkCLJdncz+gJrooXaOVPhM0ccnIIbkchPh0kLq+ldrP3P7sjO/XaK7JwxORltWdg/ifR/Zkenx8l+u1Dexyxej9IEB0dDDY+JTeXw2+MPPd8Wcv4+X8XjbQjoRd8eKC9s13HSYjwCLxtQ5ETVI1DbQmMQAYEPKnBklt7rTt9oYRIvRa0V5iAj1vqOZLggRoJt+UTNfVLgdLjT3BPUIo5OldZAA+b5MrboedLneNe7WBO3Rq7Akts1shfmdrJDlMuqmtHH5mtz0CPZAno7tEX2LZhf252+nIdeo7w0YCCpoZwmj+p/1xsVJJvv0/KNp0oxg6jarP2OIKYlovSdDiyxHoY37IzE6zQIOueXQcVe+F5g8L6CB8DE4OK0FUSwJ7BjG9D8cxcYz+arvvIwp9ZkwELe7xCl8UAXYr8QA1GPU7OFHfnpCoD4i9DZodzvMqcqTczt8kGtk0OLqwQtJFU5Wx077u7GupC7tzSH383E142IFE3ktoHlH6hwSOLcp5Hohlus4C1whL1E2Q4e7Q/VSrXvwzHWrT7S2btq9mwUg==",
    "orca": 2,
    "appCode": "register_pc",
    "cs": "pc"}

response = requests.post('https://vercode.qunar.com/inner/captcha/snapshot',
                         # cookies=cookies,
                         headers=headers,
                         json=data)
print(response.json())
print(response.text)
