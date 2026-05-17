from __future__ import annotations

from task_manager import TaskManager


def show_menu() -> None:
    print('\n=== Controle de Medicamentos ===')
    print('1 - Adicionar medicamento')
    print('2 - Listar medicamentos')
    print('3 - Marcar como tomado')
    print('4 - Remover medicamento')
    print('5 - Sair')


def list_tasks(manager: TaskManager) -> None:
    tasks = manager.list_tasks()
    if not tasks:
        print('\nNenhum medicamento cadastrado.')
        return

    print('\nMedicamentos cadastrados:')
    for task in tasks:
        schedule = task.get('scheduled_time') or 'Horário não definido'
        status = 'Tomado' if task['done'] else 'Pendente'
        taken_at = task.get('taken_at') or ''
        taken_info = f' | Registro: {taken_at}' if taken_at else ''
        print(f"{task['id']} - {task['title']} ({schedule}) [{status}]{taken_info}")


def main() -> None:
    manager = TaskManager()

    while True:
        show_menu()
        option = input('Escolha uma opção: ').strip()

        if option == '1':
            title = input('Digite o nome do medicamento: ')
            schedule_time = input('Digite o horário programado (HH:MM) [opcional]: ').strip()
            try:
                task = manager.add_task(title, schedule_time or None)
                print(f"Medicamento '{task['title']}' adicionado com sucesso.")
            except ValueError as error:
                print(error)

        elif option == '2':
            list_tasks(manager)

        elif option == '3':
            try:
                task_id = int(input('Digite o ID do medicamento marcado como tomado: '))
                task = manager.complete_task(task_id)
                print(f"Medicamento '{task['title']}' marcado como tomado.")
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
