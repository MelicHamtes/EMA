from Banco_dados import Banco_dados

bd = Banco_dados()
bd.conectar()


iterador = True
while iterador == True:
    print('o que deseja fazer?\n1: inserir deck\n2: inserir card\n3: deletar card\n4: puxar card\n5: puxar deck\n 6 listar deck')
    resposta = int(input())
    if resposta == 1:
        entrada = str(input('insira o nome do deck\n'))
        bd.inserir_deck(entrada)
    elif resposta == 2:
        n_deck = int(input())
        entrada1 = str(input('insira a frente \n'))
        entrada2 = str(input('insira o verso\n'))
        bd.inserir_card(entrada1, entrada2, n_deck, 1)
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
        print(bd.listar_decks(), type(bd.listar_decks()))

    resposta2 = input('Deseja continuar?\n')
    if resposta2.upper() == 'S':
        pass
    elif resposta2.upper() == 'N':
        break




    
