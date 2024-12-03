# Questões de Notação Big-O

## Questão 1
- **Notação Big-O**: O(1)
- **Quantidade de Operações**: 15

---

## Questão 2
- **Notação Big-O**: O(log n)
- **Quantidade de Operações**: 22 + 14 log n (se o "else" conta)
- **Explicação**:
  O algoritmo realiza uma busca verificando se o número procurado é igual ao elemento no índice do meio de um intervalo. Caso contrário:
  - Se o número for menor, a busca continua nos índices abaixo do meio.
  - Se for maior, a busca continua nos índices acima do meio.
  O processo se repete até encontrar o número ou retornar -1 (caso o número não esteja presente).

---

## Questão 3
- **Notação Big-O**: O(n)
- **Quantidade de Operações**: 17 + 6n
- **Explicação**: O algoritmo soma os elementos de uma lista.

---

## Questão 4
- **Notação Big-O**: O(n²)
- **Quantidade de Operações**: 4n² + 4n + 1
- **Explicação**: O algoritmo utiliza laços aninhados para gerar todas as combinações ordenadas possíveis de dois índices dentro do intervalo de 0 a 𝑛−1.

---

## Questão 5
### Complexidades por Cor:
- **Lilás**: O(1)
- **Laranja**: O(n log n)
- **Lilás (outra instância)**: O(n²)
- **Amarelo**: O(n³)
- **Bege**: O(2^n)

