def counting_sort(lista):
    # Passo 1: Encontrar o valor máximo na lista
    max_val = max(lista)
    
    # Passo 2: Criar um array de contagem
    count = [0] * (max_val + 1)
    
    # Passo 3: Contar as ocorrências de cada elemento
    for num in lista:
        count[num] += 1
        
    # Passo 4: Reconstruir a lista ordenada em ordem crescente
    sorted_lista = []
    for i in range(len(count)):
        sorted_lista.extend([i] * count[i])
    
    return sorted_lista

def sort_combined_half(lista):
    # Determinar o ponto médio
    mid = len(lista) // 2
    
    # Separar as duas metades
    primeira_metade = lista[:mid]
    segunda_metade = lista[mid:]
    
    # Ordenar a primeira metade em ordem decrescente
    primeira_metade_ordenada = counting_sort(primeira_metade)[::-1]
    
    # Ordenar a segunda metade em ordem crescente
    segunda_metade_ordenada = counting_sort(segunda_metade)
    
    # Combinar as duas metades
    lista_final = primeira_metade_ordenada + segunda_metade_ordenada
    return lista_final

# Exemplo de uso
lista = [12, 11, 22, 25, 90, 64, 34, 22]  # Exemplo de lista
lista_ordenada = sort_combined_half(lista)
print(lista_ordenada)  # Imprime a lista ordenada
