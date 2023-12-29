
#descomentar32
# funcao para exibir proxima pergunta
#Essa funcao basicamente vai mudar a estrutura dos objetos que criamos la em baixo
#Exemplo pega o text='' e muda para text='question'  
# def display_question():
#     question, option1, option2, option3, option4, answer = questions[current_questions]
#     # Define a pergunta da vez, mudando o text da nossa variavel la de baixo para receber o question como
#     questions_label.config(text=question)

#     option1_btn.config(text=option1, state=tk.NORMAL, command=lambda:check_answer(1))
#     option2_btn.config(text=option2, state=tk.NORMAL, command=lambda:check_answer(1))
#     option3_btn.config(text=option3, state=tk.NORMAL, command=lambda:check_answer(1))
#     option4_btn.config(text=option4, state=tk.NORMAL, command=lambda:check_answer(1))

#     currect_answer.set(answer)




#Comentado por que na dinamica desse jogo, não respondemos a outra pergunta e sim vamos para a tela inicial escolher outro tema
#sugestão de mudar para uma dinamica que de a resposta certa, e volte para a tela de selecionar pergunta

# funcao para verificar a resposta
# def check_answer(answer):
#     global score, current_questions

#     if answer == currect_answer.get():
#         score += 1

#     current_questions += 1

#     if current_questions < len(questions):
#         print('teste')
#         #display_question()
#     else:
#         show_result()