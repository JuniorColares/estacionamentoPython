import os

class Veiculo:
    def __init__(self, tipo, valor, placa, modelo, data, hentrada, mentrada, hsaida = 0, total = 0, status = 'ESTACIONADO'):
        self.__tipo = tipo
        self.__valor = valor
        self.__placa = placa
        self.__modelo = modelo
        self.__data = data
        self.__hentrada = hentrada
        self.__mentrada = mentrada
        self.__hsaida = hsaida
        self.__total = total
        self.__status = status
    
    def mostraVeiculo(self):
        print(f'\nTipo: {self.__tipo}')
        print(f'Placa: {self.__placa}')
        print(f'Modelo: {self.__modelo}')
        print(f'Entrada: {self.__hentrada}:{self.__mentrada:02.0f}')
        print(f'Status: {self.__status}')

    def registraSaida(self, hsaida):
        self.__hsaida = hsaida
        htotal = self.__hsaida - self.__hentrada
        total = htotal*self.__valor
        self.__status = 'VEÍCULO SAIU DO ESTACIONAMENTO'
        return total

def inicial():
    print('****************************************')    
    print('*       Estacionamento Infinity        *')
    print('*                                      *')
    print('*          Tabela de Preços            *')
    print('*                                      *')
    print('*   (1) Moto     - R$ 2.00 a fração    *')
    print('*   (2) Carro    - R$ 5.00 a fração    *')
    print('*   (3) Caminhão - R$ 8.00 a fração    *')
    print('*   (4) Ver listagem de veículos       *')
    print('*   (5) Procurar veículos              *')
    print('*   (6) Registrar saída                *')
    print('*   (0) Sair                           *')
    print('*                                      *')
    print('****************************************')

lista = []

while True:
    t = 'n'
    os.system('cls' if os.name == 'nt' else 'clear')
    inicial()
    var = int(input('Informe a opção desejada: '))
    if var == 1:
        tipo = 'moto'
        valor = 2.0
    elif var == 2:
        tipo = 'carro'
        valor = 5.0
    elif var == 3:
        tipo = 'caminhão'
        valor = 8.0
    elif var == 4:
        for veic in lista:
            veic.mostraVeiculo()  
            t = 's'
        if t == 'n':
            print('Nenhum veículo encontrado!')  
        a = input('')
        continue
    elif var == 5:
        pesquisa = input('Informe a placa do veículo: ')
        for veic in lista:
            if pesquisa == veic.placa:
                veic.mostraVeiculo()
                t = 's'
            if t == 'n':
                print('Nenhum veículo encontrado!')
        a = input('')
        continue
    elif var == 6:
        pesquisa = input('Informe a placa do veículo: ')
        for veic in lista:
            if pesquisa == veic.placa:
                hsaida = int(input('Informe a hora da saída: '))
                msaida = int(input('Informe os minutos de saída: '))
                if msaida > 0:
                    hsaida += 1
                total = veic.registraSaida(hsaida)
                print(f'O valor total a pagar é de R$: {total:.2f}')
                t = 's'
            if t == 'n':
                print('Nenhum veículo encontrado!')
        a = input('')
        continue
        
    elif var == 0:
        break
    else:
        print('Opção inválida!')
        continue

    placa = input(f'Informe a placa do(a) {tipo}: ')
    modelo = input(f'Qual o modelo: ')
    data = input('Data entrada (dd/mm): ')
    hentrada = int(input('Informe a hora da entrada: '))
    mentrada = int(input('Informe os minutos de entrada: '))
    
    veiculo = Veiculo(tipo, valor, placa, modelo, data, hentrada, mentrada)
    lista.append(veiculo)

