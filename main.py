import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random

# Carregar o arquivo excel
df = pd.read_excel('questions.xlsx')

#Pegar as perguntas aleatoriamente
questions = df.sample(n=10).values.tolist()

# variaveis globais
score = 0
current_questions = 0

# funcao para exibir proxima pergunta
#Essa funcao basicamente vai mudar a estrutura dos objetos que criamos la em baixo
#Exemplo pega o text='' e muda para text='question'  
def display_question():
    question, option1, option2, option3, option4, answer = questions[current_questions]
    # Define a pergunta da vez, mudando o text da nossa variavel la de baixo para receber o question como
    questions_label.config(text=question)

    option1_btn.config(text=option1, state=tk.NORMAL, command=lambda:check_answer(1))
    option2_btn.config(text=option2, state=tk.NORMAL, command=lambda:check_answer(1))
    option3_btn.config(text=option3, state=tk.NORMAL, command=lambda:check_answer(1))
    option4_btn.config(text=option4, state=tk.NORMAL, command=lambda:check_answer(1))

    currect_answer.set(answer)


# funcao para verificar a resposta
def check_answer(answer):
    global score, current_questions

    if answer == currect_answer.get():
        score += 1

    current_questions += 1

    if current_questions < len(questions):
        display_question()
    else:
        show_result()

def show_result():
    messagebox.showinfo("Quiz Finalizado", f"Parabéns! Voce completou o Quiz. \n\n Fontuação final: {score}")
    option1_btn.config(state=tk.DISABLED)
    option2_btn.config(state=tk.DISABLED)
    option3_btn.config(state=tk.DISABLED)
    option4_btn.config(state=tk.DISABLED)
    play_again_btn.pack()

#funcao para jogar novamente 
def play_again():
    global score, current_questions
    score = 0
    current_questions = 0
    random.shuffle(questions)

    option1_btn.config(state=tk.NORMAL)
    option2_btn.config(state=tk.NORMAL)
    option3_btn.config(state=tk.NORMAL)
    option4_btn.config(state=tk.NORMAL)

    play_again_btn.pack_forget()



#print(questions)


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
app_icon =PhotoImage(file="icons8-quiz-100.png")
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



display_question()

janela.mainloop()