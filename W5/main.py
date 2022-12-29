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
        pass

    def create_task(self, task: Task):
        with sqlite3.connect('W5/todo.sqlite3') as conn:
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
        with sqlite3.connect('W5/todo.sqlite3') as conn:
            cur = conn.cursor()
            cur.executemany('''
                INSERT INTO tasks (title, description, priority)
                VALUES (?, ?, ?)
            ''', [dict(task).values() for task in tasks]
            )      
            conn.commit()

    def get_all_tasks(self):
        with sqlite3.connect('W5/todo.sqlite3') as conn:
            cur = conn.cursor()
            rows = cur.execute('SELECT * FROM tasks')
        
        return rows


if __name__ == '__main__':
    init_database()

    repo = TaskRepository()

    task = Task('Quét nhà', '', 1)

    repo.create_task(task)

    for row in repo.get_all_tasks():
        print(row)
