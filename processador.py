#a = input("digite algo: ")

def testa_tipo():
    resp = 'y'
    while resp != 'n':
        a = input("digite algo: ")
        if a.isalpha():
            prensa = 'String'
        elif a.isnumeric():
            prensa = 'numerico'
        elif a.isalnum():
            prensa = 'alfanumerico'
            
        print('O valor de {} é do tipo {}'.format(a, prensa))
        
        denovo = input("deseja continuar? (y/n)")
        if denovo.lower() == "y":
            print("Reiniciando...")
        else:
            print("Até mais...")

    
    
    
testa_tipo()