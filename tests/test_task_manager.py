from pathlib import Path

import pytest

from src.task_manager import TaskManager


@pytest.fixture
def manager(tmp_path: Path) -> TaskManager:
    return TaskManager(tmp_path / 'tasks.json')


def test_add_task_successfully(manager: TaskManager) -> None:
    task = manager.add_task('Revisar lógica de programação')

    assert task['id'] == 1
    assert task['title'] == 'Revisar lógica de programação'
    assert task['done'] is False
    assert len(manager.list_tasks()) == 1


def test_add_task_with_empty_title_raises_error(manager: TaskManager) -> None:
    with pytest.raises(ValueError, match='A tarefa não pode estar vazia.'):
        manager.add_task('   ')


def test_remove_nonexistent_task_raises_error(manager: TaskManager) -> None:
    with pytest.raises(ValueError, match='Tarefa não encontrada.'):
        manager.remove_task(99)


def test_complete_task_changes_status(manager: TaskManager) -> None:
    task = manager.add_task('Estudar testes automatizados')
    completed = manager.complete_task(task['id'])

    assert completed['done'] is True
    assert manager.list_tasks()[0]['done'] is True
