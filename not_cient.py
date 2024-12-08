import math

def converter_para_notacao_cientifica(numero):
    if numero == 0:
        return "0 * 10^0"
    
    # Calcula o expoente
    expoente = math.floor(math.log10(abs(numero)))
    
    # Calcula a mantissa
    mantissa = numero / (10 ** expoente)
    
    # Formata o resultado no formato "x * 10^n"
    return f"{mantissa:.6f} * 10^{expoente}"

# Entrada do usuário
numero = float(input("Digite um número: "))

# Chama a função e exibe o resultado
resultado = converter_para_notacao_cientifica(numero)
print(f"O número em notação científica é: {resultado}")
