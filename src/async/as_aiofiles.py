import asyncio
import aiofiles


async def exemplo_arq_1():
    async with aiofiles.open('C:/Users/u56189/OneDrive - Statkraft AS/Desktop/Studies/PythonAsynchronous/src/async/texto.txt') as arquivo:
        conteudo = await arquivo.read()
    print(conteudo)


async def exemplo_arq_2():
    async with aiofiles.open('C:/Users/u56189/OneDrive - Statkraft AS/Desktop/Studies/PythonAsynchronous/src/async/texto.txt') as arquivo:
        async for linha in arquivo:
            print(linha)


def main():
    el = asyncio.get_event_loop()

    el.run_until_complete(exemplo_arq_1())
    el.close()


if __name__ == '__main__':
    main()
