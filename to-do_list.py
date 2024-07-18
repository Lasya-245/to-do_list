#TASK 1

import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        # Initialize tasks list
        self.tasks = []
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header label
        self.header_label = ttk.Label(self.main_frame, text="Welcome to To-Do List App", font=("Helvetica", 18, "bold"), padding=(0, 10))
        self.header_label.grid(row=0, column=0, columnspan=4)
        
        # Task listbox and scrollbar
        self.task_listbox = tk.Listbox(self.main_frame, width=60, height=10, font=("Helvetica", 12))
        self.task_listbox.grid(row=1, column=0, columnspan=4, pady=20)
        
        self.scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.task_listbox.yview)
        self.scrollbar.grid(row=1, column=4, sticky="ns")
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        
        # Buttons
        self.add_button = ttk.Button(self.main_frame, text="Add Task", width=15, command=self.add_task)
        self.add_button.grid(row=2, column=0, padx=5, pady=10)
        
        self.complete_button = ttk.Button(self.main_frame, text="Mark Complete", width=15, command=self.mark_complete)
        self.complete_button.grid(row=2, column=1, padx=5, pady=10)
        
        self.delete_button = ttk.Button(self.main_frame, text="Delete Task", width=15, command=self.delete_task)
        self.delete_button.grid(row=2, column=2, padx=5, pady=10)
        
        self.exit_button = ttk.Button(self.main_frame, text="Exit", width=15, command=self.root.quit)
        self.exit_button.grid(row=2, column=3, padx=5, pady=10)
        
        # Load tasks from file
        self.load_tasks()
        self.update_task_listbox()
    
    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter task:")
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_listbox()
            self.save_tasks()
    
    def mark_complete(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks[index]["completed"] = True
            self.update_task_listbox()
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as complete.")
    
    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self.update_task_listbox()
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")
    
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_name = f"[{'X' if task['completed'] else ' '}] {task['task']}"
            self.task_listbox.insert(tk.END, task_name)
    
    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(f"{task['task']},{task['completed']}\n")
    
    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                for line in f:
                    task_info = line.strip().split(',')
                    self.tasks.append({"task": task_info[0], "completed": task_info[1] == "True"})
        except FileNotFoundError:
            pass  # No saved tasks yet

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
