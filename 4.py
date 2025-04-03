def dinamic_programing_backpack(N, C, items):
    max_tab = [[0] * (C + 1) for _ in range(N + 1)]
    iterations = 0
    
    for i in range(1, N + 1):
        peso, valor = items[i]
        for j in range(1, C + 1):
            iterations += 1 
            if peso <= j:
                max_tab[i][j] = max(max_tab[i - 1][j], valor + max_tab[i - 1][j - peso])
            else:
                max_tab[i][j] = max_tab[i - 1][j]
    
    return max_tab[N][C], iterations

# values de entrada
C = 165
weights = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
values = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
items = [(0, 0)] + list(zip(weights, values))
N = len(items) - 1

# Executando a função
result, iterations = dinamic_programing_backpack(N, C, items)
print("resultado: ", result)
print("iteracoes", iterations)