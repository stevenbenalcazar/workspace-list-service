import redis
import os
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def get_cache(key):
    return redis_client.get(key)

def set_cache(key, value, expiration=60):
    redis_client.set(key, value, ex=expiration)
