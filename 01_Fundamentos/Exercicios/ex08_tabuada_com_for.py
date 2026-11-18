# 1. Leitura do número
# Convertemos para int porque a tabuada trabalha com números inteiros.
numero = int(input("Tabuada de qual número? "))


# 2. Repetição
# O for repete um bloco de código para cada valor de uma sequência.
# range(1, 11) gera os números de 1 até 10:
# o início (1) é incluído, mas o fim (11) não.
# Por isso usamos 11, para que o 10 também apareça.
# A variável multiplicador assume um valor novo a cada volta do laço (1, 2, 3, ... 10).
# Dentro do bloco, que fica indentado, calculamos o resultado da volta atual
# e exibimos uma linha da tabuada.
for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")
