from Banco_dados import Banco_dados

bd = Banco_dados()
bd.conectar()


iterador = True
while iterador == True:
    print('o que deseja fazer?\n1: inserir deck\n2: inserir card\n3: deletar card\n4: puxar card\n5: puxar deck\n 6 listar deck\n 7 puxar codigod deck \n 8 alterar card')
    resposta = int(input())
    if resposta == 1:
        entrada = str(input('insira o nome do deck\n'))
        bd.inserir_deck(entrada)
    elif resposta == 2:
        codigo_deck = int(input('insira o código do deck:\n'))
        entrada1 = str(input('insira a frente \n'))
        entrada2 = str(input('insira o verso\n'))
        bd.inserir_card(entrada1, entrada2, codigo_deck)
    elif resposta == 3:
        n_card = int(input('insira numero do card\n'))
        n_deck = int(input('insira numero do deck\n'))
        bd.deletar_card(n_card)
        print(bd.puxar_deck(codigo_deck))
    elif resposta == 4:
        n_card = int(input('numero do card\n'))
        bd.puxar_card(n_card)
    elif resposta == 5:
        n_deck = int(input())
        print(bd.puxar_deck(n_deck))
    elif resposta == 6:
        print(bd.listar_decks(1), type(bd.listar_decks(1)))
    elif resposta == 7:
        nome_deck = input()
        print(bd.puxar_codigo_deck(nome_deck))
    elif resposta == 8:
        frente_card = input('Digite a frente:\n')
        codigo = bd.puxar_codigo_card(frente_card)
        frente_novo = input('Digite a nova frente:\n')
        verso_novo = input('Digite o novo verso:\n')
        bd.alterar_card(codigo, frente_novo, verso_novo)
        print(bd.puxar_card(codigo))
    elif resposta == 9:
        frente = input('Digite a frente:\n')
        c =bd.puxar_codigo_card(frente)
        print(bd.puxar_card(c))
 
    resposta2 = input('Deseja continuar?\n')
    if resposta2.upper() == 'S':
        pass
    elif resposta2.upper() == 'N':
        break




    
