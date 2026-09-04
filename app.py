from flask import Flask
import redis

app = Flask(__name__)

redis_client = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)

@app.route("/")
def home():
    visits = redis_client.incr("visits")

    return f"""
    <h1>Docker Compose Lab</h1>
    <p>Hello from Flask + Redis!</p>
    <p>This page has been visited {visits} times.</p>
    """

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "redis": redis_client.ping()
    }

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
