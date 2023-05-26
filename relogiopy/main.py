import tkinter as tk
from tkinter import *
import os
from time import strftime, gmtime

root = tk.Tk()
root.title('Relógio Python')
root.geometry('700x500')
root.configure(background = '#ffffff')

def get_saudacao(): #1ºfuncao
    nome_usuario = 'Alunos do Sesi' #nome do login do usuário do windows
    saudacao.config(text = 'Olá, ' + nome_usuario)

def get_data():
    data_atual = strftime('%a, %d %b %Y')
    data.config(text=data_atual)
def get_horas():
    hora_atual = strftime('%H:%M:%S')
    horas.config(text=hora_atual)
    horas.after(1000, get_horas)

def get_horas_fuso(fuso_horario, label):
    hora_fuso = strftime('%H:%M:%S', gmtime(fuso_horario * 3600))
    label.config(text=hora_fuso)
    label.after(1000, lambda: get_horas_fuso(fuso_horario, label))

def select_fuso_horario(fuso_horario, label):
    get_horas_fuso(fuso_horario, label)

tela = tk.Canvas(root, width=650, height=60, bg='#ffffff', bd=0, highlightthickness=0, relief='ridge')
tela.pack()
saudacao = Label(root, bg='#ffffff', fg='#8e27ea', font=('Lato', 18))
saudacao.pack() #p retornar na tela
data = Label(root, bg='#ffffff', fg='#8e27ea', font=('Lato', 16))
data.pack(pady=2)
horas = Label(root, bg='#ffffff', fg='#8e27ea', font=('Lato', 68, 'bold'))
horas.pack(pady=2)
get_saudacao()
get_data()
get_horas()


# Ícone para selecionar os fusos horários
fuso_icon = PhotoImage(file='mund.png')  # Substitua 'mund.png' pelo caminho do ícone desejado
fuso_button = Button(root, image=fuso_icon, bg='#ffffff', bd=0, command=lambda: toggle_fusos_horarios())
fuso_button.image = fuso_icon  # Manter a referência da imagem original
fuso_button.pack()

fusos_horarios_visiveis = False

def toggle_fusos_horarios():
    global fusos_horarios_visiveis

    if fusos_horarios_visiveis:
        fusos_horarios_visiveis = False
        fuso1_label.pack_forget()
        fuso2_label.pack_forget()
        fuso3_label.pack_forget()
    else:
        fusos_horarios_visiveis = True
        select_fuso_horario(-3, fuso1_label)
        select_fuso_horario(1, fuso2_label)
        select_fuso_horario(-5, fuso3_label)

# Fuso horário 1: GMT-3 (Brasília)
fuso1_label = Label(root, bg='#ffffff', fg='#8e27ea', font=('Lato', 16))
fuso1_label.pack(pady=2)

# Fuso horário 2: GMT+1 (Londres)
fuso2_label = Label(root, bg='#ffffff', fg='#8e27ea', font=('Lato', 16))
fuso2_label.pack(pady=2)

# Fuso horário 3: GMT-5 (Nova York)
fuso3_label = Label(root, bg='#ffffff', fg='#8e27ea', font=('Lato', 16))
fuso3_label.pack(pady=2)

root.mainloop() #p deixar a janela aberta