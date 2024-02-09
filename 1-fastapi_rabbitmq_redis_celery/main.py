from fastapi import FastAPI
from tasks import predict
from celery_app import app as celery

app = FastAPI(title="teste", version="0.0.1")


@app.get("/")
def home():
    return "Home"


@app.post("/task")
def task_post():
    task_result = predict.delay()
    return {"Task id": str(task_result.id)}


@app.get("/task/{task_id}")
def task_get(task_id: str):
    task_result = celery.AsyncResult(task_id)
    if task_result.status != "PENDING":
        return {"Predict": str(task_result.get())}
    return {"Predict": "PENDING"}


@app.get("/status/{task_id}")
def task_get_status(task_id: str):
    task_result = celery.AsyncResult(task_id)
    return {"Predict status": str(task_result.status)}


# docker run -d -p 5672:5672 rabbitmq
# source env/Scripts/activate
# uvicorn main:app --host 0.0.0.0
# celery -A celery_app worker --loglevel=INFO -P threads
# celery -A celery_app worker --loglevel=INFO -P threads --pool=solo
# celery -A celery_app flower
# flower -A celery_app
