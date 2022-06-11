import requests

res = requests.get(
    url="https://www.zhihu.com/api/v4/search_v3?q=%E9%A2%84%E7%BA%A6%E4%B9%9D%E4%BB%B7&t=general&lc_idx=0&correction=1&offset=0&advert_count=0&limit=20&is_real_time=0&show_all_topics=0&search_source=Suggestion&filter_fields=&raw_query=",
    headers={
        "x-udid": "AGBQ9YDFAxRLBel97ZJuRX4mzPE3_trJT4k=",
        "x-ac-udid": "AGBQ9YDFAxRLBel97ZJuRX4mzPE3_trJT4k=",
        "x-hd": "b8bb54554503c4da7023fdf42e40cc15",
        "x-zse-96": "2.0_a828gvHqnhNxnBNBKRF0rQLBb8tpnu2qBLxqHhu0rTNY",
        "x-zse-93": "101_4_2.0",
        "user-agent": "ZhihuHybrid com.zhihu.android/Futureve/5.32.1 Mozilla/5.0 (Linux; Android 10; Redmi 8A Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36",
        'x-app-version': "5.32.1"
    },

)

print(res.json())
