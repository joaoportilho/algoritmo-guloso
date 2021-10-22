# A função abaixo tem a tarefa de ordenar de forma não-decrescente a nossa lista
# de tarefas.
def ordenador(lista):

    # Novamente estamos declarando dois arrays vazios para nos auxiliar no resto do código.
    array = []
    listaRetorno = []
    # Neste ponto, pegamos o tempo final da tarefa e adicionamos em uma lista que será ordenada
    # a ideia é simplesmente ordenar os tempos finais, e adicionar em outra lista, as tarefas completas
    # já ordenadas.
    for i in range(0, len(lista), 1):
        array.append(lista[i].fim)
    
    # O array ordenado mencionado acima, usado para armazenar os valores já ordenados.
    arrayOrdenado = sorted(array)
    
    # Variável de índice para nosso laço, para diferir de i.
    ind = 0

    # No laço abaixo, estamos simplesmente pegando os tempos ordenados e colocando
    # a primeira tarefa correspondente a ele.
    for ind in range(0, len(arrayOrdenado), 1):
        for i in range(0, len(arrayOrdenado), 1):
            if(arrayOrdenado[ind] == lista[i].fim):
                print("Ordenando...")
                listaRetorno.append(lista[i])
                ind+1
    # Retornamos a lista já arrumadinha pra ser usada no escalonador.
    return listaRetorno
 