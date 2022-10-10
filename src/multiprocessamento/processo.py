import multiprocessing

print(f'Iniciando o precesso com nome: {multiprocessing.current_process().name}')


def faz_algo(valor):
    print(f'fFazendo algo com o {valor}')


def main():
    pc = multiprocessing.Process(target=faz_algo, args=('Passáro',), name="Processo Geek")

    print(f'Iniciando o precesso com nome: {pc.name}')
    pc.start()
    pc.join()


if __name__ == '__main__':
    main()
