import threading  # 1
import time


def main():
    threads = [
        threading.Thread(target=contar, args=('elefante', 10)),  # 2
        threading.Thread(target=contar, args=('buraco', 8)),
        threading.Thread(target=contar, args=('moeda', 23)),
        threading.Thread(target=contar, args=('pato', 12)),
    ]

    [th.start() for th in threads]  # Adiciona a nossa thread na pool de threads prontas para a execução #3

    print('Podemos fazer outras coisas no programa enquanto a thread vai executando....')

    print('Geek' * 2)

    [th.join() for th in threads]  # Avisa para ficar aguardando aqui até a thread terminar a execução #4

    print('pronto')


def contar(o_que, numero):
    for n in range(1, numero + 1):
        print(f'{n} {o_que}(s)...')
        time.sleep(1)


if __name__ == '__main__':
    main()
