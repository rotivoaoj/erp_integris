import tkinter as tk
#from database.database import criar_tabelas
from database.init_db import criar_tabelas
from ui.splash import SplashScreen
from ui.tela_principal import TelaPrincipal
from ui.styles import aplicar_estilo

# cria banco
criar_tabelas()

def centralizar_janela(root, largura=1200, altura=600):

    root.update_idletasks()  # 🔥 ESSENCIAL

    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()

    x = (screen_w // 2) - (largura // 2)
    y = (screen_h // 2) - (altura // 2)

    root.geometry(f"{largura}x{altura}+{x}+{y}")

def iniciar_sistema(root, splash, tema):

    splash.root.destroy()

    root.deiconify()
    root.overrideredirect(False)
    centralizar_janela(root, 1200, 600)

    TelaPrincipal(root, tema)

root = tk.Tk()

tema = aplicar_estilo(root)

root.withdraw()

splash = SplashScreen(root)

root.after(2500, lambda: iniciar_sistema(root, splash, tema))

root.mainloop()