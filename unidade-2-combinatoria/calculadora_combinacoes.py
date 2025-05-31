from calculadora_permutacoes import fatorial
import textwrap

def combinacao_simples(n, k):
    """
    Calcula o total de combinações possíveis  de k elementos escolhidos entre n disponíveis, sem considerar a ordem (combinação simples).
    
    Fórmula: C(n, k) = n! / (k! * (n - k)!)
    """
    
    return fatorial(n) // (fatorial(k) * fatorial(n - k))


def main():
    """Função principal do programa"""
    
    while True:
        print("\n--- CALCULADORA DE COMBINAÇÕES ---\n")

        mensagem = "Calcula o total de combinações possíveis de k elementos escolhidos entre n disponíveis, sem considerar a ordem\n (combinação simples)."

        print(textwrap.fill(mensagem, width=50))

        try:
            n = int(input("\nDigite o valor de n: "))
            k = int(input("\nDigite o valor de k: "))
        except ValueError:
            print('Por favor, digite um número inteiro.')
            return

        if k < 0 or k > n or n < 0:
            print("Entrada incorreta. Atenção: '0 <= k <= n'!")
            return
        

        print("\nO total de combinações possíveis é:", combinacao_simples(n, k), ".")

        continuar = input("\nDeseja continuar? (s/n): ")
        if continuar.lower() != 's':
            break
        
        
if __name__ == "__main__":
    main()