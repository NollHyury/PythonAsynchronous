import multiprocessing


def calcular(dado):
    return dado ** 2


def main():
    tamanho_pool = multiprocessing.cpu_count() * 2  # 3 * 2 -> 6
    
    print(f'Tamanho da Pool: {tamanho_pool}')
    
    pool = multiprocessing.Pool(processes=tamanho_pool)
    
    entradas = list(range(7))
    saidas = pool.map(calcular, entradas)
    
    print(f'Saídas: {saidas}')
    
    pool.close() # Pode começar a processar
    pool.join() # Leva os processos até o fim e espera aqui
    

if __name__ == '__main__':
    main()
   
    