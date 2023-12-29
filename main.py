import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random


# Carregar o arquivo excel
df = pd.read_excel('questions.xlsx')
df2 = pd.read_excel('tipo_perguntas.xlsx') 

#Pegar as perguntas aleatoriamente
questions = df.sample(n=10).values.tolist()
tipo_perguntas = df.sample(n=4).values.tolist()


df3 = pd.DataFrame(questions, columns=["Pergunta", "opcao1", "opcao2", "opcao3", "opcao4", "resposta", "tipo_perguntas"])
tipo_1_df = df3[df3['tipo_perguntas'] == 1]
tipo_2_df = df3[df3['tipo_perguntas'] == 2]
tipo_3_df = df3[df3['tipo_perguntas'] == 3]
tipo_4_df = df3[df3['tipo_perguntas'] == 4]

perguntas_tipo_1 = tipo_1_df.sample(n=2).values.tolist()
perguntas_tipo_2 = tipo_2_df.sample(n=2).values.tolist()
perguntas_tipo_3 = tipo_3_df.sample(n=2).values.tolist()
perguntas_tipo_4 = tipo_4_df.sample(n=2).values.tolist()

# variaveis globais
score = 0
current_questions = 0


def display_types():
    
    questions_label.config(text="Qual tipo de pergunta? ")
    
    option1_btn.config(text="Entretenimento", state=tk.NORMAL, command=lambda:(selecionar_tipo_1(perguntas_tipo_1), random.shuffle(perguntas_tipo_1)))
    option2_btn.config(text="Artes", state=tk.NORMAL, command=lambda:(selecionar_tipo_1(perguntas_tipo_2),random.shuffle(perguntas_tipo_2)))
    option3_btn.config(text="Ciencia", state=tk.NORMAL, command=lambda:(selecionar_tipo_1(perguntas_tipo_3),random.shuffle(perguntas_tipo_3)))
    option4_btn.config(text="Esportes", state=tk.NORMAL, command=lambda:(selecionar_tipo_1(perguntas_tipo_4),random.shuffle(perguntas_tipo_4)))


def selecionar_tipo_1(perguntas_tipo_1):
    
    question, option1, option2, option3, option4, answer, tipo = perguntas_tipo_1[current_questions]
    questions_label.config(text=question)

    option1_btn.config(text=option1, state=tk.NORMAL, command=lambda:check_answer(1))
    option2_btn.config(text=option2, state=tk.NORMAL, command=lambda:check_answer(2))
    option3_btn.config(text=option3, state=tk.NORMAL, command=lambda:check_answer(3))
    option4_btn.config(text=option4, state=tk.NORMAL, command=lambda:check_answer(4))
    
    
    currect_answer.set(answer)


def check_answer(answer):

    if answer == currect_answer.get():
        show_result_correct()
        
    else:
        show_result_wrong(current_questions)


def embaralha_questoes(perguntas_tipo_1):
    random.shuffle(perguntas_tipo_1)


def show_result_correct():
    current_questions+1
    messagebox.showinfo("Resposta certa",f"Parabéns Resposta correta")
    option1_btn.config(state=tk.DISABLED)
    option2_btn.config(state=tk.DISABLED)
    option3_btn.config(state=tk.DISABLED)
    option4_btn.config(state=tk.DISABLED)

    play_again_btn.pack()


def show_result_wrong(answer):
    current_questions+1
    messagebox.showinfo("Resposta errada",f"Resposta incorreta, a resposta certa é {answer}")
    option1_btn.config(state=tk.DISABLED)
    option2_btn.config(state=tk.DISABLED)
    option3_btn.config(state=tk.DISABLED)
    option4_btn.config(state=tk.DISABLED)

    play_again_btn.pack()
    


#funcao para jogar novamente 
def play_again():
    random.shuffle(questions)
    option1_btn.config(state=tk.NORMAL)
    option2_btn.config(state=tk.NORMAL)
    option3_btn.config(state=tk.NORMAL)
    option4_btn.config(state=tk.NORMAL)

    play_again_btn.pack_forget()
    display_types()



#Configurando janela
janela = tk.Tk()
janela.title('Quiz')
janela.geometry('400x450')

#Definindo variaveis de cores 
background_color = "#ECECEC"
text_color = "#333333"
button_color = "#4CAF50"
button_text_color = "#FFFFFF"

janela.config(bg=background_color)
janela.option_add('*Font', 'Arial')


# Icon na tela
app_icon =PhotoImage(file="perguntadoslogo.png")
fator_reducao = 4
app_icon = app_icon.subsample(fator_reducao, fator_reducao)
app_label = tk.Label(janela, image=app_icon, bg=background_color)
app_label.pack(pady=10)


# Componentes da interface
questions_label = tk.Label(janela, text="" ,wraplength=380, bg=background_color, fg=text_color, font=("Arial",12,"bold"))
questions_label.pack(pady=20)


currect_answer = tk.IntVar()


option1_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option1_btn.pack(pady=10)

option2_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option2_btn.pack(pady=10)

option3_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option3_btn.pack(pady=10)

option4_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option4_btn.pack(pady=10)


play_again_btn = tk.Button(janela,command=play_again, text="Jogar novamente", width=30, bg=button_color, fg=button_text_color, font=("Arial", 10, "bold"))
#play_again_btn.pack(pady=10)


display_types()


janela.mainloop()