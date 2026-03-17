from __future__ import annotations

from task_manager import TaskManager


def show_menu() -> None:
    print('\n=== StudyFlow CLI ===')
    print('1 - Adicionar tarefa')
    print('2 - Listar tarefas')
    print('3 - Concluir tarefa')
    print('4 - Remover tarefa')
    print('5 - Sair')


def list_tasks(manager: TaskManager) -> None:
    tasks = manager.list_tasks()
    if not tasks:
        print('\nNenhuma tarefa cadastrada.')
        return

    print('\nTarefas cadastradas:')
    for task in tasks:
        status = 'Concluída' if task['done'] else 'Pendente'
        print(f"{task['id']} - {task['title']} [{status}]")


def main() -> None:
    manager = TaskManager()

    while True:
        show_menu()
        option = input('Escolha uma opção: ').strip()

        if option == '1':
            title = input('Digite a tarefa de estudo: ')
            try:
                task = manager.add_task(title)
                print(f"Tarefa '{task['title']}' adicionada com sucesso.")
            except ValueError as error:
                print(error)

        elif option == '2':
            list_tasks(manager)

        elif option == '3':
            try:
                task_id = int(input('Digite o ID da tarefa concluída: '))
                task = manager.complete_task(task_id)
                print(f"Tarefa '{task['title']}' concluída.")
            except ValueError as error:
                print(error)

        elif option == '4':
            try:
                task_id = int(input('Digite o ID da tarefa que deseja remover: '))
                task = manager.remove_task(task_id)
                print(f"Tarefa '{task['title']}' removida com sucesso.")
            except ValueError as error:
                print(error)

        elif option == '5':
            print('Encerrando o StudyFlow CLI...')
            break

        else:
            print('Opção inválida. Tente novamente.')


if __name__ == '__main__':
    main()
