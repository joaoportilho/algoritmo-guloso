import tarefas
import escalonador
from random import randint

# Definindo a lista para enviarmos ao sistema.
listaTeste = []

# Declarando as quatro tarefas que precisaremos escalonar.
tarefa1 = tarefas.Tarefa()
tarefa2 = tarefas.Tarefa()
tarefa3 = tarefas.Tarefa()
tarefa4 = tarefas.Tarefa()

# Estamos atribuindo valores a elas, fazendo propositalmente com que existem choques entre elas.
tarefa1.nome = "Divisão"
tarefa1.inicio = 1
tarefa1.fim = 3

tarefa2.nome = "Multiplicação"
tarefa2.inicio = 3
tarefa2.fim = 5

tarefa3.nome = "Raíz quadrada"
tarefa3.inicio = 6
tarefa3.fim = 9

tarefa4.nome = "Outra conta"
tarefa4.inicio = 2
tarefa4.fim = 6

# Estamos adicionando todas elas a uma lista.
listaTeste.append(tarefa1)
listaTeste.append(tarefa4)
listaTeste.append(tarefa2)
listaTeste.append(tarefa3)

# Chamamos a função escalonar para que todo o processo seja de fato executado.
escalonador.escalonar(listaTeste)