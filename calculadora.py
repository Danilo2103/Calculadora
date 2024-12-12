"""

# Em andamento (82%)

# Operações de uma calculadora convencional
Soma (+) [Feito]
Subtração (-) [Feito]
Multiplicação (×) [Feito]
Divisão (÷) [Feito]
Potenciação (xⁿ) [Feito]
Raiz enésima (ⁿ√x) [Feito]
Equação do Segundo Grau [Feito]
Fatorial (n!) [Feito]
Seno (sin) [Feito]
Cosseno (cos) [Feito]
Tangente (tan) [Feito]
Módulo (|x|) [Feito]
Média [Feito]
Nota Final (Quanto preciso para passar) [Feito]
Graus ↔ Radianos (deg/rad) [Feito]
Radianos ↔ Graus (rad/deg) [Feito]
Notação científica (EXP ou E) [Feito]
Variância [Feito]
Desvio Padrão (dp) [Feito]
Logaritmo decimal (log) [Feito]
Logaritmo natural (ln) [Feito]
Porcentagem (%)


# Em andamento (0%)

Conversão de Bases:
Decimal ↔ Binário ↔ Octal ↔ Hexadecimal


# Em andamento (0%)

# Futuro
Cálculo de memória:
Adicionar à memória (M+)
Subtrair da memória (M-)
Recuperar valor da memória (MR)
Limpar memória (MC)
Igualdade (=)
Limpeza/Reset (C/AC ou CE)

"""
import os
import math

class Calculadora:
    
    def soma(self, a, b):
        return a + b
    
    def subtracao(self, a, b):
        return a - b
    
    def multiplicacao(self, a, b):
        return a * b
    
    def divisao(self, a, b):
        if b == 0:
            return "Não é possível dividir por zero"
        else:
            return a / b
          
    def raiz(self, a, b):
        if b <= 0:
            return "O índice da raiz deve ser maior que zero."
        elif a < 0 and b % 2 == 0:
            return "Não é possível calcular a raiz par de um número negativo."
        else:
            return math.pow(a, 1/b)
        
    def potenciacao(self, a, b):
        return math.pow(a, b)
        
    def fatorial(self, a):
        if a < 0:
            return "Não é possível calcular o fatorial de número negativo"
        else:
            return math.factorial(a)
    
    def seno(self, a):
        return math.sin(a)
    
    def cosseno(self, a):
        return math.cos(a)
    
    def tangente(self, a):
        return math.tan(a)
    
    def modulo(self, a):
        return abs(a)
    
    def bhaskara(self, a, b, c):
        delta = pow(b, 2) - (4 * a * c)
        
        if delta < 0:
            return "Não há solução real para a equação"
        elif delta == 0:
            x1 = -b / (2 * a)
            return f"O valor real de 𝑥 é: {x1}"
        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            return f"Os valores reais da equação são: 𝑥₁: {x1} e 𝑥₂: {x2}"
    
    def media(self, a, b):
        return (a + b) / 2
    
    def nota_necessaria(self, a, b):
        media = (a + b) / 2
        if media >= 7:
            return "Você já passou!"
        else:
            nota_final = 21 - (a + b)
            return nota_final
    
    def graus_para_radianos(self, a):
        return a * (math.pi / 180)

    def radianos_para_graus(self, a):
        return a * (180 / math.pi)
    
    def variancia(self, a):
        if len(a) == 0:
            return 0
        
        media = sum(a) / len(a)
        
        soma_quadrados = sum((x - media) ** 2 for x in a)
        
        return soma_quadrados / len(a)
    
    def notacao_cientifica(self, a):
        if a == 0:
            return "0 * 10^0"
        
        expoente = math.floor(math.log10(abs(a)))
        
        mantissa = a / (10 ** expoente)
        
        return f"{mantissa:.6f} * 10^{expoente}"

    def dp(self, a):
        variancia = self.variancia(a)  # Calcula a variância
        return math.sqrt(variancia)
    
    def logaritmo_comum(self, numero):
        if numero <= 0:
            return "Erro: O número deve ser maior que zero para calcular logaritmos."
        return math.log10(numero)
        
    def logaritmo_natural(self, numero):
        if numero <= 0:
            return "Erro: O número deve ser maior que zero para calcular logaritmos."
        return math.log(numero)
    
    def logs(self):
        # Solicita ao usuário que insira um número
        try:
            numero = float(input("Digite o número para calcular os logaritmos: "))
        except ValueError:
            return "Erro: Por favor, insira um número válido."
    
        log_comum = self.logaritmo_comum(numero)
        log_natural = self.logaritmo_natural(numero)
        
        # Exibindo os resultados
        if isinstance(log_comum, str):
            return log_comum
        if isinstance(log_natural, str):
            return log_natural
        
        return (f"Logaritmo comum (base 10) de {numero}: {log_comum}\n"
                f"Logaritmo natural (base e) de {numero}: {log_natural}")
    
    # Função para calcular aumento de porcentagem
    def aumento_porcentagem(self, valor_inicial, porcentagem):
        novo_valor = valor_inicial * (1 + (porcentagem / 100))
        return novo_valor

    # Função para calcular diminuição de porcentagem
    def diminuicao_porcentagem(self, valor_inicial, porcentagem):
        novo_valor = valor_inicial * (1 - abs(porcentagem / 100))
        return novo_valor

    # Função principal para interagir com o usuário
    def porcentagem(self):
        try:
            # Solicitar ao usuário o valor inicial e a porcentagem
            valor_inicial = float(input("Digite o valor inicial: "))
            porcentagem = float(input("Digite a porcentagem (use valor positivo para aumento e negativo para diminuição): "))
        except ValueError:
            return "Erro: Por favor, insira números válidos."

        # Calcular o aumento ou diminuição de porcentagem
        if porcentagem > 0:
            novo_valor = self.aumento_porcentagem(valor_inicial, porcentagem)
            return f"O valor após o aumento de {porcentagem}% é: {novo_valor}"
        elif porcentagem < 0:
            novo_valor = self.diminuicao_porcentagem(valor_inicial, porcentagem)
            return f"O valor após a diminuição de {abs(porcentagem)}% é: {novo_valor}"
        else:
            return "A porcentagem não pode ser zero."
    
def limpar_terminal():
    # Comando para limpar o terminal, dependendo do sistema operacional
    sistema = os.name
    if sistema == 'nt':  # Windows
        os.system('cls')
    else:  # Linux ou macOS
        os.system('clear')
   
def main():
    calc = Calculadora()
    limpar_terminal()
    
    while True:
        print("\n| Calculadora Bombril |\n")
        print("- Cardápio -")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Raiz")
        print("6. Potenciação")
        print("7. Fatorial")
        print("8. Seno")
        print("9. Cosseno")
        print("10. Tangente")
        print("11. Módulo")
        print("12. Bhaskara")
        print("13. Média")
        print("14. Quanto preciso na prova final?")
        print("15. Graus para radianos")
        print("16. Radianos para graus")
        print("17. Variância")
        print("18. Converter em Notação Científica")
        print("19. Desvio Padrão")
        print("20. Logaritmo Comum e Logaritmo Natural")
        print("21. Porcentagem")
        print("0. Sair\n")
        escolha = input("Digite o número referente a operação que deseja realizar: ")
        
        if escolha == '0':
            print("Saindo...")
            break
        
        if escolha in ['1', '2', '3', '4', '6', '13']:
            limpar_terminal()
            a = float(input("Digite o primeiro valor: "))
            b = float(input("Digite o segundo valor: "))
        elif escolha in ['8', '9', '10', '11', '18']:
            limpar_terminal()
            a = float(input("Digite o valor: "))
            
        if escolha == '1':
            print("Resultado:", calc.soma(a, b))
        elif escolha == '2':
            print("Resultado:", calc.subtracao(a, b))
        elif escolha == '3':
            print("Resultado:", calc.multiplicacao(a, b))
        elif escolha == '4':
            print("Resultado:", calc.divisao(a, b))
        elif escolha == '5':
            limpar_terminal()
            a = float(input("Digite o valor do radicando: "))
            b = float(input("Digite o valor do índice da raiz: "))
            print("Resultado:", calc.raiz(a, b))
        elif escolha == '6':
            print("Resultado:", calc.potenciacao(a, b))
        elif escolha == '7':
            limpar_terminal()
            try:
                a = input("Digite o valor: ")
                a = float(a)    # Converte pra float
                if a.is_integer():  # Verifica se o número é inteiro
                    a = int(a)  # Converte pra int
                    print(f"O fatorial de {a} é: {calc.fatorial(a)}")
                else:
                    print("Erro: O fatorial só pode ser calculado para números inteiros.")
            except ValueError:
                print("Erro: Por favor, digite um número válido.")
            except Exception as e:
                print(f"Erro inesperado: {e}")
        elif escolha == '8':
            print("Resultado:", calc.seno(a))
        elif escolha == '9':
            print("Resultado:", calc.cosseno(a))
        elif escolha == '10':
            print("Resultado:", calc.tangente(a))
        elif escolha == '11':
            print("Resultado:", calc.modulo(a))
        elif escolha == '12':
            limpar_terminal()
            a = float(input("Digite o primeiro valor: "))
            b = float(input("Digite o segundo valor: "))
            c = float(input("Digite o terceiro valor: "))
            print("Resultado:", calc.bhaskara(a, b, c))
        elif escolha == '13':
            print("Resultado:", calc.media(a, b))
        elif escolha == '14':
            limpar_terminal()
            a = float(input("Digite a nota da AV1: "))
            b = float(input("Digite a nota da AV2: "))
            print("Resultado:", calc.nota_necessaria(a, b))
        elif escolha == '15':
            limpar_terminal()
            a = float(input("Digite o valor em graus: "))
            print("Resultado:", calc.graus_para_radianos(a))
        elif escolha == '16':
            limpar_terminal()
            a = float(input("Digite o valor em radianos: "))
            print("Resultado:", calc.radianos_para_graus(a))
        elif escolha == '17':
            limpar_terminal()
            a = input("Digite os valores em graus, separados por espaço: ")
            lista_de_valores = [int(x) for x in a.split()]
            print("Resultado:", calc.variancia(lista_de_valores))
        elif escolha == '18':
            print("Resultado:", calc.notacao_cientifica(a))
        elif escolha == '19':
            limpar_terminal()
            a = input("Digite os valores separados por espaço: ")
            try:
                lista_de_valores = [float(x) for x in a.split()]
                print("Resultado do Desvio Padrão:", calc.dp(lista_de_valores))
            except ValueError:
                print("Erro: Todos os valores devem ser números válidos.")
        elif escolha == '20':
            limpar_terminal()
            resultado = calc.logs()
            print(resultado)
        elif escolha == '21':
            limpar_terminal()
            resultado = calc.porcentagem()
            print(resultado)
        else:
            print("Opção inválida. Tente novamente.")
    
if __name__ == "__main__":
    main()
    
'''    

Relatório de testes:
- Calculo de Raiz Enésima fora do esperado

Esperado:
A raiz 4 de 1024 é aproximadamente: 8.0
A raiz 5 de 10000 é aproximadamente: 10.0

Resultado:
Raiz 4 de 1024: 5.656854249492381
Raiz 5 de 10000 é aproximadamente: 6.309573444801933



Melhorar:
- Mensagens de feedback para o usuário

'''