import tkinter as tk
from tkinter import ttk, messagebox
import os

class App:
    def __init__(self, root):
        self.root = root
        self.refusals = 0
        self.create_main_window()

    def create_main_window(self, message="晚上喝酒嗎?"):
        self.main_window = tk.Toplevel(self.root)
        self.main_window.title("go on drink")
        self.main_window.resizable(False, False)
        self.main_window.protocol('WM_DELETE_WINDOW', self.disable_event)  
        
        text_frame = ttk.Frame(self.main_window)
        text_frame.pack(pady=20)
        self.message_label = ttk.Label(text_frame, text=message)
        self.message_label.pack()
        
        button_frame = ttk.Frame(self.main_window)
        button_frame.pack(pady=10)
        
        accept_btn = ttk.Button(button_frame, text="喝起來", command=self.accept)
        accept_btn.grid(row=0, column=0, padx=10)

        decline_btn = ttk.Button(button_frame, text="打咩", command=self.decline)
        decline_btn.grid(row=0, column=1, padx=10)

        self.center_window(self.main_window)

    def center_window(self, window):
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def disable_event(self):
        pass  

    def accept(self):
        if self.message_label.cget("text").startswith("將在"):
            self.root.after_cancel(self.shutdown_id)  # 取消定時器
            messagebox.showinfo("取消關機", "您的電腦不會被關機。")
        else:
            messagebox.showinfo("讚啦!!!", "讚啦 我們晚上見!!!")
        
        self.main_window.destroy()
        self.root.quit()  

    def decline(self):
        self.main_window.destroy()
        self.refusals += 1

        if self.refusals == 1:
            self.create_main_window("快啦 今天缺酒精")
        elif self.refusals == 2:
            self.create_main_window("不然我還可以介紹妹子給你")
        elif self.refusals == 3:
            self.create_main_window("嗚嗚 你真的忍心拒絕我嗎oTATo")
        elif self.refusals == 4:
            self.create_shutdown_warning() 
        else:
            self.shutdown_immediately()  # 第五次拒絕後立即關機

    def create_shutdown_warning(self):
        self.create_main_window("將在20秒後將您的電腦關機")
        self.seconds_left = 20
        self.update_countdown()
        self.shutdown_id = self.root.after(20000, self.shutdown_immediately)

    def update_countdown(self):
        self.seconds_left -= 1
        self.message_label.config(text=f"將在{self.seconds_left}秒後將您的電腦關機")
        if self.seconds_left > 0:
            self.root.after(1000, self.update_countdown)

    def shutdown_immediately(self):
        os.system("shutdown -s -t 1")
        self.root.quit()  # 關機後終止應用

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # 隱藏父窗口
    app = App(root)
    root.mainloop()
