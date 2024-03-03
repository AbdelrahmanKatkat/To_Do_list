# File: main.py
# Purpose: Main script for the to-do list application using Tkinter.

import tkinter as tk

class TodoApp:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List App")

        # Create GUI components
        self.task_entry = tk.Entry(master, width=30)
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.task_listbox = tk.Listbox(master, selectmode=tk.SINGLE)

        # Pack GUI components
        self.task_entry.pack(pady=10)
        self.add_button.pack()
        self.task_listbox.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
