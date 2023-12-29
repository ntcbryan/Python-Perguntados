import pandas as pd 

#Lista de perguntas
"""
Tipos de perguntas são separados pelos numeros(ultimo campo) a seguir:

    Entretenimento = 1
    Ciência = 2
    Artes = 3
    Esporte = 4

"""
questions = [

    ["Qual filme ganhou o Oscar de Melhor Filme em 2020?", "Parasita", "1917", "Coringa", "Era Uma Vez em Hollywood", 1, 1],
    ["Quem é o protagonista da série 'Breaking Bad'?", "Walter White", "Jesse Pinkman", "Saul Goodman", "Hank Schrader", 1, 1],
    ["Qual é o último livro da série 'Harry Potter'?", "As Relíquias da Morte", "O Prisioneiro de Azkaban", "A Ordem da Fênix", "O Enigma do Príncipe", 1, 1],


    ["Quem pintou a Mona Lisa?", "Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet", 1, 2],
    ["Qual é a técnica artística de Pablo Picasso?", "Cubismo", "Impressionismo", "Realismo", "Surrealismo", 1, 2],
    ["Quem é o autor da obra 'Dom Quixote'?", "Miguel de Cervantes", "William Shakespeare", "Charles Dickens", "Jane Austen", 1, 2],

    
    ["O que é a teoria da relatividade de Einstein?", "Teoria da relatividade restrita", "Teoria da gravidade", "Teoria da evolução", "Teoria da luz", 1, 3],
    ["Quem foi o primeiro homem a pisar na lua?", "Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "John Glenn", 1, 3],
    ["Qual é a fórmula química da água?", "H2O", "CO2", "O2", "CH4", 1, 3],

    
    ["Qual país sediou a Copa do Mundo de 2018?", "Rússia", "Alemanha", "Brasil", "França", 1, 4],
    ["Quem é considerado o melhor jogador de futebol de todos os tempos?", "Pelé", "Lionel Messi", "Cristiano Ronaldo", "Diego Maradona", 1, 4],
    ["Em que esporte Michael Phelps se destacou nos Jogos Olímpicos?", "Natação", "Atletismo", "Ciclismo", "Ginástica", 1, 4]
]




# questions = [
#     ["Qual é a capital da França?", "Paris", "Londres", "Berlim", "Roma", 1,1],
#     ["Qual é o resultado de 8 + 5?", "12", "13", "15", "18", 2,2],
#     ["Quem pintou a Mona Lisa?", "Picasso", "Da Vinci", "Van Gogh", "Warhol", 2,1],
#     ["Quanto é 6 multiplicado por 7?", "36", "42", "48", "54", 2,2],
#     ["Qual é o maior planeta do sistema solar?", "Marte", "Saturno", "Júpiter", "Vênus", 3,1],
#     ["Quem escreveu a obra 'Dom Quixote'?", "Machado de Assis", "Miguel de Cervantes", "Jorge Luis Borges", "Gabriel García Márquez", 2,2],
#     ["Qual é a fórmula química da água?", "H2O", "CO2", "NaCl", "CH4", 1],
#     ["Quem foi o primeiro presidente dos Estados Unidos?", "George Washington", "Abraham Lincoln", "Thomas Jefferson", "John F. Kennedy", 1,1],
#     ["Qual é o resultado de 4 ao cubo?", "16", "32", "64", "128", 3,2],
#     ["Qual é a capital da Rússia?", "Moscou", "São Petersburgo", "Kiev", "Varsóvia", 1,1],
#     ["Quem descobriu a teoria da relatividade?", "Isaac Newton", "Galileu Galilei", "Albert Einstein", "Nikola Tesla", 3,2],
#     ["Qual é o símbolo químico do ouro?", "Au", "Ag", "Cu", "Fe", 1,1],
#     ["Quem foi o autor da obra 'Romeu e Julieta'?", "William Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen", 1,1],
#     ["Qual é a capital do Brasil?", "Rio de Janeiro", "Brasília", "São Paulo", "Salvador", 2,2],
#     ["Qual é o resultado de 9 dividido por 3?", "1", "2", "3", "4", 3,1],
#     ["Quem pintou a obra 'A Noite Estrelada'?", "Leonardo da Vinci", "Michelangelo", "Salvador Dalí", "Vincent van Gogh", 4,2],
#     ["Qual é o maior oceano do mundo?", "Atlântico", "Índico", "Pacífico", "Ártico", 3,1],
#     ["Qual é o resultado de 2 elevado a 8?", "8", "16", "64", "256", 4,2],
#     ["Quem escreveu a obra '1984'?", "George Orwell", "Aldous Huxley", "Ernest Hemingway", "F. Scott Fitzgerald", 1,1],
#     ["Qual é o resultado de 15 menos 7?", "5", "6", "7", "8", 3,2],
#     ["Quem foi o pintor do quadro 'A Última Ceia'?", "Pablo Picasso", "Salvador Dalí", "Michelangelo", "Leonardo da Vinci", 4,1]
#





tipo_perguntas = [
    ["Entretenimento",1],
    ["Ciência",2],
    ["Artes", 3],
    ["Esporte", 4]
]

# criar dataframe do pandas 
df = pd.DataFrame(questions, columns=["Perguntas","Opcao1","Opcao2","Opcao3","Opcao4","Resposta","TipoPergunta"])
df2 = pd.DataFrame(tipo_perguntas, columns=["Categoria","id_categoria"])


# Salvar no arquivo excel 
df.to_excel("questions.xlsx", index=False)
df2.to_excel("tipo_perguntas.xlsx", index=False)


print("perguntas salvas com sucesso")