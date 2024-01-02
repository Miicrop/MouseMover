import pyautogui as pag
import random
import time
import customtkinter
import threading


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x312")
        
        self.resolution_x_min = 1
        self.resolution_y_min = 1
        self.resolution_x_max = 1920
        self.resolution_y_max = 1080
        self.reset_time = 180
        self.app_is_running = False
        self.current_time = time.time()
        
        self.grid_columnconfigure(0, weight=1)
        
        
        self.button_frame = customtkinter.CTkFrame(self)
        self.button_frame.grid(row=0, column=0, columnspan=3, sticky="nsew")
        self.button_frame.grid_columnconfigure((0,1,2), weight=1)
        
        self.entry_frame = customtkinter.CTkFrame(self)
        self.entry_frame.grid(row=1, column=0, columnspan=4, sticky="nsew")
        self.entry_frame.grid_columnconfigure((0,1,2,3), weight=1)

        
        self.button_start = customtkinter.CTkButton(self.button_frame, text="Start", command=self.start_thread)
        self.button_start.grid(row=0, column=0, padx=10, pady=30)
        
        self.run_info = customtkinter.CTkLabel(self.button_frame, text="Press Start to run App")
        self.run_info.grid(row=0, column=1, padx=10, pady=30)
        
        self.button_stop = customtkinter.CTkButton(self.button_frame, text="Stop", command=self.stop)
        self.button_stop.grid(row=0, column=2, padx=10, pady=30)


        self.label0 = customtkinter.CTkLabel(self.entry_frame, text="Timer(s):")
        self.label0.grid(row=0, column=0, padx=10, pady=(50,10))
        self.entry0 = customtkinter.CTkEntry(self.entry_frame, placeholder_text="180")
        self.entry0.grid(row=0, column=1, padx=10, pady=(50,10))
        
        self.button = customtkinter.CTkButton(self.entry_frame, text="Save Settings", command=self.set_values)
        self.button.grid(row=0, column=2, padx=10, pady=(50,10))
        
        self.label1 = customtkinter.CTkLabel(self.entry_frame, text="Resolution X Min:")
        self.label1.grid(row=1, column=0, padx=10, pady=(50,10))
        self.entry1 = customtkinter.CTkEntry(self.entry_frame, placeholder_text="1")
        self.entry1.grid(row=1, column=1, padx=10, pady=(50,10))

        self.label2 = customtkinter.CTkLabel(self.entry_frame, text="Resolution X Max:")
        self.label2.grid(row=1, column=2, padx=10, pady=(50,10))
        self.entry2 = customtkinter.CTkEntry(self.entry_frame, placeholder_text="1920")
        self.entry2.grid(row=1, column=3, padx=10, pady=(50,10))

        self.label3 = customtkinter.CTkLabel(self.entry_frame, text="Resolution Y Min:")
        self.label3.grid(row=2, column=0, padx=10, pady=10)
        self.entry3 = customtkinter.CTkEntry(self.entry_frame, placeholder_text="1")
        self.entry3.grid(row=2, column=1, padx=10, pady=10)

        self.label4 = customtkinter.CTkLabel(self.entry_frame, text="Resolution Y Max:")
        self.label4.grid(row=2, column=2, padx=10, pady=10)
        self.entry4 = customtkinter.CTkEntry(self.entry_frame, placeholder_text="1080")
        self.entry4.grid(row=2, column=3, padx=10, pady=10)

    def start_thread(self):
        threading.Thread(target=self.start).start()

    def start(self):
        self.app_is_running = True
        self.update_label("App is currently running")
        self.run()
    
    def stop(self):
        self.update_label("App is stopped")
        self.app_is_running = False
    
    def update_label(self, input):
        self.run_info.configure(text=input)
        
    def set_values(self):
        if self.entry1.get() != "":
            self.resolution_x_min = int(self.entry1.get())
        if self.entry3.get() != "":
            self.resolution_y_min = int(self.entry3.get())
        if self.entry2.get() != "":
            self.resolution_x_max = int(self.entry2.get())
        if self.entry4.get() != "":
            self.resolution_y_max = int(self.entry4.get())
        if self.entry0.get() != "":
            self.reset_time = int(self.entry0.get())
        
    
    def run(self):
        while self.app_is_running:
            if time.time() - self.current_time > self.reset_time:
                x = random.randint(self.resolution_x_min, self.resolution_x_max)
                y = random.randint(self.resolution_y_min, self.resolution_y_max)
                pag.moveTo(x, y, 0.5)
                self.current_time = time.time()

app = App()
app.mainloop()



