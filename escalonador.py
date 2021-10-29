# Escalonamento de tarefas
import ordenador
from random import randint
# A função escalonar, que colocará somente as tarefas compatíveis.
def escalonar(lista):

    # Passamos a lista como parâmetro para a função ordenador, que ficará responsável por organizar
    # em ordem não-decrescente todas as tarefas, em função de tempo final. 
    listaOrdenada = ordenador.ordenador(lista)

    # Declaramos uma lista vazia para armazenar futuramente os valores obtidos do processo mais abaixo.
    listaFinal = []
    
    # Definimos a primeira tarefa como uma referência na hora de comparar.
    tarefaBase = listaOrdenada[0]
    listaFinal.append(tarefaBase)

    # No laço abaixo, estamos comparando as tarefas seguintes da lista, com a tarefa referência
    # caso o começo dela seja igual ou maior ao final da tarefa referência, ela passa no teste
    # e entra para a lista final. Assim sendo, as que não forem compatíveis são desprezadas.
    for i in range(1, len(listaOrdenada), 1):
        if(tarefaBase.fim <= listaOrdenada[i].inicio):
            listaFinal.append(listaOrdenada[i])
            tarefaBase = listaOrdenada[i]
    
    # Abaixo percorremos a lista e gravamos os resultados finalistas.

    # Aqui damos o nome ao arquivo
    numero = randint(0,10000000)

    # Aqui é o caminho onde salvaremos o arquivo com os dados gravados
    arquivo = open("escalonados/" + str(numero) + ".txt", "w")

    # Abrimos o arquivo que será responsável por armazenar quantos elementos foram escalonados dessa vez
    execucoes = open("dados.txt", "a")

    # Aqui é o laço para salvarmos o as tarefas selecionadas
    for i in range(0, len(listaFinal), 1):
        arquivo.write("A tarefa: " + listaFinal[i].nome + "\nCom início em: " + str(listaFinal[i].inicio) + "\nE final em: " + str(listaFinal[i].fim) + "\n\n")
    
    # Aqui terminamos de gravar os dados e em seguida fechamos o acesso ao arquivo
    execucoes.write(str(len(listaFinal)) + " ")
    execucoes.close()

    # Aqui fechamos o arquivo responsável peloas tarefas selecioandas
    print("Gravando as palavras selecionadas no arquivo!")
    arquivo.close()