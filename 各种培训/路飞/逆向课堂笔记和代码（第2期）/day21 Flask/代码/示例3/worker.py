import redis
import json

POOL = redis.ConnectionPool(host='124.222.193.204', port=6379, password='foobared', encoding='utf-8',
                            max_connections=1000)

while True:
    conn = redis.Redis(connection_pool=POOL)
    # data = conn.rpop("mt_task_queue")
    # 没有数据时，最多等待10s
    data = conn.brpop("mt_task_queue", timeout=30)
    conn.close()
    print(data)
    if not data:
        continue
    email, count = json.loads(data[-1].decode("utf-8"))
    print(email, count)
