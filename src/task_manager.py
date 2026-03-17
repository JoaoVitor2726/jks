from __future__ import annotations

import json
from pathlib import Path

DEFAULT_DATA_FILE = Path(__file__).resolve().parent.parent / 'data' / 'tasks.json'


class TaskManager:
    def __init__(self, data_file: Path | str | None = None) -> None:
        self.data_file = Path(data_file) if data_file else DEFAULT_DATA_FILE
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        if not self.data_file.exists():
            self._save([])

    def _load(self) -> list[dict]:
        with self.data_file.open('r', encoding='utf-8') as file:
            return json.load(file)

    def _save(self, tasks: list[dict]) -> None:
        with self.data_file.open('w', encoding='utf-8') as file:
            json.dump(tasks, file, ensure_ascii=False, indent=2)

    def add_task(self, title: str) -> dict:
        title = title.strip()
        if not title:
            raise ValueError('A tarefa não pode estar vazia.')

        tasks = self._load()
        task = {
            'id': self._next_id(tasks),
            'title': title,
            'done': False,
        }
        tasks.append(task)
        self._save(tasks)
        return task

    def list_tasks(self) -> list[dict]:
        return self._load()

    def complete_task(self, task_id: int) -> dict:
        tasks = self._load()
        for task in tasks:
            if task['id'] == task_id:
                task['done'] = True
                self._save(tasks)
                return task
        raise ValueError('Tarefa não encontrada.')

    def remove_task(self, task_id: int) -> dict:
        tasks = self._load()
        for index, task in enumerate(tasks):
            if task['id'] == task_id:
                removed = tasks.pop(index)
                self._save(tasks)
                return removed
        raise ValueError('Tarefa não encontrada.')

    @staticmethod
    def _next_id(tasks: list[dict]) -> int:
        if not tasks:
            return 1
        return max(task['id'] for task in tasks) + 1
