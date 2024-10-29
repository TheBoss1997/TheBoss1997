def counting_sort(lista):
    # Passo 1: Encontrar o valor máximo na lista
    max_val = max(lista)
    
    # Passo 2: Criar um array de contagem
    count = [0] * (max_val + 1)
    
    # Passo 3: Contar as ocorrências de cada elemento
    for num in lista:
        count[num] += 1
        
    # Passo 4: Reconstruir a lista ordenada
    sorted_lista = []
    for i in range(len(count)):
        sorted_lista.extend([i] * count[i])
    
    return sorted_lista

# Exemplo de uso com uma lista totalmente desordenada
lista_desordenada = [34, 11, 64, 12, 90, 22, 25, 22]
lista_ordenada = counting_sort(lista_desordenada)
print(lista_desordenada)  # Imprime a lista desordenada


