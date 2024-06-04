import time

from fastapi import FastAPI, Request, HTTPException
from typing import Optional
from pydantic import BaseModel
import logging
import time
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)
app = FastAPI()


# tempates = Jinja2Templates(directory='/templates/')


class Task(BaseModel):
    id: int
    title: str
    description: str
    status: Optional[str] = "new"


task_1 = Task(id=1, title='string 1', description='Description for task 1', status='New')
task_2 = Task(id=2, title='string 2', description='Description for task 2', status='InProgress')
tasks = [task_1, task_2]


@app.get("/tasks")
async def get_tasks():
    """возвращает список всех задач"""
    logger.info(f'Отработал GET запрос для всех tasks.')
    return {"tasks": tasks}


@app.get("/task/{id}")
async def update_task(task_id: int, task: Task):
    for i in range(len(tasks)):
        if tasks[i].id == task_id:
            tasks[i] = task
    logger.info(f'Отработал PUT запрос для task_id = {task_id}.')
    return task


@app.post("/tasks/")
async def create_item(task_id: int, task: Task):
    tasks.append(task)
    logger.info(f'Отработал post запрос для item id = {task_id}.')
    return task


@app.put("/task/{id}")
async def update_task(task_id: int, task: Task):
    for i in range(len(tasks)):
        if tasks[i].id == task_id:
            tasks[i] = task
    logger.info(f'Отработал PUT запрос для task_id = {task_id}.')
    return task


@app.delete("/task/{id}")
async def del_task(task_id: int):
    for i in range(len(tasks)):
        if tasks[i].id == task_id:
            return tasks.pop(i)
    return HTTPException(status_code=404, detail='Task not found')
