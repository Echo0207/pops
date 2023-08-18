import tkinter as tk
from tkinter import messagebox
import os

class App:
    def __init__(self, root):
        self.root = root
        self.refusals = 0
        self.create_main_window()

    def create_main_window(self, message="老闆我明天可以請假嗎?"):
        self.main_window = tk.Toplevel(self.root)
        self.main_window.title("go on leave")
    
        # Add this line to set the icon for your window
        self.main_window.iconbitmap('myicon.ico') 

        self.main_window.configure(bg='#ffffff')
        self.main_window.protocol('WM_DELETE_WINDOW', self.disable_event)  
    
        # Center the window on the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (300 / 2)  # 300 寬度
        y = (screen_height / 2) - (150 / 2)  # 150 高度
        self.main_window.geometry(f'300x150+{int(x)}+{int(y)}')

        self.message_label = tk.Label(self.main_window, text=message, bg='#ffffff', font=("MINGLIU", 10))
        self.message_label.pack(pady=20)
    
        button_frame = tk.Frame(self.main_window, bg='#ffffff')
        button_frame.pack(pady=10)
    
        accept_btn = tk.Button(button_frame, text="同意批假", command=self.accept, bg='#fe8082', fg='white', width=10)
        accept_btn.grid(row=0, column=0, padx=10)

        decline_btn = tk.Button(button_frame, text="拒絕", command=self.decline, bg='#c0c0c0', fg='white', width=10)
        decline_btn.grid(row=0, column=1, padx=10)


    def disable_event(self):
        pass  

    def accept(self):
        if self.message_label.cget("text").startswith("將在"):
            self.root.after_cancel(self.shutdown_id)  # 取消定時器
            messagebox.showinfo("取消關機", "您的電腦不會被關機。")
        else:
            messagebox.showinfo("老闆你好帥!!!", "好人一生平安!!!")
    
        self.main_window.destroy()
        self.root.quit()  




    def decline(self):
        self.main_window.destroy()
        self.refusals += 1

        if self.refusals == 1:
            self.create_main_window("求求你了 回頭請你喝酒")
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
