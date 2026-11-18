# 1. Leitura das notas
# Convertemos as entradas para float, como no exercício 05, para poder calcular.
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))


# 2. Validação das notas
# Antes de calcular, conferimos se as notas fazem sentido (de 0 a 10).
# O operador or significa "ou": a condição é verdadeira
# se qualquer uma das partes for verdadeira.
# Guardamos o resultado dessa checagem em notas_invalidas (True ou False)
# para deixar o if logo abaixo mais fácil de ler.
notas_invalidas = nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10


# 3. Decisão
# Se as notas forem inválidas, apenas avisamos o usuário e não calculamos nada.
# Caso contrário, calculamos a média e classificamos o aluno.
if notas_invalidas:
    print("Notas inválidas: use valores entre 0 e 10.")
else:
    media = (nota1 + nota2) / 2

    # O if / elif / else testa as condições na ordem, de cima para baixo,
    # e executa apenas o primeiro bloco cuja condição for verdadeira.
    # Por isso a ordem importa: se a média chegou até o elif,
    # já sabemos que ela é menor que 7, então basta testar se é pelo menos 5.
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    # 4. Exibição
    # Cada bloco apenas guarda o texto em situacao,
    # e exibimos o resultado uma única vez aqui.
    # Assim não repetimos os print() em cada ramo do if.
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")
