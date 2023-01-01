import sqlite3


def init_database():
    conn = sqlite3.connect('W5/todo.sqlite3')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            priority INTEGER NOT NULL
        );
    ''')

    conn.commit()
    conn.close()


class Task:
    def __init__(
        self,
        title: str,
        description: str,
        priority: int
    ) -> None:
        self.title = title
        self.description = description
        self.priority = priority
    
    def __dict__(self):
        return {
            'title': self.title,
            'description': self.description,
            'priority': self.priority
        }


class TaskRepository:
    def __init__(self) -> None:
        self.connection = sqlite3.connect('W5/todo.sqlite3') 

    def create_task(self, task: Task):
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute(
                '''
                INSERT INTO tasks (title, description, priority)
                VALUES (?, ?, ?)
                ''', 
                (task.title, task.description, task.priority)
            )
            conn.commit()

    def create_many_tasks(self, tasks: list[Task]):
        with self.connection as conn:
            cur = conn.cursor()
            cur.executemany('''
                INSERT INTO tasks (title, description, priority)
                VALUES (?, ?, ?)
            ''', [dict(task).values() for task in tasks]
            )      
            conn.commit()

    def get_all_tasks(self):
        with self.connection as conn:
            cur = conn.cursor()
            rows = cur.execute('SELECT * FROM tasks')
        
        return rows

    def find_task_by_title(self, title: str):
        with self.connection as conn:
            cur = conn.cursor()
            rows = cur.execute(f"SELECT * FROM tasks WHERE title = ?", (title, ))
            rows.fetchone()

        return row

    def update_task_description(self, task_id: int, description: str) -> None:
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute('UPDATE tasks SET description = ? WHERE id = ?', (description, task_id))
            conn.commit()

    def delete_task(self, task_id: int) -> None:
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
            conn.commit()


if __name__ == '__main__':
    init_database()

    repo = TaskRepository()

    task = Task('Lau bàn', '', 1)

    repo.create_task(task)

    for row in repo.get_all_tasks():
        print(row)

    # Find task
    rec = repo.find_task_by_title('Lau bàn')

    print()
    print(rec)

    # Udpate task
    rec = repo.find_task_by_title('Lau bàn')
    repo.update_task_description(rec[0], 'New description')

    repo.delete_task(1)
