from celery_app import app
from celery.signals import celeryd_init, task_postrun
import time


@task_postrun.connect
def init_celery(**kwargs):
    print("INICIOU O CELERY E CARREGOU O MODELO")


@celeryd_init.connect
def task_postrun_handler(
    task_id,
    task,
    retval,
    state,
    **kwargs,
):
    print(f"Task id: {task_id}")
    print(f"Estado da task: {state}")
    print(f"Valor da previsão: {retval}")


@app.task(name="teste")
def predict():
    time.sleep(5)
    return {"Predict": "5 segundos"}
