import customtkinter
import os
from PIL import Image
import store
import task

SUBJECTS = ["Math", "English", "Science"]
PRIORITY = ["Low", "Medium", "High"]

current_dir = os.path.dirname(os.path.abspath(__file__))
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class ScrollableLabelButtonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.label_list = []
        self.button_list = []

    def add_item(self, item):
        if item.priority == "Low":
            image=customtkinter.CTkImage(Image.open(os.path.join(current_dir, "images", "green.png")))
        elif item.priority == "Medium":
            image=customtkinter.CTkImage(Image.open(os.path.join(current_dir, "images", "yellow.png")))
        elif item.priority == "High":
            image=customtkinter.CTkImage(Image.open(os.path.join(current_dir, "images", "red.png")))
        label = customtkinter.CTkLabel(self, text=str(item), image=image, compound="left", font=("Arial", 14), justify="left", padx=10, pady=5)
        button = customtkinter.CTkButton(self, text="Edit")
        if self.command is not None:
            button.configure(command=lambda: self.command(item))
        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        button.grid(row=len(self.button_list), column=1, pady=(0, 10), padx=5)
        self.label_list.append(label)
        self.button_list.append(button)

    def remove_item(self, item):
        for label, button in zip(self.label_list, self.button_list):
            if str(item) == label.cget("text"):
                label.destroy()
                button.destroy()
                self.label_list.remove(label)
                self.button_list.remove(button)
                return
    
    # def open_input_dialog_event(self):
    #     input_dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="Status")
    #     if input_dialog != None:
    #         App.change_status_event(input_dialog)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("ToDo")
        self.geometry(f"{800}x{500}")

        self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.scrollable_label_button_frame = ScrollableLabelButtonFrame(master=self, width=500, command=self.label_button_frame_event, corner_radius=0)
        self.scrollable_label_button_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        for item in data.tasks:
            if item.status != "100":
                self.scrollable_label_button_frame.add_item(item)
        

        self.new_task_frame = customtkinter.CTkFrame(self)
        self.new_task_frame.grid(row=0, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.label_new_task_group = customtkinter.CTkLabel(master=self.new_task_frame, text="Create New Task:")
        self.label_new_task_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")

        self.title_input = customtkinter.CTkEntry(master=self.new_task_frame, placeholder_text="Title")
        self.title_input.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.subject_optionmenu = customtkinter.CTkOptionMenu(master=self.new_task_frame, values=SUBJECTS)
        self.subject_optionmenu.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.dueDate_input = customtkinter.CTkEntry(master=self.new_task_frame, placeholder_text="Due Date (mm-dd)")
        self.dueDate_input.grid(row=3, column=2, pady=10, padx=20, sticky="n")
        self.dueTime_input = customtkinter.CTkEntry(master=self.new_task_frame, placeholder_text="Due Time")
        self.dueTime_input.grid(row=4, column=2, pady=10, padx=20, sticky="n")
        self.priority_optionmenu = customtkinter.CTkOptionMenu(master=self.new_task_frame, values=PRIORITY)
        self.priority_optionmenu.grid(row=5, column=2, pady=10, padx=20, sticky="n")
        self.notes_input = customtkinter.CTkEntry(master=self.new_task_frame, placeholder_text="Note")
        self.notes_input.grid(row=6, column=2, pady=10, padx=20, sticky="n")
        self.done_button = customtkinter.CTkButton(master=self.new_task_frame, text="Done", command=self.new_task_event)
        self.done_button.grid(row=7, column=2, pady=10, padx=20, sticky="n")
    
    def label_button_frame_event(self, item):
        status = customtkinter.CTkInputDialog(text=item.display(), title="Status")
        status = status.get_input()
        if status != None:
            for task in data.tasks:
                if str(task) == str(item):
                    task.status = status
                    data.save()
                    if task.status == "100":
                        self.scrollable_label_button_frame.remove_item(task)
                    return
    
    def new_task_event(self):
        print("new task event")
        new_task = task.task(self.subject_optionmenu.get(), self.title_input.get(), self.dueDate_input.get(), self.dueTime_input.get(), self.priority_optionmenu.get(), "0", self.notes_input.get())
        data.addTask(new_task)
        self.scrollable_label_button_frame.add_item(new_task)
        data.save()
        self.title_input.delete(0, "end")
        self.notes_input.delete(0, "end")


if __name__ == "__main__":
    data = store.store("data.txt")
    # task1 = task.task("Math", "HW", "2023-8-21", "11:59PM", "Low", "0", "Do it")
    # task2 = task.task("English", "Essay", "2023-8-21", "12:00AM", "High", "0", "Do it")
    # data.addTask(task1)
    # data.addTask(task2)
    data.save()

    customtkinter.set_appearance_mode("dark")
    app = App()
    app.mainloop()