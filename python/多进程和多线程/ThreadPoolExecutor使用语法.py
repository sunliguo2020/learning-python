from concurrent.futures import ThreadPoolExecutor,as_completed

urls = ['http://wwww.baidu.com/'+str(page) for page in range(100)]
def craw(url):
    pass

# map函数 注意map的结构和入参是顺序对应的。
with ThreadPoolExecutor() as pool:
    results = pool.map(craw,urls)

    for result in results:
        print(results)

# future 模式，用as_completed 顺序是不定的。
with ThreadPoolExecutor() as pool:
    futures = [pool.submit(craw,url) for url in urls]
    # 按照执行顺序返回
    for future in futures:
        print(future.result())
    # 谁先执行完，谁先返回
    for future in as_completed(futures):
        print(future.result())