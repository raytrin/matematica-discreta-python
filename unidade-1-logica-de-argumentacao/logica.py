def treinar_negacao():
    """O usuário digita uma proposição e sua negação. O programa verifica se a resposta está correta."""

    negacao = {
        "p": "¬p",
        "¬p": "p",
        "p∧q": "¬pv¬q",
        "p^q": "¬pv¬q",
        "pvq": "¬p∧¬q",
        "p->q": "p∧¬q",
        "p->q": "p^¬q",
        "p<->q": "(p∧¬q) v (¬pvq)"
    }

    while True:
        proposicao = input("\nProposição (ex: p -> q): ").strip().lower().replace(" ", "")
        negacao_proposicao = input("Digite a negação: ").strip().lower().replace(" ", "")    

        if proposicao in negacao:
            if negacao[proposicao] == negacao_proposicao:
                print("\nAcertou! Parabéns!")
                   
                    
            else:
                print("\nErrou! Tente novamente.")
                print(f"Resposta correta: {negacao[proposicao]}")  


            while True:
                print("\n1 - tentar novamente")
                print("2 - sair")
                resposta = input("Digite uma das opções acima: ")

                if resposta == "1":
                    break
                elif resposta == "2":
                    return
                else:
                    print("Selecione uma opção válida!")
                
        else:
            print("Digite uma proposição válida!")


def modo_programador():
    """Recebe uma proposição lógica e mostra sua equivalência e como seria escrita em Python."""

    traducao = {
        "p∧q": "p and q",
        "p^q": "p and q",
        "pvq": "p or q",
        "p->q": "not p or q",
        "p<->q": "p == q"
    }
      
    equivalencias = {
        "p->q": "¬p v q",
        "p∧q": "¬(¬p v ¬q)",
        "p^q": "¬(¬p v ¬q)",  
        "pvq": "¬(¬p ∧ ¬q)", 
        "p<->q": "(p ∧ q) v (¬p ∧ ¬q)"
    }


    print("\nExemplos aceitos: p ∧ q, p ^ q, p v q, p -> q, p <-> q")
    proposicao = input("\nDigite a proposição: ").strip().lower().replace(" ", "")

    if proposicao in traducao:
        print(f"\nPython: {traducao[proposicao]}")
        print(f"Equivalência: {equivalencias[proposicao]}")
    else:
        print("Proposição inválida.")
      

def quiz():
    import random

    equivalencia = { 
    "p -> q": "¬pvq",
    "p ∧ q": "¬(¬pv¬q)",
    "p ^ q": "¬(¬pv¬q)",  
    "p v q": "¬(¬p∧¬q)", 
    "p <-> q": "(p∧q) v (¬p∧¬q)",
    "¬p v q": "p->q",
    "¬(¬p v ¬q)": "p∧q",
    "¬(¬p ∧ ¬q)": "pvq",
    "(p ∧ q) v (¬p ∧ ¬q)": "p<->q"
    }

    negacao = {
    "p": "¬p",
    "¬p": "p",
    "p ∧ q": "¬pv¬q",
    "p v q": "¬p∧¬q",
    "p v q": "¬p^¬q",
    "p -> q": "p∧¬q",
    "p <-> q": "(p∧¬q)v(¬pvq)"
    }

    nome_conectivo = {
        "p ∧ q": "conjunção",
        "p v q": "disjunção",
        "p -> q": "implicação",
        "p <-> q": "bicondicional"
    }

    pontuacao = 0
    print("\n" + "*" * 30)
    print("        QUIZ DE LÓGICA")
    print("*" * 30)

    while True:

        negacao_aleatoria = random.choice(list(negacao.keys()))
        equiv_aleatoria = random.choice(list(equivalencia.keys())) 
        conectivo_aleatorio = random.choice(list(nome_conectivo.keys())) 

        resp_equivalencia = input(f"\nDigite a equivalência lógica de {equiv_aleatoria}: \n").strip().lower() 

        if resp_equivalencia.replace(" ", "") == equivalencia[equiv_aleatoria].replace(" ", ""):
            print("\nAcertou! Parabéns!")
            pontuacao += 1
        else:
            print("\nErrou! Tente novamente.")
            print(f"Resposta correta: {equivalencia[equiv_aleatoria]}")


        resp_negacao = input(f"\nDigite a negação da proposição {negacao_aleatoria}: \n")
        if resp_negacao.replace(" ", "") == negacao[negacao_aleatoria].replace(" ", ""): 
            print("Acertou! Parabéns!")

            pontuacao += 1
        else:
            print("\nErrou! Tente novamente.")
            print(f"Resposta correta: {negacao[negacao_aleatoria]}")


        resp_conectivo = input(f"\nDigite o conectivo correspondente do símbolo '{conectivo_aleatorio}': \n")

        if resp_conectivo.replace(" ", "") == nome_conectivo[conectivo_aleatorio].replace(" ", ""):
            print("Acertou! Parabéns!")
            pontuacao += 1
        else:
            print("\nErrou! Tente novamente.") 
            print(f"Resposta correta: {nome_conectivo[conectivo_aleatorio]}")

        while True:
            opcao = input("\nContinuar jogando (s/n): ").lower() 
            if opcao == "n":
                print(f"\nVocê fez {pontuacao} pontos!")
                return
            elif opcao == "s":
                break
            else:
                print("Digite uma opção válida!")
                continue


def tabela_verdade():
    """Exibe tabela verdade de disjunção, conjunção, implicação e bicondicional """
        
    print("\n--------- TABELA VERDADE ---------")
        
    expressao = input("\nDigite a proposição (ex.: p and q): ")
       
    combinacoes = [(True, True), (True, False), (False, True), (False, False)]

    print(f"{"\n p":<10} | {"q":^10} | {expressao:>10}")

    print("-" * 38)
    for value in combinacoes:
        p, q = value
        if expressao == "p and q":
            result = p and q

            print(f"{str(p):<10} | {str(q):^10} | {str(result):>10} |")
            print("-" * 38)
            
        elif expressao == "p or q":
            result = p or q
            
            print(f"{str(p):<10} | {str(q):^10} | {str(result):>10} |")
            print("-" * 38)
            
        elif expressao == "not p or q":  
            result = not p or q
                 
            print(f"{str(p):<10} | {str(q):^10} | {str(result):>10} |")
            print("-" * 38)
            
        elif expressao == "p == q":  
            result = p == q
            print(f"{str(p):<10} | {str(q):^10} | {str(result):>10} |")
            print("-" * 38)  
                


def menu():
    """Exibe um menu com opções para as funções do programa"""

    while True:
        print("\n" + "*" * 35)
        print("             MENU")
        print("*" * 35) 
        print("\n1 - Treinar negação de proposições")
        print("2 - Modo programador")
        print("3 - Quiz de lógica")
        print("4 - Gerar tabela verdade")
        print("0 - Sair")

        opcao = input("\nDigite uma opção: ")

        if opcao == "1":
            treinar_negacao()
        elif opcao == "2":
            modo_programador()
        elif opcao == "3":
            quiz()
        elif opcao == "4":
            tabela_verdade()
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida!")
        


menu()
