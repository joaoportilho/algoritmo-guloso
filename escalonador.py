# Escalonamento de tarefas
import ordenador

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
    
    # Abaixo percorremos a lista e mostramos os resultados finalistas.
    print("As tarefas que foram escalonadas são:\n")

    for i in range(0, len(listaFinal), 1):
        print("A tarefa: " + listaFinal[i].nome + "\nCom início em: " + str(listaFinal[i].inicio) + "\nE final em: " + str(listaFinal[i].fim) + "\n\n")