from data_manager import load_tasks, save_tasks
from datetime import datetime

def add_task(name, description=""):
    """Добавление новой задачи"""
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "name": name,
        "description": description,
        "status": "Активная",
        "created": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(task)
    save_tasks(tasks)
    return task

def get_all_tasks():
    """Получение списка всех задач"""
    return load_tasks()

def mark_task_done(task_id):
    """Отметка задачи как выполненной"""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Выполнена"
            save_tasks(tasks)
            return True
    return False

def delete_task(task_id):
    """Удаление задачи"""
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)

def clear_completed():
    """Очистка выполненных задач"""
    tasks = load_tasks()
    tasks = [t for t in tasks if t["status"] != "Выполнена"]
    save_tasks(tasks)