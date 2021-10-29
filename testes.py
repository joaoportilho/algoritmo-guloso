# Arquivo para efetuar as 10000 execuções para testes
import tarefas
import escalonador
from random import randint

for i in range(0, 100, 1):
    # Executando pela n vez
    print("Executando pela " + str(i+1) + "vez!")

    # Definindo a lista para enviarmos ao sistema.
    listaTeste = []

    # Aleatoriamente criando as tarefas para enviar ao algoritmo de escalonamento
    for j in range(0, 10000, 1):
        tarefaAux  = tarefas.Tarefa()
        tarefaAux.nome = "Tarefa" + str(j)
        tarefaAux.inicio = randint(0,10000)
        tarefaAux.fim = tarefaAux.inicio + randint(3, 40)
        listaTeste.append(tarefaAux)
    
    # Aqui estamos escalonando as tarefas geradas aleatoriamente
    escalonador.escalonar(listaTeste)
    print("Finalizando a " + str(i+1) + "vez!")

    # Aqui estamos limpando a lista depois do uso
    listaTeste.clear()
