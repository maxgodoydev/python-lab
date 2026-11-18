# 1. Pergunta do nome
# O input() mostra a mensagem na tela, espera o usuário digitar e apertar Enter,
# e devolve o que foi digitado.
# Armazenamos esse retorno na variável nome para poder usá-la nas próximas etapas.
# Importante: o input() sempre devolve texto (str),
# mesmo que o usuário digite um número.
nome = input("Qual é o seu nome? ")


# 2. Pergunta do curso
# Repetimos a ideia para guardar a segunda informação em outra variável.
curso = input("Qual é o seu curso? ")


# 3. Mensagem personalizada
# O operador + junta (concatena) textos: montamos a frase unindo pedaços fixos
# com o conteúdo das variáveis.
# Atenção aos espaços dentro das aspas: sem o espaço depois da vírgula em "Olá, ",
# o nome ficaria colado na palavra anterior.
print("Olá, " + nome + "!")
print("Bem-vindo(a) ao curso de " + curso + ".")
