import redis
import random
import string

# 创建 Redis 连接
redis_host = '175.178.19.5'  # Redis 服务器地址
redis_port = 6379  # Redis 服务器端口
redis_password = 'kezi520'  # 如果有密码，填写密码，否则为 None

redis_conn = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

# 定义插入模拟数据的数量
total_records = 50000

# 批量插入数据
for i in range(total_records):
    # 模拟数据生成，你可以根据实际需求调整
    data_type = random.choice(['string', 'list', 'set', 'hash'])
    key = f'key_{i}'

    if data_type == 'string':
        value = ''.join(random.choices(string.ascii_letters, k=10))
        redis_conn.set(key, value)
    elif data_type == 'list':
        values = [random.randint(1, 100) for _ in range(5)]
        redis_conn.lpush(key, *values)
    elif data_type == 'set':
        values = {random.randint(1, 100) for _ in range(5)}
        redis_conn.sadd(key, *values)
    elif data_type == 'hash':
        field_values = {f'field_{j}': random.randint(1, 100) for j in range(5)}
        redis_conn.hset(key, mapping=field_values)

print(f"Inserted {total_records} records into Redis.")
