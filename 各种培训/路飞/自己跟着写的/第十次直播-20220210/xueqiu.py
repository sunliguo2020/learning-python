# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/12 9:47
"""
import requests

url = 'https://xueqiu.com/statuses/hot/listV2.json'
parms = {
    "since_id": "-1",
    "max_id": "312107",
    "size": "15"
}
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
"Cookie": "acw_tc=2760826b16446302984642854ec38d4d6a8d3efdb0533ca9fe1a37d62723cd; xq_a_token=512da9d222c381fa39dc775676c85ba2aa1ae80b; xqat=512da9d222c381fa39dc775676c85ba2aa1ae80b; xq_r_token=d25a8f2b3ad372c30f5f055e97403b5bbb67b77b; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY0NjI2MjI5MywiY3RtIjoxNjQ0NjMwMjcyMjI2LCJjaWQiOiJkOWQwbjRBWnVwIn0.jdue9kALc-iAAwsgcG3jDkd1yXtzq2HiNuHfWu8nl8FB1_YGXqN47X48VRgGk-JghJbIDv3RnfY3TI6eFkKDtkFVG1RwjhGjIHAKfH0co_2nM-RXlSolUk6_qWrQKCgCqqGpNZfSb2thuT-ZGSrjDf8FN27rTbKAwmd-e96iTOWzpVfV7YbHqDDuDhQGazgpYGrLN673sj-L9jDKU18MxhPDTyP0izWyekK6CR1aBWTK-_18KRU1KT8VlmUiUpNCLSjZV28ItTxEnrBtorX0GpaBik-nYM9ZOf3ze3iwcfege1BS58a1P1G4FEY_7DOmAq7Lrvmge2sgJuerKB_eaQ; u=481644630299368; Hm_lvt_1db88642e346389874251b5a1eded6e3=1644630381; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1644630381; device_id=54c5fb87ea0bf29f59deff0ed41ea970"
}
resp = requests.get(url = url,params=parms,headers=headers)
print(resp.json())