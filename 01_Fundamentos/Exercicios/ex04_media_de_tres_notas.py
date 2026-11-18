# 1. Variáveis das notas
# Utilizamos variáveis para armazenar as notas dos usuários.
nota1 = 8.5
nota2 = 7.0
nota3 = 9.0


# 2. Variável da média
# Criamos outra variável para armazenar o resultado de uma operação matemática.
# Dessa forma, podemos chamar media posteriormente para acessar o resultado,
# sem precisar realizar o cálculo novamente.
media = (nota1 + nota2 + nota3) / 3


# 3. Exibição do resultado
# O print() vai exibir o resultado do código na tela.
# O f antes das aspas indica que estamos utilizando uma f-string.
# Esse recurso permite combinar textos com valores de variáveis na mesma frase.
# As chaves {} indicam onde queremos inserir o valor de uma variável.
# Por exemplo, {media} será substituído pelo valor armazenado em media.
# :.2f define que o número será apresentado com duas casas decimais.
# Por exemplo, 8.1666 será exibido como 8.17.
print(f"Média final: {media:.2f}")
