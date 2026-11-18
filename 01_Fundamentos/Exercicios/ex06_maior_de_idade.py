# 1. Leitura da idade
# Convertemos a entrada para int porque a idade é um número inteiro
# e precisamos compará-la com outro número.
idade = int(input("Qual é a sua idade? "))


# 2. Decisão
# O if testa uma condição. Se ela for verdadeira (True),
# o bloco abaixo dele é executado.
# Caso contrário, o Python executa o bloco do else.
# Usamos >= ("maior ou igual") em vez de >, porque quem tem exatamente 18 anos
# já é maior de idade. Esse é o caso-limite que precisamos acertar.
# Os dois-pontos (:) abrem cada bloco, e a indentação (4 espaços) indica
# quais linhas pertencem a ele.
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
