from config.db_config import *


def add_task(description):
    """Adicionando uma nova tarefa"""
    tasks = load_tasks()
    new_task = {
        'id': get_next_id(tasks),
        'description': description,
        'status': 'not done'
    }
    tasks.append(new_task)
    save_tasks(tasks)

    print(f"Tarefa adicionada: {description}")

def update_task(task_id, status):
    """Atualizando o status da tarrefa"""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            save_tasks(tasks)
            print(f"A terafa {task_id} foi atualizada para: {status}")
            return
    print(f"Tarefa com o ID {task_id} não foi encontrada.")

def delete_task(task_id):
    """Exclui uma tarefa pelo ID"""
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f"Tarefa com ID {task_id} excluída.")

def list_tasks(status=None):
    """Lista todas as tarefas ou filtra por status"""
    tasks = load_tasks()
    filtered_tasks = tasks if status is None else [task for task in tasks if task['status'] == status]
    
    if not filtered_tasks:
        print("Nenhuma tarefa encontrada.")
    else:
        for task in filtered_tasks:
            print(f"{task['id']}. {task['description']} - {task['status']}")
