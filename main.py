import tkinter as tk
from tkinter import *
import os
from time import strftime, gmtime
from datetime import datetime, timedelta, timezone

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

# Define uma função chamada get_horas_fuso que recebe dois argumentos: fuso_horario e label
def get_horas_fuso(fuso_horario, label):
    # Cria um objeto datetime representando a hora atual em UTC
    agora = datetime.utcnow()

    # Cria um objeto timedelta representando o deslocamento de tempo para o fuso horário especificado
    fuso = timedelta(hours=fuso_horario)

    # Converte a hora atual em UTC para a hora correspondente no fuso horário especificado
    hora_fuso = agora.replace(tzinfo=timezone.utc).astimezone(timezone(fuso))

    # Converte o objeto datetime hora_fuso em uma string formatada
    hora_fuso = hora_fuso.strftime('%H:%M:%S')

    # Atualiza o texto do widget label com a hora formatada no fuso horário especificado
    label.config(text=hora_fuso)

    # Aguarda 1000 milissegundos (1 segundo) e chama a função get_horas_fuso novamente com os mesmos argumentos fuso_horario e label
    # Isso faz com que a hora exibida no widget label seja atualizada a cada segundo
    # A chamada da função é feita usando a função after() do widget label, que aguarda um determinado número de milissegundos antes de executar a função especificada (no caso, a função get_horas_fuso)
    # O argumento lambda: é usado para criar uma função anônima que chama a função get_horas_fuso com os mesmos argumentos, permitindo que a função seja chamada novamente de forma recursiva
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
fuso_icon = PhotoImage(file=r'C:\Users\Aluno\Desktop\relogiopy\mund.png')
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