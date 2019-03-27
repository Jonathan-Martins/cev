'''
Conversor básico de temperatura
'''
def main():    
    while True:
        try:
            C = int(input("Informe a temperatura em graus ºC: "))
        except ValueError as e:
            print(f'Valor inválido {e}')
            
        op = menu()
        if op != 0:
            if op == 1:
                far = fahrenheit(C)
                print(f'{C} em ºF são {far}')
                op = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
                if op not in 'sn':
                    print('Resposta inválida! Responda apenas sim ou não')
                else:
                    if op == 'n':
                        print('Adeus...')
                        break
            elif op == 2:
                kel = kelvin(C)
                print(f'{C} em K são {kel}')
                op = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
                if op not in 'sn':
                    print('Resposta inválida! Responda apenas sim ou não')
                else:
                    if op == 'n':
                        print('Adeus...')
                        break
        else:
            print('Já vai?')
            break    

def menu():
    '''
    Menu da aplicação
    '''    
    itens = {1: 'Fahrenheit', 2: 'Kelvin', 0: 'Sair'}
    for k, v in itens.items():
        print(f'{k}: {v}')
    op = int(input("Qual unidade de medida? "))
    
    if op in itens:
        return op    

def fahrenheit(grau):
    '''
    Converte de Graus Celsius (ºC) em Fahrenheit (ºF)
    '''
    F = (grau * 9/5) + 32
    return F

def kelvin(grau):
    '''
    Converte de graus Celsius (ºC) em Kelvin (K)
    '''
    K = grau + 273.15
    return K

if __name__ == '__main__':
    main()