import calendar
import tkinter as tk
from tkinter import ttk

# Lista de meses em português
meses_portugues = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

def gerar_calendario():
    try:
        # Obtém o ano inserido pelo usuário
        ano = int(entry_ano.get())
        calendario = calendar.TextCalendar(firstweekday=0)  # Começa com domingo
        texto_calendario = ""

        # Gera o calendário mês a mês
        for mes in range(1, 13):
            texto_calendario += f"\n{meses_portugues[mes - 1]} {ano}\n"
            texto_calendario += "D  S  T  Q  Q  S  S\n"
            texto_calendario += calendario.formatmonth(ano, mes).split('\n', 2)[-1] + "\n"

        # Exibe o calendário na interface
        text_calendario.delete(1.0, tk.END)
        text_calendario.insert(tk.END, texto_calendario)
    except ValueError:
        text_calendario.delete(1.0, tk.END)
        text_calendario.insert(tk.END, "Por favor, insira um ano válido.")

# Criação da janela principal
janela = tk.Tk()
janela.title("Gerador de Calendário")
janela.geometry("600x600")
janela.configure(bg="#e8f4f8")

# Título
titulo = tk.Label(janela, text="Gerador de Calendário", font=("Arial", 18, "bold"), bg="#e8f4f8", fg="#005f6b")
titulo.pack(pady=10)

# Campo para entrada do ano
frame_ano = tk.Frame(janela, bg="#e8f4f8")
frame_ano.pack(pady=10)

label_ano = tk.Label(frame_ano, text="Digite o ano:", font=("Arial", 12), bg="#e8f4f8", fg="#005f6b")
label_ano.pack(side=tk.LEFT, padx=5)

entry_ano = ttk.Entry(frame_ano, font=("Arial", 12), width=10)
entry_ano.pack(side=tk.LEFT)

botao_gerar = tk.Button(frame_ano, text="Gerar Calendário", command=gerar_calendario, font=("Arial",10,"bold"), bg="#191970", fg="white")
botao_gerar.pack(side=tk.LEFT, padx=10)

# Área para exibir o calendário
text_calendario = tk.Text(janela, font=("Courier", 10), width=80, height=30, bg="#ADFF2F", fg="#00008B", wrap=tk.WORD)
text_calendario.pack(pady=10)

# Inicialização da janela
janela.mainloop()
