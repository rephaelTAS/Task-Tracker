from config.function import *
import json
import sys
import os


# Função principal para processar a linha de comando
def main():
    while True:
        print(14*"=")
        print("Bem vindos ao gestor de tarifas 2.0")
        print("sigas as instruções para a melhor compreenção do programa")
        print(14*"=")
        print(14*"=")
        print("Para adicionar uma nova tarefa digite 1")
        print(14*"=")
        print("Para atualizar a tarefa digite 2")
        print(14*"=")
        print("Para deletar uma tarefa digite 3")
        print(14*"=")
        print("Para ver a lista digite 4")
        print(14*"=")
        print("Para filtrar a lista baseada no status da tarefa digite 5")
        print(14*"=")
        print("Sair do programa digite 6")
        print(14*"=")
        print(14*"=")

        
        
        command = int(input("diggite o número corespondente: "))

        
        if command == 1:
            print(14*"=")
            print("Escreva a tarefa")
            description = input()
            add_task(description)

        elif command == 2:
            """Mostar as tarefas já listadas"""
            print(14*"=")
            print("Suas tarefas atuais")
            print("")
            dados = load_tasks()
            for dado in dados:
                print(dado)
                print("")
            print(14*"=")

            print("Informe o id da qual será atualizada")
            task_id = int(input())
            print("use 2 'in progress', 3 'done', 1 'not done'")
            nota = int(input())
            if nota == 1:
                status = 'not done'
                update_task(task_id, status)

            elif nota == 2:
                status = 'in progress'
                update_task(task_id, status)
            
            elif nota == 3:
                status = 'done'
                update_task(task_id, status)
            else:
                print("use 2 'in progress', 3 'done', 1 'not done'")


        elif command == 3:
            """Para apagar uma tarefa"""
            print("digite o id da tarefa a ser apagada")
            id = int(input())

            task_id = id
            delete_task(task_id)
            print("")
            print(14*"=")
            print("Lista Atualizada")
            print("")
            lista = load_tasks()
            for dado in lista:
                print(dado)
                print("")

        elif command == 4:
            """Para ver a lista de tarefas"""
            dados = load_tasks()
            print(14*"=")
            for dado in dados:
                print(dado)
                print("")

        elif command == 5:
            """Para filtrar a lista baseando nos status"""
            print("use 2 'in progress', 3 'done', 1 'not done'")
            nota = int(input())
            if nota == 1:
                status = 'not done'
                list_tasks(status)

            elif nota == 2:
                status = 'in progress'
                list_tasks(status)

            elif nota == 3:
                status = 'done'
                list_tasks(status)

            else:
                print("Status inválido.")
            
                print("Use os numero que foram informados")
        elif command == 6:
            break

        else:
            print("Comando inválido.")
            print("Use os numero que foram informados")



if __name__ == '__main__':
    main()    
