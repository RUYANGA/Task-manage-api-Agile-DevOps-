from app.models import Task

tasks: list[Task] = []


def reset():
    tasks.clear()
