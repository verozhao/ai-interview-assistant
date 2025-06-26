from pinecone import Pinecone
import redis

pc = Pinecone(api_key=settings.pinecone_api_key)
index = pc.Index("interview-assistant")
redis_client = redis.from_url(settings.redis_url)