def decimal_para_binario(decimal):
    return bin(decimal)[2:]  # Remove o prefixo "0b"

def decimal_para_octal(decimal):
    return oct(decimal)[2:]  # Remove o prefixo "0o"

def decimal_para_hexadecimal(decimal):
    return hex(decimal)[2:].upper()  # Remove o prefixo "0x" e converte para maiúsculas

def binario_para_decimal(binario):
    return int(binario, 2)  # Converte a string binária para decimal

def octal_para_decimal(octal):
    return int(octal, 8)  # Converte a string octal para decimal

def hexadecimal_para_decimal(hexadecimal):
    return int(hexadecimal, 16)  # Converte a string hexadecimal para decimal

# Funções adicionais para conversão indireta:
def binario_para_octal(binario):
    decimal = binario_para_decimal(binario)
    return decimal_para_octal(decimal)

def binario_para_hexadecimal(binario):
    decimal = binario_para_decimal(binario)
    return decimal_para_hexadecimal(decimal)

def octal_para_binario(octal):
    decimal = octal_para_decimal(octal)
    return decimal_para_binario(decimal)

def octal_para_hexadecimal(octal):
    decimal = octal_para_decimal(octal)
    return decimal_para_hexadecimal(decimal)

def hexadecimal_para_binario(hexadecimal):
    decimal = hexadecimal_para_decimal(hexadecimal)
    return decimal_para_binario(decimal)

def hexadecimal_para_octal(hexadecimal):
    decimal = hexadecimal_para_decimal(hexadecimal)
    return decimal_para_octal(decimal)

# Exemplo de uso:
decimal = 255
print(f"Decimal: {decimal}")
print(f"Binário: {decimal_para_binario(decimal)}")
print(f"Octal: {decimal_para_octal(decimal)}")
print(f"Hexadecimal: {decimal_para_hexadecimal(decimal)}")

binario = "11111111"
print(f"\nBinário: {binario}")
print(f"Decimal: {binario_para_decimal(binario)}")
print(f"Octal: {binario_para_octal(binario)}")
print(f"Hexadecimal: {binario_para_hexadecimal(binario)}")

octal = "377"
print(f"\nOctal: {octal}")
print(f"Decimal: {octal_para_decimal(octal)}")
print(f"Binário: {octal_para_binario(octal)}")
print(f"Hexadecimal: {octal_para_hexadecimal(octal)}")

hexadecimal = "FF"
print(f"\nHexadecimal: {hexadecimal}")
print(f"Decimal: {hexadecimal_para_decimal(hexadecimal)}")
print(f"Binário: {hexadecimal_para_binario(hexadecimal)}")
print(f"Octal: {hexadecimal_para_octal(hexadecimal)}")
