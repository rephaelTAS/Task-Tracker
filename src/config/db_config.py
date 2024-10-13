import json
import os


ficheiro = os.path.join("src", "database", "data.json")

# Verifica se o arquivo json existe, se não, cria um novo
if not os.path.exists(ficheiro):
    with open(ficheiro, 'w') as file:
        json.dump([], file) #Lista vazia para armazenar as tarefas

def load_tasks():
    """Lendo as tarefas no arquivo"""
    with open(ficheiro, 'r') as file:
        return json.load(file)
    
def save_tasks(tasks):
    """Salvando as tarefas"""
    with open(ficheiro, 'w') as file:
        json.dump(tasks, file, indent=4)

def get_next_id(tasks):
    """Obtendo o número de Id"""
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1


