"""

# Em andamento

# Operações de uma calculadora convencional
Soma (+) [Feito]
Subtração (-) [Feito]
Multiplicação (×) [Feito]
Divisão (÷) [Feito]
Raiz quadrada (√) [Feito]
Potenciação (xⁿ) [Feito]
Raiz enésima (ⁿ√x) [Feito]
Exponencial (eˣ) [Feito]
Equação do Segundo Grau [Feito]
Fatorial (n!) [Feito]
Seno (sin) [Feito]
Cosseno (cos) [Feito]
Tangente (tan) [Feito]
Módulo (|x|) [Feito]
Média
Graus ↔ Radianos (deg/rad)
Radianos ↔ Graus (rad/deg)
Logaritmo decimal (log)
Logaritmo natural (ln)
Porcentagem (%)
Notação científica (EXP ou E)
Soma acumulada
Variância

Conversão de Bases:
Decimal ↔ Binário ↔ Octal ↔ Hexadecimal

# Futuro
Cálculo de memória:
Adicionar à memória (M+)
Subtrair da memória (M-)
Recuperar valor da memória (MR)
Limpar memória (MC)
Igualdade (=)
Limpeza/Reset (C/AC ou CE)

"""

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
            return "Erro: Divisão por zero"
        else:
            return a / b
        
    def raiz_quadrada(self, a):
        if a < 0:
            return "Erro: Raiz quadrada de número negativo"
        else:
            return math.sqrt(a)
        
    def raiz(self, a, n):
        if n <= 0:
            return "O índice da raiz deve ser maior que zero."
        elif a < 0 and n % 2 == 0:
            "Erro: Não é possível calcular a raiz par de um número negativo."
        else:
            return math.pow(a, 1/n)
        
    def potenciacao(self, a, b):
        return math.pow(a, b)
        
    def fatorial(self, n):
        if n < 0:
            return "Erro: Fatorial de número negativo"
        else:
            return math.factorial(n)
    
    def seno(self, a):
        return math.sin(a)
    
    def cosseno(self, a):
        return math.cos(a)
    
    def tangente(self, a):
        return math.tan(a)
    
    def modulo(a):
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
    
    