# Algoritmos de Ordenação

Este documento explica e demonstra diferentes algoritmos de ordenação utilizando Python, incluindo suas complexidades de tempo e exemplos de código.

## Bubble Sort

### Descrição:
O **Bubble Sort** é um algoritmo simples de ordenação que repetidamente percorre a lista, compara elementos adjacentes e os troca se estiverem na ordem errada. O processo é repetido até que a lista esteja ordenada.

### Complexidade:
- **Melhor caso**: O(n)
- **Pior caso**: O(n²)
- **Caso médio**: O(n²)

### Código em Python:
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Exemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(lista))
```

### Explicação:
No pior caso, o algoritmo faz O(n²) comparações, já que precisa verificar cada elemento com todos os outros. No melhor caso, o algoritmo pode ser mais eficiente se o array já estiver quase ordenado.


## Quick Sort

### Descrição:
O **Quick Sort** é um algoritmo de ordenação que usa o paradigma de **Divisão e Conquista**. Ele seleciona um 'pivô' e particiona a lista em duas sublistas: uma com elementos menores que o pivô e outra com elementos maiores, e depois ordena as sublistas recursivamente.

### Complexidade:
- **Melhor caso**: O(n log n)
- **Pior caso**: O(n²) (ocorre quando o pivô escolhido é o menor ou maior valor)
- **Caso médio**: O(n log n)

### Código em Python:
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivô = arr[len(arr) // 2]
        esquerda = [x for x in arr if x < pivô]
        meio = [x for x in arr if x == pivô]
        direita = [x for x in arr if x > pivô]
        return quick_sort(esquerda) + meio + quick_sort(direita)

# Exemplo de uso
lista = [10, 7, 8, 9, 1, 5]
print(quick_sort(lista))
```

### Explicação:
O Quick Sort divide o array em partes menores até que cada parte tenha 0 ou 1 elementos. Depois, junta essas partes de maneira ordenada.


## Merge Sort

### Descrição:
O **Merge Sort** é outro algoritmo de **Divisão e Conquista** que divide o array em duas metades, as ordena recursivamente e depois as combina em um array final ordenado.

### Complexidade:
- **Melhor caso**: O(n log n)
- **Pior caso**: O(n log n)
- **Caso médio**: O(n log n)

### Código em Python:
```python
def merge_sort(arr):
    if len(arr) > 1:
        meio = len(arr) // 2
        esquerda = arr[:meio]
        direita = arr[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                arr[k] = esquerda[i]
                i += 1
            else:
                arr[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            arr[k] = esquerda[i]
            i += 1
            k += 1

        enquanto j < len(direita):
            arr[k] = direita[j]
            j += 1
            k += 1

    return arr

# Exemplo de uso
lista = [12, 11, 13, 5, 6, 7]
print(merge_sort(lista))
```

### Explicação:
O Merge Sort tem complexidade O(n log n) em todos os casos, já que sempre divide o array em duas metades e depois combina as partes ordenadas.


## Insertion Sort

### Descrição:
O **Insertion Sort** funciona construindo uma lista ordenada, inserindo cada novo elemento na posição correta em relação aos elementos já ordenados.

### Complexidade:
- **Melhor caso**: O(n)
- **Pior caso**: O(n²)
- **Caso médio**: O(n²)

### Código em Python:
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i-1
        while j >= 0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
    return arr

# Exemplo de uso
lista = [12, 11, 13, 5, 6]
print(insertion_sort(lista))
```

### Explicação:
O Insertion Sort é eficiente para pequenos arrays ou arrays que já estão quase ordenados, sendo O(n) no melhor caso.


## Timsort

### Descrição

**Timsort** é um algoritmo híbrido de ordenação, que combina **Merge Sort** e **Insertion Sort**. Ele foi desenvolvido por Tim Peters em 2002 e é usado como o algoritmo padrão de ordenação em linguagens como Python e Java. A ideia principal por trás do **Timsort** é dividir a lista em pequenas sublistas chamadas "runs", que são ordenadas individualmente usando **Insertion Sort** e, em seguida, essas sublistas são mescladas usando **Merge Sort**.

O **Timsort** é altamente eficiente em listas que já estão parcialmente ordenadas, o que é uma vantagem sobre outros algoritmos de ordenação.

### Complexidade

- **Melhor Caso**: `O(n)`
- **Caso Médio**: `O(n log n)`
- **Pior Caso**: `O(n log n)`

### Vantagens
- Excelente desempenho em dados parcialmente ordenados.
- Combina o melhor de dois algoritmos eficientes: **Insertion Sort** (para pequenas listas) e **Merge Sort** (para grandes listas).
- Utilizado em bibliotecas de sorting padrão devido à sua versatilidade e eficiência.

### Implementação em Python

```python
# Definindo o tamanho mínimo dos "runs"
RUN = 32

# Função de insertion sort para pequenos arrays
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        chave = arr[i]
        j = i - 1
        while j >= left and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave

# Função merge para unir as sublistas ordenadas
def merge(arr, l, m, r):
    # Tamanho das sublistas
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    
    # Copiando dados para subarrays temporários
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l

    # Mesclando as sublistas de volta ao array original
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copiando os elementos restantes, se houver
    while i < len1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len2:
        arr[k] = right[j]
        j += 1
        k += 1

# Função principal do Timsort
def timsort(arr):
    n = len(arr)

    # Aplicando insertion sort em sublistas de tamanho RUN
    for i in range(0, n, RUN):
        insertion_sort(arr, i, min((i + RUN - 1), n - 1))

    # Começando a mesclar as sublistas
    size = RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), n - 1)

            # Fazendo o merge se houver elementos para mesclar
            if mid < right:
                merge(arr, left, mid, right)

        size = 2 * size

    return arr

# Exemplo de uso
arr = [5, 21, 7, 23, 19, 10, 15, 20, 35, 3, 12, 9, 1]
print(timsort(arr))
```

### Passos do Algoritmo

1. **Divisão em "Runs"**: O array original é dividido em várias sublistas menores (chamadas "runs") de tamanho pré-definido (geralmente 32 ou 64 elementos).
   
2. **Insertion Sort nos "Runs"**: Cada sublista é ordenada individualmente usando **Insertion Sort**. Este método é muito eficiente para listas pequenas.

3. **Mesclagem dos "Runs"**: Depois que todos os "runs" são ordenados, eles são mesclados usando o algoritmo **Merge Sort**, até que o array completo esteja ordenado.

## Selection Sort

### Descrição:
O **Selection Sort** é um algoritmo que divide o array em duas partes: a parte ordenada e a parte não ordenada. Ele seleciona o menor (ou maior) elemento da parte não ordenada e o move para a parte ordenada.

### Complexidade:
- **Melhor caso**: O(n²)
- **Pior caso**: O(n²)
- **Caso médio**: O(n²)

### Código em Python:
```python
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Exemplo de uso
lista = [64, 25, 12, 22, 11]
print(selection_sort(lista))
```

### Explicação:
Embora simples, o Selection Sort é ineficiente para grandes arrays devido à sua complexidade O(n²).
