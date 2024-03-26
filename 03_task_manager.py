import mysql.connector

class TaskManager:
    def __init__(self, host, username, password, database):
        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='taskmanager'
        )
        self.cursor = self.db.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INT AUTO_INCREMENT PRIMARY KEY, task_name VARCHAR(255), due_date DATE)")

    def add_task(self, task_name, due_date):
        sql = "INSERT INTO tasks (task_name, due_date) VALUES (%s, %s)"
        val = (task_name, due_date)
        self.cursor.execute(sql, val)
        self.db.commit()
        print("Task added successfully")

    def view_tasks(self):
        self.cursor.execute("SELECT * FROM tasks")
        tasks = self.cursor.fetchall()
        if not tasks:
            print("No tasks found")
        else:
            for task in tasks:
                print(task)

    def update_task(self, task_id, new_task_name, new_due_date):
        sql = "UPDATE tasks SET task_name = %s, due_date = %s WHERE id = %s"
        val = (new_task_name, new_due_date, task_id)
        self.cursor.execute(sql, val)
        self.db.commit()
        print("Task updated successfully")

    def delete_task(self, task_id):
        sql = "DELETE FROM tasks WHERE id = %s"
        val = (task_id,)
        self.cursor.execute(sql, val)
        self.db.commit()
        print("Task deleted successfully")

    def close_connection(self):
        self.cursor.close()
        self.db.close()

def main():
    task_manager = TaskManager("localhost", "yourusername", "yourpassword", "task_manager")

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task_manager.add_task(task_name, due_date)
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to update: "))
            new_task_name = input("Enter new task name: ")
            new_due_date = input("Enter new due date (YYYY-MM-DD): ")
            task_manager.update_task(task_id, new_task_name, new_due_date)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            task_manager.delete_task(task_id)
        elif choice == "5":
            print("Exiting program")
            task_manager.close_connection()
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
