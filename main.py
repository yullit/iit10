from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, Gauge

app = FastAPI()

# Створення метрик
REQUEST_COUNTER = Counter('request_count', 'Total number of requests')
IN_PROGRESS = Gauge('in_progress_requests', 'Number of requests in progress')

# Ініціалізація Prometheus Instrumentator
Instrumentator().instrument(app).expose(app)

@app.get("/")
async def hello():
    REQUEST_COUNTER.inc()
    IN_PROGRESS.inc()
    response = "Hello, World!"
    IN_PROGRESS.dec()
    return {"message": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)