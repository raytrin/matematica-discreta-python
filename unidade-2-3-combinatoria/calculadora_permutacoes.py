def fatorial(numero):
    """Calcula o fatorial de um número n!"""

    if numero < 0:
        raise ValueError("O fatorial não está definido para números negativos")
    
    if numero in (0, 1):
        return 1

    resultado = 1
    for n in range(2, numero + 1):
        resultado *= n

    return resultado

def permutacao(n):
   """Calcula permutação simples P(n) = n!"""

   return fatorial(n)

def permutacao_circular(n):
   """Calcula permutação circular (n-1)!"""

   if n <= 0:
        raise ValueError("O número de elementos deve ser positivo")   

   return fatorial(n - 1)

def permutacao_elementos_repetidos(palavra):
    """
    Calcula permutação com elementos repetidos: n! / (a! * b! * ...)
    onde n = total de elementos, 
    a,b,... = frequências dos elementos repetidos
    """

    if not palavra:
        return 0

    # Calcula a frquência de cada caractere
    processados = [] 
    denominador = 1
    
    for letra in palavra:
        if letra not in processados:
            freq = palavra.count(letra)
            if freq > 1:
                denominador *= fatorial(freq)
            processados.append(letra)
    
    return fatorial(len(palavra)) // denominador

# Menu do usuário
def menu():
    """Cria o menu de opções"""

    print("-" * 5, "CALCULADORA", "-" * 5)
    
    print("\n1 - Fatorial (n!)")
    print("2 - Permutação simples (P(n))")
    print("3 - Permutação circular ((n-1)!)")
    print("4 - Permutação com repetição (n!/a!b!...)")
    print("0 - Sair")
    opcao = input("\nDigite uma opção: ")

    if opcao == "1":
        try:
            num = int(input("Digite o número: "))
            print(f"O resultado é: {fatorial(num)}.")    
        except ValueError:
            print("\nDigite um número válido, por favor!")
    
    elif opcao == "2":
        try:
            num = int(input("Digite o número: "))
            print(f"\nO resultado é: {permutacao(num)}.")    
        except ValueError:
            print("Digite um número válido, por favor!")
    
    elif opcao == "3":
        try:
            num = int(input("Digite o número de elementos: "))
            print(f"\nO resultado é: {permutacao_circular(num)}.")    
        except ValueError:
            print("Digite um número válido, por favor!")
    
    elif opcao == "4":
        palavra = input("Digite a palavra: ").strip()
        if palavra:
            print(f"\nO resultado é: {permutacao_elementos_repetidos(palavra)}.")    
        else:
            print("Digite uma palavra válida, por favor!")
    
    elif opcao == "0":
        print("Saindo da calculadora...")
        return False
    
    else:
        print("Opção inválida!")

    return True

# Loop principal
def main():
    """Função principal do programa"""

    while True:
        if not menu():
            break

        input("\nDigite 'Enter' para continuar...")   


if __name__ == "__main__":
    main()
    
