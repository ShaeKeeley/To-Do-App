import tkinter as tk

# WINDOW
window = tk.Tk()
window.title("To Do App")
window.geometry("200x200")

#ADDING TASK
def addTask():
    Task = task.get()
    if task:
        taskList.insert(tk.END, Task)
        task.delete(0, tk.END)
        

#REMOVING TASK
def removeTask():
    selectTask = taskList.curselection()
    if selectTask:
        taskList.delete(selectTask)


#WIDGETS IN WINDOW
label = tk.Label(window, text="Add task:")
task = tk.Entry(window)
button1 = tk.Button(window, text="Add task", command=addTask)
button2 = tk.Button(window, text="Remove task", command=removeTask)
taskList = tk.Listbox(window)

label.pack()
task.pack()
button1.pack()
button2.pack()
taskList.pack()

window.mainloop()