# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2024-03-19 12:37
"""
import pprint

import requests

cookies = {
    '_zap': '6cc272a9-fab9-48cd-80bf-abff70c21536',
    'd_c0': 'AHBWO4qj1xePTmvvvLzm1-P5ya-H2eLVjLI=|1702388268',
    '_xsrf': 'ilBJqmFgU8UurgfMhq65J4dEu0tegi1I',
    '__snaker__id': '61tnc5jXnp6uo3h0',
    'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49': '1710820695',
    'SESSIONID': 'Y7j6W5CKQIl8e6KEKLplDKox4rqymjIQm4qC2qxojuV',
    'JOID': 'VVgVC0xr-EsCjH9mOGQ_m5I18JUoNc8pO9tNJXs6ticy5kkqfe3itWiLeG4_4fTDVbcN2_6CONFj-CWzob_t-5A=',
    'osd': 'VVgTC05r-E0Cjn9mPmQ9m5Iz8JcoNckpOdtNI3s4tic05ksqfevit2iLfm494fTFVbUN2_iCOtFj_iWxob_r-5I=',
    'l_n_c': '1',
    'l_cap_id': '"ZTVlYjY2ZTQ4MTIxNGQ3OTkxM2MzZGYwOTZkNWNmZTA=|1710822060|a47581e625628480707aa27ce1bd49aa82e49d53"',
    'r_cap_id': '"MDIyNjc4NzkyNjQ0NDY0M2I1ZWRmMmQ4ZjE4ZTc5NWM=|1710822060|601d7a9febcdba76b7ebb6b48307a848df2477ae"',
    'cap_id': '"N2FlYTBkZDMyOWRjNDkwNzlkZDU3NjI1Mzg5MWY1MzE=|1710822060|3dbd5e839b06e6e4ca7fd04ec8f4200db06d5991"',
    'n_c': '1',
    'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49': '1710822111',
    'captcha_session_v2': '2|1:0|10:1710822108|18:captcha_session_v2|88:YWNjNXJOUTdJT3ZJR2czY2wvbUljYU5vc01CR0pVS0x2WHY0by9JZWIvUHdMYjdKM1J2K2pqR1Mzd0hnbmVCMA==|470c9ab148d6ce240acecce69993175d4f4a04569c441df8a2578d662955270e',
    'gdxidpyhxdE': 'mBNiSYCoUolX2z8vRH21kDs2%2FIU1%2FfnHjUDNX52iuRbf97Qw0g17UDPx4gPEvxu37%2FwLf7TVagiV%5C6epIEQI6ToMirKz2UPHYR6jxM4ri7ykEG5%2Bv3jo6EoA2f1KRl%5CTGSE8rV1DGSdm%5C%2F1OEUkqob%5CcdHIcbVezGwnxpkmjCDR3613N%3A1710823289071',
    'KLBRSID': 'e42bab774ac0012482937540873c03cf|1710822459|1710820686',
}

headers = {
    'authority': 'www.zhihu.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    # 'cookie': '_zap=6cc272a9-fab9-48cd-80bf-abff70c21536; d_c0=AHBWO4qj1xePTmvvvLzm1-P5ya-H2eLVjLI=|1702388268; _xsrf=ilBJqmFgU8UurgfMhq65J4dEu0tegi1I; __snaker__id=61tnc5jXnp6uo3h0; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1710820695; SESSIONID=Y7j6W5CKQIl8e6KEKLplDKox4rqymjIQm4qC2qxojuV; JOID=VVgVC0xr-EsCjH9mOGQ_m5I18JUoNc8pO9tNJXs6ticy5kkqfe3itWiLeG4_4fTDVbcN2_6CONFj-CWzob_t-5A=; osd=VVgTC05r-E0Cjn9mPmQ9m5Iz8JcoNckpOdtNI3s4tic05ksqfevit2iLfm494fTFVbUN2_iCOtFj_iWxob_r-5I=; l_n_c=1; l_cap_id="ZTVlYjY2ZTQ4MTIxNGQ3OTkxM2MzZGYwOTZkNWNmZTA=|1710822060|a47581e625628480707aa27ce1bd49aa82e49d53"; r_cap_id="MDIyNjc4NzkyNjQ0NDY0M2I1ZWRmMmQ4ZjE4ZTc5NWM=|1710822060|601d7a9febcdba76b7ebb6b48307a848df2477ae"; cap_id="N2FlYTBkZDMyOWRjNDkwNzlkZDU3NjI1Mzg5MWY1MzE=|1710822060|3dbd5e839b06e6e4ca7fd04ec8f4200db06d5991"; n_c=1; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1710822111; captcha_session_v2=2|1:0|10:1710822108|18:captcha_session_v2|88:YWNjNXJOUTdJT3ZJR2czY2wvbUljYU5vc01CR0pVS0x2WHY0by9JZWIvUHdMYjdKM1J2K2pqR1Mzd0hnbmVCMA==|470c9ab148d6ce240acecce69993175d4f4a04569c441df8a2578d662955270e; gdxidpyhxdE=mBNiSYCoUolX2z8vRH21kDs2%2FIU1%2FfnHjUDNX52iuRbf97Qw0g17UDPx4gPEvxu37%2FwLf7TVagiV%5C6epIEQI6ToMirKz2UPHYR6jxM4ri7ykEG5%2Bv3jo6EoA2f1KRl%5CTGSE8rV1DGSdm%5C%2F1OEUkqob%5CcdHIcbVezGwnxpkmjCDR3613N%3A1710823289071; KLBRSID=e42bab774ac0012482937540873c03cf|1710822459|1710820686',
    'referer': 'https://www.zhihu.com/question/27968331/answer/38937314',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'x-requested-with': 'fetch',
    'x-zse-93': '101_3_3.0',
    'x-zse-96': '2.0_IBHo+DGRafshcHklHHuuColrl/1HAa5NfjL1trvK0nMBYDrQ3QlkRiL+U9dC5xb3',
}

response = requests.get(
    'https://www.zhihu.com/api/v4/questions/27968331/feeds?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Creaction_instruction%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B*%5D.author.follower_count%2Cvip_info%2Cbadge%5B*%5D.topics%3Bdata%5B*%5D.settings.table_of_content.enabled&offset=&limit=3&order=default&platform=desktop',
    cookies=cookies,
    headers=headers,
)

pprint.pprint(response.json())
